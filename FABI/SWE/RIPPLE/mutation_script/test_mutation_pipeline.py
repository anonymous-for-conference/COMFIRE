from __future__ import annotations

import json
import subprocess
import tempfile
import unittest
from pathlib import Path

from RIPPLE.mutation_script.mutation_pipeline import generate, load_level, normalize_replacement


ROOT = Path(__file__).resolve().parents[2]
CASE = ROOT / "original_passed_cases/Codex/gpt54mini_lite/cases/astropy__astropy-6938"
BASE_REPO = Path("/data/zlyuaj/coding_agent/Real_inconsistency_mining/repositories/astropy")
BASE_COMMIT = "c76af9ed6bb89bfba45b9f5bc1e635188278e2fa"


class MutationPipelineTest(unittest.TestCase):
    def test_model_whitespace_is_fitted_to_original(self):
        self.assertEqual(normalize_replacement("    Original.\n", "Changed."), "    Changed.\n")
        self.assertEqual(normalize_replacement("\tOriginal.", "   Changed.\n"), "\tChanged.")
        self.assertEqual(
            normalize_replacement("    First\n        continuation\n", "First changed\ncontinuation changed"),
            "    First changed\n        continuation changed\n",
        )

    def test_level_one_shape(self):
        clusters, docs = load_level(CASE, "level_1")
        self.assertEqual(len(clusters), 1)
        self.assertEqual(len(clusters[0]), 2)
        self.assertEqual(len({row["documentation_id"] for row in clusters[0]}), 1)
        self.assertIn(clusters[0][0]["documentation_id"], docs)

    def test_exact_doc_only_patch(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = root / "repo"
            target = repo / "astropy/io/fits/fitsrec.py"
            target.parent.mkdir(parents=True)
            source = subprocess.check_output(
                ["git", "show", f"{BASE_COMMIT}:astropy/io/fits/fitsrec.py"],
                cwd=BASE_REPO, text=True,
            )
            target.write_text(source)
            subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
            subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=repo, check=True)
            subprocess.run(["git", "config", "user.name", "Test"], cwd=repo, check=True)
            subprocess.run(["git", "add", "."], cwd=repo, check=True)
            subprocess.run(["git", "commit", "-qm", "base"], cwd=repo, check=True)

            def selector(*_):
                return {"applicable_operators": ["L2"], "operator_reasons": []}

            replacements = iter([
                "        Convert internal array values back to binary table representation.\n",
                "        The ``input_field`` is the character array representing the values, and\n"
                "        the ``output_field`` is the internal representation of the ASCII\n"
                "        output that will be written.\n",
            ])

            def mutator(*_):
                return {"mutated_unit_source": next(replacements), "changed_contract": "test", "evidence": "test"}

            result = generate(
                CASE, repo, root / "out", "level_1", 6938,
                selector=selector, local_mutator=mutator,
            )
            self.assertEqual(result["mutation_count"], 2)
            patch = (root / "out/mutation.patch").read_text()
            self.assertIn("binary table representation", patch)
            self.assertIn("character array representing the values", patch)
            self.assertNotIn("output_field.replace", patch)
            compile(target.read_text(), str(target), "exec")

    def test_relational_cluster_retries_incomplete_unit_ids(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            repo = root / "repo"
            target = repo / "astropy/io/fits/fitsrec.py"
            target.parent.mkdir(parents=True)
            source = subprocess.check_output(
                ["git", "show", f"{BASE_COMMIT}:astropy/io/fits/fitsrec.py"],
                cwd=BASE_REPO, text=True,
            )
            target.write_text(source)
            subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
            subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=repo, check=True)
            subprocess.run(["git", "config", "user.name", "Test"], cwd=repo, check=True)
            subprocess.run(["git", "add", "."], cwd=repo, check=True)
            subprocess.run(["git", "commit", "-qm", "base"], cwd=repo, check=True)

            clusters, _ = load_level(CASE, "level_1")
            unit_ids = [row["unit_id"] for row in clusters[0]]
            originals = {row["unit_id"]: row["unit_source"] for row in clusters[0]}
            calls = []

            def selector(*_):
                return {"applicable_operators": ["R1"], "operator_reasons": []}

            def relational_mutator(_repo, prompt, _output, _log, _schema):
                calls.append(prompt)
                ids = unit_ids[:1] if len(calls) == 1 else unit_ids
                return {"mutations": [{
                    "unit_id": unit_id,
                    "mutated_unit_source": originals[unit_id] if len(calls) == 2 and index == 0 else (
                        "Convert internal array values back to the representation owned by the table writer."
                        if index == 0 else
                        "The table writer owns conversion of input and output fields to their internal representations."
                    ),
                    "changed_contract": "Assign conversion responsibility to the table writer.",
                    "evidence": "Mock repository evidence.",
                } for index, unit_id in enumerate(ids)]}

            result = generate(
                CASE, repo, root / "out", "level_1", 6938,
                selector=selector, relational_mutator=relational_mutator,
                forced_operator="R1", enabled_operators=("R1", "R2", "R3"),
            )
            self.assertEqual(len(calls), 3)
            self.assertIn("Missing IDs", calls[1])
            self.assertIn("Invalid mutations", calls[2])
            self.assertEqual(result["mutation_count"], len(unit_ids))
            self.assertTrue((root / "out/cluster_0001/cluster_mutation.attempt_01.response.json").exists())
            self.assertTrue((root / "out/cluster_0001/cluster_mutation.attempt_02.response.json").exists())
            self.assertTrue((root / "out/cluster_0001/cluster_mutation.attempt_03.response.json").exists())
            canonical = json.loads((root / "out/cluster_0001/cluster_mutation.response.json").read_text())
            self.assertEqual({row["unit_id"] for row in canonical["mutations"]}, set(unit_ids))


if __name__ == "__main__":
    unittest.main()
