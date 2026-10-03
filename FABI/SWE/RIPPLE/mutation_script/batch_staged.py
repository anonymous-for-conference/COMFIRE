#!/usr/bin/env python3
"""Run isolated mutation, inference, and evaluation stages with barriers."""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import datetime as dt
import json
import hashlib
import os
import signal
import subprocess
import sys
import traceback
from pathlib import Path

from experiment import (API_KEY, BASE_URL, INTERFACE, analyze_trace, atomic_json,
                        atomic_text, now, prepare_local_worktree)
from mutation_pipeline import generate

ROOT = Path("/data/zlyuaj/coding_agent/EviFuzz")
CASES = ROOT / "original_passed_cases/Codex/gpt54mini_lite/cases"
RESULTS = ROOT / "RIPPLE/mutation_result"
REPOS = Path("/data/zlyuaj/coding_agent/Real_inconsistency_mining/repositories")


def run_command(command: list[str], log_path: Path, env: dict[str, str] | None = None) -> None:
    timeout = int(os.environ.get("RIPPLE_COMMAND_TIMEOUT_SECONDS", str(4 * 60 * 60)))
    with log_path.open("a") as log:
        proc = subprocess.Popen(
            command, stdout=log, stderr=subprocess.STDOUT, env=env,
            start_new_session=True,
        )
        try:
            returncode = proc.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid, signal.SIGTERM)
            try:
                proc.wait(timeout=30)
            except subprocess.TimeoutExpired:
                os.killpg(proc.pid, signal.SIGKILL)
                proc.wait(timeout=30)
            raise TimeoutError(f"command exceeded {timeout}s; see {log_path}")
    if returncode:
        raise RuntimeError(f"command exited {returncode}; see {log_path}")


def socket_path(root: Path, stage: str) -> str:
    token = hashlib.sha256(f"{root}:{stage}".encode()).hexdigest()[:16]
    return f"/tmp/ripple-{stage[:4]}-{token}.sock"


def mutation_stage(item: dict) -> dict:
    root, case = Path(item["run_root"]), Path(item["case_dir"])
    root.mkdir(parents=True, exist_ok=False)
    task = json.loads((case / "task.json").read_text())
    atomic_json(root / "status.json", {"phase": "mutation", "updated_at": now()})
    repo = prepare_local_worktree(root, Path(item["base_repo"]), task["base_commit"])
    atomic_json(root / "source_repo.json", {"base_repo": item["base_repo"], "private_worktree": str(repo),
                "base_commit": task["base_commit"], "source_repo_was_modified": False})
    manifest = generate(case, repo, root / "mutation", "level_1,level_2", item["seed"], 5,
                        enabled_operators=tuple(x.strip() for x in os.environ.get("RIPPLE_OPERATORS", "L1,L2,L3").split(",") if x.strip()))
    atomic_json(root / "repo_map.json", {item["instance_id"]: str(repo)})
    atomic_json(root / "status.json", {"phase": "mutation_complete", "updated_at": now(),
                "mutation_count": manifest["mutation_count"], "selected_cluster_count": 5})
    return item


def inference_stage(item: dict) -> dict:
    root = Path(item["run_root"])
    atomic_json(root / "status.json", {"phase": "inference", "updated_at": now()})
    env = os.environ.copy()
    env.update({"OPENAI_API_KEY": API_KEY, "OPENAI_BASE_URL": BASE_URL})
    agent = item.get("agent", "codex")
    command = [sys.executable, str(INTERFACE), "run", "--agent", agent,
               "--repo-map", str(root / "repo_map.json"), "--output", str(root / "interface"),
               "--ids", item["instance_id"], "--run", "1", "--workers", "1",
               "--socket", socket_path(root, "inference"), "--inference-only"]
    run_command(command, root / "INFERENCE.log", env)
    if not (root / "interface/predictions.jsonl").is_file():
        raise RuntimeError("inference completed without predictions.jsonl")
    atomic_json(root / "status.json", {"phase": "inference_complete", "updated_at": now()})
    return item


def evaluation_stage(item: dict) -> dict:
    root = Path(item["run_root"])
    atomic_json(root / "status.json", {"phase": "evaluation", "updated_at": now()})
    agent = item.get("agent", "codex")
    command = [sys.executable, str(INTERFACE), "evaluate", "--agent", agent,
               "--output", str(root / "interface"), "--run", "1", "--workers", "1",
               "--socket", socket_path(root, "evaluation"),
               "--mutation-patch", str(root / "mutation/mutation.patch"),
               "--repo", str(root / "worktree")]
    run_command(command, root / "EVALUATION.log")
    summary = json.loads((root / "interface/evaluation_summary/official_summary.json").read_text())
    if item["instance_id"] not in summary.get("completed_ids", []):
        raise RuntimeError("official evaluation did not complete target instance")
    return item


