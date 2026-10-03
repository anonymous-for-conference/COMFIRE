from __future__ import annotations

import json
import subprocess
from pathlib import Path

from mutation_script.mutation_pipeline import (
    DEFAULT_OPERATORS,
    ToolBudgetExceeded,
    applicable_operators,
    apply_mutations,
    error_category,
    load_clusters,
    select_clusters,
    normalize,
    preserve_cluster_claims,
    validate_relational_response,
)
from mutation_script.runner_support import apply_multi_file_mutation


def git(repo: Path, *args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=repo, text=True).strip()


def init_repo(path: Path) -> None:
    subprocess.run(["git", "init", "-q", path], check=True)
    subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=path, check=True)
    subprocess.run(["git", "config", "user.name", "Test"], cwd=path, check=True)


def test_load_clusters_ignores_level_and_avoids_duplicate_units(tmp_path: Path) -> None:
    case = tmp_path / "case"
    case.mkdir()
    doc = {
        "documentation_id": "doc", "function_source": 'def f():\n    """One. Two."""\n',
        "documentation_source": '    """One. Two."""\n', "function_start_line": 1,
        "documentation_start_line": 2, "documentation_end_line": 2,
    }
    (case / "all_doc.jsonl").write_text(json.dumps(doc) + "\n")
    rows = []
    for level, cluster, unit in (("level_1", "c1", "u1"), ("level_2", "c2", "u1"), ("level_3", "c3", "u2")):
        rows.append({
            "level": level, "cluster_id": cluster, "documentation_id": "doc", "unit_id": unit,
            "file": "x.py", "file_line_start": 2, "unit_index": 1, "mutable": True,
        })
    (case / "clustered_doc.jsonl").write_text("".join(json.dumps(row) + "\n" for row in rows))
    clusters, _ = load_clusters(case)
    selected = select_clusters(clusters, 2, 1)
    assert len(clusters) == 3
    assert len({row["unit_id"] for cluster in selected for row in cluster}) == 2


def test_operator_selection_filters_relational_and_falls_back_to_l1() -> None:
    allowed, fallback = applicable_operators(
        {"applicable_operators": ["R2", "L3", "R1", "L3"]}, DEFAULT_OPERATORS,
    )
    assert allowed == ["L3"]
    assert fallback is False
    allowed, fallback = applicable_operators(
        {"applicable_operators": ["R1", "R3"]}, DEFAULT_OPERATORS,
    )
    assert allowed == ["L1"]
    assert fallback is True
    assert DEFAULT_OPERATORS == ("L1", "L2", "L3")


def test_operator_selection_relational_only_falls_back_to_r1() -> None:
    enabled = ("R1", "R2", "R3")
    allowed, fallback = applicable_operators(
        {"applicable_operators": ["L1", "R3", "R2", "R3"]}, enabled,
    )
    assert allowed == ["R3", "R2"]
    assert fallback is False
    assert applicable_operators({"applicable_operators": []}, enabled) == (["R1"], True)


def test_validate_relational_response_requires_complete_changed_units() -> None:
    cluster = [
        {"unit_id": "u1", "unit_source": "    The parser owns validation.\n"},
        {"unit_id": "u2", "unit_source": "    Calls the validator.\n"},
    ]
    response = {"mutations": [
        {"unit_id": "u1", "mutated_unit_source": "The loader owns validation.",
         "changed_contract": "owner", "evidence": "Parser validates in parser.py."},
        {"unit_id": "u2", "mutated_unit_source": "Calls the normalizer.",
         "changed_contract": "endpoint", "evidence": "The code invokes Validator."},
    ]}
    assert set(validate_relational_response(response, cluster)) == {"u1", "u2"}
    response["mutations"][1]["evidence"] = ""
    try:
        validate_relational_response(response, cluster)
    except ValueError as exc:
        assert "empty evidence" in str(exc)
    else:
        raise AssertionError("empty relational evidence was accepted")


def test_relational_error_categories() -> None:
    assert error_category(ToolBudgetExceeded("too many tools")) == "exploration_budget"
    assert error_category(RuntimeError("429 concurrency limit")) == "provider_transient"
    assert error_category(ValueError("unit_id mismatch")) == "model_output"


def test_select_clusters_uses_all_available_below_k() -> None:
    clusters = [[{"unit_id": "one"}], [{"unit_id": "two"}], [{"unit_id": "one"}]]
    selected = select_clusters(clusters, 3, 7)
    assert len(selected) == 2
    assert {row["unit_id"] for cluster in selected for row in cluster} == {"one", "two"}


