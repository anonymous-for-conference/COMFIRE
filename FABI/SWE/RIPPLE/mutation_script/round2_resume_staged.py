#!/usr/bin/env python3
"""Resume round-two inference/evaluation with per-agent concurrency limits."""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import datetime as dt
import hashlib
import json
import os
import signal
import subprocess
import sys
import threading
import time
import traceback
from pathlib import Path

ROOT = Path("/data/zlyuaj/coding_agent/EviFuzz")
INTERFACE = ROOT / "RIPPLE/swe-bench-lite_interface.py"
API_KEY = "sk-de21c76052d94acbbc3011a71629f36d"
BASE_URL = "https://rightapi.ai/codex/v1"
AGENTS = ("codex", "sweagent", "opencode")
WORKERS = {"codex": 2, "sweagent": 1, "opencode": 2}
COMMAND_TIMEOUT = 4 * 60 * 60


def now() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def atomic_json(path: Path, value: object) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    temporary.replace(path)


def instance_id(run: Path) -> str:
    manifest = run / "mutation/manifest.json"
    if manifest.is_file():
        try:
            return json.loads(manifest.read_text())["instance_id"]
        except (KeyError, OSError, json.JSONDecodeError):
            pass
    return run.name.split("_", 1)[1]


def valid_prediction(run: Path) -> bool:
    path = run / "interface/predictions.jsonl"
    try:
        rows = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
        return (len(rows) == 1 and rows[0].get("instance_id") == instance_id(run)
                and isinstance(rows[0].get("model_patch"), str))
    except (OSError, ValueError, json.JSONDecodeError, IndexError):
        return False


def valid_evaluation(run: Path) -> bool:
    path = run / "interface/evaluation_summary/official_summary.json"
    try:
        summary = json.loads(path.read_text())
        return instance_id(run) in summary.get("completed_ids", [])
    except (OSError, ValueError, json.JSONDecodeError):
        return False


def discover(main: Path, retry: Path, repair: Path) -> dict[tuple[str, str], Path]:
    selected: dict[tuple[str, str], Path] = {}
    for base in (main, retry, repair):
        for agent in AGENTS:
            runs = base / agent / "runs"
            if not runs.is_dir():
                continue
            for run in sorted(runs.iterdir()):
                if not run.is_dir():
                    continue
                key = (agent, instance_id(run))
                current = selected.get(key)
                if base == repair or (run / "mutation/manifest.json").is_file() or current is None:
                    selected[key] = run
    return selected


def wait_for_manifest(run: Path, timeout: int = 2 * 60 * 60) -> None:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if (run / "mutation/manifest.json").is_file() and (run / "mutation/mutation.patch").is_file():
            return
        time.sleep(15)
    raise TimeoutError(f"mutation manifest did not appear within {timeout}s: {run}")


def run_command(command: list[str], log: Path, env: dict[str, str] | None = None) -> None:
    with log.open("a") as handle:
        proc = subprocess.Popen(command, stdout=handle, stderr=subprocess.STDOUT,
                                env=env, start_new_session=True)
        try:
            returncode = proc.wait(timeout=COMMAND_TIMEOUT)
        except subprocess.TimeoutExpired:
            os.killpg(proc.pid, signal.SIGTERM)
            try:
                proc.wait(timeout=30)
            except subprocess.TimeoutExpired:
                os.killpg(proc.pid, signal.SIGKILL)
            raise TimeoutError(f"command exceeded {COMMAND_TIMEOUT}s")
    if returncode:
        raise RuntimeError(f"command exited {returncode}; see {log}")


def archive_incomplete_interface(run: Path, attempt: int) -> None:
    interface = run / "interface"
    if interface.exists() and not valid_prediction(run):
        destination = run / f"interface_incomplete_before_resume_{attempt:02d}"
        suffix = 1
        while destination.exists():
            destination = run / f"interface_incomplete_before_resume_{attempt:02d}_{suffix:02d}"
            suffix += 1
        interface.rename(destination)