def finalize(item: dict, error: str | None = None) -> dict:
    root, case = Path(item["run_root"]), Path(item["case_dir"])
    task = json.loads((case / "task.json").read_text())
    result = {"instance_id": item["instance_id"], "run_root": str(root), "error": error}
    try:
        if not error:
            manifest = json.loads((root / "mutation/manifest.json").read_text())
            trace = analyze_trace(root, manifest)
            official = trace.get("official_summary", {})
            resolved = item["instance_id"] in official.get("resolved_ids", [])
            locations = [x for c in manifest["clusters"] for x in c["locations"]]
            seen = sum(bool(x["mutated_text_seen"]) for x in trace["locations"])
            cluster_lines = [f"- `{c['cluster_id']}`：Level `{c['locations'][0].get('level', c['cluster_id'].split(':')[-2])}`，operator `{c['selected_operator']}`，{len(c['locations'])} 个位置。" for c in manifest["clusters"]]
            text = [f"# {item['instance_id']} Level 1 + Level 2 Mutation 分析", "",
                    "## 结论", "", f"- K=5，优先选择 Level 1，不足时由 Level 2 补齐。",
                    f"- 共 mutation {len(locations)} 个文档位置；轨迹确认读到 {seen}/{len(locations)} 个。",
                    f"- Official evaluation：`resolved={str(resolved).lower()}`。", "",
                    "## 选中 Cluster", "", *cluster_lines, "",
                    "## 详细产物", "", "- 句子级变异前后：`mutation/cluster_*/location_*.json`。",
                    "- 结构化 prompt：`mutation/cluster_*/*.prompt.md`。", "- Mutation patch：`mutation/mutation.patch`。",
                    "- Agent 轨迹命中与最终 patch：`trace_analysis.json`。", "",
                    "本次 mutation、inference、evaluation 分阶段执行；每个 case 使用独立 private worktree、输出目录、Podman socket 和 evaluation run ID。"]
            atomic_text(root / "分析.md", "\n".join(text) + "\n")
            result.update({"resolved": resolved, "mutation_count": len(locations), "mutated_seen": seen,
                           "clusters": [{"cluster_id": c["cluster_id"], "operator": c["selected_operator"],
                                         "locations": len(c["locations"])} for c in manifest["clusters"]]})
    finally:
        repo = root / "worktree"
        if (repo / ".git").exists():
            reset = subprocess.run(["git", "reset", "--hard", task["base_commit"]], cwd=repo,
                                   text=True, capture_output=True)
            clean = subprocess.run(["git", "clean", "-fd"], cwd=repo, text=True, capture_output=True)
            status = subprocess.run(["git", "status", "--porcelain"], cwd=repo, text=True, capture_output=True)
            restored = reset.returncode == 0 and clean.returncode == 0 and not status.stdout
            atomic_json(root / "restore.json", {"restored": restored, "status": status.stdout, "time": now()})
            result["restored"] = restored
        atomic_json(root / "status.json", {"phase": "failed" if error else "completed", "updated_at": now(), "error": error})
    return result


