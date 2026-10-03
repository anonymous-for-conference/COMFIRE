#!/usr/bin/env python3
"""Rerun every archived mutation failure under four documentation mitigations."""

from __future__ import annotations

import argparse
import concurrent.futures as futures
import csv
import datetime as dt
import hashlib
import json
import os
import shutil
import signal
import subprocess
import sys
import tempfile
import threading
import time
import traceback
from pathlib import Path
from typing import Any

HERE = Path(__file__).resolve().parent
RIPPLE = HERE.parents[1]
ARCHIVE = RIPPLE / "mutation_result/local4r1_repo4r2/two_round_result"
OUTPUT_DEFAULT = RIPPLE / "mutation_result/enhancement"
INTERFACE = RIPPLE / "swe-bench-lite_interface.py"
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(RIPPLE / "mutation_script"))

from doc_filter import strip_repository  # noqa: E402
from experiment import prepare_local_worktree  # noqa: E402
from metrics import extract  # noqa: E402
from strategies import STRATEGIES, prompt_for  # noqa: E402

MODEL = "gpt-5.4-mini-ca"
REQUESTED_ENDPOINT = "https://api.chatanywhere.tech/v1/chat/completions"
BASE_URL = "https://api.chatanywhere.tech/v1"
AGENTS = ("codex", "opencode", "sweagent")
write_lock = threading.Lock()


def now() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def atomic_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    temporary.replace(path)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text())


def emit(output: Path, **event: object) -> None:
    row = {"time": now(), **event}
    with write_lock, (output / "events.jsonl").open("a") as handle:
        handle.write(json.dumps(row, ensure_ascii=False) + "\n")
        handle.flush()


def discover(rounds: tuple[str, ...], agents: tuple[str, ...]) -> list[dict[str, str]]:
    items: list[dict[str, str]] = []
    for round_name in rounds:
        for agent in agents:
            parent = ARCHIVE / round_name / "error" / agent
            for source in sorted(parent.iterdir() if parent.exists() else []):
                if not source.is_dir() or not (source / "mutation/mutation.patch").is_file():
                    continue
                manifest = read_json(source / "mutation/manifest.json")
                source_repo = read_json(source / "source_repo.json")
                items.append({
                    "round": round_name, "agent": agent,
                    "instance_id": manifest["instance_id"], "source": str(source),
                    "base_repo": source_repo["base_repo"], "base_commit": source_repo["base_commit"],
                    "run_name": source.name,
                })
    return items


def excluded_inputs(rounds: tuple[str, ...], agents: tuple[str, ...]) -> list[dict[str, object]]:
    excluded: list[dict[str, object]] = []
    for round_name in rounds:
        for agent in agents:
            parent = ARCHIVE / round_name / "error" / agent
            for source in sorted(parent.iterdir() if parent.exists() else []):
                if not source.is_dir() or (source / "mutation/mutation.patch").is_file():
                    continue
                status = read_json(source / "status.json") if (source / "status.json").is_file() else {}
                excluded.append({
                    "round": round_name, "agent": agent, "run_name": source.name,
                    "reason": "mutation stage did not produce mutation/mutation.patch; no post-mutation agent failure exists",
                    "source_phase": status.get("phase"), "source_error": status.get("error"),
                    "source": str(source),
                })
    return excluded


def command(command_line: list[str], log: Path, env: dict[str, str] | None = None,
            timeout: int = 4 * 60 * 60) -> None:
    log.parent.mkdir(parents=True, exist_ok=True)
    with log.open("a") as handle:
        process = subprocess.Popen(
            command_line, stdout=handle, stderr=subprocess.STDOUT, env=env,
            start_new_session=True,
        )
        try:
            returncode = process.wait(timeout=timeout)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.wait(timeout=30)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait(timeout=30)
            raise TimeoutError(f"command exceeded {timeout}s: {command_line[0]}")
    if returncode:
        raise RuntimeError(f"command returned {returncode}; see {log}")


def socket_path(run: Path, stage: str) -> str:
    digest = hashlib.sha256(f"{run}:{stage}".encode()).hexdigest()[:16]
    return f"/tmp/ripple-enh-{stage[:3]}-{digest}.sock"


