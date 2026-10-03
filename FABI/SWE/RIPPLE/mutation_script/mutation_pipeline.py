#!/usr/bin/env python3
"""Generate exact, documentation-only mutations from clustered_doc.jsonl."""

from __future__ import annotations

import argparse
import ast
import hashlib
import io
import json
import os
import random
import re
import subprocess
import time
import tokenize
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Callable

from openai import OpenAI

try:
    from .prompts import OPERATOR_DEFINITIONS, SELECTOR_PROMPT, mutation_prompt
except ImportError:  # Direct script execution.
    from prompts import OPERATOR_DEFINITIONS, SELECTOR_PROMPT, mutation_prompt


SELECTOR_MODEL = "gpt-5.6-luna"
LOCAL_MODEL = "gpt-5.6-terra"
RELATIONAL_MODEL = "gpt-5.6-luna"
API_KEY = os.environ.get("RIPPLE_API_KEY", "sk-de21c76052d94acbbc3011a71629f36d")
BASE_URL = os.environ.get("RIPPLE_BASE_URL", "https://rightapi.ai/codex/v1")
OPERATORS = tuple(OPERATOR_DEFINITIONS)
LOCAL_OPERATORS = {"L1", "L2", "L3"}
ENABLED_OPERATORS = LOCAL_OPERATORS

SELECTION_SCHEMA = {
    "type": "object",
    "properties": {
        "applicable_operators": {
            "type": "array", "items": {"type": "string", "enum": list(OPERATORS)},
        },
        "operator_reasons": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "operator": {"type": "string", "enum": list(OPERATORS)},
                    "reason": {"type": "string"},
                },
                "required": ["operator", "reason"],
                "additionalProperties": False,
            },
        },
    },
    "required": ["applicable_operators", "operator_reasons"],
    "additionalProperties": False,
}

MUTATION_SCHEMA = {
    "type": "object",
    "properties": {
        "mutated_unit_source": {"type": "string"},
        "changed_contract": {"type": "string"},
        "evidence": {"type": "string"},
    },
    "required": ["mutated_unit_source", "changed_contract", "evidence"],
    "additionalProperties": False,
}

CLUSTER_MUTATION_SCHEMA = {
    "type": "object",
    "properties": {
        "mutations": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "unit_id": {"type": "string"},
                    "mutated_unit_source": {"type": "string"},
                    "changed_contract": {"type": "string"},
                    "evidence": {"type": "string"},
                },
                "required": ["unit_id", "mutated_unit_source", "changed_contract", "evidence"],
                "additionalProperties": False,
            },
        }
    },
    "required": ["mutations"],
    "additionalProperties": False,
}


def atomic_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + f".{os.getpid()}.tmp")
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    tmp.replace(path)


def atomic_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + f".{os.getpid()}.tmp")
    tmp.write_text(value)
    tmp.replace(path)


def jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def _strip_fence(value: str) -> str:
    value = value.strip()
    if value.startswith("```"):
        value = value.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    return value


def parse_json_object(value: str) -> dict[str, Any]:
    """Parse JSON even when a CLI wrapper appends status/progress text."""
    text = _strip_fence(value).strip()
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        decoder = json.JSONDecoder()
        starts = [i for i, ch in enumerate(text) if ch == "{"]
        parsed = None
        for start in starts:
            try:
                candidate, _ = decoder.raw_decode(text[start:])
                if isinstance(candidate, dict):
                    parsed = candidate
                    break
            except json.JSONDecodeError:
                continue
        if parsed is None:
            raise
    if not isinstance(parsed, dict):
        raise ValueError("expected JSON object")
    return parsed


def chat_json(model: str, effort: str, prompt: str, schema: dict[str, Any]) -> dict[str, Any]:
    client = OpenAI(api_key=API_KEY, base_url=BASE_URL, timeout=300, max_retries=2)
    for attempt in range(1, 7):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                reasoning_effort=effort,
                max_tokens=8192,
                response_format={
                    "type": "json_schema",
                    "json_schema": {"name": "ripple_mutation", "strict": True, "schema": schema},
                },
            )
            return json.loads(_strip_fence(response.choices[0].message.content or ""))
        except Exception as exc:
            retryable = isinstance(exc, json.JSONDecodeError) or any(
                code in str(exc).lower()
                for code in ("429", "rate_limit", "timeout", "connection", "empty response")
            )
            if attempt == 6 or not retryable:
                raise
            time.sleep(min(60, 5 * 2 ** (attempt - 1)))
    raise AssertionError("unreachable")


