#!/usr/bin/env python3
"""Strict two-stage enhancement experiment: all inference, then all evaluation."""

from __future__ import annotations

import argparse
import concurrent.futures as futures
import datetime as dt
import hashlib
import json
import os
import shutil
import subprocess
import sys
import threading
import time
import traceback
from pathlib import Path
from typing import Any, Callable

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from metrics import extract
from run_experiment import (
    AGENTS, BASE_URL, INTERFACE, MODEL, OUTPUT_DEFAULT, REQUESTED_ENDPOINT,
    aggregate, atomic_json, combine_prediction, command, discover, emit,
    excluded_inputs, now, prepare, read_json, resolved, restore, socket_path,
)
from strategies import STRATEGIES, prompt_for

COMPOSITION_VERSION = 2
REMOVE_DOCS_NO_MUTATION_VERSION = 3
status_lock = threading.Lock()


def run_path(output: Path, item: dict[str, str], strategy: str) -> Path:
    return output / strategy / item["round"] / item["agent"] / item["run_name"]


def job_id(item: dict[str, str], strategy: str) -> str:
    return f"{strategy}:{item['round']}:{item['agent']}:{item['instance_id']}"


def environment(item: dict[str, str], strategy: str, api_key: str) -> dict[str, str]:
    value = os.environ.copy()
    value.update({
        "OPENAI_API_KEY": api_key, "OPENAI_BASE_URL": BASE_URL,
        "EVIFUZZ_MODEL": MODEL, "EVIFUZZ_SYSTEM_PROMPT": prompt_for(strategy),
        "EVIFUZZ_MUTATION_HOOK": str(HERE / "doc_filter.py"),
        "EVIFUZZ_MUTATION_SOURCE_AGENT": item["agent"],
        "EVIFUZZ_COMMIT_BASELINE": "1", "RIPPLE_ENHANCEMENT_STRATEGY": strategy,
        "EVIFUZZ_MAX_ATTEMPTS": "3", "VERIFIED_MAX_ATTEMPTS": "3",
    })
    return value


def composition_valid(run: Path, strategy: str) -> bool:
    required = (run / "combined.patch", run / "agent.patch", run / "interface/agent_predictions.jsonl")
    if not all(path.is_file() and path.stat().st_size for path in required):
        return False
    if strategy != "remove_docs":
        return True
    metadata = run / "composition.json"
    return metadata.is_file() and read_json(metadata).get("version") in {
        COMPOSITION_VERSION, REMOVE_DOCS_NO_MUTATION_VERSION,
    }


def archive_incomplete(output: Path, run: Path, reason: str) -> None:
    if not run.exists():
        return
    relative = run.relative_to(output)
    stamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    destination = output / "history_pre_staged" / relative.parent / f"{relative.name}_{stamp}"
    destination.parent.mkdir(parents=True, exist_ok=True)
    run.rename(destination)
    atomic_json(destination / "ARCHIVE_REASON.json", {"time": now(), "reason": reason, "original": str(run)})