def test_preserve_cluster_claims_keeps_one_deterministically() -> None:
    cluster = [{"unit_id": f"u{i}"} for i in range(5)]
    preserved, mutated = preserve_cluster_claims(cluster, 1, 17)
    again, _ = preserve_cluster_claims(cluster, 1, 17)
    assert preserved == again
    assert len(preserved) == 1
    assert len(mutated) == 4
    assert {x["unit_id"] for x in preserved}.isdisjoint(x["unit_id"] for x in mutated)


def test_normalize_removes_added_trailing_whitespace() -> None:
    original = "    First line.\n\n    Second line.\n"
    mutated = "First changed.  \n   \nSecond changed.\t\n"
    assert normalize(original, mutated) == "    First changed.\n\n    Second changed.\n"


def test_apply_mutations_changes_only_docstrings(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    init_repo(repo)
    source = 'def answer():\n    """Return one.\n\n    Stable details.\n    """\n    return 1\n'
    (repo / "sample.py").write_text(source)
    subprocess.run(["git", "add", "."], cwd=repo, check=True)
    subprocess.run(["git", "commit", "-qm", "base"], cwd=repo, check=True)
    doc_source = '    """Return one.\n\n    Stable details.\n    """\n'
    docs = {"doc": {
        "file": "sample.py", "documentation_source": doc_source,
        "documentation_start_line": 2, "documentation_end_line": 5,
    }}
    mutation = {
        "documentation_id": "doc", "unit_id": "unit", "source_start_offset": 7,
        "source_end_offset": 18, "original_unit_source": "Return one.",
        "mutated_unit_source": "Return two.",
    }
    changed = apply_mutations(repo, docs, [mutation])
    assert changed == ["sample.py"]
    assert "Return two." in (repo / "sample.py").read_text()
    assert "return 1" in (repo / "sample.py").read_text()


def test_runner_support_accepts_manifest_file_set(tmp_path: Path) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    init_repo(repo)
    for name in ("a.txt", "b.txt"):
        (repo / name).write_text("old\n")
    subprocess.run(["git", "add", "."], cwd=repo, check=True)
    subprocess.run(["git", "commit", "-qm", "base"], cwd=repo, check=True)
    base = git(repo, "rev-parse", "HEAD")
    for name in ("a.txt", "b.txt"):
        (repo / name).write_text("new\n")
    patch = subprocess.check_output(["git", "diff", "--binary", "--"], cwd=repo, text=True)
    subprocess.run(["git", "reset", "--hard", "-q", base], cwd=repo, check=True)
    mutation_root = tmp_path / "mutations"
    case = mutation_root / "codex" / "iid"
    case.mkdir(parents=True)
    (case / "mutation.patch").write_text(patch)
    (case / "mutation.json").write_text(json.dumps({"files": ["a.txt", "b.txt"]}))
    audit = tmp_path / "audit.json"
    mutation_commit = apply_multi_file_mutation(
        repo, {"instance_id": "iid", "base_commit": base}, mutation_root,
        "codex", audit, lambda path, text: path.write_text(text),
    )
    recorded = json.loads(audit.read_text())
    assert recorded["files"] == ["a.txt", "b.txt"]
    assert recorded["mutation_commit"] == mutation_commit == git(repo, "rev-parse", "HEAD")
    assert git(repo, "diff", "--name-only", mutation_commit, "--") == ""
    assert git(repo, "diff", "--name-only", base, "--").splitlines() == ["a.txt", "b.txt"]


def test_local_clone_works_inside_output_filesystem(tmp_path: Path) -> None:
    source = tmp_path / "source"
    source.mkdir()
    init_repo(source)
    (source / "file.txt").write_text("content\n")
    subprocess.run(["git", "add", "."], cwd=source, check=True)
    subprocess.run(["git", "commit", "-qm", "base"], cwd=source, check=True)
    output = tmp_path / "output"
    output.mkdir()
    clone = output / "worktree" / "repo"
    clone.parent.mkdir()
    subprocess.run(["git", "clone", "--local", "--no-checkout", "-q", str(source), str(clone)], check=True)
    subprocess.run(["git", "checkout", "--detach", "-q", git(source, "rev-parse", "HEAD")], cwd=clone, check=True)
    assert (clone / "file.txt").read_text() == "content\n"