def bounded_context(doc: dict[str, Any]) -> str:
    """Return a location with at most 100 lines before and after its documentation."""
    source = doc["function_source"]
    lines = source.splitlines(keepends=True)
    if len(lines) <= 201:
        return source
    function_start = int(doc["function_start_line"])
    doc_start = int(doc["documentation_start_line"]) - function_start
    doc_end = int(doc["documentation_end_line"]) - function_start
    start = max(0, doc_start - 100)
    end = min(len(lines), doc_end + 101)
    prefix = f"... omitted lines {function_start}-{function_start + start - 1} ...\n" if start else ""
    suffix = f"... omitted after line {function_start + end - 1} ...\n" if end < len(lines) else ""
    return prefix + "".join(lines[start:end]) + suffix


def load_level(case_dir: Path, level: str) -> tuple[list[list[dict[str, Any]]], dict[str, dict[str, Any]]]:
    docs = {row["documentation_id"]: row for row in jsonl(case_dir / "all_doc.jsonl")}
    rows = [row for row in jsonl(case_dir / "clustered_doc.jsonl") if row["level"] == level]
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        if row["documentation_id"] not in docs:
            raise ValueError(f"missing documentation_id {row['documentation_id']}")
        groups[row["cluster_id"]].append(row)
    ordered = [sorted(groups[key], key=lambda row: (row["file"], row["file_line_start"], row["unit_index"])) for key in sorted(groups)]
    return ordered, docs


def load_levels_priority(case_dir: Path, levels: list[str]) -> tuple[list[list[dict[str, Any]]], dict[str, dict[str, Any]]]:
    """Load clusters from levels in priority order, deduplicating cluster IDs."""
    docs = {row["documentation_id"]: row for row in jsonl(case_dir / "all_doc.jsonl")}
    rows = [row for row in jsonl(case_dir / "clustered_doc.jsonl") if row["level"] in levels]
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        if row["documentation_id"] not in docs:
            raise ValueError(f"missing documentation_id {row['documentation_id']}")
        groups[row["cluster_id"]].append(row)
    ordered = []
    for level in levels:
        keys = sorted(k for k, vals in groups.items() if vals[0]["level"] == level)
        ordered.extend(sorted((sorted(groups[k], key=lambda r: (r["file"], r["file_line_start"], r["unit_index"])) for k in keys), key=lambda c: c[0]["cluster_id"]))
    return ordered, docs


def selector_input(cluster: list[dict[str, Any]], docs: dict[str, dict[str, Any]]) -> str:
    payload = {
        "cluster_id": cluster[0]["cluster_id"],
        "cluster_label": cluster[0]["cluster_label"],
        "cluster_summary": cluster[0]["cluster_summary"],
        "locations": [
            {
                "file": row["file"], "symbol": row["symbol"],
                "lines": [row["file_line_start"], row["file_line_end"]],
                "documentation_unit": row["unit_source"],
                "complete_documentation": docs[row["documentation_id"]]["documentation_source"],
            }
            for row in cluster
        ],
        "operators": {
            key: {"name": value[0], "definition": value[1]}
            for key, value in OPERATOR_DEFINITIONS.items()
        },
    }
    return SELECTOR_PROMPT + "\n\nCLUSTER INPUT:\n" + json.dumps(payload, ensure_ascii=False, indent=2)


def mutation_input(operator: str, row: dict[str, Any], doc: dict[str, Any], repo: Path) -> str:
    payload = {
        "repository_root": str(repo),
        "target_file": row["file"],
        "target_symbol": row["symbol"],
        "target_file_lines": [row["file_line_start"], row["file_line_end"]],
        "documentation_lines": [doc["documentation_start_line"], doc["documentation_end_line"]],
        "complete_access_location": bounded_context(doc),
        "target_unit_source": row["unit_source"],
        "cluster_label": row["cluster_label"],
        "cluster_summary": row["cluster_summary"],
    }
    exploration = ""
    if operator not in LOCAL_OPERATORS:
        exploration = (
            "\nYou are a read-only Codex repository agent. Explore callers, callees, "
            "and directly related entities before deciding the false relation. You have a "
            "hard budget of at most five model calls; therefore run at most four focused "
            "read-only shell tool executions, then return the required JSON. Do not edit files.\n"
        )
    return mutation_prompt(operator) + exploration + "\nMUTATION INPUT:\n" + json.dumps(payload, ensure_ascii=False, indent=2)


