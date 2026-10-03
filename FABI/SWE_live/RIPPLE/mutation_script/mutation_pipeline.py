#!/usr/bin/env python3
"""Documentation mutation and mutation-aware SWE-bench Live smoke runner.

The clean harness is copied into a run-private directory.  Its worker applies a
case patch after pristine checkout validation and before inference, so shared
repository mirrors and the checked-in clean harness are never changed.
"""
from __future__ import annotations

import argparse
import ast
import csv
import datetime as dt
import hashlib
import io
import json
import os
import random
import re
import signal
import shutil
import subprocess
import sys
import tempfile
import time
import tokenize
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import defaultdict
from pathlib import Path
from typing import Any

from openai import OpenAI

ROOT = Path(__file__).resolve().parents[1]
LIVE_ROOT = ROOT.parent
PLACEMENT_ROOT = LIVE_ROOT / "original_passed_cases_luna" / "placement" / "clean_runs"
CSV_PATH = LIVE_ROOT / "original_passed_cases_luna" / "token_stable_cases.csv"
KEY_FILE = Path("/data/zlyuaj/coding_agent/luna_key.txt")
BIG_REPOS = Path("/data/zlyuaj/coding_agent_big_files/swebench-live-lite/repos")
CODEX = Path("/data/zlyuaj/.nvm/versions/node/v24.18.0/bin/codex")
MODEL = "gpt-5.6-luna"
OPS = {
    "L1": "Interface Contract Drift",
    "L2": "Outcome Contract Drift",
    "L3": "State / Behavior Semantics Drift",
    "R1": "Responsibility / Ownership Drift",
    "R2": "Applicability / Scope Drift",
    "R3": "Dependency / Interaction Drift",
}


def now() -> str:
    return dt.datetime.now().astimezone().isoformat(timespec="seconds")


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(path.name + f".tmp.{os.getpid()}")
    tmp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")
    os.replace(tmp, path)


def read_key() -> tuple[str, str]:
    lines = KEY_FILE.read_text().splitlines()
    key = lines[0].strip()
    base = next((re.search(r"base_url\s*=\s*['\"]([^'\"]+)", x).group(1)
                 for x in lines[1:] if re.search(r"base_url\s*=", x)), "")
    if not key or not base:
        raise RuntimeError(f"invalid API key file: {KEY_FILE}")
    return key, base


def model_json(prompt: str, schema: dict[str, Any], effort: str = "medium") -> dict[str, Any]:
    key, base = read_key()
    client = OpenAI(api_key=key, base_url=base,
                    timeout=float(os.environ.get("RIPPLE_API_TIMEOUT", "45")), max_retries=0)
    last_error = None
    # Relational mutation makes many sequential calls.  A transient provider
    # outage must not turn an entire six-lane run into deterministic failures.
    for attempt in range(7):
        try:
            response = client.chat.completions.create(
                model=MODEL, messages=[{"role": "user", "content": prompt}],
                reasoning_effort=effort, max_tokens=4096,
                response_format={"type": "json_schema", "json_schema": {
                    "name": "mutation", "strict": True, "schema": schema}},
            )
            text = (response.choices[0].message.content or "").strip()
            if text.startswith("```"):
                text = text.split("\n", 1)[1].rsplit("```", 1)[0].strip()
            return json.loads(text)
        except Exception as exc:
            last_error = exc
            message = str(exc)
            if attempt < 6:
                if any(code in message for code in ("429", "502", "503", "504", "temporarily unavailable")):
                    time.sleep((5, 10, 20, 40, 60, 90)[attempt])
                else:
                    time.sleep(min(30, 2 ** attempt))
    raise RuntimeError(f"model request failed after 7 attempts: {last_error}")


