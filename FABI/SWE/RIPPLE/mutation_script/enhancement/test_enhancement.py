from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from doc_filter import strip_repository
from run_experiment import combine_prediction, discover, excluded_inputs
from strategies import STRATEGIES, prompt_for


class EnhancementTests(unittest.TestCase):
    def test_all_strategy_prompts_exist(self):
        for strategy in STRATEGIES:
            self.assertTrue(prompt_for(strategy).strip())
        self.assertIn("Task requirement", prompt_for("evidence_boundary"))
        self.assertIn("edit-boundary", prompt_for("evidence_boundary"))

    def test_doc_filter_preserves_python_line_count_and_behavior(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "example.py"
            source.write_text('"""wrong module docs"""\n\nclass Empty:\n    """only docs"""\n\ndef add(a, b):\n    """wrong function docs"""\n    # misleading comment\n    return a + b\n')
            readme = root / "README.md"; readme.write_text("wrong docs\nsecond line\n")
            before_lines = source.read_text().count("\n")
            result = strip_repository(root)
            self.assertEqual(source.read_text().count("\n"), before_lines)
            self.assertNotIn("wrong function docs", source.read_text())
            self.assertEqual(readme.read_text(), "\n\n")
            namespace: dict[str, object] = {}
            exec(source.read_text(), namespace)
            self.assertEqual(namespace["add"](2, 3), 5)
            self.assertEqual(namespace["Empty"].__doc__, "")
            self.assertEqual(result["changed_file_count"], 2)

    def test_failure_archive_count(self):
        rows = discover(("round1", "round2"), ("codex", "opencode", "sweagent"))
        self.assertEqual(len(rows), 49)
        self.assertEqual(sum(row["round"] == "round1" for row in rows), 27)
        self.assertEqual(sum(row["round"] == "round2" for row in rows), 22)
        excluded = excluded_inputs(("round1", "round2"), ("codex", "opencode", "sweagent"))
        self.assertEqual(len(excluded), 28)
        self.assertTrue(all(row["round"] == "round1" for row in excluded))

    def test_remove_docs_replays_agent_delta_without_mutation(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            run = root / "remove_docs" / "round1" / "codex" / "case"
            repo = run / "worktree"
            interface = run / "interface"
            repo.mkdir(parents=True)
            interface.mkdir()
            subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
            subprocess.run(["git", "config", "user.name", "test"], cwd=repo, check=True)
            subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=repo, check=True)
            source = repo / "module.py"
            source.write_text('"""trusted original docs"""\n\ndef value():\n    """function docs"""\n    return 1\n')
            subprocess.run(["git", "add", "."], cwd=repo, check=True)
            subprocess.run(["git", "commit", "-qm", "base"], cwd=repo, check=True)
            base = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip()
            strip_repository(repo)
            subprocess.run(["git", "add", "."], cwd=repo, check=True)
            subprocess.run(["git", "commit", "-qm", "docs removed"], cwd=repo, check=True)
            source.write_text(source.read_text().replace("return 1", "return 2"))
            agent_patch = subprocess.check_output(["git", "diff", "--binary"], cwd=repo, text=True)
            prediction = {"instance_id": "example__example-1", "model_patch": agent_patch}
            (interface / "predictions.jsonl").write_text(json.dumps(prediction) + "\n")
            item = {"base_commit": base, "instance_id": "example__example-1"}

            combine_prediction(run, item, repo, apply_mutation=False)

            self.assertFalse((run / "mutation.patch").exists())
            self.assertIn("trusted original docs", source.read_text())
            self.assertIn("function docs", source.read_text())
            self.assertIn("return 2", source.read_text())
            self.assertNotIn("trusted original docs", (run / "combined.patch").read_text())

    def test_remove_docs_preserves_docs_when_agent_edit_overlaps_them(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            run = root / "remove_docs" / "round1" / "opencode" / "case"
            repo = run / "worktree"
            interface = run / "interface"
            repo.mkdir(parents=True)
            interface.mkdir()
            subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
            subprocess.run(["git", "config", "user.name", "test"], cwd=repo, check=True)
            subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=repo, check=True)
            source = repo / "module.py"
            source.write_text('def value():\n    """original docs"""\n    return 1\n')
            subprocess.run(["git", "add", "."], cwd=repo, check=True)
            subprocess.run(["git", "commit", "-qm", "base"], cwd=repo, check=True)
            base = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=repo, text=True).strip()
            strip_repository(repo)
            subprocess.run(["git", "add", "."], cwd=repo, check=True)
            subprocess.run(["git", "commit", "-qm", "docs removed"], cwd=repo, check=True)
            source.write_text("def value():\n    'agent replaced blank doc region'\n    return 2\n")
            patch = subprocess.check_output(["git", "diff", "--binary"], cwd=repo, text=True)
            (interface / "predictions.jsonl").write_text(json.dumps({
                "instance_id": "example__example-2", "model_patch": patch,
            }) + "\n")

            combine_prediction(run, {
                "base_commit": base, "instance_id": "example__example-2",
            }, repo, apply_mutation=False)

            self.assertIn('"""original docs"""', source.read_text())
            self.assertNotIn("agent replaced blank doc region", source.read_text())
            self.assertIn("return 2", source.read_text())


if __name__ == "__main__":
    unittest.main()