def relational_cluster_input(operator: str, cluster: list[dict[str, Any]],
                             docs: dict[str, dict[str, Any]], repo: Path) -> str:
    payload = {
        "repository_root": str(repo),
        "cluster_id": cluster[0]["cluster_id"],
        "cluster_label": cluster[0]["cluster_label"],
        "cluster_summary": cluster[0]["cluster_summary"],
        "locations": [{
            "unit_id": row["unit_id"], "target_file": row["file"],
            "target_symbol": row["symbol"],
            "target_file_lines": [row["file_line_start"], row["file_line_end"]],
            "complete_access_location": bounded_context(docs[row["documentation_id"]]),
            "target_unit_source": row["unit_source"],
        } for row in cluster],
    }
    instructions = (
        "\nTreat all locations as expressions of one clustered software fact. Explore the "
        "repository once, choose one coherent false repository relation governed by the "
        f"selected {operator} operator, and apply that same relation consistently to every "
        "location. Return exactly one mutation for every supplied unit_id; do not omit, add, "
        "or duplicate unit_ids. Do not edit repository files.\n"
    )
    return mutation_prompt(operator) + instructions + "\nCLUSTER MUTATION INPUT:\n" + json.dumps(payload, ensure_ascii=False, indent=2)


def codex_json(repo: Path, prompt: str, output: Path, log: Path,
               schema: dict[str, Any] = MUTATION_SCHEMA) -> dict[str, Any]:
    """Run a read-only Codex agent, limiting it to five tool executions."""
    output.parent.mkdir(parents=True, exist_ok=True)
    schema_path = output.with_suffix(".schema.json")
    atomic_json(schema_path, schema)
    config_dir = output.parent / "codex_home"
    config_dir.mkdir(exist_ok=True)
    atomic_text(
        config_dir / "config.toml",
        "model_provider = \"rightcode\"\n"
        "model = \"gpt-5.6-luna\"\n"
        "model_reasoning_effort = \"medium\"\n"
        "disable_response_storage = true\n"
        "approval_policy = \"never\"\n"
        "sandbox_mode = \"read-only\"\n\n"
        "[model_providers.rightcode]\n"
        "name = \"rightcode\"\n"
        f"base_url = {json.dumps(BASE_URL)}\n"
        "env_key = \"OPENAI_API_KEY\"\n"
        "wire_api = \"responses\"\n",
    )
    command = [
        "codex", "exec", "-m", RELATIONAL_MODEL,
        "-c", 'model_reasoning_effort="medium"', "--ephemeral", "--ignore-rules",
        "--skip-git-repo-check", "-s", "read-only", "-C", str(repo), "--json",
        "--output-schema", str(schema_path), "--output-last-message", str(output), "-",
    ]
    env = os.environ.copy()
    env.update({"OPENAI_API_KEY": API_KEY, "CODEX_HOME": str(config_dir), "TERM": "dumb", "NO_COLOR": "1"})
    tool_calls = 0
    with log.open("w") as handle:
        proc = subprocess.Popen(
            command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True, env=env, start_new_session=True,
        )
        assert proc.stdin is not None and proc.stdout is not None
        proc.stdin.write(prompt)
        proc.stdin.close()
        for line in proc.stdout:
            handle.write(line)
            handle.flush()
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            item = event.get("item") or {}
            if event.get("type") == "item.started" and item.get("type") == "command_execution":
                tool_calls += 1
                if tool_calls > 5:
                    proc.terminate()
                    raise RuntimeError("Codex relational mutation exceeded five tool executions")
        rc = proc.wait(timeout=30)
    if rc:
        raise RuntimeError(f"Codex relational mutation exited {rc}; see {log}")
    value = parse_json_object(output.read_text())
    value["tool_executions"] = tool_calls
    return value


def _semantic_tokens(source: str) -> list[tuple[int, str]]:
    tree = ast.parse(source)
    doc_ranges = []
    for node in ast.walk(tree):
        body = getattr(node, "body", None)
        if isinstance(body, list) and body:
            first = body[0]
            if isinstance(first, ast.Expr) and isinstance(first.value, ast.Constant) and isinstance(first.value.value, str):
                doc_ranges.append((first.lineno, first.end_lineno or first.lineno))
    result = []
    for token in tokenize.generate_tokens(io.StringIO(source).readline):
        if token.type in {tokenize.COMMENT, tokenize.ENCODING, tokenize.NL, tokenize.NEWLINE,
                          tokenize.INDENT, tokenize.DEDENT, tokenize.ENDMARKER}:
            continue
        if token.type == tokenize.STRING and any(a <= token.start[0] <= b for a, b in doc_ranges):
            continue
        result.append((token.type, token.string))
    return result