def clusters_for(case: dict[str, str], k: int, seed: int) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    path = PLACEMENT_ROOT / case["agent"] / case["instance_id"] / "clustered_doc.jsonl"
    rows = [json.loads(line) for line in path.read_text().splitlines() if line.strip()]
    docs = {row["documentation_id"]: row for row in
            (json.loads(line) for line in (path.parent / "all_doc.jsonl").read_text().splitlines() if line.strip())}
    grouped: dict[str, list[dict[str, Any]]] = {}
    for row in rows:
        grouped.setdefault(row["cluster_id"], []).append(row)
    values = [{"cluster_id": cid, "label": items[0].get("cluster_label", ""),
               "summary": items[0].get("cluster_summary", ""), "items": items}
              for cid, items in grouped.items()
              if all(any(char.isalpha() for char in item["unit_text"]) for item in items)]
    random.Random(f"{seed}:{case['agent']}:{case['instance_id']}").shuffle(values)
    selected, occupied = [], set()
    for cluster in values:
        units = {item["unit_id"] for item in cluster["items"]}
        if occupied.isdisjoint(units):
            selected.append(cluster)
            occupied.update(units)
        if len(selected) == k:
            break
    if not selected:
        raise ValueError(f"no nonoverlapping clusters: {case['agent']} {case['instance_id']}")
    return selected, docs


def position_context(item: dict[str, Any], doc: dict[str, Any]) -> str:
    source = doc["function_source"]
    lines = source.splitlines(keepends=True)
    if len(lines) > 201:
        start = max(0, int(doc["documentation_start_line"]) - int(doc["function_start_line"]) - 100)
        end = min(len(lines), int(doc["documentation_end_line"]) - int(doc["function_start_line"]) + 101)
        lines = lines[start:end]
    return (f"FILE: {item['file']} (documentation lines {item['documentation_start_line']}-"
            f"{item['documentation_end_line']}, function lines {item['function_start_line']}-"
            f"{item['function_end_line']})\nQUALNAME: {item['qualname']}\n"
            f"FUNCTION AND DOCUMENTATION:\n" + "".join(lines) +
            f"\nTARGET DOCUMENTATION SENTENCE:\n{item['unit_text']}")


def choose_operator(cluster: dict[str, Any], enabled: tuple[str, ...]) -> tuple[str, list[str]]:
    docs = "\n\n".join(f"POSITION {i+1}\n{p['unit_text']}" for i, p in enumerate(cluster["items"]))
    rules = ("R1 requires a behavior or concern with a real alternative repository owner. "
             "R2 requires a meaningful applicability domain: mode, path, configuration, platform, version, lifecycle, or entity set. "
             "R3 requires a real or strongly implied call, dependency, delegation, communication, or data-flow relation between entities. "
             "Do not select R2 merely for a return type/value, or R3 merely for a local outcome or an ownership change."
             if all(x.startswith("R") for x in enabled) else
             "L1 requires interface invocation/access; L2 requires output/return/exception; "
             "L3 requires current operation behavior/state/side effect.")
    prompt = f"""You select documentation mutation operators for one cluster.
Return every applicable operator from {','.join(enabled)}. Be permissive, but
each selected operator must be feasible for every location in this cluster.
{rules}
Return only operators from the enabled list. An empty list falls back to R1.
CLUSTER LABEL: {cluster['label']}\nSUMMARY: {cluster['summary']}\n{docs}"""
    schema = {"type": "object", "properties": {"operators": {"type": "array", "items": {"type": "string", "enum": list(enabled)}}}, "required": ["operators"], "additionalProperties": False}
    result = model_json(prompt, schema)
    chosen = [x for x in result.get("operators", []) if x in enabled]
    return random.choice(chosen or ["L3" if "L3" in enabled else enabled[0]]), chosen


RELATIONAL_RULES = {
    "R1": "Reassign one documented behavior or concern to a DIFFERENT REAL repository entity. Name the false owner and the actual owner. Do not merely change a return type, local state, or scope.",
    "R2": "Change ONLY the documented applicability domain (mode, branch, configuration, platform, version, lifecycle, or entity set). Keep return type/value, owner, and call endpoints unchanged.",
    "R3": "Change ONLY a relation between two REAL repository entities: invocation, dependency, delegation, communication, or data flow. Name both endpoints. Keep return type/value, owner, and applicability scope unchanged.",
}


