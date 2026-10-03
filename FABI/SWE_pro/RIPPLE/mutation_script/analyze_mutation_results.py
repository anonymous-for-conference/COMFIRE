#!/usr/bin/env python3
"""Analyze documentation mutation trajectories against the three clean runs."""
import csv
import difflib
import glob
import json
import os
import re
import statistics
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RUN = os.path.join(ROOT, "mutation_result", "full_local6_20260921_220749")
ORIGINAL = "/data/zlyuaj/coding_agent/EviFuzz_SWE_pro/original_passed_cases_luna"
AGENTS = {"codex": "Codex", "opencode": "OpenCode", "swe-agent": "SWE_Agent"}

# A score below .97 is a meaningful structural/content change relative to the
# closest of three clean runs. Length changes catch short aborted/restarted runs.
SIMILARITY_THRESHOLD = 0.97


def trajectory_text(path, agent):
    out = []
    if agent in ("codex", "opencode"):
        for line in open(path, errors="replace"):
            try:
                event = json.loads(line)
            except Exception:
                continue
            if not isinstance(event, dict):
                continue
            if agent == "codex":
                item = event.get("item", {})
                kind = item.get("type", "")
                if kind == "agent_message":
                    out.append(item.get("text", ""))
                elif kind == "command_execution":
                    out.append("CMD " + item.get("command", ""))
            else:
                kind = event.get("type")
                part = event.get("part", {})
                if kind == "text":
                    out.append(part.get("text", ""))
                elif kind == "tool_use":
                    state = part.get("state", {})
                    out.append("TOOL " + part.get("tool", "") + " " +
                               json.dumps(state.get("input", {}), sort_keys=True))
    else:
        raw = open(path, errors="replace").read()
        try:
            parsed = json.loads(raw)
            items = parsed.get("trajectory", parsed if isinstance(parsed, list) else [])
            for item in items:
                if isinstance(item, dict):
                    for key in ("action", "observation", "thought", "response", "command", "args"):
                        if item.get(key):
                            out.append(key.upper() + " " + str(item[key]))
        except Exception:
            out.append(raw)
    return "\n".join(out)


def normalize(text):
    text = text.lower()
    text = re.sub(r"\d{4,}", "N", text)
    text = re.sub(r"[/\\][\w./-]+", "PATH", text)
    return re.sub(r"[^a-z0-9_ ]+", " ", text)


def clean_paths(agent, instance_id):
    base = os.path.join(ORIGINAL, AGENTS[agent], "cases", instance_id)
    return (glob.glob(base + "/round_*/run_1/**/*.traj", recursive=True) +
            glob.glob(base + "/round_*/run_1/**/*.jsonl", recursive=True))


def mutation_trace(agent, instance_id):
    paths = [p for p in glob.glob(os.path.join(RUN, agent, "cases", instance_id,
                                                "run_1", "**", "*"), recursive=True)
             if p.endswith((".traj", ".jsonl"))]
    return paths[0] if paths else None


def conflict_evidence(text):
    # Require a natural-language relation between the documentation and the
    # error signal; this excludes paths such as docs/docsite/.../ignore.
    patterns = [
        r"\b(?:documentation|docstring|docs?)\b.{0,100}\b(?:wrong|incorrect|inaccurate|contradict(?:s|ed|ion)?|conflict(?:s|ed)?|stale|outdated|misleading|unreliable|mismatch|does not match|doesn't match)\b",
        r"\b(?:wrong|incorrect|inaccurate|contradict(?:s|ed|ion)?|conflict(?:s|ed)?|stale|outdated|misleading|unreliable|mismatch|does not match|doesn't match)\b.{0,100}\b(?:documentation|docstring|docs?)\b",
        r"\b(?:ignore|disregard|do not trust|not trust)\b.{0,60}\b(?:documentation|docstring|docs?)\b",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, re.I | re.S)
        if match:
            context = re.sub(r"\s+", " ", match.group(0)).strip()
            # File paths, git history, and test assertions are not recognition
            # that the mutated documentation is unreliable.
            window = text[max(0, match.start() - 120):match.end() + 120].lower()
            if any(token in window for token in ("./docs", "docs if", "or not doc", "doc[k]", "git log", "git show", "assertion", "assert ", "legacy", "changelog", "history", "context.cliargs", "raise ")):
                continue
            return context[:300]
    return ""