def resolved(interface: Path, instance_id: str) -> bool | None:
    summary = interface / "evaluation_summary/official_summary.json"
    if not summary.is_file():
        return None
    data = read_json(summary)
    if instance_id in data.get("resolved_ids", []):
        return True
    if instance_id in data.get("unresolved_ids", []):
        return False
    return None


def prepare(item: dict[str, str], run: Path, apply_mutation: bool = True) -> Path:
    repo = prepare_local_worktree(run, Path(item["base_repo"]), item["base_commit"])
    if apply_mutation:
        mutation = Path(item["source"]) / "mutation/mutation.patch"
        shutil.copy2(mutation, run / "mutation.patch")
        shutil.copy2(Path(item["source"]) / "mutation/manifest.json", run / "mutation_manifest.json")
        subprocess.run(["git", "apply", str(run / "mutation.patch")], cwd=repo, check=True)
    atomic_json(run / "repo_map.json", {item["instance_id"]: str(repo)})
    atomic_json(run / "source.json", item)
    return repo


def replay_without_document_changes(repo: Path, base_commit: str,
                                    documentation_free_commit: str) -> None:
    """Merge Agent edits onto the original tree while preserving its docs."""
    changed = subprocess.check_output(
        ["git", "diff", "--name-only", "-z", documentation_free_commit, "--"],
        cwd=repo,
    ).split(b"\0")
    paths = [path.decode("utf-8", "surrogateescape") for path in changed if path]
    merged: dict[str, bytes | None] = {}
    with tempfile.TemporaryDirectory() as directory:
        scratch = Path(directory)
        for index, relative in enumerate(paths):
            current = repo / relative
            ancestor_result = subprocess.run(
                ["git", "show", f"{documentation_free_commit}:{relative}"], cwd=repo,
                stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
            )
            base_result = subprocess.run(
                ["git", "show", f"{base_commit}:{relative}"], cwd=repo,
                stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
            )
            if ancestor_result.returncode != 0:
                merged[relative] = current.read_bytes() if current.exists() else None
                continue
            if not current.exists():
                merged[relative] = (base_result.stdout if base_result.returncode == 0
                                    and base_result.stdout != ancestor_result.stdout else None)
                continue
            if base_result.returncode != 0:
                merged[relative] = current.read_bytes()
                continue
            base_lines = base_result.stdout.splitlines(keepends=True)
            ancestor_lines = ancestor_result.stdout.splitlines(keepends=True)
            agent_lines = current.read_bytes().splitlines(keepends=True)
            if len(base_lines) == len(ancestor_lines) == len(agent_lines):
                merged[relative] = b"".join(
                    original if original != stripped else agent
                    for original, stripped, agent in zip(
                        base_lines, ancestor_lines, agent_lines, strict=True,
                    )
                )
                continue
            ours = scratch / f"{index}.ours"
            ancestor = scratch / f"{index}.ancestor"
            theirs = scratch / f"{index}.theirs"
            ours.write_bytes(base_result.stdout)
            ancestor.write_bytes(ancestor_result.stdout)
            theirs.write_bytes(current.read_bytes())
            result = subprocess.run(
                ["git", "merge-file", "-p", "--ours", str(ours), str(ancestor), str(theirs)],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            )
            if result.returncode not in (0, 1):
                raise RuntimeError(
                    f"three-way Agent replay failed for {relative}: "
                    f"{result.stderr.decode(errors='replace').strip()}"
                )
            merged[relative] = result.stdout
    subprocess.run(["git", "reset", "--hard", base_commit], cwd=repo, check=True,
                   stdout=subprocess.DEVNULL)
    subprocess.run(["git", "clean", "-fd"], cwd=repo, check=True,
                   stdout=subprocess.DEVNULL)
    for relative, content in merged.items():
        path = repo / relative
        if content is None:
            path.unlink(missing_ok=True)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(content)