def prepare_mutated_repo(run: Path) -> tuple[Path, str]:
    source = json.loads((run / "source_repo.json").read_text())
    commit = source["base_commit"]
    repo = run / "worktree"
    subprocess.run(["git", "reset", "--hard", commit], cwd=repo, check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["git", "clean", "-fd"], cwd=repo, check=True,
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["git", "apply", str(run / "mutation/mutation.patch")], cwd=repo,
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return repo, commit


def socket_path(run: Path, stage: str, attempt: int) -> str:
    token = hashlib.sha256(f"{run}:{stage}:{attempt}".encode()).hexdigest()[:16]
    return f"/tmp/ripple-r2r-{token}.sock"


def infer(agent: str, run: Path, emit) -> None:
    wait_for_manifest(run)
    if valid_prediction(run):
        return
    iid = instance_id(run)
    for attempt in (1, 2):
        emit("inference", "attempt_started", agent, iid, run, attempt=attempt)
        archive_incomplete_interface(run, attempt)
        repo = None
        commit = None
        try:
            repo, commit = prepare_mutated_repo(run)
            env = os.environ.copy()
            env.update({"OPENAI_API_KEY": API_KEY, "OPENAI_BASE_URL": BASE_URL})
            command = [sys.executable, str(INTERFACE), "run", "--agent", agent,
                       "--repo-map", str(run / "repo_map.json"), "--output", str(run / "interface"),
                       "--ids", iid, "--run", "1", "--workers", "1",
                       "--socket", socket_path(run, "inference", attempt), "--inference-only"]
            run_command(command, run / f"INFERENCE_RESUME_attempt_{attempt:02d}.log", env)
            if not valid_prediction(run):
                raise RuntimeError("inference returned without a valid one-row prediction")
            emit("inference", "success", agent, iid, run, attempt=attempt)
            return
        except Exception as exc:
            (run / f"INFERENCE_RESUME_attempt_{attempt:02d}.failure.log").write_text(
                traceback.format_exc())
            emit("inference", "attempt_failed", agent, iid, run, attempt=attempt,
                 error=f"{type(exc).__name__}: {exc}")
            if attempt == 2:
                raise
        finally:
            if repo is not None and commit is not None:
                subprocess.run(["git", "reset", "--hard", commit], cwd=repo,
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                subprocess.run(["git", "clean", "-fd"], cwd=repo,
                               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def evaluate(agent: str, run: Path, emit) -> None:
    if valid_evaluation(run):
        return
    iid = instance_id(run)
    for attempt in (1, 2):
        emit("evaluation", "attempt_started", agent, iid, run, attempt=attempt)
        try:
            command = [sys.executable, str(INTERFACE), "evaluate", "--agent", agent,
                       "--output", str(run / "interface"), "--run", "1", "--workers", "1",
                       "--socket", socket_path(run, "evaluation", attempt),
                       "--mutation-patch", str(run / "mutation/mutation.patch"),
                       "--repo", str(run / "worktree")]
            run_command(command, run / f"EVALUATION_RESUME_attempt_{attempt:02d}.log")
            if not valid_evaluation(run):
                raise RuntimeError("official evaluation did not complete the target instance")
            emit("evaluation", "success", agent, iid, run, attempt=attempt)
            return
        except Exception as exc:
            (run / f"EVALUATION_RESUME_attempt_{attempt:02d}.failure.log").write_text(
                traceback.format_exc())
            emit("evaluation", "attempt_failed", agent, iid, run, attempt=attempt,
                 error=f"{type(exc).__name__}: {exc}")
            if attempt == 2:
                raise


def run_pool(stage: str, jobs: list[tuple[str, Path]], function, emit) -> dict[str, str]:
    errors: dict[str, str] = {}
    groups = {agent: [(agent, run) for selected_agent, run in jobs if selected_agent == agent]
              for agent in AGENTS}
    chunks = []
    for agent in AGENTS:
        count = WORKERS[agent]
        chunks.extend(groups[agent][index::count] for index in range(count))

    def worker(chunk):
        for agent, run in chunk:
            iid = instance_id(run)
            try:
                function(agent, run, emit)
            except Exception as exc:
                errors[f"{agent}:{iid}"] = f"{type(exc).__name__}: {exc}"
                emit(stage, "failed", agent, iid, run, error=errors[f"{agent}:{iid}"])

    with cf.ThreadPoolExecutor(max_workers=sum(WORKERS.values())) as executor:
        list(executor.map(worker, chunks))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--main", type=Path, required=True)
    parser.add_argument("--retry", type=Path, required=True)
    parser.add_argument("--repair", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.main = args.main.resolve()
    args.retry = args.retry.resolve()
    args.repair = args.repair.resolve()
    args.output = args.output.resolve()
    output = args.output
    output.mkdir(parents=True, exist_ok=True)
    started_at = now()
    events_lock = threading.Lock()

    def emit(stage, event, agent, iid, run, **extra):
        row = {"time": now(), "stage": stage, "event": event, "agent": agent,
               "instance_id": iid, "run_root": str(run), **extra}
        with events_lock, (output / "events.jsonl").open("a") as handle:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
            handle.flush()

    selected = discover(args.main, args.retry, args.repair)
    expected_repair = ("codex", "sympy__sympy-18532")
    deadline = time.monotonic() + 120
    while expected_repair not in selected and time.monotonic() < deadline:
        time.sleep(2)
        selected = discover(args.main, args.retry, args.repair)
    if expected_repair not in selected:
        raise RuntimeError("repair mutation run directory was not created within 120 seconds")
    if len(selected) != 312:
        raise RuntimeError(f"expected 312 unique agent/case pairs, found {len(selected)}")

    prediction_cache = {key for key, run in selected.items() if valid_prediction(run)}
    inference_jobs = [(agent, run) for (agent, iid), run in selected.items()
                      if (agent, iid) not in prediction_cache]
    config = {
        "run_id": output.name, "started_at": started_at,
        "task": "round-two missing inference resume, followed by missing official evaluation",
        "working_directory": str(ROOT), "inputs": [str(args.main), str(args.retry), str(args.repair)],
        "model": "gpt-5.4-mini", "api_config": "RightAPI codex endpoint (key omitted)",
        "base_url": BASE_URL, "worker_counts": WORKERS, "command_timeout_seconds": COMMAND_TIMEOUT,
        "retry_limit": 2, "cache_policy": "valid one-row predictions and completed official evaluations",
        "total_cases": len(selected), "prediction_cache_hit": len(prediction_cache),
        "per_agent_total": {agent: sum(key[0] == agent for key in selected) for agent in AGENTS},
        "per_agent_prediction_cache_hit": {
            agent: sum(key[0] == agent for key in prediction_cache) for agent in AGENTS
        },
        "inference_execute_this_run": len(inference_jobs), "output_dir": str(output),
    }
    atomic_json(output / "RUN_CONFIG.json", config)
    (output / "RUN_CONFIG.md").write_text(
        "# Round 2 Resume Configuration\n\n" +
        "\n".join(f"- {key}: `{value}`" for key, value in config.items()) + "\n")
    (output / "RUN.log").write_text(
        f"{started_at} start; inference jobs={len(inference_jobs)}; cache={len(prediction_cache)}\n")
    atomic_json(output / "status.json", {
        "updated_at": now(), "phase": "inference", "started_at": started_at,
        "completed": len(prediction_cache), "total": len(selected),
        "remaining": len(inference_jobs), "success": len(prediction_cache), "failed": 0,
        "errors": 0, "eta": "unknown", "pid": os.getpid(),
        "log": str(output / "RUN.log"), "output_dir": str(output),
        "cache_hit": len(prediction_cache), "executed_this_run": 0,
    })
    inference_errors = run_pool("inference", inference_jobs, infer, emit)
    missing = [f"{agent}:{iid}" for (agent, iid), run in selected.items() if not valid_prediction(run)]
    if missing:
        atomic_json(output / "FINAL_SUMMARY.json", {"finished_at": now(),
                    "phase": "inference_failed", "missing_predictions": missing,
                    "errors": inference_errors})
        return 1

    evaluation_cache = {key for key, run in selected.items() if valid_evaluation(run)}
    evaluation_jobs = [(agent, run) for (agent, iid), run in selected.items()
                       if (agent, iid) not in evaluation_cache]
    emit("barrier", "all_predictions_valid", "all", "all", output,
         predictions=len(selected), evaluation_cache_hit=len(evaluation_cache),
         evaluation_jobs=len(evaluation_jobs))
    evaluation_errors = run_pool("evaluation", evaluation_jobs, evaluate, emit)
    missing_eval = [f"{agent}:{iid}" for (agent, iid), run in selected.items()
                    if not valid_evaluation(run)]
    summary = {"finished_at": now(), "phase": "completed" if not missing_eval else "evaluation_failed",
               "total": len(selected), "valid_predictions": len(selected),
               "evaluation_cache_hit": len(evaluation_cache),
               "evaluation_executed_this_run": len(evaluation_jobs),
               "missing_evaluations": missing_eval,
               "inference_errors": inference_errors, "evaluation_errors": evaluation_errors}
    atomic_json(output / "FINAL_SUMMARY.json", summary)
    return 0 if not missing_eval else 1


if __name__ == "__main__":
    raise SystemExit(main())
