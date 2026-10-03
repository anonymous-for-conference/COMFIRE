#!/usr/bin/env python3
"""Remove repository documentation while preserving source line structure."""

from __future__ import annotations

import ast
import io
import json
import os
import sys
import tokenize
from pathlib import Path

DOC_NAMES = {
    "readme", "contributing", "changelog", "changes", "authors", "install",
    "code_of_conduct", "security", "documentation",
}
DOC_SUFFIXES = {".md", ".mdown", ".markdown", ".rst", ".rest", ".adoc"}
SKIP_PARTS = {".git", ".hg", ".svn", "node_modules", "vendor", "dist", "build"}


def _blank_span(lines: list[str], start: tuple[int, int], end: tuple[int, int]) -> None:
    start_line, start_col = start
    end_line, end_col = end
    for number in range(start_line - 1, end_line):
        left = start_col if number == start_line - 1 else 0
        right = end_col if number == end_line - 1 else len(lines[number].rstrip("\r\n"))
        body = lines[number]
        ending = body[len(body.rstrip("\r\n")):]
        content = body[:len(body) - len(ending)] if ending else body
        lines[number] = content[:left] + " " * max(0, right - left) + content[right:] + ending


def _empty_docstring(lines: list[str], start: tuple[int, int], end: tuple[int, int]) -> None:
    """Replace a docstring with an empty literal without changing line count."""
    _blank_span(lines, start, end)
    line_number, column = start
    line = lines[line_number - 1]
    lines[line_number - 1] = line[:column] + "''" + line[column + 2:]


def strip_python(path: Path) -> bool:
    raw = path.read_bytes()
    try:
        encoding, _ = tokenize.detect_encoding(io.BytesIO(raw).readline)
        text = raw.decode(encoding)
        tree = ast.parse(text)
    except (SyntaxError, UnicodeError, LookupError):
        return False
    doc_spans: list[tuple[tuple[int, int], tuple[int, int]]] = []
    comment_spans: list[tuple[tuple[int, int], tuple[int, int]]] = []
    for node in ast.walk(tree):
        body = getattr(node, "body", None)
        if isinstance(body, list) and body and isinstance(body[0], ast.Expr):
            value = body[0].value
            if isinstance(value, ast.Constant) and isinstance(value.value, str):
                doc_spans.append(((body[0].lineno, body[0].col_offset),
                                  (body[0].end_lineno or body[0].lineno, body[0].end_col_offset or 0)))
    try:
        for token in tokenize.generate_tokens(io.StringIO(text).readline):
            if token.type == tokenize.COMMENT and not (
                token.start[0] <= 2 and ("coding" in token.string or token.string.startswith("#!"))
            ):
                comment_spans.append((token.start, token.end))
    except tokenize.TokenError:
        return False
    if not doc_spans and not comment_spans:
        return False
    lines = text.splitlines(keepends=True)
    for start, end in sorted(comment_spans, reverse=True):
        _blank_span(lines, start, end)
    for start, end in sorted(doc_spans, reverse=True):
        _empty_docstring(lines, start, end)
    updated = "".join(lines)
    if updated != text:
        path.write_bytes(updated.encode(encoding))
        return True
    return False


def is_doc_file(path: Path) -> bool:
    stem = path.stem.lower().replace("-", "_")
    in_docs_tree = any(part.lower() in {"doc", "docs", "documentation"} for part in path.parts)
    return (path.suffix.lower() in DOC_SUFFIXES or stem in DOC_NAMES
            or (path.suffix.lower() == ".txt" and in_docs_tree))


def strip_repository(repo: Path) -> dict[str, object]:
    changed: list[str] = []
    bytes_removed = 0
    for path in repo.rglob("*"):
        if not path.is_file() or any(part in SKIP_PARTS for part in path.relative_to(repo).parts):
            continue
        relative = str(path.relative_to(repo))
        before = path.stat().st_size
        if path.suffix.lower() == ".py":
            did_change = strip_python(path)
        elif is_doc_file(path):
            try:
                text = path.read_text()
            except (OSError, UnicodeError):
                continue
            replacement = "".join("\n" if line.endswith("\n") else "" for line in text.splitlines(keepends=True))
            did_change = replacement != text
            if did_change:
                path.write_text(replacement)
        else:
            did_change = False
        if did_change:
            changed.append(relative)
            bytes_removed += max(0, before - path.stat().st_size)
    return {"changed_files": changed, "changed_file_count": len(changed), "bytes_removed": bytes_removed}


def main() -> int:
    if len(sys.argv) < 3:
        raise SystemExit("usage: doc_filter.py REPO INSTANCE_ID [RUN ATTEMPT_DIR AGENT]")
    repo = Path(sys.argv[1]).resolve()
    strategy = os.environ.get("RIPPLE_ENHANCEMENT_STRATEGY", "")
    result: dict[str, object] = {"strategy": strategy, "instance_id": sys.argv[2], "repo": str(repo)}
    if strategy == "remove_docs":
        result.update(strip_repository(repo))
    else:
        result.update({"changed_files": [], "changed_file_count": 0, "bytes_removed": 0})
    if len(sys.argv) >= 5:
        audit = Path(sys.argv[4]) / "documentation_filter.json"
        audit.parent.mkdir(parents=True, exist_ok=True)
        audit.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