def infer_one(output: Path, item: dict[str, str], strategy: str, api_key: str,
              timeout: int, attempt: int) -> dict[str, Any]:
    run = run_path(output, item, strategy)
    if composition_valid(run, strategy):
        if not (run / "inference_result.json").exists():
            atomic_json(run / "inference_result.json", {
                "phase": "inference_complete", "cached_from_prebarrier_run": True,
                "composition_version": COMPOSITION_VERSION if strategy == "remove_docs" else 1,
                "time": now(), "job_id": job_id(item, strategy),
            })
        return {"job_id": job_id(item, strategy), "run_root": str(run), "cached": True}
    prediction = run / "interface/predictions.jsonl"
    repo = run / "worktree"
    if strategy != "remove_docs" and prediction.is_file() and (run / "mutation.patch").is_file() and (repo / ".git").is_dir():
        try:
            rows = [json.loads(line) for line in prediction.read_text().splitlines() if line.strip()]
            if len(rows) == 1 and rows[0].get("model_patch", "").strip():
                combine_prediction(run, item, repo)
                restore(run, item, repo)
                atomic_json(run / "composition.json", {
                    "version": COMPOSITION_VERSION, "strategy": strategy,
                    "method": "recovered completed inference, direct Agent delta over mutation",
                    "time": now(),
                })
                result = {"phase": "inference_complete", "recovered_after_stop": True,
                          "composition_version": COMPOSITION_VERSION, "time": now(),
                          "job_id": job_id(item, strategy), "run_root": str(run)}
                atomic_json(run / "inference_result.json", result)
                return result
        except Exception:
            # Preserve the failed recovery with the rest of the interrupted run
            # and execute a fresh inference attempt below.
            pass
    if run.exists():
        archive_incomplete(output, run, "inference artifact absent or obsolete composition")
    run.mkdir(parents=True, exist_ok=True)
    repo: Path | None = None
    emit(output, event="inference_started", stage_attempt=attempt, strategy=strategy, **item)
    try:
        apply_mutation = strategy != "remove_docs"
        repo = prepare(item, run, apply_mutation=apply_mutation)
        env = environment(item, strategy, api_key)
        env["SWE_CASE_TIMEOUT"] = str(timeout)
        env["EVIFUZZ_RUN_ID"] = "ripple-enh-inf-" + hashlib.sha256(job_id(item, strategy).encode()).hexdigest()[:20]
        command([
            sys.executable, str(INTERFACE), "run", "--agent", item["agent"],
            "--repo-map", str(run / "repo_map.json"), "--output", str(run / "interface"),
            "--ids", item["instance_id"], "--run", "1", "--workers", "1",
            "--socket", socket_path(run, f"inference-{attempt}"), "--inference-only",
        ], run / f"INFERENCE_attempt_{attempt:02d}.log", env, timeout + 900)
        combine_prediction(run, item, repo, apply_mutation=apply_mutation)
        composition_version = (
            REMOVE_DOCS_NO_MUTATION_VERSION if strategy == "remove_docs"
            else COMPOSITION_VERSION
        )
        atomic_json(run / "composition.json", {
            "version": composition_version, "strategy": strategy,
            "method": "documentation-free inference on original base; replay Agent delta only" if strategy == "remove_docs" else "direct Agent delta over mutation",
            "mutation_applied": apply_mutation,
            "mutation_patch": str(run / "mutation.patch") if apply_mutation else None,
            "agent_patch": str(run / "agent.patch"),
            "combined_patch": str(run / "combined.patch"), "time": now(),
        })
        result = {"phase": "inference_complete", "cached_from_prebarrier_run": False,
                  "composition_version": composition_version, "time": now(),
                  "job_id": job_id(item, strategy), "run_root": str(run)}
        atomic_json(run / "inference_result.json", result)
        emit(output, event="inference_finished", stage_attempt=attempt, strategy=strategy, **item)
        return result
    except Exception as exc:
        atomic_json(run / "inference_failure.json", {
            "time": now(), "attempt": attempt, "error": f"{type(exc).__name__}: {exc}",
            "traceback": traceback.format_exc(),
        })
        emit(output, event="inference_attempt_failed", stage_attempt=attempt,
             error=f"{type(exc).__name__}: {exc}", strategy=strategy, **item)
        raise
    finally:
        if repo is not None and (repo / ".git").exists():
            restore(run, item, repo)