def mutate_sentence(item: dict[str, Any], doc: dict[str, Any], operator: str,
                    repo: Path, artifact: Path | None = None) -> str:
    context = position_context(item, doc)
    if operator.startswith("R"):
        if not CODEX.exists():
            raise RuntimeError(f"Codex executable missing: {CODEX}")
        if artifact is None:
            raise RuntimeError("relational mutation requires an artifact directory")
        artifact.mkdir(parents=True, exist_ok=True)
        key, base = read_key()
        schema = {"type": "object", "properties": {
            "original_span": {"type": "string"}, "replacement_span": {"type": "string"},
            "occurrence": {"type": "integer", "minimum": 1},
            "changed_contract": {"type": "string"},
            "evidence": {"type": "string"}, "explored_files": {"type": "array", "items": {"type": "string"}},
        }, "required": ["original_span", "replacement_span", "occurrence", "changed_contract", "evidence", "explored_files"],
            "additionalProperties": False}
        write_json(artifact / "schema.json", schema)
        prompt = f"""You are a repository researcher creating exactly one documentation sentence mutation.
Read the target file at its supplied line numbers and EXPLORE related caller, callee,
and entity code in this checkout using read-only commands. Use the actual repository
evidence to choose a plausible but false documented relation. Do not edit any file.
Use at most four focused shell commands. Do not list or search the whole repository;
start at the supplied file and symbol, then inspect directly related files. Return
your final JSON immediately after finding enough evidence.

Selected operator {operator}: {OPS[operator]}.
{RELATIONAL_RULES[operator]}

Return strict JSON with: original_span (a SHORT, exact, contiguous substring from
TARGET DOCUMENTATION SOURCE, entirely on one source line), replacement_span (the
replacement text for only that substring, with no newline), occurrence (1-based
index of this exact original_span within TARGET DOCUMENTATION SOURCE, counting
from left to right; use 1 when unique), changed_contract
(the false claim and why it is {operator}), evidence (actual repository fact with
entity names), explored_files (paths you inspected). Change exactly one claim.
Preserve every other character, line break, field directive, and adjacent sentence.
For a `name: value` documentation field, mutate the value after the colon; never
alter the field name before the colon. If the same word occurs in both, select
the occurrence in the value (usually occurrence 2).
Do not replace a whole multi-line unit or combine multiple documentation fields.
Do not include a :param/:return field label in either span. If this target cannot
support the selected operator after exploration, explain that in evidence and
return both spans as empty strings so the caller can choose another cluster.

LOCATION AND COMPLETE FUNCTION CONTEXT:
{context}

TARGET DOCUMENTATION SOURCE (choose original_span verbatim from here):
{item['unit_source']}
"""
        (artifact / "prompt.md").write_text(prompt)
        (artifact / "config.toml").write_text(
            f'model = "{MODEL}"\nmodel_provider = "luna"\nmodel_reasoning_effort = "high"\n'
            'approval_policy = "never"\nsandbox_mode = "read-only"\n'
            '[shell_environment_policy]\ninherit = "all"\nexclude = ["OPENAI_API_KEY"]\n'
            f'[model_providers.luna]\nname = "luna"\nbase_url = "{base}"\n'
            'env_key = "OPENAI_API_KEY"\nwire_api = "responses"\n')
        env = os.environ.copy()
        env.update(CODEX_HOME=str(artifact), OPENAI_API_KEY=key)
        command = [str(CODEX), "--disable", "shell_snapshot", "--disable", "plugins",
                   "--disable", "recommended_plugins", "--disable", "remote_plugin",
                   "exec", "-C", str(repo), "--ephemeral",
                   "--json", "-m", MODEL, "-s", "read-only", "--output-schema",
                   str(artifact / "schema.json"), "--output-last-message",
                   str(artifact / "response.json"), "-"]
        with (artifact / "codex.jsonl").open("w") as log:
            process = subprocess.Popen(command, cwd=repo, env=env, stdin=subprocess.PIPE,
                                       stdout=log, stderr=subprocess.STDOUT, text=True,
                                       start_new_session=True)
            try:
                process.communicate(input=prompt,
                                    timeout=float(os.environ.get("RIPPLE_CODEX_TIMEOUT", "300")))
            except subprocess.TimeoutExpired as exc:
                os.killpg(process.pid, signal.SIGKILL)
                process.wait()
                raise RuntimeError(f"Codex exploration timed out; see {artifact / 'codex.jsonl'}") from exc
        if process.returncode:
            raise RuntimeError(f"Codex exploration exited {process.returncode}; see {artifact / 'codex.jsonl'}")
        result = json.loads((artifact / "response.json").read_text())
        original_source = item["unit_source"]
        if (not result["changed_contract"].strip() or not result["evidence"].strip()
                or not result["explored_files"]):
            raise ValueError(f"Codex did not provide a supported {operator} mutation; see {artifact}")
        replacement = replace_document_span(original_source, result["original_span"],
                                            result["replacement_span"], result["occurrence"])
        judge_schema = {"type": "object", "properties": {
            "operator": {"type": "string", "enum": ["L1", "L2", "L3", "R1", "R2", "R3", "OTHER"]},
            "reason": {"type": "string"}},
            "required": ["operator", "reason"], "additionalProperties": False}
        judgment = model_json(
            "Classify the semantic CLAIM introduced by the replacement relative to "
            "the original documentation. Classify the documented claim's subject, "
            "even when repository evidence proves that claim false; a false relation "
            "is still R3 and a false scope restriction is still R2. "
            "R1: assigns a behavior to another repository entity. "
            "R2: changes the set of modes, paths, configurations, platforms, "
            "versions, lifecycle stages, or entities where a contract applies. "
            "R3: adds, removes, or changes an invocation, delegation, dependency, "
            "communication, or data-flow relation between named repository entities. "
            "The absence of the claimed call in actual code is evidence of a valid "
            "false R3 claim, not a reason to label it L3. Likewise, an untrue mode "
            "restriction is R2, not L3. L1 concerns API invocation parameters or "
            "names; L2 concerns return values, types, exceptions, or output shape; "
            "L3 concerns behavior or state without changing relation, owner, or "
            "applicability. Do not trust the proposed label; identify the changed "
            "claim directly from ORIGINAL and REPLACEMENT.\n"
            f"ORIGINAL: {original_source}\nREPLACEMENT: {replacement}\n"
            f"PROPOSED CONTRACT: {result['changed_contract']}\n"
            f"REPOSITORY EVIDENCE: {result['evidence']}",
            judge_schema, "medium")
        write_json(artifact / "operator_judgment.json", judgment)
        if judgment["operator"] != operator:
            raise ValueError(f"operator mismatch: requested {operator}, classified {judgment['operator']}: {judgment['reason']}")
        return replacement
    prompt = f"""You are generating one plausible documentation-only mutant.
Operator {operator}: {OPS[operator]}.
Read the complete function context below. Change exactly one semantic claim in the
TARGET DOCUMENTATION SENTENCE so it becomes false according to the implementation,
while preserving style, indentation, markup, and sentence length where practical.
Return only the replacement sentence, without quotes or explanation. For R1/R2/R3,
reason from the repository and use concrete caller/callee/entity names; do not
change executable code. The replacement must be non-empty and materially different.
{context}"""
    schema = {"type": "object", "properties": {"replacement": {"type": "string"}}, "required": ["replacement"], "additionalProperties": False}
    try:
        return model_json(prompt, schema, "medium").get("replacement", "")
    except Exception as exc:
        raise RuntimeError(f"mutation failed for {item['unit_id']}: {exc}") from exc


