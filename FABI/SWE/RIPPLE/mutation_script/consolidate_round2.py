#!/usr/bin/env python3
"""Consolidate recovered round-two cases and produce audited final statistics."""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import shutil
from pathlib import Path

AGENTS = ("codex", "sweagent", "opencode")


def read(path: Path):
    return json.loads(path.read_text())


def atomic(path: Path, value) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    temporary.replace(path)


def iid(run: Path) -> str:
    return run.name.split("_", 1)[1]


def valid_prediction(run: Path, expected: str) -> bool:
    try:
        rows = [json.loads(x) for x in (run / "interface/predictions.jsonl").read_text().splitlines() if x.strip()]
        return len(rows) == 1 and rows[0].get("instance_id") == expected and isinstance(rows[0].get("model_patch"), str)
    except (OSError, json.JSONDecodeError):
        return False


def official(run: Path, expected: str) -> dict | None:
    path = run / "interface/evaluation_summary/official_summary.json"
    try:
        value = read(path)
        return value if expected in value.get("completed_ids", []) else None
    except (OSError, json.JSONDecodeError):
        return None


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def remove_tree(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.exists():
        shutil.rmtree(path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--first", type=Path, required=True)
    parser.add_argument("--main", type=Path, required=True)
    parser.add_argument("--retry", type=Path, required=True)
    parser.add_argument("--repair", type=Path, required=True)
    args = parser.parse_args()
    for name in ("first", "main", "retry", "repair"):
        setattr(args, name, getattr(args, name).resolve())

    targets = {}
    for agent in AGENTS:
        for run in sorted((args.main / agent / "runs").iterdir()):
            if run.is_dir():
                key = (agent, iid(run))
                if key in targets:
                    raise RuntimeError(f"duplicate main target: {key}")
                targets[key] = run
    if len(targets) != 312:
        raise RuntimeError(f"main directory must contain 312 case directories, found {len(targets)}")

    recovered = {}
    for root in (args.retry, args.repair):
        for agent in AGENTS:
            runs = root / agent / "runs"
            if not runs.is_dir():
                continue
            for run in sorted(runs.iterdir()):
                if not (run / "mutation/manifest.json").is_file():
                    continue
                key = (agent, read(run / "mutation/manifest.json")["instance_id"])
                if key in recovered:
                    raise RuntimeError(f"duplicate recovered source: {key}")
                recovered[key] = run
    if len(recovered) != 9:
        raise RuntimeError(f"expected 9 recovered case sources, found {len(recovered)}")

    plan = []
    for key, source in sorted(recovered.items()):
        target = targets.get(key)
        if target is None:
            raise RuntimeError(f"recovered case has no main target: {key}")
        source_meta, target_meta = read(source / "source_repo.json"), read(target / "source_repo.json")
        if source_meta["base_commit"] != target_meta["base_commit"]:
            raise RuntimeError(f"base commit mismatch for {key}")
        if not valid_prediction(source, key[1]) or official(source, key[1]) is None:
            raise RuntimeError(f"recovered source is incomplete for {key}: {source}")
        plan.append((key, source, target, source_meta, target_meta))

    provenance = []
    for key, source, target, source_meta, target_meta in plan:
        for directory in ("mutation", "interface"):
            remove_tree(target / directory)
            os.replace(source / directory, target / directory)
        for filename in ("round2_decision.json", "status.json"):
            source_file = source / filename
            if source_file.is_file():
                shutil.copy2(source_file, target / filename)
        for log in source.glob("*.log"):
            shutil.copy2(log, target / f"RECOVERY_{source.parents[2].name}_{log.name}")
        atomic(target / "repo_map.json", {key[1]: str(target / "worktree")})
        atomic(target / "source_repo.json", {
            **target_meta, "private_worktree": str(target / "worktree"),
            "consolidated_from": str(source),
        })
        provenance.append({
            "agent": key[0], "instance_id": key[1], "source": str(source),
            "target": str(target), "base_commit": source_meta["base_commit"],
            "mutation_patch_sha256": sha256(target / "mutation/mutation.patch"),
            "prediction_sha256": sha256(target / "interface/predictions.jsonl"),
        })

    final_rows = []
    per_agent = {}
    for agent in AGENTS:
        rows = []
        for (selected_agent, instance), run in sorted(targets.items()):
            if selected_agent != agent:
                continue
            manifest = read(run / "mutation/manifest.json")
            summary = official(run, instance)
            if not valid_prediction(run, instance) or summary is None:
                raise RuntimeError(f"post-consolidation case incomplete: {agent}:{instance}")
            resolved = instance in summary.get("resolved_ids", [])
            row = {
                "agent": agent, "instance_id": instance, "run_root": str(run),
                "resolved": resolved, "error": None,
                "mutation_count": manifest.get("mutation_count"),
                "selected_cluster_count": manifest.get("selected_cluster_count"),
            }
            rows.append(row)
            final_rows.append(row)
        per_agent[agent] = {
            "executed": len(rows), "resolved": sum(x["resolved"] for x in rows),
            "task_failures": sum(not x["resolved"] for x in rows),
            "infrastructure_failures": 0,
        }
        atomic(args.main / agent / "BATCH_SUMMARY.json", {
            "finished_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
            "total": len(rows), "results": rows, "errors": {},
        })

    first_stats = {}
    first_correct = set()
    for agent in AGENTS:
        batch = read(args.first / agent / "BATCH_SUMMARY.json")
        rows = batch["results"]
        first_correct.update((agent, row["instance_id"]) for row in rows if row.get("resolved") is True)
        first_stats[agent] = {
            "executed": len(rows),
            "resolved": sum(row.get("resolved") is True for row in rows),
            "task_failures": sum(row.get("resolved") is False for row in rows),
            "infrastructure_failures": sum(bool(row.get("error")) for row in rows),
        }
    second_keys = set(targets)
    correct_not_started = sorted({f"{a}:{i}" for a, i in first_correct - second_keys})
    report = {
        "schema_version": 1,
        "finished_at": dt.datetime.now().astimezone().isoformat(timespec="seconds"),
        "first_round": first_stats,
        "second_round": per_agent,
        "first_round_correct_but_second_round_not_started": correct_not_started,
        "first_round_correct_but_second_round_not_started_count": len(correct_not_started),
        "historical_recovery": {
            "initial_missing_mutation_manifests": 9,
            "initial_manifest_present_but_missing_predictions": 60,
            "final_missing_mutation_manifests": 0,
            "final_missing_predictions": 0,
            "final_missing_evaluations": 0,
        },
        "consolidated_recovered_cases": provenance,
        "results": final_rows,
    }
    atomic(args.main / "FINAL_ROUND2_SUMMARY.json", report)
    atomic(args.main / "BATCH_SUMMARY.json", {
        "finished_at": report["finished_at"], "total": len(final_rows),
        "results": final_rows, "errors": {},
    })
    atomic(args.main / "CONSOLIDATION_MANIFEST.json", {
        "finished_at": report["finished_at"], "moves": provenance,
    })
    atomic(args.main / "status.json", {
        "updated_at": report["finished_at"], "phase": "completed",
        "completed": 312, "total": 312, "remaining": 0,
        "success": 312, "failed": 0, "errors": 0, "eta": "0",
        "pid": None, "pid_alive": False, "output_dir": str(args.main),
        "inference": {"completed": 312, "total": 312, "remaining": 0},
        "evaluation": {"completed": 312, "total": 312, "remaining": 0},
    })

    lines = [
        "# 第二轮 Mutation 最终汇总", "",
        f"- 完成时间：`{report['finished_at']}`",
        "- Mutation manifest：`312/312`",
        "- Inference prediction：`312/312`",
        "- Official evaluation：`312/312`",
        "- 基础设施失败：`0`", "", "## 分 Agent 统计", "",
        "| Agent | 第一轮执行 | 第一轮任务失败 | 第一轮基础设施失败 | 第二轮执行 | 第二轮任务失败 | 第二轮基础设施失败 |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for agent in AGENTS:
        one, two = first_stats[agent], per_agent[agent]
        lines.append(f"| {agent} | {one['executed']} | {one['task_failures']} | {one['infrastructure_failures']} | {two['executed']} | {two['task_failures']} | {two['infrastructure_failures']} |")
    lines.extend(["", "## 启动完整性", "",
                  f"- 第一轮正确但第二轮最终未正常启动：`{len(correct_not_started)}`。",
                  "- 历史上曾有 9 个缺失 mutation manifest、60 个缺失 prediction；全部已恢复，不计为最终 failure。", "",
                  "任务失败表示 official evaluation 为 unresolved；基础设施失败表示没有形成可判定的 official result，两者分开统计。", ""])
    (args.main / "最终汇总.md").write_text("\n".join(lines))
    live = [
        "# Round 2 Final Status", "",
        "- 状态：`completed`", f"- 完成时间：`{report['finished_at']}`",
        "- Mutation：`312/312`", "- Inference：`312/312`",
        "- Evaluation：`312/312`", "- 剩余：`0`",
        "- 第二轮基础设施失败：`0`", "- PID alive：`false`", "",
        "详细统计：`最终汇总.md`；机器可读结果：`FINAL_ROUND2_SUMMARY.json`。", "",
    ]
    (args.main / "LIVE_PROCESS.md").write_text("\n".join(live))
    (args.main / "LIVE_PROGRESS.md").write_text("\n".join(live))


if __name__ == "__main__":
    main()