def evaluate_one(output: Path, item: dict[str, str], strategy: str, api_key: str,
                 timeout: int, attempt: int) -> dict[str, Any]:
    run = run_path(output, item, strategy)
    formal = run / "formal_evaluation.json"
    if formal.is_file() and read_json(formal).get("phase") == "completed":
        return read_json(formal)
    if not composition_valid(run, strategy):
        raise RuntimeError(f"evaluation blocked by missing inference artifact: {run}")
    interface = run / "interface"
    rows = [json.loads(line) for line in (interface / "agent_predictions.jsonl").read_text().splitlines() if line.strip()]
    if len(rows) != 1:
        raise RuntimeError("saved Agent prediction cardinality is not one")
    rows[0]["model_patch"] = (run / "combined.patch").read_text()
    (interface / "predictions.jsonl").write_text(json.dumps(rows[0], ensure_ascii=False) + "\n")
    env = environment(item, strategy, api_key)
    run_id = "ripple-enh-eval-" + hashlib.sha256(f"{job_id(item, strategy)}:{attempt}".encode()).hexdigest()[:20]
    env.update({"EVIFUZZ_RUN_ID": run_id, "SWE_EVALUATION_PREDICTIONS": str(interface / "predictions.jsonl")})
    emit(output, event="evaluation_started", stage_attempt=attempt, strategy=strategy, **item)
    try:
        command([
            sys.executable, str(INTERFACE), "evaluate", "--agent", item["agent"],
            "--output", str(interface), "--run", "1", "--workers", "1",
            "--socket", socket_path(run, f"formal-evaluation-{attempt}"),
        ], run / f"FORMAL_EVALUATION_attempt_{attempt:02d}.log", env, timeout)
        outcome = resolved(interface, item["instance_id"])
        if outcome is None:
            raise RuntimeError("official evaluation omitted target instance")
        metric = extract(run, item["agent"])
        result = {
            **item, "strategy": strategy, "phase": "completed", "resolved": outcome,
            "error": None, **metric, "run_root": str(run), "finished_at": now(),
            "formal_post_barrier_evaluation": True, "evaluation_attempt": attempt,
        }
        atomic_json(run / "result.json", result)
        atomic_json(formal, result)
        emit(output, event="evaluation_finished", stage_attempt=attempt, strategy=strategy,
             resolved=outcome, **item)
        return result
    except Exception as exc:
        atomic_json(run / f"formal_evaluation_failure_attempt_{attempt:02d}.json", {
            "time": now(), "error": f"{type(exc).__name__}: {exc}",
            "traceback": traceback.format_exc(),
        })
        emit(output, event="evaluation_attempt_failed", stage_attempt=attempt,
             error=f"{type(exc).__name__}: {exc}", strategy=strategy, **item)
        raise


def write_status(output: Path, base: dict[str, Any], phase: str, completed: int,
                 total: int, errors: int, last_error: str | None = None) -> None:
    with status_lock:
        atomic_json(output / "status.json", {
            **base, "updated_at": now(), "phase": phase, "completed": completed,
            "total": total, "remaining": max(0, total - completed),
            "success": completed, "failed": 0, "errors": errors, "eta": "unknown",
            "last_error": last_error,
        })