def semantic_tokens(source: str) -> list[tuple[int, str]]:
    tree = ast.parse(source)
    doc_ranges = []
    for node in ast.walk(tree):
        body = getattr(node, "body", None)
        if isinstance(body, list) and body:
            first = body[0]
            if (isinstance(first, ast.Expr) and isinstance(first.value, ast.Constant)
                    and isinstance(first.value.value, str)):
                doc_ranges.append((first.lineno, first.end_lineno or first.lineno))
    ignored = {tokenize.COMMENT, tokenize.ENCODING, tokenize.NL, tokenize.NEWLINE,
               tokenize.INDENT, tokenize.DEDENT, tokenize.ENDMARKER}
    return [(token.type, token.string) for token in tokenize.generate_tokens(io.StringIO(source).readline)
            if token.type not in ignored and not (token.type == tokenize.STRING and any(
                start <= token.start[0] <= end for start, end in doc_ranges))]


def replace_document_span(source: str, original_span: str, replacement_span: str,
                          occurrence: int) -> str:
    if (not original_span.strip() or not replacement_span.strip()
            or "\n" in original_span or "\n" in replacement_span
            or original_span == replacement_span or occurrence < 1):
        raise ValueError("invalid documentation span")
    pos = -1
    for _ in range(occurrence):
        pos = source.find(original_span, pos + 1)
        if pos < 0:
            raise ValueError("documentation span occurrence missing")
    line_start = source.rfind("\n", 0, pos) + 1
    line_end = source.find("\n", line_start)
    line_end = len(source) if line_end < 0 else line_end
    line = source[line_start:line_end]
    label = re.match(r"^[ \t]*[A-Za-z_][\w.-]*:", line)
    if label and pos < line_start + label.end():
        raise ValueError("documentation field name cannot be mutated")
    return source[:pos] + replacement_span + source[pos + len(original_span):]