def case_result(agent, manifest_path):
    manifest = json.load(open(manifest_path))
    instance_id = manifest["instance_id"]
    trace_path = mutation_trace(agent, instance_id)
    clean = clean_paths(agent, instance_id)
    mutated_text = trajectory_text(trace_path, agent) if trace_path else ""
    clean_texts = [trajectory_text(p, agent) for p in clean]
    normalized_mutated = normalize(mutated_text)
    normalized_clean = [normalize(t) for t in clean_texts]
    scores = [difflib.SequenceMatcher(None, normalized_mutated, t).quick_ratio()
              for t in normalized_clean]
    similarity = max(scores) if scores else 0.0
    clean_lengths = [len(t) for t in normalized_clean]
    clean_median = statistics.median(clean_lengths) if clean_lengths else 0
    length_ratio = (len(normalized_mutated) / clean_median) if clean_median else 0.0
    unresolved = instance_id not in set(json.load(open(
        os.path.join(RUN, agent, "evaluation_result.json"))).get("resolved_ids", []))
    raw_lower = mutated_text.lower()
    access_positions = [p for name in manifest.get("files", [])
                        for needle in (name.lower(), os.path.basename(name).lower())
                        for p in [raw_lower.find(needle)] if p >= 0]
    access_position = min(access_positions) if access_positions else -1
    mutation_file_observed = access_position >= 0
    contract_terms = set()
    for cluster in manifest.get("clusters", []):
        for location in cluster.get("locations", []):
            contract_terms.update(re.findall(
                r"[a-zA-Z_][a-zA-Z0-9_-]{4,}",
                location.get("changed_contract", "") + " " + location.get("mutated_unit_source", "")))
    post_access = raw_lower[access_position:] if access_position >= 0 else ""
    observed_contract_terms = sorted(term.lower() for term in contract_terms if term.lower() in post_access)
    # Two claim-specific terms after the documentation access provide a
    # conservative semantic attribution signal; one generic word is noise.
    mutation_contract_observed = len(observed_contract_terms) >= 2
    trace_changed = (similarity < SIMILARITY_THRESHOLD or length_ratio < 0.5 or length_ratio > 1.5)
    # Correct runs only, with an observable link to the mutated documentation.
    affected = (not unresolved and bool(trace_path) and bool(clean_texts) and trace_changed
                and mutation_file_observed and mutation_contract_observed)
    evidence = conflict_evidence(mutated_text)
    explicit_conflict = bool(evidence) and affected
    files = sorted(set(manifest.get("files", [])))
    operators = sorted(set(c.get("selected_operator", "") for c in manifest.get("clusters", [])))
    changed = [loc.get("changed_contract", "") for c in manifest.get("clusters", [])
               for loc in c.get("locations", []) if loc.get("changed_contract")]
    return {
        "agent": agent, "instance_id": instance_id,
        "trace_present": bool(trace_path), "clean_trace_count": len(clean),
        "mutation_files": ";".join(files), "operators": ";".join(operators),
        "changed_contracts": " | ".join(changed),
        "similarity_to_closest_clean": round(similarity, 6),
        "mutated_trace_chars": len(normalized_mutated),
        "clean_median_chars": int(clean_median), "length_ratio": round(length_ratio, 6),
        "evaluation_unresolved": unresolved, "affected": affected,
        "trace_changed": trace_changed,
        "mutation_file_observed": mutation_file_observed,
        "mutation_contract_observed": mutation_contract_observed,
        "observed_contract_terms": ";".join(observed_contract_terms),
        "explicit_conflict_recognition": explicit_conflict,
        "conflict_evidence": evidence,
    }


def main():
    rows = []
    for agent in AGENTS:
        for path in sorted(glob.glob(os.path.join(RUN, "mutations", agent, "*", "mutation.json"))):
            rows.append(case_result(agent, path))
    out = os.path.join(RUN, "result_analysis")
    os.makedirs(out, exist_ok=True)
    fields = list(rows[0])
    with open(os.path.join(out, "case_analysis.csv"), "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader(); writer.writerows(rows)
    by_agent = {}
    for agent in AGENTS:
        subset = [r for r in rows if r["agent"] == agent]
        by_agent[agent] = {"total": len(subset),
                           "correct_resolved": sum(not r["evaluation_unresolved"] for r in subset),
                           "affected": sum(r["affected"] for r in subset),
                           "explicit_conflict_recognition": sum(r["explicit_conflict_recognition"] for r in subset),
                           "affected_and_explicit_conflict": sum(r["affected"] and r["explicit_conflict_recognition"] for r in subset)}
    expected = {}
    stable_csv = os.path.join(ORIGINAL, "token_stable_cases.csv")
    if os.path.exists(stable_csv):
        with open(stable_csv, newline="") as f:
            for item in csv.DictReader(f):
                expected.setdefault(item["agent"], set()).add(item["instance_id"])
    present = {AGENTS[a]: {r["instance_id"] for r in rows if r["agent"] == a} for a in AGENTS}
    missing = {agent: sorted(ids - present.get(agent, set())) for agent, ids in expected.items()}
    summary = {"run": os.path.basename(RUN), "rule_similarity_threshold": SIMILARITY_THRESHOLD,
               "total": len(rows),
               "correct_resolved_total": sum(not r["evaluation_unresolved"] for r in rows),
               "affected": sum(r["affected"] for r in rows),
               "explicit_conflict_recognition": sum(r["explicit_conflict_recognition"] for r in rows),
               "affected_and_explicit_conflict": sum(r["affected"] and r["explicit_conflict_recognition"] for r in rows),
               "expected_token_stable_total": sum(len(ids) for ids in expected.values()),
               "missing_from_mutation_run": missing,
               "by_agent": by_agent,
               "operator_counts": dict(Counter(op for r in rows for op in r["operators"].split(";") if op))}
    with open(os.path.join(out, "summary.json"), "w") as f:
        json.dump(summary, f, indent=2); f.write("\n")
    with open(os.path.join(out, "README.md"), "w") as f:
        f.write("# Mutation trajectory analysis\n\n")
        f.write("Each row in `case_analysis.csv` is one mutation case. Only evaluation-resolved cases can be affected. Following the paper definition, `affected` requires a structural deviation from the closest clean run, an observed access to the mutated documentation file, and at least two claim-specific terms from the mutated contract appearing after that access. This is the semantic attribution gate; generic variation and unresolved runs are excluded. `explicit_conflict_recognition` requires an explicit statement that documentation disagrees with executable evidence or is incorrect/unreliable.\n\n")
        f.write("The manifest records the exact mutation files, operators, original/mutated documentation, and changed contract for every case.\n")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