def run_stage(output: Path, jobs: list[tuple[dict[str, str], str]], name: str,
              worker_count: int, attempts: int, function: Callable, base_status: dict[str, Any],
              api_key: str, timeout: int) -> tuple[bool, dict[str, str]]:
    done: set[str] = set()
    errors: dict[str, str] = {}
    pending = jobs[:]
    for attempt in range(1, attempts + 1):
        errors = {}
        with futures.ThreadPoolExecutor(max_workers=worker_count) as pool:
            submitted = {
                pool.submit(function, output, item, strategy, api_key, timeout, attempt): (item, strategy)
                for item, strategy in pending
            }
            for future in futures.as_completed(submitted):
                item, strategy = submitted[future]
                identifier = job_id(item, strategy)
                try:
                    future.result(); done.add(identifier)
                except Exception as exc:
                    errors[identifier] = f"{type(exc).__name__}: {exc}"
                write_status(output, base_status, name, len(done), len(jobs), len(errors),
                             errors.get(identifier))
        if not errors:
            return True, {}
        pending = [(item, strategy) for item, strategy in jobs if job_id(item, strategy) in errors]
        if attempt < attempts:
            emit(output, event=f"{name}_retry_barrier", failed=len(pending), next_attempt=attempt + 1)
    return False, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT_DEFAULT)
    parser.add_argument("--strategies", default=",".join(STRATEGIES))
    parser.add_argument("--rounds", default="round1,round2")
    parser.add_argument("--agents", default=",".join(AGENTS))
    parser.add_argument("--inference-workers", type=int, default=3)
    parser.add_argument("--evaluation-workers", type=int, default=1)
    parser.add_argument("--case-timeout", type=int, default=3600)
    parser.add_argument("--api-key-env", default="RIPPLE_ENHANCEMENT_API_KEY")
    args = parser.parse_args()
    output = args.output.resolve(); output.mkdir(parents=True, exist_ok=True)
    api_key = os.environ.get(args.api_key_env, "").strip()
    if not api_key:
        raise RuntimeError(f"API key must be supplied through {args.api_key_env}")
    strategies = tuple(x for x in args.strategies.split(",") if x)
    rounds = tuple(x for x in args.rounds.split(",") if x)
    agents = tuple(x for x in args.agents.split(",") if x)
    items = discover(rounds, agents)
    excluded = excluded_inputs(rounds, agents)
    jobs = [(item, strategy) for index, item in enumerate(items)
            for strategy in strategies[index % len(strategies):] + strategies[:index % len(strategies)]]
    # Previous per-case evaluations are retained but are not formal results for
    # the strict post-inference-barrier protocol.
    for item, strategy in jobs:
        run = run_path(output, item, strategy)
        result = run / "result.json"
        if result.exists() and not (run / "formal_evaluation.json").exists():
            result.replace(run / "prebarrier_result.json")
    started = now()
    config = {
        "task": "strict staged documentation mitigation rerun", "run_id": output.name,
        "started_at": started, "model": MODEL, "requested_endpoint": REQUESTED_ENDPOINT,
        "client_base_url": BASE_URL, "api_key": "omitted", "source_failure_records": len(items),
        "excluded_pre_inference_failures": len(excluded), "strategies": strategies,
        "total_jobs": len(jobs), "inference_workers": args.inference_workers,
        "evaluation_workers": args.evaluation_workers, "case_timeout_seconds": args.case_timeout,
        "stage_order": ["all_inference", "validated_barrier", "all_official_evaluation"],
        "output_dir": str(output),
    }
    atomic_json(output / "RUN_CONFIG_STAGED.json", config)
    (output / "RUN_CONFIG_STAGED.md").write_text(
        "# Strict staged enhancement run\n\n" + "\n".join(f"- {key}: `{value}`" for key, value in config.items()) + "\n")
    atomic_json(output / "EXCLUDED_INPUTS.json", excluded)
    base_status = {
        "started_at": started, "pid": os.getpid(), "log": str(output / "RUN.log"),
        "output_dir": str(output), "inference_total": len(jobs), "evaluation_total": len(jobs),
    }
    write_status(output, base_status, "inference", 0, len(jobs), 0)
    ok, errors = run_stage(output, jobs, "inference", args.inference_workers, 3,
                           infer_one, base_status, api_key, args.case_timeout)
    if not ok:
        atomic_json(output / "INFERENCE_BLOCKERS.json", errors)
        write_status(output, base_status, "inference_blocked", len(jobs) - len(errors), len(jobs), len(errors),
                     "evaluation not started because inference barrier is incomplete")
        return 1
    barrier_rows = []
    for item, strategy in jobs:
        run = run_path(output, item, strategy)
        barrier_rows.append({
            "job_id": job_id(item, strategy), "combined_patch": str(run / "combined.patch"),
            "sha256": hashlib.sha256((run / "combined.patch").read_bytes()).hexdigest(),
        })
    atomic_json(output / "INFERENCE_BARRIER.json", {
        "time": now(), "valid": len(barrier_rows) == len(jobs), "count": len(barrier_rows),
        "expected": len(jobs), "jobs": barrier_rows,
    })
    emit(output, event="inference_barrier_complete", count=len(barrier_rows))
    write_status(output, base_status, "evaluation", 0, len(jobs), 0)
    ok, errors = run_stage(output, jobs, "evaluation", args.evaluation_workers, 3,
                           evaluate_one, base_status, api_key, args.case_timeout)
    if not ok:
        atomic_json(output / "EVALUATION_BLOCKERS.json", errors)
        write_status(output, base_status, "evaluation_blocked", len(jobs) - len(errors), len(jobs), len(errors))
        aggregate(output, len(jobs))
        return 1
    aggregate(output, len(jobs))
    write_status(output, {**base_status, "finished_at": now()}, "completed", len(jobs), len(jobs), 0)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