def normalize_unit(original: str, replacement: str, preserve_structure: bool = False) -> str:
    if preserve_structure:
        if (not replacement.strip() or replacement == original
                or replacement.count("\n") != original.count("\n")
                or any(mark in replacement for mark in ('"""', "'''", "```"))):
            raise ValueError("invalid structured documentation replacement")
        directive = re.compile(r"(?m)^[ \t]*:[A-Za-z_]+(?:[ \t]+[A-Za-z_][\w]*)?:")
        if directive.findall(original) != directive.findall(replacement):
            raise ValueError("documentation field directives changed")
        if [re.match(r"^[ \t]*", line).group(0) for line in original.splitlines()] != [
                re.match(r"^[ \t]*", line).group(0) for line in replacement.splitlines()]:
            raise ValueError("documentation indentation changed")
        field = re.compile(r"^[ \t]*([A-Za-z_][\w.-]*):")
        for old_line, new_line in zip(original.splitlines(), replacement.splitlines()):
            old_label = field.match(old_line)
            if old_label:
                new_label = field.match(new_line)
                if not new_label or old_label.group(1) != new_label.group(1):
                    raise ValueError("documentation field name changed")
        return replacement
    body = replacement.strip(" \t\r\n")
    if not body or any(mark in body for mark in ('"""', "'''", "```")):
        raise ValueError("empty replacement or forbidden delimiter")
    old_lines = original.splitlines()
    new_lines = body.splitlines()
    if len(new_lines) != 1:
        raise ValueError("replacement must be one documentation sentence")
    # Preserve the original leading and trailing whitespace exactly.
    leading = re.match(r"^\s*", original).group(0)
    trailing = re.search(r"\s*$", original).group(0)
    result = leading + body + trailing
    if result == original or result.strip() == original.strip():
        raise ValueError("replacement is unchanged")
    return result


def apply_document_edits(repo: Path, docs: dict[str, dict[str, Any]], changes: list[dict[str, Any]]) -> list[str]:
    by_doc: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for change in changes:
        by_doc[change["documentation_id"]].append(change)
    before: dict[Path, str] = {}
    per_file: dict[Path, list[tuple[int, int, str, str]]] = defaultdict(list)
    for doc_id, edits in by_doc.items():
        doc = docs[doc_id]
        path = repo / doc["file"]
        original_file = before.setdefault(path, path.read_text())
        original_doc = doc["documentation_source"]
        lines = original_file.splitlines(keepends=True)
        start_line = int(doc["documentation_start_line"]) - 1
        end_line = int(doc["documentation_end_line"])
        if "".join(lines[start_line:end_line]) != original_doc:
            raise ValueError(f"docstring location mismatch: {path}:{start_line + 1}")
        updated_doc = original_doc
        for edit in sorted(edits, key=lambda row: row["source_start_offset"], reverse=True):
            a, b = edit["source_start_offset"], edit["source_end_offset"]
            if original_doc[a:b] != edit["original_source"]:
                raise ValueError(f"unit offset mismatch: {edit['unit_id']}")
            updated_doc = updated_doc[:a] + edit["replacement_source"] + updated_doc[b:]
        start = sum(len(line) for line in lines[:start_line])
        per_file[path].append((start, start + len(original_doc), original_doc, updated_doc))
    for path, spans in per_file.items():
        value = before[path]
        for start, end, original_doc, updated_doc in sorted(spans, reverse=True):
            if value[start:end] != original_doc:
                raise ValueError(f"overlapping docstrings: {path}")
            value = value[:start] + updated_doc + value[end:]
        if path.suffix == ".py" and semantic_tokens(before[path]) != semantic_tokens(value):
            raise ValueError(f"non-documentation tokens changed: {path}")
        path.write_text(value)
    subprocess.run(["git", "diff", "--check"], cwd=repo, check=True, capture_output=True)
    return sorted(str(path.relative_to(repo)) for path in per_file)