def parallel_stage(name: str, func, items: list[dict], workers: int, log: Path) -> tuple[list[dict], dict[str, str]]:
    ok, errors = [], {}
    with log.open("a") as f:
        f.write(f"[{now()}] stage={name} start items={len(items)} workers={workers}\n")
    if not items:
        with log.open("a") as f:
            f.write(f"[{now()}] stage={name} skipped: no successful inputs\n")
        return ok, errors
    with cf.ThreadPoolExecutor(max_workers=min(workers, len(items))) as pool:
        futures = {pool.submit(func, item): item for item in items}
        for future in cf.as_completed(futures):
            item = futures[future]
            try:
                ok.append(future.result())
            except Exception as exc:
                errors[item["instance_id"]] = f"{type(exc).__name__}: {exc}"
                with (Path(item["run_root"]) / f"{name.upper()}_FAILURE.log").open("w") as f:
                    f.write(traceback.format_exc())
    with log.open("a") as f:
        f.write(f"[{now()}] stage={name} end success={len(ok)} failed={len(errors)}\n")
    return ok, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ids", default="astropy__astropy-12907,astropy__astropy-14995")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--resume-roots", help="comma-separated failed run roots whose completed mutation patches should be reused")
    parser.add_argument("--evaluation-roots", help="comma-separated roots with valid inference attempts to evaluate without rerunning inference")
    args = parser.parse_args()
    if args.evaluation_roots:
        batch_id = dt.datetime.now().strftime("level12_k5_staged2_eval_%Y%m%d_%H%M%S")
        batch_root = RESULTS / batch_id
        batch_root.mkdir()
        items = []
        for value in args.evaluation_roots.split(","):
            run_root = Path(value).resolve()
            manifest = json.loads((run_root / "mutation/manifest.json").read_text())
            iid = manifest["instance_id"]
            attempts = sorted((run_root / "interface/cases" / iid).glob("attempt_*"), reverse=True)
            valid = next((p for p in attempts if (p / "validation.json").is_file()
                          and json.loads((p / "validation.json").read_text()).get("valid") is True), None)
            if valid is None:
                raise RuntimeError(f"no valid inference attempt for {iid}")
            prediction = json.loads((valid / "prediction.json").read_text())
            atomic_text(run_root / "interface/predictions.jsonl", json.dumps(prediction, ensure_ascii=False) + "\n")
            source = json.loads((run_root / "source_repo.json").read_text())
            items.append({"instance_id": iid, "case_dir": str(CASES / iid), "base_repo": source["base_repo"],
                          "run_root": str(run_root), "seed": manifest["seed"]})
        atomic_json(batch_root / "BATCH_CONFIG.json", {"batch_id": batch_id, "started_at": now(),
                    "evaluation_roots": [x["run_root"] for x in items], "workers": args.workers,
                    "stages": ["reuse_valid_inference", "evaluation"]})
        log = batch_root / "BATCH.log"
        log.write_text("")
        active, errors = parallel_stage("evaluation", evaluation_stage, items, args.workers, log)
        results = [finalize(item, errors.get(item["instance_id"])) for item in items]
        atomic_json(batch_root / "BATCH_SUMMARY.json", {"batch_id": batch_id, "finished_at": now(), "results": results})
        print(batch_root)
        return 1 if errors else 0
    if args.resume_roots:
        batch_id = dt.datetime.now().strftime("level12_k5_staged2_resume_%Y%m%d_%H%M%S")
        batch_root = RESULTS / batch_id
        batch_root.mkdir()
        items = []
        for value in args.resume_roots.split(","):
            run_root = Path(value).resolve()
            manifest = json.loads((run_root / "mutation/manifest.json").read_text())
            iid = manifest["instance_id"]
            source = json.loads((run_root / "source_repo.json").read_text())
            repo = run_root / "worktree"
            if subprocess.check_output(["git", "status", "--porcelain"], cwd=repo, text=True).strip():
                raise RuntimeError(f"resume worktree is not clean: {repo}")
            subprocess.run(["git", "apply", str(run_root / "mutation/mutation.patch")], cwd=repo, check=True)
            failed_interface = run_root / "interface"
            if failed_interface.exists():
                failed_interface.rename(run_root / f"interface_failed_{dt.datetime.now().strftime('%H%M%S')}")
            items.append({"instance_id": iid, "case_dir": str(CASES / iid), "base_repo": source["base_repo"],
                          "run_root": str(run_root), "seed": manifest["seed"]})
        atomic_json(batch_root / "BATCH_CONFIG.json", {"batch_id": batch_id, "started_at": now(),
                    "resume_roots": [x["run_root"] for x in items], "workers": args.workers,
                    "stages": ["reuse_completed_mutation", "inference", "evaluation"]})
        log = batch_root / "BATCH.log"
        log.write_text("")
        active, all_errors = parallel_stage("inference", inference_stage, items, args.workers, log)
        active, errors = parallel_stage("evaluation", evaluation_stage, active, args.workers, log); all_errors.update(errors)
        results = [finalize(item, all_errors.get(item["instance_id"])) for item in items]
        atomic_json(batch_root / "BATCH_SUMMARY.json", {"batch_id": batch_id, "finished_at": now(), "results": results})
        print(batch_root)
        return 1 if all_errors else 0
    ids = [x for x in args.ids.split(",") if x]
    if len(ids) != 2:
        raise ValueError("this validation run requires exactly two cases")
    batch_id = dt.datetime.now().strftime("level12_k5_staged2_%Y%m%d_%H%M%S")
    batch_root = RESULTS / batch_id
    batch_root.mkdir()
    items = []
    for index, iid in enumerate(ids, 1):
        slug = iid.split("__", 1)[0]
        items.append({"instance_id": iid, "case_dir": str(CASES / iid), "base_repo": str(REPOS / slug),
                      "run_root": str(RESULTS / f"{iid.replace('__','_').replace('-','')}_l12_k5_{batch_id[-6:]}_{index:02d}"),
                      "seed": 6938 + index})
    atomic_json(batch_root / "BATCH_CONFIG.json", {"batch_id": batch_id, "started_at": now(), "ids": ids,
                "k": 5, "levels": ["level_1", "level_2"], "selection": "Level 1 first; Level 2 fills shortage",
                "operators": ["L1", "L2", "L3"], "workers": args.workers,
                "stages": ["mutation", "inference", "evaluation"]})
    log = batch_root / "BATCH.log"
    log.write_text("")
    active, all_errors = parallel_stage("mutation", mutation_stage, items, args.workers, log)
    active, errors = parallel_stage("inference", inference_stage, active, args.workers, log); all_errors.update(errors)
    active, errors = parallel_stage("evaluation", evaluation_stage, active, args.workers, log); all_errors.update(errors)
    results = [finalize(item, all_errors.get(item["instance_id"])) for item in items]
    atomic_json(batch_root / "BATCH_SUMMARY.json", {"batch_id": batch_id, "finished_at": now(), "results": results})
    print(batch_root)
    return 1 if all_errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
