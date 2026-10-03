"""Shared adapter helpers for applying multi-file mutation patches."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


def apply_multi_file_mutation(repo: Path, row: dict, mutation_root: Path, agent: str,
                              audit_path: Path, writer) -> str:
    patch_path = mutation_root / agent / row["instance_id"] / "mutation.patch"
    metadata_path = patch_path.parent / "mutation.json"
    if not patch_path.is_file() or not patch_path.read_text().strip():
        raise RuntimeError(f"missing mutation patch: {patch_path}")
    metadata = json.loads(metadata_path.read_text())
    expected = sorted(metadata.get("files") or ([metadata["file"]] if metadata.get("file") else []))
    if not expected:
        raise RuntimeError(f"mutation manifest has no changed files: {metadata_path}")
    subprocess.run(["git", "apply", "--check", str(patch_path)], cwd=repo, check=True,
                   capture_output=True, text=True)
    subprocess.run(["git", "apply", str(patch_path)], cwd=repo, check=True,
                   capture_output=True, text=True)
    changed = sorted(subprocess.check_output(
        ["git", "diff", "--name-only", row["base_commit"], "--"], cwd=repo, text=True
    ).splitlines())
    if changed != expected:
        raise RuntimeError(f"mutation changed unexpected files: expected={expected!r} actual={changed!r}")
    subprocess.run(["git", "add", "--", *expected], cwd=repo, check=True)
    subprocess.run([
        "git", "-c", "user.name=Mutation Baseline", "-c",
        "user.email=mutation-baseline@example.invalid", "commit", "-qm",
        "Apply documentation mutation baseline",
    ], cwd=repo, check=True)
    mutation_commit = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=repo, text=True
    ).strip()
    writer(audit_path, json.dumps({
        "patch": str(patch_path), "sha256": hashlib.sha256(patch_path.read_bytes()).hexdigest(),
        "files": expected, "base_commit": row["base_commit"],
        "mutation_commit": mutation_commit, "applied": True,
    }, ensure_ascii=False, indent=2) + "\n")
    return mutation_commit