def make_patch(case: dict[str, str], clusters: list[dict[str, Any]], docs: dict[str, dict[str, Any]],
               out: Path, enabled: tuple[str, ...] = ("L1", "L2", "L3")) -> dict[str, Any]:
    repo_slug = case["repo"].replace("/", "__") + ".git"
    mirror = BIG_REPOS / repo_slug
    if not mirror.exists():
        raise FileNotFoundError(mirror)
    patch_dir = out / "patches" / case["agent"] / case["instance_id"]
    patch_dir.mkdir(parents=True, exist_ok=True)
    changes: list[dict[str, Any]] = []
    selections: list[dict[str, Any]] = []
    staging = out / "staging"
    staging.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=f"{case['agent']}-{case['instance_id']}-", dir=staging) as td:
        checkout = Path(td) / "repo"
        subprocess.run(["git", "clone", "--shared", "-q", str(mirror), str(checkout)], check=True, capture_output=True)
        subprocess.run(["git", "checkout", "--detach", "-q", case["base_commit"]], cwd=checkout, check=True)
        seen_units: set[str] = set()
        for cluster in clusters:
            first, applicable = choose_operator(cluster, enabled)
            alternatives = [operator for operator in applicable if operator != first]
            random.shuffle(alternatives)
            last_error = None
            for operator in [first, *alternatives]:
                cluster_changes = []
                try:
                    for item in cluster["items"]:
                        if item["unit_id"] in seen_units:
                            continue
                        doc = docs[item["documentation_id"]]
                        unit_error = None
                        for attempt in range(3):
                            try:
                                unit_hash = hashlib.sha256(item["unit_id"].encode()).hexdigest()[:16]
                                artifact = patch_dir / "agent_logs" / unit_hash / operator / f"attempt_{attempt:02d}"
                                replacement = mutate_sentence(item, doc, operator, checkout, artifact)
                                replacement_source = normalize_unit(item["unit_source"], replacement,
                                                                    preserve_structure=operator.startswith("R"))
                                break
                            except Exception as exc:
                                unit_error = exc
                        else:
                            raise RuntimeError(f"unit mutation failed after 3 attempts: {item['unit_id']}: {unit_error}")
                        cluster_changes.append({"cluster_id": cluster["cluster_id"], "operator": operator,
                                                "unit_id": item["unit_id"], "documentation_id": item["documentation_id"],
                                                "file": item["file"], "qualname": item["qualname"],
                                                "line": item["file_line_start"], "original": item["unit_text"],
                                                "replacement": replacement, "original_source": item["unit_source"],
                                                "replacement_source": replacement_source,
                                                "source_start_offset": item["source_start_offset"],
                                                "source_end_offset": item["source_end_offset"]})
                except Exception as exc:
                    last_error = exc
                    continue
                changes.extend(cluster_changes)
                seen_units.update(change["unit_id"] for change in cluster_changes)
                selections.append({"cluster_id": cluster["cluster_id"], "operator": operator,
                                   "applicable_operators": applicable})
                break
            else:
                raise RuntimeError(f"cluster mutation failed for all applicable operators: "
                                   f"{cluster['cluster_id']}: {last_error}")
        files = apply_document_edits(checkout, docs, changes)
        patch = subprocess.run(["git", "diff", "--binary", "--", *files], cwd=checkout,
                               check=True, text=True, capture_output=True).stdout
        if not patch.strip():
            raise ValueError("empty mutation patch")
    patch_path = patch_dir / "mutation.patch"
    patch_path.write_text(patch)
    metadata = {"case": {key: case[key] for key in ("agent", "instance_id", "repo", "base_commit")},
                "clusters": selections, "changes": changes, "files": files, "patch": str(patch_path),
                "sha256": hashlib.sha256(patch.encode()).hexdigest()}
    write_json(patch_dir / "mutation.json", metadata)
    return metadata


