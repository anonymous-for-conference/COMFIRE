#!/usr/bin/env python3
"""Run one agent's clean cases through isolated staged mutation experiments."""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import datetime as dt
import json
import os
import statistics
import subprocess
import sys
import time
import traceback
from pathlib import Path
from typing import Any, Callable

from batch_staged import (evaluation_stage, finalize, inference_stage,
                          mutation_stage, socket_path)
from experiment import atomic_json, atomic_text, now
from mutation_pipeline import jsonl

ROOT = Path("/data/zlyuaj/coding_agent/EviFuzz")
CASES = ROOT / "original_passed_cases/Codex/gpt54mini_lite/cases"
AGENT = "codex"
AGENT_DISPLAY = "Codex"
EXPECTED_CASES = 149
RESULTS = ROOT / "RIPPLE/mutation_result"
REPOSITORY_ROOT = Path("/data/zlyuaj/coding_agent/Real_inconsistency_mining/repositories")
SPECIAL_REPOS = {
    "pytest-dev/pytest": Path("/data/zlyuaj/coding_agent/Real_inconsistency_mining/pytest"),
    "scikit-learn/scikit-learn": Path("/data/zlyuaj/coding_agent/sklearn"),
}
STAGES = ("mutation", "inference", "evaluation")
K = 5
LEVELS = ("level_1", "level_2")
OPERATORS = tuple(x.strip() for x in os.environ.get("RIPPLE_OPERATORS", "L1,L2,L3").split(",") if x.strip())


def read_json(path: Path) -> Any:
    return json.loads(path.read_text())


def repo_for(slug: str) -> Path:
    return SPECIAL_REPOS.get(slug, REPOSITORY_ROOT / slug.split("/", 1)[1])


def cluster_counts(case_dir: Path) -> dict[str, int]:
    rows = jsonl(case_dir / "clustered_doc.jsonl")
    return {
        level: len({row["cluster_id"] for row in rows if row["level"] == level})
        for level in LEVELS
    }