def apply_mutations(repo: Path, docs: dict[str, dict[str, Any]], mutations: list[dict[str, Any]]) -> None:
    by_doc: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for mutation in mutations:
        by_doc[mutation["documentation_id"]].append(mutation)
    before_files: dict[Path, str] = {}
    resolved_docs = []
    for documentation_id, changes in by_doc.items():
        doc = docs[documentation_id]
        path = repo / doc["file"]
        baseline = before_files.setdefault(path, path.read_text())
        source = doc["documentation_source"]
        lines = baseline.splitlines(keepends=True)
        annotated_start = int(doc["documentation_start_line"]) - 1
        annotated_end = int(doc["documentation_end_line"])
        if "".join(lines[annotated_start:annotated_end]) == source:
            actual_start, actual_end = annotated_start, annotated_end
        else:
            offsets = []
            offset = baseline.find(source)
            while offset >= 0:
                offsets.append(offset)
                offset = baseline.find(source, offset + 1)
            if len(offsets) != 1:
                raise ValueError(
                    f"repository documentation mismatch and exact source has "
                    f"{len(offsets)} matches at {path}:{annotated_start + 1}"
                )
            actual_start = baseline.count("\n", 0, offsets[0])
            actual_end = actual_start + len(source.splitlines(keepends=True))
        resolved_docs.append((path, actual_start, actual_end, documentation_id, changes))

    # Apply later docstrings first. A mutation may legitimately change a
    # docstring's line count; descending source order keeps every earlier
    # location stable. Exact unique fallback handles trace line metadata that
    # is slightly shifted relative to the task's base commit.
    for path, doc_start, doc_end, documentation_id, changes in sorted(
        resolved_docs, key=lambda item: (str(item[0]), -item[1])
    ):
        doc = docs[documentation_id]
        source = doc["documentation_source"]
        for change in sorted(changes, key=lambda x: x["source_start_offset"], reverse=True):
            unit_start, unit_end = change["source_start_offset"], change["source_end_offset"]
            if source[unit_start:unit_end] != change["original_unit_source"]:
                raise ValueError(f"offset/source mismatch for {change['unit_id']}")
            source = source[:unit_start] + change["mutated_unit_source"] + source[unit_end:]
        lines = path.read_text().splitlines(keepends=True)
        if "".join(lines[doc_start:doc_end]) != doc["documentation_source"]:
            raise ValueError(f"repository documentation mismatch at {path}:{doc_start + 1}")
        lines[doc_start:doc_end] = source.splitlines(keepends=True)
        path.write_text("".join(lines))
    for path, before in before_files.items():
        after = path.read_text()
        if path.suffix == ".py" and _semantic_tokens(before) != _semantic_tokens(after):
            raise ValueError(f"mutation is not documentation-only: {path}")
    subprocess.run(["git", "diff", "--check"], cwd=repo, check=True)


def validate_replacement(original: str, mutated: str) -> None:
    if not mutated or mutated == original:
        raise ValueError("model returned an empty or unchanged mutation")
    if '"""' in mutated or "'''" in mutated or "```" in mutated:
        raise ValueError("mutation introduced a delimiter/code fence")


def normalize_replacement(original: str, mutated: str) -> str:
    """Fit semantic model output to the source unit's whitespace convention."""
    if not isinstance(mutated, str):
        raise ValueError("model returned a non-string mutation")
    body = mutated.strip(" \t\r\n")
    if not body:
        raise ValueError("model returned an empty mutation")
    lines = body.splitlines()
    original_lines = original.splitlines()
    base_indent = re.match(r"^[ \t]*", original).group(0)
    indents = ([re.match(r"^[ \t]*", line).group(0) for line in original_lines]
               if len(original_lines) == len(lines) else [base_indent] * len(lines))
    normalized = "\n".join(indent + line.lstrip(" \t") for indent, line in zip(indents, lines))
    if original.endswith("\r\n"):
        normalized = normalized.replace("\n", "\r\n") + "\r\n"
    elif original.endswith("\n"):
        normalized += "\n"
    return normalized