def prepare_selection(rows: list[dict[str, str]], root: Path) -> Path:
    selection = root / "selections"; selection.mkdir(parents=True, exist_ok=True)
    mapping = {"SWE_Agent": "swe-agent", "OpenCode": "opencode", "Codex": "codex"}
    for display, name in mapping.items():
        ids = [r["instance_id"] for r in rows if r["agent"] == display]
        write_json(selection / f"{name}.json", {"agent": name, "instance_ids": ids})
    return selection


def make_harness_copy(root: Path, patch_root: Path) -> Path:
    src = LIVE_ROOT
    dst = root / "harness"
    dst.mkdir(parents=True, exist_ok=True)
    for name in ("live_common.py", "agent_coordinator.py", "orchestrate.py", "agent_worker.py", "sweagent_compat.py", "export_results.py"):
        shutil.copy2(src / name, dst / name)
    worker = dst / "agent_worker.py"
    text = worker.read_text()
    marker = "        validate_clean_checkout(repo, row[\"base_commit\"])"
    injected = marker + "\n        mutation_root = os.environ.get(\"RIPPLE_MUTATION_PATCH_ROOT\")\n        if not mutation_root:\n            raise RuntimeError(\"mutation patch root is missing\")\n        patch_dir = Path(mutation_root) / self.args.agent / row[\"instance_id\"]\n        patch = patch_dir / \"mutation.patch\"\n        metadata = read_json(patch_dir / \"mutation.json\", {})\n        if metadata.get(\"status\") == \"no_documentation\":\n            return\n        if not patch.is_file() or not patch.read_text().strip():\n            raise RuntimeError(f\"mutation patch is missing or empty: {patch}\")\n        run_checked([\"git\", \"apply\", \"--check\", str(patch)], cwd=repo)\n        run_checked([\"git\", \"apply\", \"--binary\", str(patch)], cwd=repo)"
    if marker not in text:
        raise RuntimeError("worker pristine-check marker not found")
    worker.write_text(text.replace(marker, injected, 1))
    worker_text = worker.read_text()
    reset_marker = '"base_commit": row["base_commit"], "reset": True'
    if reset_marker not in worker_text:
        raise RuntimeError("SWE-Agent reset marker not found")
    worker.write_text(worker_text.replace(reset_marker, '"base_commit": row["base_commit"], "reset": False', 1))
    orchestrator = dst / "orchestrate.py"
    orchestrator_text = orchestrator.read_text()
    old_lock = '"--eval-lock", str(self.eval_lock),'
    new_lock = '"--eval-lock", str(self.root / "locks" / f"{agent}.evaluation.lock"),'
    if old_lock not in orchestrator_text:
        raise RuntimeError("evaluation lock marker not found")
    orchestrator.write_text(orchestrator_text.replace(old_lock, new_lock, 1))
    from harness_fixups import apply_private_harness_fixups
    apply_private_harness_fixups(dst)
    return dst


def run_harness(rows: list[dict[str, str]], run_root: Path, patch_root: Path) -> int:
    harness = make_harness_copy(run_root, patch_root)
    selection = prepare_selection(rows, run_root)
    env = os.environ.copy(); key, base = read_key(); env.update(OPENAI_API_KEY=key, OPENAI_BASE_URL=base, RIPPLE_MUTATION_PATCH_ROOT=str(patch_root))
    command = [sys.executable, str(harness / "orchestrate.py"), "--run", run_root.name,
               "--output", str(run_root), "--export", str(run_root / "export"),
               "--selection-dir", str(selection), "--agent-parallelism", "3",
               "--inference-workers", "2", "--eval-workers", "2", "--ignore-external-load",
               "--podman-socket", f"/tmp/ripple-{run_root.name}.sock"]
    log = run_root / "RUN.log"; run_root.mkdir(parents=True, exist_ok=True)
    with log.open("a") as handle:
        return subprocess.run(command, cwd=harness, env=env, stdout=handle, stderr=subprocess.STDOUT).returncode


