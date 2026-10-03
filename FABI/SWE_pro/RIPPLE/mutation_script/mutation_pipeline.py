#!/usr/bin/env python3
"""Generate one validated multi-cluster, documentation-only mutation patch."""

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
import tempfile
import time
import tokenize
from collections import defaultdict
from pathlib import Path
from typing import Any

from openai import OpenAI

try:
    from .prompts import mutation_prompt, selector_prompt
except ImportError:
    from prompts import mutation_prompt, selector_prompt


MODEL = "gpt-5.6-luna"
ALL_OPERATORS = ("L1", "L2", "L3", "R1", "R2", "R3")
DEFAULT_OPERATORS = ("L1", "L2", "L3")
LOCAL_OPERATORS = {"L1", "L2", "L3"}
RELATIONAL_OPERATORS = {"R1", "R2", "R3"}
REPOSITORIES = {
    "ansible/ansible": Path("/data/zlyuaj/coding_agent_big_files/swebench-pro/repos/ansible"),
    "internetarchive/openlibrary": Path("/data/zlyuaj/coding_agent_big_files/swebench-pro/repos/openlibrary"),
    "qutebrowser/qutebrowser": Path("/data/zlyuaj/coding_agent_big_files/swebench-pro/repos/qutebrowser"),
}
CODEX = Path("/data/zlyuaj/.nvm/versions/node/v24.18.0/bin/codex")

def selection_schema(enabled_operators: tuple[str, ...]) -> dict[str, Any]:
    return {
        "type": "object",
        "properties": {
            "applicable_operators": {
                "type": "array", "items": {"type": "string", "enum": list(enabled_operators)},
            },
        "operator_reasons": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "operator": {"type": "string", "enum": list(enabled_operators)},
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
CLUSTER_SCHEMA = {
    "type": "object",
    "properties": {
        "mutations": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "unit_id": {"type": "string"},
                    **MUTATION_SCHEMA["properties"],
                },
                "required": ["unit_id", *MUTATION_SCHEMA["required"]],
                "additionalProperties": False,
            },
        }
    },
    "required": ["mutations"],
    "additionalProperties": False,
}


def atomic_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f"{path.name}.{os.getpid()}.tmp")
    temporary.write_text(text)
    temporary.replace(path)


