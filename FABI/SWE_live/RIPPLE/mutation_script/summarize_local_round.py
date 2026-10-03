#!/usr/bin/env python3
"""Compare the finished local-operator run with its three clean runs."""
from __future__ import annotations

import argparse
import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIVE_ROOT = ROOT.parent
sys.path.insert(0, str(LIVE_ROOT))
from export_luna_three_round_cases import metrics  # noqa: E402

SLUG = {"SWE_Agent": "swe-agent", "OpenCode": "opencode", "Codex": "codex"}
FIELDS = ("pass_at_1", "total_tokens", "agent_calls", "read_locations", "patch_edited_lines")


def mean(values):
    return sum(values) / len(values)


def summarize(rows):
    result = {"cases": len(rows), "resolved": sum(r["resolved"] for r in rows), "metrics": {}}
    for field in FIELDS:
        baseline = mean([r[f"clean_{field}"] for r in rows])
        mutated = mean([r[f"mutated_{field}"] for r in rows])
        result["metrics"][field] = {
            "clean_mean": baseline, "mutated_mean": mutated,
            "delta": mutated - baseline,
            "change_pct": (mutated / baseline - 1) * 100 if baseline else None,
        }
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-root", type=Path, default=ROOT / "mutation_result/live-local-20260927-a")
    args = parser.parse_args()
    run = args.run_root.resolve()
    output = run / "comparison"
    output.mkdir(exist_ok=True)
    clean_csv = LIVE_ROOT / "original_passed_cases_luna/token_stable_cases.csv"
    clean = list(csv.DictReader(clean_csv.open(newline="")))
    result_rows = list(csv.DictReader((run / "export/results.csv").open(newline="")))
    result_map = {(r["agent"], r["instance_id"]): r for r in result_rows}
    expected = {(SLUG[r["agent"]], r["instance_id"]) for r in clean}
    if set(result_map) != expected or len(clean) != 172:
        raise RuntimeError("local and clean case sets differ")
    if any(row["official_resolved"] not in {"True", "False"} for row in result_rows):
        raise RuntimeError("unexpected official evaluation result")
    detail = []
    groups = defaultdict(list)
    for row in clean:
        agent, slug, iid = row["agent"], SLUG[row["agent"]], row["instance_id"]
        case = run / "export" / f"{slug}_example_{iid}"
        value = metrics(slug, case)
        resolved = result_map[(slug, iid)]["official_resolved"] == "True"
        current = {
            "pass_at_1": float(resolved),
            "total_tokens": value["total_tokens"],
            "agent_calls": value["agent_calls"],
            "read_locations": value["read_locations"],
            "patch_edited_lines": value["patch_edited_lines"],
        }
        clean_mean = {field: mean([float(row[f"round_{number}_{field}"])
                                   for number in (1, 2, 3)])
                      for field in FIELDS if field != "pass_at_1"}
        clean_mean["pass_at_1"] = 1.0
        entry = {"agent": agent, "instance_id": iid, "resolved": resolved,
                 "outcome": "resolved" if resolved else "unresolved"}
        for field in FIELDS:
            baseline = clean_mean[field]
            entry.update({f"clean_{field}": baseline, f"mutated_{field}": current[field],
                          f"delta_{field}": current[field] - baseline,
                          f"change_pct_{field}": (current[field] / baseline - 1) * 100
                          if baseline else ""})
        detail.append(entry)
        groups[agent].append(entry)
        groups["overall"].append(entry)
    with (output / "case_comparison.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(detail[0]))
        writer.writeheader()
        writer.writerows(detail)
    summary = {"run": run.name, "clean_source": str(clean_csv), "cases": len(detail),
               "definitions": {
                   "pass_at_1": "official resolved fraction; clean cases resolved in each of three runs",
                   "total_tokens": "input plus output tokens under the clean extractor's agent-specific accounting",
                   "agent_calls": "SWE-Agent API calls, OpenCode step_finish events, or reconstructed Codex response batches",
                   "read_locations": "read/search tool access-event count, not unique source locations",
                   "patch_edited_lines": "added plus deleted code patch lines, excluding diff headers",
                   "change_pct": "100 * (mutated aggregate mean / three-clean-run aggregate mean - 1)",
               }, "groups": {}, "by_outcome": {}}
    for agent in ("SWE_Agent", "OpenCode", "Codex", "overall"):
        rows = groups[agent]
        summary["groups"][agent] = summarize(rows)
        summary["by_outcome"][agent] = {}
        for outcome in ("resolved", "unresolved"):
            subset = [row for row in rows if row["outcome"] == outcome]
            if not subset:
                raise RuntimeError(f"empty {agent} {outcome} group")
            summary["by_outcome"][agent][outcome] = summarize(subset)
        if sum(item["cases"] for item in summary["by_outcome"][agent].values()) != len(rows):
            raise RuntimeError(f"outcome partition mismatch: {agent}")
    (output / "summary.json").write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary["by_outcome"], indent=2))


if __name__ == "__main__":
    main()
