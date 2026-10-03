#!/usr/bin/env python3
"""Summarize completed enhancement evaluations and model-use metrics."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


def metric(row: dict, result_path: Path) -> tuple[int | None, int | None, int | None]:
    values = (row.get("input_tokens"), row.get("output_tokens"), row.get("model_calls"))
    if all(isinstance(value, (int, float)) for value in values):
        return tuple(int(value) for value in values)  # type: ignore[return-value]
    root = Path(row["run_root"])
    candidates = list(root.glob("interface/**/metrics.json"))
    if not candidates:
        return None, None, None
    data = json.loads(candidates[-1].read_text())
    if row["agent"] == "sweagent":
        return (int(data.get("input_tokens", 0)), int(data.get("output_tokens", 0)),
                int(data.get("api_calls", 0)))
    return (int(data.get("input_tokens", 0)), int(data.get("output_tokens", 0)),
            int(data.get("model_calls", 0)))


def summarize(root: Path) -> dict:
    rows = []
    for path in root.glob("*/*/*/*/result.json"):
        row = json.loads(path.read_text())
        input_tokens, output_tokens, calls = metric(row, path)
        row = {**row, "input_tokens": input_tokens, "output_tokens": output_tokens,
               "total_tokens": (input_tokens + output_tokens
                                if input_tokens is not None and output_tokens is not None else None),
               "model_calls": calls}
        rows.append(row)
    rows.sort(key=lambda row: (row["strategy"], row["agent"], row["round"], row["instance_id"]))

    def group(key_fields: tuple[str, ...]) -> list[dict]:
        groups = defaultdict(list)
        for row in rows:
            groups[tuple(row[field] for field in key_fields)].append(row)
        output = []
        for key, members in sorted(groups.items()):
            resolved = sum(bool(row.get("resolved")) for row in members)
            token_rows = [row for row in members if row["total_tokens"] is not None]
            call_rows = [row for row in members if row["model_calls"] is not None]
            item = dict(zip(key_fields, key))
            item.update({
                "cases": len(members), "resolved": resolved,
                "correctness": resolved / len(members) if members else None,
                "average_input_tokens": (sum(row["input_tokens"] for row in token_rows) / len(token_rows)
                                          if token_rows else None),
                "average_output_tokens": (sum(row["output_tokens"] for row in token_rows) / len(token_rows)
                                           if token_rows else None),
                "average_total_tokens": (sum(row["total_tokens"] for row in token_rows) / len(token_rows)
                                         if token_rows else None),
                "average_model_calls": (sum(row["model_calls"] for row in call_rows) / len(call_rows)
                                        if call_rows else None),
                "metric_complete_cases": len(token_rows),
            })
            output.append(item)
        return output

    return {
        "total_result_files": len(rows),
        "strategies": group(("strategy",)),
        "agent_strategy": group(("agent", "strategy")),
        "agent": group(("agent",)),
        "all_49_cases_by_strategy": group(("strategy",)),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--json", type=Path, required=True)
    parser.add_argument("--markdown", type=Path, required=True)
    args = parser.parse_args()
    summary = summarize(args.root.resolve())
    args.json.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    lines = ["# Enhancement experiment summary", "", f"- Result files: `{summary['total_result_files']}`", "- Correctness is `resolved / cases`.", "- Token and call averages use all cases with a validated metrics artifact.", ""]
    for title, key in (("By method (49 cases each)", "strategies"), ("By Agent and method", "agent_strategy"), ("All agents by method (49-case aggregate)", "all_49_cases_by_strategy")):
        lines += [f"## {title}", "", "| Group | Cases | Resolved | Correctness | Avg input tokens | Avg output tokens | Avg total tokens | Avg model calls | Metric cases |", "|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
        for row in summary[key]:
            label = "/".join(str(row[field]) for field in ("agent", "strategy") if field in row) or row.get("strategy", "")
            lines.append("| {label} | {cases} | {resolved} | {correctness:.4f} | {average_input_tokens} | {average_output_tokens} | {average_total_tokens} | {average_model_calls} | {metric_complete_cases} |".format(label=label, **row))
        lines.append("")
    args.markdown.write_text("\n".join(lines) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