def update_progress(run_root: Path, phase: str, completed: int, total: int, current: str = "") -> None:
    state = {"updated_at": now(), "phase": phase, "started_at": run_root.name,
             "completed": completed, "total": total, "remaining": max(0, total - completed),
             "success": 0, "failed": 0, "errors": 0, "eta": "unknown",
             "pid": os.getpid(), "log": str(run_root / "RUN.log"), "output_dir": str(run_root),
             "current": current}
    write_json(run_root / "status.json", state)
    (run_root / "LIVE_PROGRESS.md").write_text("\n".join([
        "# RIPPLE mutation smoke run", "", f"- updated_at: `{state['updated_at']}`",
        f"- phase: **{phase}**", f"- completed: `{completed}/{total}`",
        f"- remaining: `{state['remaining']}`", f"- success: `{state['success']}`",
        f"- failed: `{state['failed']}`", f"- infrastructure errors: `{state['errors']}`",
        f"- ETA: `{state['eta']}`", f"- current: `{current or 'none'}`",
        f"- RUN log: `{state['log']}`", f"- output: `{run_root}`", ""]))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "mutation_result")
    parser.add_argument("--k", type=int, default=3)
    parser.add_argument("--seed", type=int, default=20260926)
    parser.add_argument("--smoke", type=int, default=2, help="cases per agent")
    parser.add_argument("--mutate-only", action="store_true")
    parser.add_argument("--run-id", default="")
    args = parser.parse_args()
    args.output = args.output.resolve(); args.output.mkdir(parents=True, exist_ok=True)
    rows = list(csv.DictReader(CSV_PATH.open()))
    selected = []
    for agent in ("SWE_Agent", "OpenCode", "Codex"):
        for row in [r for r in rows if r["agent"] == agent][: args.smoke]:
            artifact = Path(row["round_1_artifact"])
            task = json.loads((artifact / "task.json").read_text())
            row = dict(row)
            row.update(repo=task["repo"], base_commit=task["base_commit"])
            selected.append(row)
    run_id = args.run_id or f"mutation-smoke-{dt.datetime.now().strftime('%Y%m%d_%H%M%S')}"
    run_root = args.output / run_id; run_root.mkdir(parents=True, exist_ok=True)
    write_json(run_root / "RUN_CONFIG.json", {"run": run_id, "started_at": now(), "model": MODEL, "cases_per_agent": args.smoke, "clusters_per_case": args.k, "inference_workers_per_agent": 2, "agent_parallelism": 3, "evaluation": "existing orchestrate.py official harness", "output": str(run_root)})
    mutations = []
    patch_root = run_root / "patches"
    try:
        update_progress(run_root, "mutation", 0, len(selected), "starting cluster/operator selection")
        for case in selected:
            clusters, docs = clusters_for(case, args.k, args.seed)
            mutations.append(make_patch(case, clusters, docs, run_root))
            update_progress(run_root, "mutation", len(mutations), len(selected), case["instance_id"])
        (run_root / "patch_index.json").write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in mutations) + "\n")
        if args.mutate_only:
            update_progress(run_root, "mutation_complete", len(mutations), len(selected))
            return 0
        # The worker expects patch files directly under patch root by instance ID.
        flat = run_root / "worker_patches"; flat.mkdir(exist_ok=True)
        for meta in mutations:
            slug = {"SWE_Agent": "swe-agent", "OpenCode": "opencode", "Codex": "codex"}[meta["case"]["agent"]]
            source = Path(meta["patch"]); target = flat / slug / meta["case"]["instance_id"]
            target.mkdir(exist_ok=True); shutil.copy2(source, target / "mutation.patch")
            shutil.copy2(source.parent / "mutation.json", target / "mutation.json")
        rc = run_harness(selected, run_root, flat)
        update_progress(run_root, "complete" if rc == 0 else "failed", len(mutations), len(selected))
        state = json.loads((run_root / "status.json").read_text()); state["exit_code"] = rc; write_json(run_root / "status.json", state)
        return rc
    except Exception as exc:
        write_json(run_root / "status.json", {"phase": "failed", "error": f"{type(exc).__name__}: {exc}", "updated_at": now()})
        raise


if __name__ == "__main__":
    raise SystemExit(main())