def _edit_distance_at_most_two(left: str, right: str) -> bool:
    """Accept at most two transcription edits in an opaque SHA-like ID."""
    if abs(len(left) - len(right)) > 2:
        return False
    previous = list(range(len(right) + 1))
    for row, left_char in enumerate(left, 1):
        current = [row]
        for column, right_char in enumerate(right, 1):
            current.append(min(
                current[-1] + 1,
                previous[column] + 1,
                previous[column - 1] + (left_char != right_char),
            ))
        if min(current) > 2:
            return False
        previous = current
    return previous[-1] <= 2


def align_transcribed_unit_ids(
    returned: list[dict[str, Any]], expected: set[str]
) -> dict[str, str]:
    """Repair uniquely identifiable one-character mistakes in returned IDs."""
    actual = {item.get("unit_id") for item in returned}
    missing = expected - actual
    extra = {unit_id for unit_id in actual - expected if isinstance(unit_id, str)}
    if len(missing) != 1 or len(extra) != 1:
        return {}
    expected_id, returned_id = next(iter(missing)), next(iter(extra))
    if not _edit_distance_at_most_two(expected_id, returned_id):
        return {}
    for item in returned:
        if item.get("unit_id") == returned_id:
            item["unit_id"] = expected_id
            return {returned_id: expected_id}
    return {}