def discover(batch_root: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    items, failures = [], []
    case_dirs = sorted(
        path for path in CASES.iterdir()
        if path.is_dir() and (path / "task.json").is_file()
        and (path / "clustered_doc.jsonl").is_file()
        and (path / "all_doc.jsonl").is_file()
    )
    for index, case_dir in enumerate(case_dirs, 1):
        task = read_json(case_dir / "task.json")
        iid, slug = task["instance_id"], task["repo"]
        base_repo = repo_for(slug)
        counts = cluster_counts(case_dir)
        reasons = []
        if not (base_repo / ".git").exists():
            reasons.append(f"local repository missing: {base_repo}")
        elif subprocess.run(
            ["git", "cat-file", "-e", f"{task['base_commit']}^{{commit}}"],
            cwd=base_repo, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        ).returncode:
            reasons.append(f"base commit missing: {task['base_commit']}")
        if sum(counts.values()) < K:
            reasons.append(
                f"K={K} unavailable: level_1={counts['level_1']}, "
                f"level_2={counts['level_2']}"
            )
        item = {
            "index": index, "instance_id": iid, "repo_slug": slug,
            "case_dir": str(case_dir), "base_repo": str(base_repo),
            "base_commit": task["base_commit"],
            "run_root": str(batch_root / "runs" / f"{index:03d}_{iid}"),
            "seed": 6938 + index, "cluster_counts": counts, "agent": AGENT,
        }
        items.append(item)
        if reasons:
            failures.append({"instance_id": iid, "reasons": reasons})
    return items, failures


def append_event(root: Path, event: str, **fields: Any) -> None:
    record = {"time": now(), "event": event, **fields}
    with (root / "events.jsonl").open("a") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")
        handle.flush()
        os.fsync(handle.fileno())


def events(root: Path) -> list[dict[str, Any]]:
    path = root / "events.jsonl"
    if not path.exists():
        return []
    result = []
    for line in path.read_text(errors="replace").splitlines():
        try:
            result.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return result


def elapsed_seconds(started_at: str, ended_at: str | None = None) -> float:
    start = dt.datetime.fromisoformat(started_at)
    end = dt.datetime.fromisoformat(ended_at) if ended_at else dt.datetime.now().astimezone()
    return max(0.0, (end - start).total_seconds())


def format_duration(seconds: float) -> str:
    seconds = max(0, round(seconds))
    hours, rem = divmod(seconds, 3600)
    minutes, secs = divmod(rem, 60)
    if hours:
        return f"{hours}h {minutes}m"
    if minutes:
        return f"{minutes}m {secs}s"
    return f"{secs}s"


def derive_status(root: Path) -> dict[str, Any]:
    config = read_json(root / "BATCH_CONFIG.json")
    records = events(root)
    phase = "preflight"
    stage_total = config["total"]
    stage_completed = stage_success = stage_failed = 0
    stage_cache_hits = stage_executed_completed = 0
    stage_executed_total = stage_total
    phase_started = config["started_at"]
    terminal: dict[str, str] = {}
    last_event = config["started_at"]
    error_details = []
    done = False
    exit_code = None
    for event in records:
        last_event = event["time"]
        kind = event["event"]
        if kind == "batch_started" and event.get("resume"):
            terminal = {}
            error_details = []
            done = False
            exit_code = None
        elif kind == "stage_started":
            phase = event["stage"]
            stage_total = event["total"]
            stage_completed = stage_success = stage_failed = 0
            stage_cache_hits = stage_executed_completed = 0
            stage_executed_total = event.get("executed_this_run", event["total"])
            phase_started = event["time"]
        elif kind == "case_stage_succeeded" and event["stage"] == phase:
            stage_completed += 1
            stage_success += 1
            if event.get("cache_hit"):
                stage_cache_hits += 1
            else:
                stage_executed_completed += 1
        elif kind == "case_stage_failed" and event["stage"] == phase:
            stage_completed += 1
            stage_failed += 1
            stage_executed_completed += 1
            terminal[event["instance_id"]] = "failed"
            error_details.append({"instance_id": event["instance_id"], "stage": phase,
                                  "error": event["error"]})
        elif kind == "preflight_failed":
            terminal[event["instance_id"]] = "failed"
            error_details.append({"instance_id": event["instance_id"], "stage": "preflight",
                                  "error": "; ".join(event["reasons"])})
        elif kind == "case_finalized":
            terminal[event["instance_id"]] = "failed" if event.get("error") else "success"
        elif kind == "batch_finished":
            done = True
            exit_code = event["exit_code"]
            phase = "completed" if exit_code == 0 else "completed_with_failures"
    process = read_json(root / "process.json") if (root / "process.json").exists() else {}
    pid = process.get("pid")
    alive = bool(pid) and Path(f"/proc/{pid}").exists()
    if not done and pid and not alive:
        phase = "failed"
    remaining_stage = max(0, stage_total - stage_completed)
    if done or remaining_stage == 0:
        eta = "0s" if done else "waiting for stage barrier"
        eta_basis = "stage finished" if done else "no remaining item in current stage"
    elif stage_executed_completed:
        rate = stage_executed_completed / max(1.0, elapsed_seconds(phase_started))
        eta = format_duration(remaining_stage / rate) if rate > 0 else "unknown"
        eta_basis = (
            f"current-attempt executed average {rate:.4f} case/s over "
            f"{stage_executed_completed} terminal items; cache hits excluded"
        )
    else:
        eta = "unknown"
        eta_basis = "no terminal item in current stage yet"
    stalled_seconds = elapsed_seconds(last_event)
    status = {
        "run_id": config["run_id"], "updated_at": now(), "phase": phase,
        "started_at": config["started_at"], "completed": len(terminal),
        "total": config["total"], "remaining": config["total"] - len(terminal),
        "success": sum(value == "success" for value in terminal.values()),
        "failed": sum(value == "failed" for value in terminal.values()),
        "errors": len(error_details), "error_details": error_details[-20:],
        "current_stage_completed": stage_completed, "current_stage_total": stage_total,
        "current_stage_success": stage_success, "current_stage_failed": stage_failed,
        "cache_hits": stage_cache_hits, "executed_this_run": stage_executed_total,
        "executed_completed": stage_executed_completed,
        "eta": eta, "eta_basis": eta_basis, "pid": pid, "process_alive": alive,
        "log": process.get("log", str(root / "RUN.log")), "output_dir": str(root),
        "last_event_at": last_event, "seconds_since_last_event": round(stalled_seconds),
        "activity": "stalled" if alive and stalled_seconds > 1800 else ("running" if alive else "stopped"),
        "exit_code": exit_code,
    }
    return status


def render_progress(status: dict[str, Any]) -> str:
    config = read_json(Path(status["output_dir"]) / "BATCH_CONFIG.json")
    display = config.get("agent_display", "Codex")
    return "\n".join([
        f"# RIPPLE {display} 全量实验进度", "",
        f"- Run：`{status['run_id']}`",
        f"- 当前阶段：`{status['phase']}`（mutation / inference / evaluation 严格 barrier）",
        f"- 当前阶段：{status['current_stage_completed']}/{status['current_stage_total']} terminal，"
        f"成功 {status['current_stage_success']}，失败 {status['current_stage_failed']}",
        f"- 当前 attempt：cache hit {status['cache_hits']}；计划实际执行 "
        f"{status['executed_this_run']}；已实际 terminal {status['executed_completed']}",
        f"- 全批次最终状态：{status['completed']}/{status['total']} terminal，"
        f"成功 {status['success']}，失败 {status['failed']}，剩余 {status['remaining']}",
        f"- 活动状态：`{status['activity']}`；主进程存活：`{str(status['process_alive']).lower()}`",
        f"- ETA：`{status['eta']}`；依据：{status['eta_basis']}",
        f"- 最近事件：`{status['last_event_at']}`（{status['seconds_since_last_event']} 秒前）",
        f"- 最近更新：`{status['updated_at']}`", "",
        "统计口径：当前阶段完成数来自本 run 的 `events.jsonl` 成功/失败事件；"
        "全批次 completed 仅统计已经最终成功或不再进入后续阶段的 case。缓存不跨 batch 使用。", "",
        f"- 原始日志：`{status['log']}`",
        f"- 输出目录：`{status['output_dir']}`", "",
    ])


def monitor(root: Path, interval: int) -> int:
    atomic_json(root / "monitor_process.json", {
        "pid": os.getpid(), "started_at": now(), "interval_seconds": interval,
    })
    while True:
        try:
            status = derive_status(root)
            atomic_json(root / "status.json", status)
            atomic_text(root / "LIVE_PROGRESS.md", render_progress(status))
            if status["phase"] in {"completed", "completed_with_failures", "failed"}:
                return 0
        except Exception:
            atomic_text(root / "MONITOR_FAILURE.log", traceback.format_exc())
        time.sleep(interval)


def stage_is_complete(item: dict[str, Any], stage: str) -> bool:
    root = Path(item["run_root"])
    if stage == "mutation":
        manifest = root / "mutation/manifest.json"
        patch = root / "mutation/mutation.patch"
        if not (manifest.is_file() and patch.is_file()):
            return False
        repo = root / "worktree"
        if not (repo / ".git").exists():
            return False
        expected = read_json(manifest)["patch_sha256"]
        import hashlib
        if hashlib.sha256(patch.read_bytes()).hexdigest() != expected:
            return False
        current = subprocess.check_output(["git", "diff", "--binary", "--"], cwd=repo)
        if not current.strip():
            subprocess.run(["git", "apply", str(patch)], cwd=repo, check=True)
            current = subprocess.check_output(["git", "diff", "--binary", "--"], cwd=repo)
        return current == patch.read_bytes()
    if stage == "inference":
        predictions = root / "interface/predictions.jsonl"
        if not predictions.is_file():
            return False
        rows = [json.loads(line) for line in predictions.read_text().splitlines() if line.strip()]
        return len(rows) == 1 and rows[0].get("instance_id") == item["instance_id"]
    summary = root / "interface/evaluation_summary/official_summary.json"
    return summary.is_file() and item["instance_id"] in read_json(summary).get("completed_ids", [])


def stage_is_complete_safe(item: dict[str, Any], stage: str) -> bool:
    try:
        return stage_is_complete(item, stage)
    except (OSError, ValueError, KeyError, json.JSONDecodeError, subprocess.SubprocessError):
        return False


def clean_failed_attempt(item: dict[str, Any], stage: str) -> None:
    root = Path(item["run_root"])
    for path in (socket_path(root, stage),):
        Path(path).unlink(missing_ok=True)
    if stage == "mutation" and root.exists() and not stage_is_complete_safe(item, stage):
        # Mutation generation is not resumable within a cluster. Preserve evidence and
        # classify the case as failed instead of silently deleting a partial attempt.
        return


def mutation_resumable(item: dict[str, Any]) -> dict[str, Any]:
    root = Path(item["run_root"])
    if root.exists() and not stage_is_complete_safe(item, "mutation"):
        attempt = 1
        while root.with_name(root.name + f"_mutation_failed_attempt_{attempt:02d}").exists():
            attempt += 1
        root.rename(root.with_name(root.name + f"_mutation_failed_attempt_{attempt:02d}"))
    return mutation_stage(item)


def prepare_inference_retry(item: dict[str, Any]) -> None:
    root = Path(item["run_root"])
    interface = root / "interface"
    if interface.exists() and not stage_is_complete_safe(item, "inference"):
        attempt = 1
        while (root / f"interface_inference_failed_attempt_{attempt:02d}").exists():
            attempt += 1
        interface.rename(root / f"interface_inference_failed_attempt_{attempt:02d}")


def execute_stage(
    batch_root: Path, stage: str, function: Callable[[dict[str, Any]], dict[str, Any]],
    items: list[dict[str, Any]], workers: int,
) -> tuple[list[dict[str, Any]], dict[str, str]]:
    pending, ok, errors = [], [], {}
    for item in items:
        if stage_is_complete_safe(item, stage):
            ok.append(item)
        else:
            if stage == "inference":
                prepare_inference_retry(item)
            pending.append(item)
    append_event(batch_root, "stage_started", stage=stage, total=len(items),
                 workers=min(workers, max(1, len(pending))), cache_hits=len(ok),
                 executed_this_run=len(pending))
    # Emit cache hits after stage_started so monitor stage counters remain exact.
    for item in ok:
        append_event(batch_root, "case_stage_succeeded", stage=stage,
                     instance_id=item["instance_id"], cache_hit=True)
    if not pending:
        append_event(batch_root, "stage_finished", stage=stage, success=len(ok), failed=0)
        return ok, errors
    with cf.ThreadPoolExecutor(max_workers=min(workers, len(pending))) as pool:
        futures = {pool.submit(function, item): item for item in pending}
        for future in cf.as_completed(futures):
            item = futures[future]
            try:
                ok.append(future.result())
                append_event(batch_root, "case_stage_succeeded", stage=stage,
                             instance_id=item["instance_id"], cache_hit=False)
            except Exception as exc:
                error = f"{type(exc).__name__}: {exc}"
                errors[item["instance_id"]] = error
                failure = Path(item["run_root"]) / f"{stage.upper()}_FAILURE.log"
                atomic_text(failure, traceback.format_exc())
                clean_failed_attempt(item, stage)
                append_event(batch_root, "case_stage_failed", stage=stage,
                             instance_id=item["instance_id"], error=error,
                             failure_log=str(failure))
    append_event(batch_root, "stage_finished", stage=stage, success=len(ok), failed=len(errors))
    return ok, errors


def write_run_config(root: Path, config: dict[str, Any]) -> None:
    lines = [
        "# RUN CONFIG", "", f"- 任务：{config['agent_display']} 所有 clean case 的 RIPPLE mutation 批量实验",
        f"- Run ID：`{config['run_id']}`", f"- 启动时间：`{config['started_at']}`",
        f"- 工作目录：`{ROOT}`", f"- 输入：`{CASES}`（{config['total']} cases）",
        f"- Mutation：K=5；Level 1 优先，Level 1 不足时由 Level 2 补齐；operator={','.join(config['operators'])}",
        "- 模型/API：selector gpt-5.6-luna；local mutation gpt-5.6-terra medium；"
        f"inference {config['agent_display']} gpt-5.4-mini（API key 不落盘）",
        f"- 并发：每阶段 {config['workers']} case workers；每 case interface workers=1",
        f"- 阶段：{' -> '.join(config['stages'])}，阶段间 barrier",
        f"- 超时：单个 inference/evaluation 命令 {config['command_timeout_seconds']} 秒",
        "- 重试：模型网络错误最多 6 次指数退避；unchanged mutation 最多 3 次；"
        "case 阶段失败不盲目重跑，保留 failure log",
        "- 缓存：仅同一 batch 断点恢复；不复用其他 batch 的结果",
        f"- Evaluation：`{ROOT / 'RIPPLE/swe-bench-lite_interface.py'} evaluate`",
        f"- 输出：`{root}`", "",
    ]
    atomic_text(root / "RUN_CONFIG.md", "\n".join(lines))


def run_batch(args: argparse.Namespace) -> int:
    root = args.output.resolve()
    root.mkdir(parents=True, exist_ok=True)
    (root / "runs").mkdir(exist_ok=True)
    event_path = root / "events.jsonl"
    if event_path.exists() and event_path.stat().st_size and not args.resume:
        raise FileExistsError(f"non-empty batch requires --resume: {root}")
    if not event_path.exists():
        event_path.write_text("")
    items, preflight_failures = discover(root)
    if len(items) != EXPECTED_CASES:
        raise RuntimeError(f"expected {EXPECTED_CASES} clean cases, discovered {len(items)}")
    prior_config = read_json(root / "BATCH_CONFIG.json") if (root / "BATCH_CONFIG.json").exists() else None
    started = prior_config["started_at"] if prior_config else now()
    config = {
        "run_id": root.name, "started_at": started, "total": len(items),
        "agent": AGENT, "agent_display": AGENT_DISPLAY, "cases": str(CASES),
        "workers": args.workers, "k": K, "levels": list(LEVELS),
        "selection": "Level 1 first; Level 2 fills shortage", "operators": list(OPERATORS),
        "stages": list(STAGES), "command_timeout_seconds": args.command_timeout,
        "case_list": items, "preflight_failures": preflight_failures,
    }
    if not (root / "BATCH_CONFIG.json").exists():
        atomic_json(root / "BATCH_CONFIG.json", config)
        write_run_config(root, config)
    atomic_json(root / "process.json", {
        "pid": os.getpid(), "started_at": started, "tmux_session": args.tmux_session,
        "log": str((root / args.run_log).resolve()), "monitor_pid": args.monitor_pid,
    })
    append_event(root, "batch_started", total=len(items), workers=args.workers, resume=args.resume)
    failed_ids = set()
    all_errors: dict[str, str] = {}
    for failure in preflight_failures:
        iid = failure["instance_id"]
        failed_ids.add(iid)
        all_errors[iid] = "; ".join(failure["reasons"])
        append_event(root, "preflight_failed", **failure)
    active = [item for item in items if item["instance_id"] not in failed_ids]
    stage_functions = {
        "mutation": mutation_resumable, "inference": inference_stage,
        "evaluation": evaluation_stage,
    }
    for stage in STAGES:
        active, stage_errors = execute_stage(
            root, stage, stage_functions[stage], active, args.workers,
        )
        all_errors.update(stage_errors)
    results = []
    for item in items:
        error = all_errors.get(item["instance_id"])
        try:
            result = finalize(item, error)
        except Exception as exc:
            error = error or f"finalize {type(exc).__name__}: {exc}"
            result = {"instance_id": item["instance_id"], "run_root": item["run_root"],
                      "error": error, "restored": False}
            atomic_text(Path(item["run_root"]) / "FINALIZE_FAILURE.log", traceback.format_exc())
        results.append(result)
        append_event(root, "case_finalized", instance_id=item["instance_id"], error=error,
                     restored=result.get("restored"))
    counts = [result["mutation_count"] for result in results if "mutation_count" in result]
    summary = {
        "run_id": root.name, "started_at": started, "finished_at": now(),
        "total": len(items), "success": sum(not result.get("error") for result in results),
        "failed": sum(bool(result.get("error")) for result in results),
        "mutation_location_stats": ({"min": min(counts), "max": max(counts),
                                     "mean": statistics.mean(counts)} if counts else None),
        "results": results,
    }
    atomic_json(root / "BATCH_SUMMARY.json", summary)
    exit_code = 1 if summary["failed"] else 0
    append_event(root, "batch_finished", exit_code=exit_code,
                 success=summary["success"], failed=summary["failed"])
    return exit_code


def initialize(output: Path, workers: int, command_timeout: int) -> int:
    root = output.resolve()
    root.mkdir(parents=True, exist_ok=False)
    (root / "runs").mkdir()
    items, failures = discover(root)
    if len(items) != EXPECTED_CASES:
        raise RuntimeError(f"expected {EXPECTED_CASES} clean cases, discovered {len(items)}")
    config = {
        "run_id": root.name, "started_at": now(), "total": len(items),
        "agent": AGENT, "agent_display": AGENT_DISPLAY, "cases": str(CASES),
        "workers": workers, "k": K, "levels": list(LEVELS),
        "selection": "Level 1 first; Level 2 fills shortage", "operators": list(OPERATORS),
        "stages": list(STAGES), "command_timeout_seconds": command_timeout,
        "case_list": items, "preflight_failures": failures,
    }
    atomic_json(root / "BATCH_CONFIG.json", config)
    write_run_config(root, config)
    (root / "events.jsonl").write_text("")
    (root / "RUN.log").write_text("")
    print(root)
    return 0


def preflight(output: Path) -> int:
    items, failures = discover(output.resolve())
    report = {"total": len(items), "eligible": len(items) - len(failures),
              "failures": failures, "repo_counts": {}}
    for item in items:
        report["repo_counts"][item["repo_slug"]] = report["repo_counts"].get(item["repo_slug"], 0) + 1
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if len(items) == EXPECTED_CASES else 1


def configure_agent(agent: str) -> None:
    global AGENT, AGENT_DISPLAY, CASES, EXPECTED_CASES
    settings = {
        "codex": ("Codex", "Codex", 149),
        "sweagent": ("SWE-Agent", "SWE-Agent", 74),
        "opencode": ("OpenCode", "OpenCode", 144),
    }
    AGENT = agent
    directory, AGENT_DISPLAY, EXPECTED_CASES = settings[agent]
    CASES = ROOT / "original_passed_cases" / directory / "gpt54mini_lite" / "cases"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--agent", choices=("codex", "sweagent", "opencode"), default="codex")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--command-timeout", type=int, default=4 * 60 * 60)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--initialize", action="store_true")
    parser.add_argument("--preflight", action="store_true")
    parser.add_argument("--monitor", action="store_true")
    parser.add_argument("--monitor-interval", type=int, default=20)
    parser.add_argument("--tmux-session")
    parser.add_argument("--monitor-pid", type=int)
    parser.add_argument("--run-log", default="RUN.log")
    args = parser.parse_args()
    configure_agent(args.agent)
    if args.initialize:
        return initialize(args.output, args.workers, args.command_timeout)
    if args.preflight:
        return preflight(args.output)
    if args.monitor:
        return monitor(args.output.resolve(), args.monitor_interval)
    os.environ["RIPPLE_COMMAND_TIMEOUT_SECONDS"] = str(args.command_timeout)
    return run_batch(args)


if __name__ == "__main__":
    raise SystemExit(main())