def combine_prediction(run: Path, item: dict[str, str], repo: Path,
                       apply_mutation: bool = True) -> None:
    predictions = run / "interface/predictions.jsonl"
    rows = [json.loads(line) for line in predictions.read_text().splitlines() if line.strip()]
    if len(rows) != 1 or not rows[0].get("model_patch", "").strip():
        raise RuntimeError("expected one non-empty agent-only prediction")
    agent_patch = run / "agent.patch"
    agent_patch.write_text(rows[0]["model_patch"])
    subprocess.run(["git", "reset", "--hard", item["base_commit"]], cwd=repo, check=True,
                   stdout=subprocess.DEVNULL)
    subprocess.run(["git", "clean", "-fd"], cwd=repo, check=True, stdout=subprocess.DEVNULL)
    if apply_mutation:
        subprocess.run(["git", "apply", str(run / "mutation.patch")], cwd=repo, check=True)
    if run.parts[-4] == "remove_docs":
        subprocess.run(["git", "add", "-A"], cwd=repo, check=True)
        commit_env = os.environ.copy()
        commit_env.update({
            "GIT_AUTHOR_NAME": "RIPPLE Enhancement", "GIT_AUTHOR_EMAIL": "ripple@localhost",
            "GIT_COMMITTER_NAME": "RIPPLE Enhancement", "GIT_COMMITTER_EMAIL": "ripple@localhost",
        })
        if apply_mutation:
            subprocess.run(["git", "commit", "-q", "-m", "mutation baseline"], cwd=repo, env=commit_env, check=True)
        mutation_commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip()
        strip_repository(repo)
        documentation_patch = run / "documentation_removal.patch"
        documentation_patch.write_bytes(subprocess.check_output(
            ["git", "diff", "--binary", "--unified=0", mutation_commit, "--"], cwd=repo,
        ))
        subprocess.run(["git", "add", "-A"], cwd=repo, check=True)
        subprocess.run(["git", "commit", "-q", "-m", "documentation-free inference baseline"], cwd=repo, env=commit_env, check=True)
        documentation_free_commit = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=repo, text=True,
        ).strip()
        applied = subprocess.run(["git", "apply", str(agent_patch)], cwd=repo, text=True,
                                 stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if applied.returncode:
            raise RuntimeError(f"agent delta does not apply to reconstructed documentation-free baseline: {applied.stdout.strip()}")
        if apply_mutation:
            restored = subprocess.run(
                ["git", "apply", "-R", "--unidiff-zero", str(documentation_patch)], cwd=repo,
                text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            )
            if restored.returncode:
                raise RuntimeError(f"documentation restoration overlaps Agent edits: {restored.stdout.strip()}")
        else:
            # Keep this audit artifact, but replay through a three-way merge so
            # adjacent or overlapping documentation changes cannot poison it.
            agent_zero = run / "agent_zero_context.patch"
            agent_zero.write_bytes(subprocess.check_output(
                ["git", "diff", "--binary", "--unified=0", documentation_free_commit, "--"],
                cwd=repo,
            ))
            replay_without_document_changes(
                repo, item["base_commit"], documentation_free_commit,
            )
    else:
        applied = subprocess.run(
            ["git", "apply", str(agent_patch)], cwd=repo, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        )
        if applied.returncode:
            raise RuntimeError(f"agent delta does not apply over mutation: {applied.stdout.strip()}")
    combined = subprocess.check_output(
        ["git", "diff", "--binary", item["base_commit"], "--"], cwd=repo, text=True,
    )
    if not combined.strip():
        raise RuntimeError("combined mutation and agent patch is empty")
    (run / "combined.patch").write_text(combined)
    (run / "interface/agent_predictions.jsonl").write_text(predictions.read_text())
    rows[0]["model_patch"] = combined
    predictions.write_text(json.dumps(rows[0], ensure_ascii=False) + "\n")


def restore(run: Path, item: dict[str, str], repo: Path) -> None:
    reset = subprocess.run(["git", "reset", "--hard", item["base_commit"]], cwd=repo,
                           text=True, capture_output=True)
    clean = subprocess.run(["git", "clean", "-fd"], cwd=repo, text=True, capture_output=True)
    status = subprocess.run(["git", "status", "--porcelain"], cwd=repo, text=True, capture_output=True)
    atomic_json(run / "restore.json", {
        "restored": reset.returncode == 0 and clean.returncode == 0 and not status.stdout,
        "reset_returncode": reset.returncode, "clean_returncode": clean.returncode,
        "status": status.stdout, "time": now(),
    })


def execute_case(output: Path, item: dict[str, str], strategy: str,
                 api_key: str, timeout: int) -> dict[str, object]:
    run = output / strategy / item["round"] / item["agent"] / item["run_name"]
    result_file = run / "result.json"
    reuse_inference = False
    if result_file.is_file():
        cached = read_json(result_file)
        if cached.get("phase") == "completed":
            emit(output, event="cache_hit", strategy=strategy, **item)
            return cached
        reuse_inference = (run / "combined.patch").is_file() and (run / "interface/agent_predictions.jsonl").is_file()
        if reuse_inference:
            rows = [json.loads(line) for line in (run / "interface/agent_predictions.jsonl").read_text().splitlines() if line.strip()]
            if len(rows) != 1:
                raise RuntimeError(f"invalid saved agent prediction in {run}")
            rows[0]["model_patch"] = (run / "combined.patch").read_text()
            (run / "interface/predictions.jsonl").write_text(json.dumps(rows[0], ensure_ascii=False) + "\n")
        else:
            stamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
            previous = run.parent / f"{run.name}.previous_{stamp}"
            run.rename(previous)
            run.mkdir(parents=True)
            attempts = run / "previous_attempts"; attempts.mkdir()
            previous.rename(attempts / previous.name)
    run.mkdir(parents=True, exist_ok=True)
    repo: Path | None = None
    started = time.time()
    error: str | None = None
    phase = "preparing"
    emit(output, event="case_started", strategy=strategy, **item)
    try:
        env = os.environ.copy()
        env.update({
            "OPENAI_API_KEY": api_key, "OPENAI_BASE_URL": BASE_URL,
            "EVIFUZZ_MODEL": MODEL, "EVIFUZZ_SYSTEM_PROMPT": prompt_for(strategy),
            "EVIFUZZ_MUTATION_HOOK": str(HERE / "doc_filter.py"),
            "EVIFUZZ_MUTATION_SOURCE_AGENT": item["agent"],
            "EVIFUZZ_COMMIT_BASELINE": "1",
            "RIPPLE_ENHANCEMENT_STRATEGY": strategy,
            "EVIFUZZ_MAX_ATTEMPTS": "3", "VERIFIED_MAX_ATTEMPTS": "3",
            "SWE_CASE_TIMEOUT": str(timeout),
            "EVIFUZZ_RUN_ID": "ripple-enh-" + hashlib.sha256(
                f"{strategy}:{item['round']}:{item['agent']}:{item['instance_id']}".encode()
            ).hexdigest()[:20],
        })
        if not reuse_inference:
            repo = prepare(item, run)
            phase = "inference"
            command([
                sys.executable, str(INTERFACE), "run", "--agent", item["agent"],
                "--repo-map", str(run / "repo_map.json"), "--output", str(run / "interface"),
                "--ids", item["instance_id"], "--run", "1", "--workers", "1",
                "--socket", socket_path(run, "inference"), "--inference-only",
            ], run / "INFERENCE.log", env, timeout + 900)
            phase = "composition"
            combine_prediction(run, item, repo)
        phase = "evaluation"
        env["SWE_EVALUATION_PREDICTIONS"] = str(run / "interface/predictions.jsonl")
        evaluation_errors = []
        inference_run_id = env["EVIFUZZ_RUN_ID"]
        for attempt in (1, 2):
            try:
                env["EVIFUZZ_RUN_ID"] = f"{inference_run_id}-eval{attempt}"
                command([
                    sys.executable, str(INTERFACE), "evaluate", "--agent", item["agent"],
                    "--output", str(run / "interface"), "--run", "1", "--workers", "1",
                    "--socket", socket_path(run, f"evaluation-{attempt}"),
                ], run / f"EVALUATION_attempt_{attempt:02d}.log", env, timeout)
                break
            except Exception as exc:
                evaluation_errors.append(f"attempt {attempt}: {type(exc).__name__}: {exc}")
                if attempt == 2:
                    raise RuntimeError("; ".join(evaluation_errors)) from exc
        outcome = resolved(run / "interface", item["instance_id"])
        if outcome is None:
            raise RuntimeError("official evaluation omitted the target instance")
        phase = "completed"
    except Exception as exc:
        outcome = None
        error = f"{type(exc).__name__}: {exc}"
        (run / "failure.log").write_text(traceback.format_exc())
        phase = "infrastructure_error"
    finally:
        if repo is not None and (repo / ".git").exists():
            restore(run, item, repo)
    metrics = extract(run, item["agent"])
    result: dict[str, object] = {
        **item, "strategy": strategy, "phase": phase, "resolved": outcome,
        "error": error, **metrics, "elapsed_seconds": round(time.time() - started, 2),
        "run_root": str(run), "finished_at": now(),
    }
    atomic_json(result_file, result)
    emit(output, event="case_finished", **result)
    return result


def aggregate(output: Path, expected: int) -> None:
    results = [read_json(path) for path in output.glob("*/*/*/*/result.json")]
    results = [row for row in results if isinstance(row, dict)]
    fields = [
        "strategy", "round", "agent", "instance_id", "phase", "resolved", "error",
        "input_tokens", "output_tokens", "total_tokens", "model_calls", "model_calls_source", "elapsed_seconds", "run_root",
    ]
    with (output / "case_results.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader(); writer.writerows(sorted(results, key=lambda x: tuple(str(x.get(k, "")) for k in ("strategy", "round", "agent", "instance_id"))))
    summary: list[dict[str, object]] = []
    config = read_json(output / "RUN_CONFIG.json") if (output / "RUN_CONFIG.json").is_file() else {}
    active_strategies = tuple(config.get("strategies", STRATEGIES))
    expected_per_strategy = int(config.get("eligible_post_mutation_failures", 0))
    for strategy in active_strategies:
        selected = [row for row in results if row.get("strategy") == strategy]
        evaluated = [row for row in selected if row.get("resolved") is not None]
        values = lambda key: [row[key] for row in selected if isinstance(row.get(key), (int, float))]
        tokens = values("total_tokens"); calls = values("model_calls")
        summary.append({
            "strategy": strategy, "expected": expected_per_strategy, "completed_records": len(selected),
            "evaluated": len(evaluated), "resolved": sum(row.get("resolved") is True for row in evaluated),
            "accuracy": round(sum(row.get("resolved") is True for row in evaluated) / len(evaluated), 6) if evaluated else None,
            "infrastructure_errors": sum(row.get("phase") == "infrastructure_error" for row in selected),
            "total_tokens": sum(tokens) if tokens else None,
            "mean_tokens": round(sum(tokens) / len(tokens), 2) if tokens else None,
            "total_model_calls": sum(calls) if calls else None,
            "mean_model_calls": round(sum(calls) / len(calls), 2) if calls else None,
        })
    atomic_json(output / "SUMMARY.json", {"generated_at": now(), "expected_records": expected, "strategies": summary})
    lines = ["# Enhancement experiment summary", "", "| Strategy | Evaluated | Resolved | Accuracy | Tokens | Mean tokens | Model calls | Mean calls | Infra errors |", "|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for row in summary:
        accuracy = "N/A" if row["accuracy"] is None else f"{100 * float(row['accuracy']):.2f}%"
        lines.append(f"| {row['strategy']} | {row['evaluated']} | {row['resolved']} | {accuracy} | {row['total_tokens'] or 'N/A'} | {row['mean_tokens'] or 'N/A'} | {row['total_model_calls'] or 'N/A'} | {row['mean_model_calls'] or 'N/A'} | {row['infrastructure_errors']} |")
    (output / "SUMMARY.md").write_text("\n".join(lines) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=OUTPUT_DEFAULT)
    parser.add_argument("--strategies", default=",".join(STRATEGIES))
    parser.add_argument("--rounds", default="round1,round2")
    parser.add_argument("--agents", default=",".join(AGENTS))
    parser.add_argument("--workers", type=int, default=3)
    parser.add_argument("--case-timeout", type=int, default=3600)
    parser.add_argument("--api-key-env", default="RIPPLE_ENHANCEMENT_API_KEY")
    parser.add_argument("--limit", type=int, help="limit source failures for a smoke run")
    args = parser.parse_args()
    output = args.output.resolve(); output.mkdir(parents=True, exist_ok=True)
    strategies = tuple(x for x in args.strategies.split(",") if x)
    if not strategies or any(x not in STRATEGIES for x in strategies):
        raise ValueError(f"strategies must be drawn from {STRATEGIES}")
    api_key = os.environ.get(args.api_key_env, "").strip()
    if not api_key:
        raise RuntimeError(f"API key must be supplied through {args.api_key_env}; it is never stored")
    selected_rounds = tuple(args.rounds.split(",")); selected_agents = tuple(args.agents.split(","))
    items = discover(selected_rounds, selected_agents)
    excluded = excluded_inputs(selected_rounds, selected_agents)
    atomic_json(output / "EXCLUDED_INPUTS.json", excluded)
    if args.limit is not None:
        items = items[:args.limit]
    # Interleave and rotate strategies by case so endpoint/load drift does not
    # systematically favor the strategy that happens to run first.
    jobs = []
    for index, item in enumerate(items):
        ordered = strategies[index % len(strategies):] + strategies[:index % len(strategies)]
        jobs.extend((item, strategy) for strategy in ordered)
    started = now()
    config = {
        "task": "documentation mitigation rerun of archived mutation failures",
        "run_id": output.name, "started_at": started, "working_directory": str(RIPPLE),
        "archive": str(ARCHIVE), "archive_error_records": len(items) + len(excluded),
        "eligible_post_mutation_failures": len(items), "excluded_pre_inference_failures": len(excluded),
        "strategies": strategies,
        "total_jobs": len(jobs), "model": MODEL, "requested_endpoint": REQUESTED_ENDPOINT,
        "client_base_url": BASE_URL, "api_key": "omitted", "workers": args.workers,
        "case_timeout_seconds": args.case_timeout, "retry_limit": 3,
        "cache_policy": "reuse only result.json with phase=completed",
        "evaluation": "official SWE-bench Lite harness through swe-bench-lite_interface.py",
        "output_dir": str(output),
    }
    atomic_json(output / "RUN_CONFIG.json", config)
    (output / "RUN_CONFIG.md").write_text("# Enhancement run configuration\n\n" + "\n".join(f"- {key}: `{value}`" for key, value in config.items()) + "\n")
    atomic_json(output / "status.json", {
        "updated_at": now(), "phase": "running", "started_at": started,
        "completed": 0, "total": len(jobs), "remaining": len(jobs),
        "success": 0, "failed": 0, "errors": 0, "eta": "unknown",
        "pid": os.getpid(), "log": str(output / "RUN.log"), "output_dir": str(output),
        "cache_hit": 0, "executed_this_run": 0,
    })
    with futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        pending = {pool.submit(execute_case, output, item, strategy, api_key, args.case_timeout): (item, strategy) for item, strategy in jobs}
        for future in futures.as_completed(pending):
            future.result()
            aggregate(output, len(jobs))
    aggregate(output, len(jobs))
    rows = [read_json(path) for path in output.glob("*/*/*/*/result.json")]
    infra = sum(row.get("phase") == "infrastructure_error" for row in rows)
    atomic_json(output / "status.json", {
        "updated_at": now(), "phase": "completed" if not infra else "completed_with_errors",
        "started_at": started, "finished_at": now(), "completed": len(rows), "total": len(jobs),
        "remaining": max(0, len(jobs) - len(rows)), "success": len(rows) - infra,
        "failed": sum(row.get("resolved") is False for row in rows), "errors": infra,
        "eta": "0s", "pid": os.getpid(), "log": str(output / "RUN.log"),
        "output_dir": str(output), "cache_hit": 0, "executed_this_run": len(rows),
    })
    return 1 if infra else 0


if __name__ == "__main__":
    raise SystemExit(main())