def atomic_json(path: Path, value: Any) -> None:
    atomic_text(path, json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def api_config(path: Path) -> tuple[str, str]:
    content = path.read_text()
    key = content.splitlines()[0].strip()
    match = re.search(r"base_url\s*=\s*['\"]([^'\"]+)", content)
    if not key or not match:
        raise ValueError(f"invalid API config: {path}")
    return key, match.group(1)


def strip_fence(text: str) -> str:
    text = text.strip()
    if text.startswith("```"):
        text = text.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    return text


def parse_object(text: str) -> dict[str, Any]:
    text = strip_fence(text)
    try:
        value = json.loads(text)
    except json.JSONDecodeError:
        decoder = json.JSONDecoder()
        value = None
        for index, char in enumerate(text):
            if char != "{":
                continue
            try:
                candidate, _ = decoder.raw_decode(text[index:])
            except json.JSONDecodeError:
                continue
            if isinstance(candidate, dict):
                value = candidate
                break
        if value is None:
            raise
    if not isinstance(value, dict):
        raise ValueError("model response is not a JSON object")
    return value


class LunaClient:
    def __init__(self, key: str, base_url: str):
        self.key = key
        self.base_url = base_url
        self.client = OpenAI(api_key=key, base_url=base_url, timeout=300, max_retries=0)

    def json(self, prompt: str, schema: dict[str, Any], effort: str = "medium") -> dict[str, Any]:
        last_error: Exception | None = None
        # This account is also used by long-running clean experiments. Wait up
        # to roughly 35 minutes for a provider concurrency slot rather than
        # turning expected cross-run contention into a failed mutation case.
        for attempt in range(1, 41):
            try:
                response = self.client.chat.completions.create(
                    model=MODEL,
                    messages=[{"role": "user", "content": prompt}],
                    reasoning_effort=effort,
                    max_tokens=8192,
                    response_format={"type": "json_schema", "json_schema": {
                        "name": "ripple_mutation", "strict": True, "schema": schema,
                    }},
                )
                return parse_object(response.choices[0].message.content or "")
            except Exception as exc:
                last_error = exc
                transient = isinstance(exc, json.JSONDecodeError) or any(
                    marker in str(exc).lower()
                    for marker in (
                        "429", "502", "503", "rate_limit", "concurrency limit",
                        "timeout", "connection", "temporarily unavailable", "upstream_error",
                    )
                )
                if attempt == 40 or not transient:
                    break
                time.sleep(min(60, 5 * 2 ** (attempt - 1)))
        raise RuntimeError(f"Luna structured request failed: {last_error}") from last_error


def bounded_context(doc: dict[str, Any]) -> str:
    """Include no more than 100 lines before and after the documentation."""
    source = doc["function_source"]
    lines = source.splitlines(keepends=True)
    if len(lines) <= 201:
        return source
    function_start = int(doc["function_start_line"])
    doc_start = int(doc["documentation_start_line"]) - function_start
    doc_end = int(doc["documentation_end_line"]) - function_start
    start = max(0, doc_start - 100)
    end = min(len(lines), doc_end + 101)
    prefix = f"... omitted through repository line {function_start + start - 1} ...\n" if start else ""
    suffix = f"... omitted after repository line {function_start + end - 1} ...\n" if end < len(lines) else ""
    return prefix + "".join(lines[start:end]) + suffix


def load_clusters(case_dir: Path) -> tuple[list[list[dict[str, Any]]], dict[str, dict[str, Any]]]:
    docs = {row["documentation_id"]: row for row in read_jsonl(case_dir / "all_doc.jsonl")}
    groups: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in read_jsonl(case_dir / "clustered_doc.jsonl"):
        if not row.get("mutable", True):
            continue
        if row["documentation_id"] not in docs:
            raise ValueError(f"unknown documentation_id: {row['documentation_id']}")
        groups[row["cluster_id"]].append(row)
    clusters = [sorted(rows, key=lambda row: (row["file"], row["file_line_start"], row["unit_index"]))
                for _, rows in sorted(groups.items())]
    return clusters, docs


def select_clusters(clusters: list[list[dict[str, Any]]], k: int, seed: int) -> list[list[dict[str, Any]]]:
    if k < 1:
        raise ValueError("k must be positive")
    candidates = clusters[:]
    random.Random(seed).shuffle(candidates)
    selected: list[list[dict[str, Any]]] = []
    occupied: set[str] = set()
    for cluster in candidates:
        unit_ids = {row["unit_id"] for row in cluster}
        if occupied.isdisjoint(unit_ids):
            selected.append(cluster)
            occupied.update(unit_ids)
        if len(selected) == k:
            return selected
    if selected:
        return selected
    raise ValueError("no non-overlapping mutable documentation clusters are available")


def preserve_cluster_claims(cluster: list[dict[str, Any]], count: int, seed: int
                            ) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Deterministically split a cluster into consistent and mutated claims."""
    if count < 0:
        raise ValueError("preserve count must be non-negative")
    if count >= len(cluster):
        raise ValueError("a selected cluster must retain at least one claim to mutate")
    preserved = random.Random(seed).sample(cluster, count) if count else []
    preserved_ids = {row["unit_id"] for row in preserved}
    mutated = [row for row in cluster if row["unit_id"] not in preserved_ids]
    return preserved, mutated


def selector_input(cluster: list[dict[str, Any]], docs: dict[str, dict[str, Any]],
                   enabled_operators: tuple[str, ...]) -> str:
    payload = {
        "cluster_id": cluster[0]["cluster_id"],
        "cluster_label": cluster[0].get("cluster_label"),
        "cluster_summary": cluster[0].get("cluster_summary"),
        "locations": [{
            "unit_id": row["unit_id"], "file": row["file"], "symbol": row["symbol"],
            "target_documentation_sentence": row["unit_text"],
            "complete_access_location": bounded_context(docs[row["documentation_id"]]),
        } for row in cluster],
    }
    return selector_prompt(enabled_operators) + "\n\nCLUSTER INPUT:\n" + json.dumps(payload, ensure_ascii=False, indent=2)


def applicable_operators(selection: dict[str, Any],
                         enabled_operators: tuple[str, ...]) -> tuple[list[str], bool]:
    enabled = set(enabled_operators)
    allowed = list(dict.fromkeys(
        operator for operator in selection.get("applicable_operators", [])
        if operator in enabled
    ))
    fallback = not allowed
    return (allowed or [enabled_operators[0]]), fallback


def local_input(operator: str, row: dict[str, Any], doc: dict[str, Any]) -> str:
    payload = {
        "operator": operator, "repository_file": row["file"], "symbol": row["symbol"],
        "repository_line": row["file_line_start"],
        "complete_access_location": bounded_context(doc),
        "TARGET_UNIT_SOURCE": row["unit_source"],
    }
    return mutation_prompt(operator) + "\n\nMUTATION INPUT:\n" + json.dumps(payload, ensure_ascii=False, indent=2)


def relational_input(operator: str, cluster: list[dict[str, Any]], docs: dict[str, dict[str, Any]],
                     tool_budget: int) -> str:
    payload = {
        "operator": operator,
        "cluster_id": cluster[0]["cluster_id"],
        "cluster_summary": cluster[0].get("cluster_summary"),
        "locations": [{
            "unit_id": row["unit_id"], "repository_file": row["file"],
            "repository_line": row["file_line_start"], "symbol": row["symbol"],
            "complete_access_location": bounded_context(docs[row["documentation_id"]]),
            "TARGET_UNIT_SOURCE": row["unit_source"],
        } for row in cluster],
    }
    instructions = """
Explore the repository read-only to identify callers, callees, sibling entities, and related contracts. Use the exact file paths and line numbers above as anchors. Apply one coherent repository-level false relation to every location in the cluster and return exactly one mutation per unit_id. Each false relation must be grounded in a real repository entity or execution scope found during exploration; never invent a symbol. Do not edit any file. You may execute at most {tool_budget} read-only shell commands. Return JSON matching the supplied schema and no prose.
"""
    return (mutation_prompt(operator) + instructions.format(tool_budget=tool_budget)
            + "\nCLUSTER MUTATION INPUT:\n" + json.dumps(payload, ensure_ascii=False, indent=2)
            + "\n\nJSON SCHEMA:\n" + json.dumps(CLUSTER_SCHEMA, indent=2))


class ToolBudgetExceeded(RuntimeError):
    pass


def error_category(exc: Exception) -> str:
    message = str(exc).lower()
    if isinstance(exc, ToolBudgetExceeded):
        return "exploration_budget"
    if any(marker in message for marker in (
        "429", "502", "503", "rate limit", "concurrency limit", "timeout",
        "connection", "temporarily unavailable", "upstream", "reconnecting",
    )):
        return "provider_transient"
    if isinstance(exc, (json.JSONDecodeError, ValueError)) or any(
        marker in message for marker in ("schema", "unit_id", "unchanged", "empty", "delimiter")
    ):
        return "model_output"
    if "codex exited" in message or "last message" in message:
        return "agent_runtime"
    return "unknown"


def codex_json(repo: Path, prompt: str, output: Path, log: Path, client: LunaClient,
               tool_budget: int) -> dict[str, Any]:
    schema_path = output.with_suffix(".schema.json")
    atomic_json(schema_path, CLUSTER_SCHEMA)
    home = output.parent / "codex_home"
    home.mkdir(exist_ok=True)
    config = (
        f'model = "{MODEL}"\nmodel_provider = "cctq"\nmodel_reasoning_effort = "high"\n'
        'approval_policy = "never"\nsandbox_mode = "read-only"\n'
        '[shell_environment_policy]\ninherit = "all"\nexclude = ["OPENAI_API_KEY"]\n'
        '[model_providers.cctq]\nname = "cctq"\n'
        f'base_url = "{client.base_url}"\nenv_key = "OPENAI_API_KEY"\nwire_api = "responses"\n'
    )
    atomic_text(home / "config.toml", config)
    env = os.environ.copy()
    env.update(CODEX_HOME=str(home), OPENAI_API_KEY=client.key)
    command = [str(CODEX), "--disable", "shell_snapshot", "--disable", "plugins",
               "--disable", "recommended_plugins", "--disable", "remote_plugin", "exec",
               "-C", str(repo), "--ephemeral", "--ignore-rules", "--json", "-m", MODEL,
               "-s", "read-only", "--output-schema", str(schema_path),
               "--output-last-message", str(output), "-"]
    tool_calls = 0
    with log.open("w") as handle:
        process = subprocess.Popen(
            command, cwd=repo, env=env, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT, text=True, start_new_session=True,
        )
        assert process.stdin is not None and process.stdout is not None
        process.stdin.write(prompt)
        process.stdin.close()
        for line in process.stdout:
            handle.write(line)
            handle.flush()
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue
            item = event.get("item") or {}
            if event.get("type") == "item.started" and item.get("type") == "command_execution":
                tool_calls += 1
                if tool_calls > tool_budget:
                    process.terminate()
                    try:
                        process.wait(timeout=30)
                    except subprocess.TimeoutExpired:
                        process.kill()
                        process.wait(timeout=30)
                    raise ToolBudgetExceeded(
                        f"relational Codex exceeded {tool_budget} tool executions"
                    )
        returncode = process.wait(timeout=30)
    if returncode:
        raise RuntimeError(f"relational Codex exited {returncode}; see {log}")
    if not output.is_file():
        raise RuntimeError("relational Codex produced no last message")
    value = parse_object(output.read_text())
    value["tool_executions"] = tool_calls
    return value


def validate_relational_response(response: dict[str, Any], cluster: list[dict[str, Any]]) -> dict[str, dict]:
    expected = {row["unit_id"] for row in cluster}
    returned = response.get("mutations", [])
    if not isinstance(returned, list):
        raise ValueError("relational response mutations is not a list")
    returned_ids = [item.get("unit_id") for item in returned if isinstance(item, dict)]
    if len(returned) != len(expected) or len(set(returned_ids)) != len(returned_ids):
        raise ValueError("relational response must contain every expected unit_id exactly once")
    if set(returned_ids) != expected:
        raise ValueError("relational response unit_id set does not match the cluster")
    by_id = {item["unit_id"]: item for item in returned}
    for row in cluster:
        item = by_id[row["unit_id"]]
        for field in ("changed_contract", "evidence"):
            if not isinstance(item.get(field), str) or not item[field].strip():
                raise ValueError(f"relational response has empty {field}: {row['unit_id']}")
        normalize(row["unit_source"], item.get("mutated_unit_source"))
    return by_id


def normalize(original: str, mutated: str) -> str:
    if not isinstance(mutated, str):
        raise ValueError("mutation is not text")
    body = mutated.strip(" \t\r\n")
    if not body:
        raise ValueError("mutation is empty")
    source_lines, output_lines = original.splitlines(), body.splitlines()
    base_indent = re.match(r"^[ \t]*", original).group(0)
    indents = ([re.match(r"^[ \t]*", line).group(0) for line in source_lines]
               if len(source_lines) == len(output_lines) else [base_indent] * len(output_lines))
    normalized_lines = []
    for indent, line in zip(indents, output_lines):
        content = line.strip(" \t")
        normalized_lines.append(indent + content if content else "")
    value = "\n".join(normalized_lines)
    if original.endswith("\r\n"):
        value = value.replace("\n", "\r\n") + "\r\n"
    elif original.endswith("\n"):
        value += "\n"
    if value == original or any(token in value for token in ('"""', "'''", "```")):
        raise ValueError("mutation is unchanged or contains a forbidden delimiter")
    return value


def semantic_tokens(source: str) -> list[tuple[int, str]]:
    tree = ast.parse(source)
    doc_ranges = []
    for node in ast.walk(tree):
        body = getattr(node, "body", None)
        if isinstance(body, list) and body:
            first = body[0]
            if isinstance(first, ast.Expr) and isinstance(first.value, ast.Constant) and isinstance(first.value.value, str):
                doc_ranges.append((first.lineno, first.end_lineno or first.lineno))
    ignored = {tokenize.COMMENT, tokenize.ENCODING, tokenize.NL, tokenize.NEWLINE,
               tokenize.INDENT, tokenize.DEDENT, tokenize.ENDMARKER}
    result = []
    for token in tokenize.generate_tokens(io.StringIO(source).readline):
        if token.type in ignored:
            continue
        if token.type == tokenize.STRING and any(start <= token.start[0] <= end for start, end in doc_ranges):
            continue
        result.append((token.type, token.string))
    return result


def apply_mutations(repo: Path, docs: dict[str, dict[str, Any]], mutations: list[dict[str, Any]]) -> list[str]:
    by_doc: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for mutation in mutations:
        by_doc[mutation["documentation_id"]].append(mutation)
    before_files: dict[Path, str] = {}
    locations = []
    for doc_id, changes in by_doc.items():
        doc = docs[doc_id]
        path = repo / doc["file"]
        baseline = before_files.setdefault(path, path.read_text())
        source = doc["documentation_source"]
        annotated_start = int(doc["documentation_start_line"]) - 1
        annotated_end = int(doc["documentation_end_line"])
        if "".join(baseline.splitlines(keepends=True)[annotated_start:annotated_end]) == source:
            start, end = annotated_start, annotated_end
        else:
            matches = [match.start() for match in re.finditer(re.escape(source), baseline)]
            if len(matches) != 1:
                raise ValueError(f"documentation source mismatch at {doc['file']}:{annotated_start + 1}")
            start = baseline.count("\n", 0, matches[0])
            end = start + len(source.splitlines(keepends=True))
        locations.append((path, start, end, doc_id, changes))
    for path, start, end, doc_id, changes in sorted(locations, key=lambda item: (str(item[0]), -item[1])):
        original_doc = docs[doc_id]["documentation_source"]
        updated_doc = original_doc
        for change in sorted(changes, key=lambda item: item["source_start_offset"], reverse=True):
            a, b = int(change["source_start_offset"]), int(change["source_end_offset"])
            if original_doc[a:b] != change["original_unit_source"]:
                raise ValueError(f"unit offset mismatch: {change['unit_id']}")
            updated_doc = updated_doc[:a] + change["mutated_unit_source"] + updated_doc[b:]
        lines = path.read_text().splitlines(keepends=True)
        if "".join(lines[start:end]) != original_doc:
            raise ValueError(f"documentation moved during mutation: {path}:{start + 1}")
        lines[start:end] = updated_doc.splitlines(keepends=True)
        path.write_text("".join(lines))
    for path, before in before_files.items():
        after = path.read_text()
        if path.suffix == ".py" and semantic_tokens(before) != semantic_tokens(after):
            raise ValueError(f"non-documentation Python tokens changed: {path}")
    subprocess.run(["git", "diff", "--check"], cwd=repo, check=True)
    return sorted(str(path.relative_to(repo)) for path in before_files)


def generate(case_dir: Path, task: dict[str, Any], output: Path, seed: int, k: int,
             api_path: Path, enabled_operators: tuple[str, ...] = DEFAULT_OPERATORS,
             relational_attempts: int = 5, relational_tool_budget: int = 8,
             relational_max_tool_budget: int = 24, documents_per_cluster: int = 0,
             preserve_documents_per_cluster: int = 0) -> dict[str, Any]:
    if not enabled_operators or not set(enabled_operators) <= set(ALL_OPERATORS):
        raise ValueError(f"invalid enabled operators: {enabled_operators}")
    clusters, docs = load_clusters(case_dir)
    if preserve_documents_per_cluster < 0:
        raise ValueError("preserve_documents_per_cluster must be non-negative")
    if documents_per_cluster and preserve_documents_per_cluster:
        raise ValueError("document sampling and document preservation are mutually exclusive")
    candidates = ([cluster for cluster in clusters
                   if len(cluster) > preserve_documents_per_cluster]
                  if preserve_documents_per_cluster else clusters)
    selected_full = select_clusters(candidates, k, seed)
    if documents_per_cluster < 0:
        raise ValueError("documents_per_cluster must be non-negative")
    if documents_per_cluster:
        selected_full = [random.Random(seed + index).sample(cluster, min(documents_per_cluster, len(cluster)))
                         for index, cluster in enumerate(selected_full)]
    selected = []
    preserved_by_cluster = []
    for index, cluster in enumerate(selected_full):
        preserved, mutated = preserve_cluster_claims(
            cluster, preserve_documents_per_cluster, seed + index,
        )
        preserved_by_cluster.append(preserved)
        selected.append(mutated)
    key, base_url = api_config(api_path)
    client = LunaClient(key, base_url)
    source_repo = REPOSITORIES[task["repo"]]
    output.mkdir(parents=True, exist_ok=False)
    # Keep the temporary clone on the experiment filesystem. The source repos
    # and /tmp may be different mounts, which makes `git clone --local` fail
    # while attempting to hard-link object packs across devices.
    with tempfile.TemporaryDirectory(prefix="worktree-", dir=output) as temporary:
        repo = Path(temporary) / "repo"
        subprocess.run(["git", "clone", "--local", "--no-checkout", "-q", str(source_repo), str(repo)], check=True)
        subprocess.run(["git", "checkout", "--detach", "-q", task["base_commit"]], cwd=repo, check=True)
        mutations = []
        cluster_results = []
        rng = random.Random(seed)
        for cluster_index, (full_cluster, cluster, preserved) in enumerate(
                zip(selected_full, selected, preserved_by_cluster), 1):
            cluster_dir = output / f"cluster_{cluster_index:04d}"
            cluster_dir.mkdir()
            prompt = selector_input(full_cluster, docs, enabled_operators)
            atomic_text(cluster_dir / "operator_selection.prompt.md", prompt)
            selection = client.json(prompt, selection_schema(enabled_operators), "medium")
            allowed, fallback = applicable_operators(selection, enabled_operators)
            operator = rng.choice(allowed)
            atomic_json(cluster_dir / "operator_selection.json", {
                **selection, "applicable_operators": allowed,
                "fallback_used": fallback, "selected_operator": operator,
            })
            relational = {}
            if operator not in LOCAL_OPERATORS:
                expected = {row["unit_id"] for row in cluster}
                last_error = None
                error_history = []
                retry_context = ""
                for attempt in range(1, relational_attempts + 1):
                    tool_budget = min(
                        relational_max_tool_budget,
                        relational_tool_budget + (attempt - 1) * max(2, relational_tool_budget // 2),
                    )
                    rel_prompt = relational_input(operator, cluster, docs, tool_budget) + retry_context
                    prompt_path = cluster_dir / f"cluster_mutation.attempt_{attempt:02d}.prompt.md"
                    response_path = cluster_dir / f"cluster_mutation.attempt_{attempt:02d}.response.json"
                    log_path = cluster_dir / f"cluster_mutation.attempt_{attempt:02d}.codex.jsonl"
                    atomic_text(prompt_path, rel_prompt)
                    try:
                        response = codex_json(
                            repo, rel_prompt, response_path, log_path, client, tool_budget,
                        )
                        relational = validate_relational_response(response, cluster)
                        atomic_json(cluster_dir / "cluster_mutation.response.json", response)
                        break
                    except Exception as exc:
                        last_error = exc
                        category = error_category(exc)
                        error_record = {
                            "attempt": attempt, "category": category,
                            "tool_budget": tool_budget, "error_type": type(exc).__name__,
                            "error": str(exc), "log": str(log_path),
                        }
                        error_history.append(error_record)
                        atomic_json(
                            cluster_dir / f"cluster_mutation.attempt_{attempt:02d}.error.json",
                            error_record,
                        )
                        retry_context = (
                            "\n\nRECOVERY REQUIREMENTS:\n"
                            f"- Previous failure category: {category}.\n"
                            f"- Previous failure: {exc}.\n"
                            f"- Return each unit exactly once: {sorted(expected)}.\n"
                            "- Re-explore from the supplied file/line anchors and use real repository entities.\n"
                            "- Make every replacement materially different while preserving its sentence formatting.\n"
                        )
                if not relational:
                    atomic_json(cluster_dir / "cluster_mutation.errors.json", error_history)
                    raise RuntimeError(
                        f"relational mutation failed after {relational_attempts} attempts: {last_error}"
                    )
            location_results = []
            for location_index, row in enumerate(cluster, 1):
                stem = cluster_dir / f"location_{location_index:04d}"
                if operator in LOCAL_OPERATORS:
                    local_prompt = local_input(operator, row, docs[row["documentation_id"]])
                    atomic_text(stem.with_suffix(".prompt.md"), local_prompt)
                    response = None
                    last_error = None
                    for attempt in range(1, 4):
                        try:
                            response = client.json(local_prompt, MUTATION_SCHEMA, "medium")
                            response["mutated_unit_source"] = normalize(row["unit_source"], response["mutated_unit_source"])
                            break
                        except Exception as exc:
                            last_error = exc
                            local_prompt += "\n\nRETRY: Return a materially changed false contract while preserving formatting."
                    if response is None:
                        raise RuntimeError(f"local mutation failed: {last_error}")
                else:
                    response = relational[row["unit_id"]]
                    response["mutated_unit_source"] = normalize(row["unit_source"], response["mutated_unit_source"])
                atomic_json(stem.with_suffix(".response.json"), response)
                record = {
                    "cluster_id": row["cluster_id"], "operator": operator,
                    "documentation_id": row["documentation_id"], "unit_id": row["unit_id"],
                    "file": row["file"], "symbol": row["symbol"],
                    "file_line_start": row["file_line_start"], "file_line_end": row["file_line_end"],
                    "source_start_offset": row["source_start_offset"], "source_end_offset": row["source_end_offset"],
                    "original_unit_source": row["unit_source"],
                    "mutated_unit_source": response["mutated_unit_source"],
                    "changed_contract": response["changed_contract"], "evidence": response["evidence"],
                }
                atomic_json(stem.with_suffix(".json"), record)
                mutations.append(record)
                location_results.append(record)
            cluster_results.append({
                "cluster_id": cluster[0]["cluster_id"], "label": cluster[0].get("cluster_label"),
                "all_levels_in_source_data": sorted({level for row in cluster for level in row.get("levels", [row.get("level")]) if level}),
                "applicable_operators": allowed, "selected_operator": operator,
                "consistent_locations": [{
                    "documentation_id": row["documentation_id"], "unit_id": row["unit_id"],
                    "file": row["file"], "symbol": row["symbol"],
                    "original_unit_source": row["unit_source"],
                } for row in preserved],
                "locations": location_results,
            })
        selected_operators = {cluster["selected_operator"] for cluster in cluster_results}
        if not selected_operators <= set(enabled_operators):
            raise RuntimeError(
                f"disabled mutation operator selected: {sorted(selected_operators - set(enabled_operators))}"
            )
        changed_files = apply_mutations(repo, docs, mutations)
        patch = subprocess.check_output(["git", "diff", "--binary", "--"], cwd=repo, text=True)
        if not patch.strip():
            raise RuntimeError("mutation patch is empty")
        atomic_text(output / "mutation.patch", patch)
        manifest = {
            "status": "validated", "instance_id": task["instance_id"], "repo": task["repo"],
            "base_commit": task["base_commit"], "seed": seed, "k": k,
            "enabled_operators": list(enabled_operators),
            "relational_attempts": relational_attempts,
            "relational_tool_budget": relational_tool_budget,
            "relational_max_tool_budget": relational_max_tool_budget,
            "selected_cluster_count": len(selected), "mutation_count": len(mutations),
            "preserve_documents_per_cluster": preserve_documents_per_cluster,
            "files": changed_files, "clusters": cluster_results,
            "patch_sha256": hashlib.sha256(patch.encode()).hexdigest(),
        }
        atomic_json(output / "mutation.json", manifest)
        return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case-dir", type=Path, required=True)
    parser.add_argument("--task", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--api-config", type=Path, default=Path("/data/zlyuaj/coding_agent/luna_key.txt"))
    parser.add_argument("--seed", type=int, default=20260921)
    parser.add_argument("-k", type=int, default=3)
    parser.add_argument("--operators", nargs="+", choices=ALL_OPERATORS,
                        default=list(DEFAULT_OPERATORS))
    parser.add_argument("--relational-attempts", type=int, default=5)
    parser.add_argument("--relational-tool-budget", type=int, default=8)
    parser.add_argument("--relational-max-tool-budget", type=int, default=24)
    parser.add_argument("--documents-per-cluster", type=int, default=0,
                        help="random mutable documentation locations per selected cluster; 0 keeps all")
    parser.add_argument("--preserve-documents-per-cluster", type=int, default=0,
                        help="random claims kept consistent in each selected cluster")
    args = parser.parse_args()
    task = json.loads(args.task.read_text())
    generate(
        args.case_dir.resolve(), task, args.output.resolve(), args.seed, args.k, args.api_config,
        tuple(args.operators), args.relational_attempts, args.relational_tool_budget,
        args.relational_max_tool_budget, args.documents_per_cluster,
        args.preserve_documents_per_cluster,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