def generate(
    case_dir: Path,
    repo: Path,
    output: Path,
    level: str,
    seed: int,
    k: int | None = None,
    selector: Callable[[str, str, str, dict[str, Any]], dict[str, Any]] = chat_json,
    local_mutator: Callable[[str, str, str, dict[str, Any]], dict[str, Any]] = chat_json,
    relational_mutator: Callable[..., dict[str, Any]] = codex_json,
    forced_operator: str | None = None,
    enabled_operators: tuple[str, ...] | None = None,
    selected_cluster_ids: tuple[str, ...] | None = None,
) -> dict[str, Any]:
    levels = [part.strip() for part in level.split(",") if part.strip()]
    clusters, docs = (load_levels_priority(case_dir, levels) if len(levels) > 1 else load_level(case_dir, level))
    rng = random.Random(seed)
    if selected_cluster_ids is not None:
        wanted = set(selected_cluster_ids)
        clusters = [cluster for cluster in clusters if cluster[0]["cluster_id"] in wanted]
        if {cluster[0]["cluster_id"] for cluster in clusters} != wanted:
            raise ValueError("one or more selected_cluster_ids are unavailable")
    if k is not None:
        if not 1 <= k <= len(clusters):
            raise ValueError(f"k must be in [1, {len(clusters)}]")
        if len(levels) > 1:
            selected = []
            for selected_level in levels:
                candidates = [cluster for cluster in clusters if cluster[0]["level"] == selected_level]
                take = min(k - len(selected), len(candidates))
                if take:
                    selected.extend(rng.sample(candidates, take))
                if len(selected) == k:
                    break
            clusters = selected
        else:
            clusters = rng.sample(clusters, k)
    output.mkdir(parents=True, exist_ok=True)
    mutations: list[dict[str, Any]] = []
    cluster_records = []
    enabled = set(enabled_operators or ENABLED_OPERATORS)
    for cluster_index, cluster in enumerate(clusters, 1):
        cluster_dir = output / f"cluster_{cluster_index:04d}"
        cluster_dir.mkdir()
        select_prompt = selector_input(cluster, docs)
        atomic_text(cluster_dir / "operator_selection.prompt.md", select_prompt)
        selection = selector(SELECTOR_MODEL, "medium", select_prompt, SELECTION_SCHEMA)
        # Some compatible endpoints occasionally unwrap the structured response
        # and return the operator list itself.  Treat that form as a valid
        # selector response instead of failing the whole case with
        # ``list has no attribute get``.  The normal object-shaped response is
        # left unchanged.
        if isinstance(selection, list):
            selection = {
                "applicable_operators": [
                    x if isinstance(x, str) else x.get("operator")
                    for x in selection
                    if isinstance(x, str) or (isinstance(x, dict) and isinstance(x.get("operator"), str))
                ],
                "operator_reasons": [],
                "selector_unwrapped_list": True,
            }
        elif not isinstance(selection, dict):
            selection = {"applicable_operators": [], "operator_reasons": [],
                         "selector_invalid_response": repr(selection)}
        # The caller may restrict the enabled operator family (for example to
        # repository-relational R1-R3).  The selector is still asked for all
        # six operators, then its answer is filtered to the configured family.
        allowed = list(dict.fromkeys(
            op for op in selection.get("applicable_operators", [])
            if op in enabled or op == forced_operator
        ))
        if forced_operator in OPERATORS and forced_operator not in allowed:
            allowed.append(forced_operator)
        fallback = not allowed
        if fallback:
            allowed = ["R1" if enabled <= {"R1", "R2", "R3"} else "L1"]
        operator = forced_operator if forced_operator in allowed or forced_operator in OPERATORS else rng.choice(allowed)
        atomic_json(cluster_dir / "operator_selection.json", {**selection, "fallback_to_R1": fallback, "selected_operator": operator})
        location_records = []
        relational_responses: dict[str, dict[str, Any]] = {}
        if operator not in LOCAL_OPERATORS:
            prompt = relational_cluster_input(operator, cluster, docs, repo)
            atomic_text(cluster_dir / "cluster_mutation.prompt.md", prompt)
            expected = {row["unit_id"] for row in cluster}
            source_by_id = {row["unit_id"]: row["unit_source"] for row in cluster}
            retry_prompt = prompt
            last_error: Exception | None = None
            for relational_attempt in range(1, 7):
                attempt_prefix = f"cluster_mutation.attempt_{relational_attempt:02d}"
                attempt_prompt = cluster_dir / f"{attempt_prefix}.prompt.md"
                attempt_response = cluster_dir / f"{attempt_prefix}.response.json"
                attempt_log = cluster_dir / f"{attempt_prefix}.codex.jsonl"
                atomic_text(attempt_prompt, retry_prompt)
                try:
                    response = relational_mutator(
                        repo, retry_prompt, attempt_response, attempt_log, CLUSTER_MUTATION_SCHEMA,
                    )
                    # Mock mutators do not necessarily persist their returned response.
                    atomic_json(attempt_response, response)
                    returned = response.get("mutations", [])
                    aligned_ids = align_transcribed_unit_ids(returned, expected)
                    returned_ids = [item.get("unit_id") for item in returned]
                    counts = Counter(returned_ids)
                    actual = set(returned_ids)
                    duplicates = sorted(str(unit_id) for unit_id, count in counts.items() if count > 1)
                    missing = sorted(expected - actual)
                    extra = sorted(str(unit_id) for unit_id in actual - expected)
                    if not missing and not extra and not duplicates and len(returned) == len(expected):
                        invalid_mutations = {}
                        for item in returned:
                            try:
                                normalized = normalize_replacement(
                                    source_by_id[item["unit_id"]], item["mutated_unit_source"])
                                validate_replacement(source_by_id[item["unit_id"]], normalized)
                            except (KeyError, ValueError) as exc:
                                invalid_mutations[item.get("unit_id", "<missing>")] = str(exc)
                        if not invalid_mutations:
                            relational_responses = {item["unit_id"]: item for item in returned}
                            atomic_json(cluster_dir / "cluster_mutation.response.json", {
                                **response, "aligned_unit_ids": aligned_ids,
                            })
                            break
                        last_error = ValueError(
                            f"cluster response has invalid sentence mutations: {invalid_mutations}"
                        )
                        retry_prompt = prompt + (
                            "\n\nRETRY REQUIREMENT: The previous response had a complete unit_id set, but one or "
                            "more returned sentences were empty, unchanged, or structurally invalid. Return a "
                            "meaningfully changed false documented contract for every unit_id, while preserving "
                            "the same coherent repository-level relation across the cluster.\n"
                            f"Expected IDs: {json.dumps(sorted(expected), ensure_ascii=False)}\n"
                            f"Invalid mutations: {json.dumps(invalid_mutations, ensure_ascii=False)}"
                        )
                        if relational_attempt == 6:
                            raise RuntimeError(
                                "relational cluster mutation failed after 3 attempts"
                            ) from last_error
                        continue
                    last_error = ValueError(
                        "cluster mutation must return exactly one result per unit_id; "
                        f"missing={missing}, extra={extra}, duplicates={duplicates}"
                    )
                    retry_prompt = prompt + (
                        "\n\nRETRY REQUIREMENT: The previous structured response had an invalid unit_id set. "
                        "Return every expected unit_id exactly once and no other IDs. Do not omit or duplicate "
                        "locations. Preserve the same coherent repository-level mutation across the cluster.\n"
                        f"Expected IDs: {json.dumps(sorted(expected), ensure_ascii=False)}\n"
                        f"Returned IDs: {json.dumps(returned_ids, ensure_ascii=False)}\n"
                        f"Missing IDs: {json.dumps(missing, ensure_ascii=False)}\n"
                        f"Extra IDs: {json.dumps(extra, ensure_ascii=False)}\n"
                        f"Duplicate IDs: {json.dumps(duplicates, ensure_ascii=False)}"
                    )
                except Exception as exc:
                    last_error = exc
                    retry_prompt = prompt + (
                        "\n\nRETRY REQUIREMENT: The previous repository-agent attempt failed before a valid "
                        "cluster response was accepted. Explore within the same five-command budget, then return "
                        "every expected unit_id exactly once and no other IDs.\n"
                        f"Expected IDs: {json.dumps(sorted(expected), ensure_ascii=False)}\n"
                        f"Previous error: {type(exc).__name__}: {exc}"
                    )
                    if relational_attempt == 6:
                        raise RuntimeError(
                            "relational cluster mutation failed after 6 attempts"
                        ) from last_error
        for location_index, row in enumerate(cluster, 1):
            doc = docs[row["documentation_id"]]
            prompt = mutation_input(operator, row, doc, repo)
            stem = cluster_dir / f"location_{location_index:04d}"
            atomic_text(stem.with_suffix(".prompt.md"), prompt)
            if operator in LOCAL_OPERATORS:
                for mutation_attempt in range(1, 4):
                    retry_prompt = prompt if mutation_attempt == 1 else prompt + (
                        "\n\nRETRY REQUIREMENT: Your previous response did not change the target sentence. "
                        "Return a meaningfully different, false documented contract while preserving formatting."
                    )
                    response = local_mutator(LOCAL_MODEL, "medium", retry_prompt, MUTATION_SCHEMA)
                    try:
                        response["mutated_unit_source"] = normalize_replacement(
                            row["unit_source"], response["mutated_unit_source"])
                        validate_replacement(row["unit_source"], response["mutated_unit_source"])
                        break
                    except ValueError:
                        if mutation_attempt == 3:
                            raise
            else:
                response = relational_responses[row["unit_id"]]
                atomic_json(stem.with_suffix(".response.json"), response)
            mutated = normalize_replacement(row["unit_source"], response["mutated_unit_source"])
            validate_replacement(row["unit_source"], mutated)
            record = {
                "cluster_id": row["cluster_id"], "cluster_label": row["cluster_label"],
                "operator": operator, "documentation_id": row["documentation_id"],
                "unit_id": row["unit_id"], "file": row["file"], "symbol": row["symbol"],
                "file_line_start": row["file_line_start"], "file_line_end": row["file_line_end"],
                "source_start_offset": row["source_start_offset"], "source_end_offset": row["source_end_offset"],
                "original_unit_source": row["unit_source"], "mutated_unit_source": mutated,
                "changed_contract": response.get("changed_contract", ""),
                "evidence": response.get("evidence", ""),
                "complete_access_location": bounded_context(doc),
            }
            atomic_json(stem.with_suffix(".json"), record)
            mutations.append(record)
            location_records.append(record)
        cluster_records.append({
            "cluster_id": cluster[0]["cluster_id"], "label": cluster[0]["cluster_label"],
            "applicable_operators": allowed, "selected_operator": operator,
            "locations": location_records,
        })
    apply_mutations(repo, docs, mutations)
    patch = subprocess.check_output(["git", "diff", "--binary", "--"], cwd=repo, text=True)
    if not patch.strip():
        raise RuntimeError("mutation produced an empty git patch")
    atomic_text(output / "mutation.patch", patch)
    result = {
        "instance_id": json.loads((case_dir / "task.json").read_text())["instance_id"],
        "level": level, "seed": seed, "selected_cluster_count": len(clusters),
        "mutation_count": len(mutations), "clusters": cluster_records,
        "patch_sha256": hashlib.sha256(patch.encode()).hexdigest(),
    }
    atomic_json(output / "manifest.json", result)
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case-dir", type=Path, required=True)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--level", default="level_1")
    parser.add_argument("--seed", type=int, default=6938)
    parser.add_argument("--k", type=int)
    args = parser.parse_args()
    generate(args.case_dir.resolve(), args.repo.resolve(), args.output.resolve(), args.level, args.seed, args.k)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
