#!/usr/bin/env python3
"""Summarize evaluation outcomes and inference usage for a completed RIPPLE run."""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
from statistics import mean


AGENTS = ("swe-agent", "opencode", "codex")


def read_json(path: Path) -> dict:
    return json.loads(path.read_text())


def read_jsonl(path: Path) -> list[dict]:
    records = []
    for line in path.read_text(errors="replace").splitlines():
        if not line.startswith("{"):
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return records


def swe_usage(path: Path) -> dict:
    stats = (read_json(path).get("info") or {}).get("model_stats") or {}
    input_tokens = int(stats.get("tokens_sent") or stats.get("input_tokens") or 0)
    output_tokens = int(stats.get("tokens_received") or stats.get("output_tokens") or 0)
    return {
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": input_tokens + output_tokens,
        "model_calls": int(stats.get("api_calls") or 0),
    }


def opencode_usage(path: Path) -> dict:
    calls = [record for record in read_jsonl(path) if record.get("type") == "step_finish"]
    input_tokens = output_tokens = total_tokens = 0
    for call in calls:
        tokens = ((call.get("part") or {}).get("tokens") or {})
        cache = tokens.get("cache") or {}
        input_tokens += int(tokens.get("input") or 0) + int(cache.get("read") or 0)
        output_tokens += int(tokens.get("output") or 0) + int(tokens.get("reasoning") or 0)
        total_tokens += int(tokens.get("total") or 0)
    return {
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": total_tokens,
        "model_calls": len(calls),
    }


def codex_usage(path: Path) -> dict:
    records = read_jsonl(path)
    usage = next(
        (record.get("usage") or {} for record in reversed(records)
         if record.get("type") == "turn.completed"),
        {},
    )

    # Match the model-call convention used to produce token_stable_cases.csv.
    model_calls = 0
    active_tools: set[str] = set()
    for record in records:
        item = record.get("item") or {}
        item_type = item.get("type")
        item_id = str(item.get("id") or "")
        if record.get("type") == "item.started" and item_type != "agent_message":
            if not active_tools:
                model_calls += 1
            active_tools.add(item_id)
        elif record.get("type") == "item.completed" and item_type != "agent_message":
            if item_id not in active_tools and not active_tools:
                model_calls += 1
            active_tools.discard(item_id)
        elif record.get("type") == "item.completed" and item_type == "agent_message":
            model_calls += 1
            active_tools.clear()

    input_tokens = int(usage.get("input_tokens") or 0)
    output_tokens = int(usage.get("output_tokens") or 0)
    return {
        "input_tokens": input_tokens,
        "output_tokens": output_tokens,
        "total_tokens": input_tokens + output_tokens,
        "model_calls": model_calls,
        "cached_input_tokens": int(usage.get("cached_input_tokens") or 0),
    }


def aggregate(items: list[dict], denominator: int | None = None) -> dict:
    fields = sorted({key for item in items for key in item})
    totals = {field: sum(item.get(field, 0) for item in items) for field in fields}
    result = {
        "artifact_count": len(items),
        "totals": totals,
        "averages_per_artifact": {
            field: mean(item.get(field, 0) for item in items) if items else 0
            for field in fields
        },
    }
    if denominator is not None:
        result["averages_per_task"] = {
            field: totals[field] / denominator if denominator else 0 for field in fields
        }
    return result


def final_and_attempted_files(run_root: Path, agent: str) -> tuple[list[Path], list[Path]]:
    workers = run_root / agent / "workers"
    if agent == "swe-agent":
        attempted = sorted(workers.glob("worker_*/cases/*/attempt_*/**/*.traj"))
        by_case: dict[str, Path] = {}
        for path in attempted:
            case_id = next(part for part in path.parts if part.startswith("instance_"))
            if case_id not in by_case or str(path) > str(by_case[case_id]):
                by_case[case_id] = path
        return sorted(by_case.values()), attempted
    if agent == "opencode":
        final = sorted(workers.glob("worker_*/cases/*/opencode.jsonl"))
        attempted = sorted(workers.glob("worker_*/cases/*/opencode*.jsonl"))
        return final, attempted
    final = sorted(workers.glob("worker_*/cases/*/codex.jsonl"))
    attempted = sorted(workers.glob("worker_*/cases/*/codex*.jsonl"))
    return final, attempted


def usage_for(agent: str, path: Path) -> dict:
    if agent == "swe-agent":
        return swe_usage(path)
    if agent == "opencode":
        return opencode_usage(path)
    return codex_usage(path)


def case_id_for_path(path: Path) -> str:
    try:
        return next(part for part in path.parts if part.startswith("instance_"))
    except StopIteration as exc:
        raise RuntimeError(f"cannot identify case for usage artifact: {path}") from exc


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-root", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    run_root = args.run_root.resolve()

    status = read_json(run_root / "status.json")
    result = {
        "run_root": str(run_root),
        "phase": status.get("phase"),
        "started_at": status.get("started_at"),
        "completed_at": status.get("updated_at"),
        "input_total": status.get("input_total"),
        "eligible_total": status.get("total"),
        "excluded": status.get("excluded") or [],
        "agents": {},
    }
    mutation_files = sorted((run_root / "mutations").glob("*/*/mutation.json"))
    operators: Counter[str] = Counter()
    for path in mutation_files:
        for cluster in read_json(path).get("clusters") or []:
            operators[str(cluster.get("selected_operator"))] += 1
    result["mutation"] = {
        "successful": len(mutation_files),
        "eligible": int(status.get("total") or 0),
        "input_total": int(status.get("input_total") or 0),
        "success_rate_eligible": len(mutation_files) / int(status["total"]),
        "coverage_rate_input": len(mutation_files) / int(status["input_total"]),
        "selected_operator_counts": dict(sorted(operators.items())),
        "selected_cluster_count": sum(operators.values()),
    }
    overall_final: list[dict] = []
    overall_attempted: list[dict] = []
    overall_total = overall_resolved = 0

    for agent in AGENTS:
        evaluation = read_json(run_root / agent / "evaluation_result.json")
        final_paths, attempted_paths = final_and_attempted_files(run_root, agent)
        completed_ids = set(evaluation.get("completed_ids") or [])
        final_paths = [path for path in final_paths if case_id_for_path(path) in completed_ids]
        attempted_paths = [path for path in attempted_paths if case_id_for_path(path) in completed_ids]
        final = [usage_for(agent, path) for path in final_paths]
        attempted = [usage_for(agent, path) for path in attempted_paths]
        total = int(evaluation["total"])
        resolved = int(evaluation["resolved"])
        if len(final) != total:
            raise RuntimeError(f"{agent}: {len(final)} final usage artifacts for {total} tasks")
        result["agents"][agent] = {
            "evaluation": {
                "status": evaluation.get("status"),
                "total": total,
                "input_total": int(evaluation.get("input_total", total)),
                "officially_excluded": int(evaluation.get("officially_excluded", 0)),
                "resolved": resolved,
                "unresolved": int(evaluation["unresolved"]),
                "pass_rate": resolved / total,
                "errors": evaluation.get("errors") or 0,
            },
            "final_inference": aggregate(final, total),
            "all_attempts": aggregate(attempted, total),
        }
        overall_total += total
        overall_resolved += resolved
        overall_final.extend(final)
        overall_attempted.extend(attempted)

    result["overall"] = {
        "evaluation": {
            "total": overall_total,
            "resolved": overall_resolved,
            "unresolved": overall_total - overall_resolved,
            "pass_rate": overall_resolved / overall_total,
        },
        "final_inference": aggregate(overall_final, overall_total),
        "all_attempts": aggregate(overall_attempted, overall_total),
    }
    output = args.output or run_root / "FINAL_SUMMARY.json"
    output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
